# Validation and known pitfalls

Choose checks proportionate to the change. Do not create tests that merely restate the implementation. For reused assets, repeat checks after meaningful edits or failures, not indefinitely.

## Content and planning

- Recalculate flight and transfer margins, dates/weekdays, time zones and every overnight assignment. A delayed service should not retain the original arrival promise.
- Verify the same working route, deadlines and current hotel labels across pages and diagram. Do not overwrite user's choices when adding alternatives.
- Confirm source links, date/occupancy scope for prices, and labels for assumptions. Course availability, exact rates, walking routes and future transport inventory may remain pending.

## HTML and behavior

- Parse HTML; find duplicate IDs, missing local files and broken anchors. Verify one global navigation block and one include per shared asset.
- Test hover enter/leave, pinned persistence, switching back to hover, touch/click, Escape and keyboard focus. Verify section search and current-section indication after scrolling.
- Test a menu link into closed details; the target must open and become visible below the sticky header. Preserve old filters, print controls and their required IDs.
- For editable arrangements, test old backups, single and split stays, date coverage, invalid imports, missing storage, cross-page links and page-selector state transfer. Ensure notes render as text.
- Rerun generators and compare outputs; the second run should not add duplicate UI or lose content.

## Visual inspection

Inspect the actual page at desktop and narrow viewport sizes, including hover and pinned navigation, longest table, route diagram and print preview. Check contrast, focus, overflowing headings, panel overlap and image legibility. Render final SVG/PNG separately if used.

If browser access or rendering is blocked, stop that access path and report the limit. Do not bypass an access block by rehosting. Structural/logic checks can continue but are not evidence of visual correctness. Do not claim a PDF was delivered unless it was actually generated and inspected.

## Learned failure cases

1. Removing all `nav` elements erased a timeline's filter/print toolbar. Target only the obsolete global navigation.
2. Adding a top anchor to a main element that already had an ID created duplicate ID attributes. Preserve the original and anchor a wrapper.
3. Styling every nested `main` broke a timeline grid. Use direct-child scope for handbook shell layout.
4. Selecting “On hover” left the button focused, keeping the panel open. Release pointer focus while retaining keyboard behavior.
5. A hotel quote's stay total was mistaken for a nightly rate; normalize only against that quote's actual nights.
6. A claimed walking distance was shorter than straight line. Verify the route and entrance before recommending walking.
7. A late SVG curve edit left the PNG stale. Render the final source after all geometry changes.
8. A supplier timetable was treated as future availability. Keep a proposed sailing visibly pending until the actual date is confirmed.
