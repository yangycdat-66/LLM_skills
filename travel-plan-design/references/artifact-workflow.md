# HTML, SVG, PDF and Notion

Use this workflow when the user wants a maintained travel handbook across devices.

## Ownership and update loop

- HTML and generator sources in the private repository are the canonical plan and evidence index. Preserve original source URLs, dated quotes and explicit decision/confirmation status.
- SVG is a quick visual reference: route, daily schedule, transfer chain or curated topic sheet. Keep full-page/whole-plan SVGs as labelled reference exports, not the default mobile reading surface.
- PDF is the printable edition and offline fallback. Keep a compact field edition alongside full reference detail.
- Notion is the mobile detailed-reading and annotation surface. Use native headings, lists, checkboxes, callouts and links. Turn wide tables into vertically stacked labelled records. Preserve full source detail beneath concise summaries.
- New decisions captured in Notion must be reviewed and reconciled into the source handbook before re-exporting. Use [Notion reconciliation](notion-sync.md) to check automatically during active project work, import clear plan edits, and rebuild affected artifacts. Do not imply background or conflict-free two-way synchronization. Keep user-authored notes separate from generated source sections; never overwrite them during a refresh.

## Organization and portability

Add an artifact hub and manifest linking current HTML topics, quick SVGs, PDFs, Notion pages, evidence snapshots and historical appendices. Preserve old paths/anchors rather than moving existing artifacts just to create neat folders. Record generation time, source hashes, publication destinations and validation separately from the original evidence dates. An export date is not a new research-verification date.

Keep the main Notion dashboard short: dates, route, urgent pending confirmations and topic links. Group details by reading task, with an artifact library and a separate notes/confirmations page. Link existing visa/document pages instead of duplicating personal records. Read the connector's Markdown/upload documentation before writes. Use explicit local-file uploads; keep reusable upload URLs/tokens out of source, logs and manifests. Attach concise PDFs and route images; bulky original HTML bundles remain downloadable files, not native Notion content.

For offline HTML preview, embed needed assets or provide a complete portable bundle. Test an isolated preview with sibling-file access blocked, not only file:// or a local server. Inline SVG avoids sibling-file resolution failures. Prefix SVG definition IDs when combining documents. Label reduced-resolution preview photos; keep original downloads available. Explain font portability, static snapshots, and browser-only state limitations.

## Verification

Check source-topic coverage, local links, unique IDs, table conversion without text/link loss, artifact sizes, source hashes and note preservation. Test narrow/desktop layouts, zoom, selection and actual download content. Render quick SVGs and PDF pages; inspect for clipping, missing glyphs and bottom-content loss. Check connector warnings and actual publication results; distinguish local build, remote publication, and phone-device verification.

Before travel, make essential Notion pages available offline individually and save the compact PDF on the device. Verify actual phone behavior when available. Do not claim notes/choices synced or files uploaded merely because a manifest was generated.
