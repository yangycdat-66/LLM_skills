---
name: notion-workflow
description: Create and organize the user's Notion pages with native page icons, native tables of contents, restrained block background colors, and mobile-friendly reading structure. Use whenever creating, editing, organizing, or publishing Notion content, in any project or standalone conversation. Do not use for read-only lookups or unrelated artifact formatting.
---

# Personal Notion workflow

Use this as the user's global, project-independent page-design convention. Load it for every Notion content-writing task; combine it with domain skills when relevant. Apply it to pages within the requested scope, including relevant child pages. Preserve existing content, evidence and user notes.

## Native page essentials

- Set an actual native page icon through the page icon property. An emoji typed into the title or a callout does not satisfy this rule. Choose one meaningful emoji or supported Notion icon; retain an appropriate existing native icon. Do not rename existing pages just to remove title emoji unless requested.
- Include exactly one native table-of-contents block near the top of every page, following a short introduction. Use genuine headings so the contents is useful. Do not substitute a manually typed list of links. On short pages, keep a few meaningful headings rather than padding the page.
- Use native blocks and restrained background colors for scanning: blue for section navigation, yellow for pending items or deadlines, gray for sources/history/update notes. Green may identify explicitly confirmed items; never infer confirmation from a color. Reserve red for actual critical warnings. Labels must carry the meaning without relying on color alone.
- Keep body text mostly uncolored. Use a single-column reading order, short paragraphs, labelled records for wide comparisons, and toggles for secondary reference detail. Keep current decisions, route diagrams, deadlines and essential actions visible.

## Editing safely and efficiently

1. Fetch the requested page and relevant children. Inspect truncation/unknown-block metadata before editing. Preserve page IDs, child-page/database tags, files, native mentions, existing checkmarks and notes.
2. Prefer connected Notion tools. Read their current schema and `notion://docs/notion-flavored-markdown-spec` before content writes; do not guess API fields or block syntax. Use native mentions for Notion destinations and date mentions where appropriate.
3. Use targeted edits to headings, introductory blocks and missing contents. Set icons through `update_properties` with the native `icon` field. Keep edits idempotent: no duplicate contents, repeated introductions or accumulated decoration on later runs.
4. Current connector syntax supports `<table-of-contents color="gray" />`, `<h2 color="blue_bg">Section</h2>` and `<callout icon="💡" color="yellow_bg">Attention text</callout>`. Recheck live documentation if capabilities change. CSS/HTML styling is not a native Notion substitute.
5. If a required native feature is unavailable in the connector, use the authenticated UI when available and authorized. Report any remaining limitation; do not present an imitation as the native feature.
6. Inspect write results and resolve warnings. Do not refetch merely to verify a warning-free update. When visual review is available, inspect a representative long page and dashboard at narrow width; otherwise state that actual mobile appearance remains unverified.

## Generated reading copies

Update the generator as well as live formatting so a later refresh retains the convention. Icons are page metadata and must be applied by the publishing step; contents and colored blocks belong in generated content. Never let a generated refresh replace user-owned notes. Follow the relevant project's source-ownership rules and preserve confirmed versus pending facts. Formatting changes do not reverify source facts.

## Keep improving and publish

Incorporate explicit new preferences into the relevant rule, avoiding duplicate or trip-specific instructions. Keep the discoverable personal copy and repository copy aligned. Validate frontmatter with skill-creator's quick_validate.py when available and test changes on the authorized real task. Report what was actually checked.

Maintain the standalone repository copy at `notion-workflow/SKILL.md` in `yangycdat-66/LLM_skills` and the personal installed copy at `~/.codex/skills/notion-workflow/SKILL.md`. Do not embed this skill in a specific project. Before Git writes inspect status and stage only intended files; for connector writes fetch existing content first. Preserve unrelated work and repository visibility. Use ordinary commits and fast-forward updates, never force-push. Publish only reusable instructions: no private page content, page IDs, attachments, credentials or user-note snapshots. Future edits do not authorize unrelated remote publishing.
