import copy
import json
import tempfile
import unittest
from pathlib import Path
from notion_sync import capture, compare, checkpoint, normalized


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'plan.html').write_text('Leave at 08:00', encoding='utf-8')
        self.config = {'pages': {'daily': {'id': 'abc', 'sources': ['plan.html']}}}
        self.incoming = {'pages': {'daily': {'id': 'abc', 'complete': True, 'content': '<h2>Plan</h2>\nLeave at 08:00'}}}
        self.base = capture(self.root, self.config, self.incoming)

    def current(self):
        return capture(self.root, self.config, self.incoming)

    def status(self):
        return compare(self.base, self.current(), self.config)['pages'][0]['status']

    def test_remote_only_and_dual_changes(self):
        self.incoming['pages']['daily']['content'] = '<h2>Plan</h2>\nLeave at 09:00'
        self.assertEqual(self.status(), 'notion-changed')
        (self.root / 'plan.html').write_text('Leave at 10:00', encoding='utf-8')
        self.assertEqual(self.status(), 'both-changed')

    def test_local_only_and_formatting(self):
        self.incoming['pages']['daily']['content'] = '<toggle heading="h2" color="gray_bg">Plan\n\nLeave at 08:00\n</toggle>'
        self.assertEqual(self.status(), 'format-only')
        (self.root / 'plan.html').write_text('Leave at 09:00', encoding='utf-8')
        self.assertEqual(self.status(), 'local-changed')

    def test_dates_links_checkboxes_not_erased(self):
        for old, new in [('08:00', '09:00'), ('[x]', '[ ]'), ('https://a.test', 'https://b.test'), ('<date start="2026-11-14" />', '<date start="2026-11-15" />')]:
            self.assertNotEqual(normalized(old), normalized(new))

    def test_incomplete_wrong_or_missing_page_rejected(self):
        for change in [{'complete': False}, {'truncated': True}, {'unknown_block_count': 1}, {'unknown_block_ids': ['x']}, {'id': 'wrong'}]:
            incoming = copy.deepcopy(self.incoming)
            incoming['pages']['daily'].update(change)
            with self.assertRaises(AssertionError): capture(self.root, self.config, incoming)
        with self.assertRaises(AssertionError): capture(self.root, self.config, {'pages': {}})

    def test_missing_source_rejected(self):
        (self.root / 'plan.html').unlink()
        with self.assertRaises(AssertionError): self.current()

    def test_stale_resolution_and_unresolved_change_rejected(self):
        current = self.current()
        report = compare(self.base, current, self.config)
        resolution = {k: report[k] for k in ('currentFingerprint', 'baseFingerprint')}
        resolution['pages'] = {'daily': {'action': 'unchanged', 'reason': 'No difference'}}
        target = self.root / 'state.json'
        checkpoint(target, current, report, resolution)
        self.assertTrue(target.exists())
        self.incoming['pages']['daily']['content'] = 'A new hotel decision'
        new_report = compare(self.base, self.current(), self.config)
        with self.assertRaises(AssertionError): checkpoint(target, self.current(), new_report, resolution)
        resolution.update({k: new_report[k] for k in ('currentFingerprint', 'baseFingerprint')})
        with self.assertRaises(AssertionError): checkpoint(target, self.current(), new_report, resolution)

    def test_first_capture_and_mapping_change(self):
        self.assertEqual(compare(None, self.current(), self.config)['pages'][0]['status'], 'baseline-required')
        config = copy.deepcopy(self.config)
        config['pages']['daily']['notes'] = True
        with self.assertRaises(AssertionError): compare(self.base, capture(self.root, config, self.incoming), config)


if __name__ == '__main__': unittest.main()
