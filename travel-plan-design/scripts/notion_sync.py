"""Offline Notion/source comparison. Fetch pages through the connector first.

This helper never interprets plan decisions, edits HTML, or publishes remotely.
Its private report supplies a three-way diff for the agent's reconciliation.
"""
import argparse
import difflib
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)


def normalized(content):
    # Remove presentation only. Preserve words, URLs, numbers, dates and checks.
    content = re.sub(r'<table-of-contents\b[^>]*/>', '', content)
    content = re.sub(r'\s(?:color|icon)="[^"]*"', '', content)
    content = re.sub(r'</?(?:h[1-4]|toggle|b|strong|i|em|span)\b[^>]*>', '', content)
    content = re.sub(r'^#{1,4}\s+', '', content, flags=re.M)
    content = content.replace('**', '')
    return re.sub(r'\s+', ' ', content).strip()


def delta(before, after):
    return '\n'.join(difflib.unified_diff(before.splitlines(), after.splitlines(),
                                         fromfile='baseline', tofile='current', lineterm=''))


def capture(project, config, snapshot):
    expected = config['pages']
    incoming = snapshot['pages']
    assert set(incoming) == set(expected), 'Missing or unexpected Notion page: do not advance baseline'
    pages, sources = {}, {}
    for key, mapping in expected.items():
        item = incoming[key]
        assert item['id'].replace('-', '') == mapping['id'].replace('-', ''), f'Wrong page: {key}'
        assert item.get('complete') is True and isinstance(item.get('content'), str), f'Incomplete fetch: {key}'
        assert not item.get('truncated') and not item.get('unknown_block_count') and not item.get('unknown_block_ids'), f'Omitted blocks: {key}'
        pages[key] = dict(id=item['id'], content=item['content'],
                          editedAt=item.get('editedAt'), hash=digest(item['content']),
                          semanticHash=digest(normalized(item['content'])))
        for relative in mapping['sources']:
            target = (project / relative).resolve()
            assert target.is_relative_to(project.resolve()), 'Source outside project'
            assert target.is_file(), f'Missing source: {relative}'
            content = target.read_text(encoding='utf-8')
            sources[relative] = dict(hash=digest(content), content=content)
    return dict(schema=1, capturedAt=datetime.now(timezone.utc).isoformat(),
                pages=pages, sources=sources, mappingHash=digest(json.dumps(expected, sort_keys=True)))


def compare(base, current, config):
    if base:
        assert base['mappingHash'] == current['mappingHash'], 'Page mapping changed; review and migrate baseline explicitly'
    rows = []
    for key, mapping in config['pages'].items():
        new = current['pages'][key]
        old = base['pages'][key] if base else None
        changed_sources = [p for p in mapping['sources'] if not base or base['sources'][p]['hash'] != current['sources'][p]['hash']]
        raw_changed = bool(old and old['hash'] != new['hash'])
        semantic_changed = bool(old and old['semanticHash'] != new['semanticHash'])
        if not base: status = 'baseline-required'
        elif semantic_changed and changed_sources: status = 'both-changed'
        elif semantic_changed: status = 'notion-changed'
        elif changed_sources: status = 'local-changed'
        elif raw_changed: status = 'format-only'
        else: status = 'unchanged'
        rows.append(dict(key=key, status=status, notesPage=mapping.get('notes', False),
                         sourceFiles=mapping['sources'], changedSources=changed_sources,
                         notionDiff=delta(old['content'], new['content']) if old and raw_changed else '',
                         localDiffs={p: delta(base['sources'][p]['content'], current['sources'][p]['content'])
                                     for p in changed_sources} if base else {}))
    return dict(schema=1, currentFingerprint=digest(json.dumps(current, sort_keys=True)),
                baseFingerprint=digest(json.dumps(base, sort_keys=True)), pages=rows,
                instruction='Agent reviews diffs, imports clear plan changes, rebuilds artifacts, preserves notes; this report does not perform a merge.')


def checkpoint(state_path, current, report, resolution):
    assert resolution['currentFingerprint'] == report['currentFingerprint'], 'Stale resolution/current sources'
    assert resolution['baseFingerprint'] == report['baseFingerprint'], 'Baseline changed during review'
    decisions = resolution['pages']
    assert set(decisions) == {r['key'] for r in report['pages']}, 'Every page needs a disposition'
    allowed = {'unchanged', 'format-only', 'imported-and-built', 'published-and-built',
               'merged-and-built', 'note-only-reviewed', 'bootstrap-reviewed'}
    for row in report['pages']:
        decision = decisions[row['key']]
        assert decision['action'] in allowed and decision.get('reason'), f'Unresolved: {row["key"]}'
        if row['status'] == 'baseline-required':
            assert decision['action'] == 'bootstrap-reviewed', 'First baseline must be reviewed'
        elif row['status'] in ('notion-changed', 'both-changed', 'local-changed'):
            assert decision['action'] in {'imported-and-built', 'published-and-built', 'merged-and-built', 'note-only-reviewed'}, 'Changed content cannot be dismissed as unchanged'
        else:
            assert decision['action'] != 'bootstrap-reviewed', 'Bootstrap cannot hide later edits'
    current['resolution'] = resolution
    # Reports fingerprint only snapshot data, not the preceding resolution record.
    write(state_path, current)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'checkpoint'])
    parser.add_argument('--project', required=True)
    parser.add_argument('--snapshot', required=True)
    parser.add_argument('--config', default='notion-sync.json')
    parser.add_argument('--resolution')
    args = parser.parse_args()
    project = Path(args.project).resolve()
    config = read(project / args.config)
    folder = project / 'private/notion-sync'
    state_path = folder / 'state.json'
    base = read(state_path) if state_path.exists() else None
    if base: base.pop('resolution', None)
    current = capture(project, config, read(args.snapshot))
    # Captured time must not change the review fingerprint for the same snapshot.
    current['capturedAt'] = read(args.snapshot)['fetchedAt']
    report = compare(base, current, config)
    if args.command == 'checkpoint':
        assert args.resolution, 'Supply a reviewed resolution, never silently accept changes'
        checkpoint(state_path, current, report, read(args.resolution))
    write(folder / 'report.json', report)
    print(json.dumps({r['key']: r['status'] for r in report['pages']}, ensure_ascii=False))
    print('Baseline saved.' if args.command == 'checkpoint' else 'Private diff report written; baseline unchanged.')


if __name__ == '__main__':
    main()
