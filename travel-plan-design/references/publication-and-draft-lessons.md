# Draft reconciliation and travel publication

Reusable lessons from applying the handbook workflow. Examples are synthetic; do not copy a traveler's bookings, personal identifiers or dated prices into other trips.

## Resolve a scratch export before designing

- Preserve the uploaded original and record the basis of the edited plan. An explicit dated section that says it replaces earlier arrangements takes precedence for those facts; physical position at the end of an export does not establish recency.
- Build a small conflict ledger: fact, competing values, chosen source, status and consequence. Retain unaffected details. Ask only when a consequential conflict remains unresolved.
- Recalculate weekdays, all hotel nights, meal totals and transfer margins. If a title says five days but dates span seven calendar days and six nights, state the actual dates and explain the five main sightseeing days.
- A seminar ending at 11:00 makes an 11:02 departure from a distant railway station impossible. Mark the original ticket as requiring change; an afternoon candidate remains unconfirmed until the actual changed order is supplied.
- Distinguish selected, user-reported booked, and independently checked. “Accommodation determined” need not mean paid or booked. Do not promote it.
- Keep transport changes complete: pickup date/location, return location, fuel or charging assumptions and old orders needing amendment. Do not leave obsolete car pickup instructions elsewhere.
- Recompute all budget inclusions. If breakfast is newly included, remove the obsolete breakfast reserve. A meal budget with no remaining contingency must not be described as including one. Label meals plus admission as a partial total, not the whole trip cost.
- Editing a supplied plan does not establish current service availability. Carry source dates and clearly label unverified prices, restaurant hours, candidate trains and ticket-release rules.

## Match the existing Notion hierarchy and visual language

Before publishing, fetch the Travel hub, its destination database/schema, a comparable destination page and a comparable dated itinerary. Inspect actual hierarchy, property names, card conventions and content style, not just page titles.

The established destination-gallery pattern is:

Travel → destination gallery → destination page → dated trip plan → topic pages.

Use destination names such as Yunnan or Philippines for gallery cards. Put an individual dated tour inside its destination page. Reuse an existing destination when available. Never turn a dated itinerary into a destination card merely to make it appear in the gallery.

- Match the reference dashboard: short date/time-zone callout, urgent deadline callout, table of contents, visible route image, colored section headings and native topic links.
- Keep the dashboard short. Use topic pages only where useful: daily itinerary, accommodation/transport, food/budget, preparation, files/history and separate notes/new confirmations. Do not force irrelevant categories or inflate a simple trip.
- Daily details should be readable on phones: concise summary first, expandable dated sections, short labeled records rather than wide tables. Keep full evidence reachable.
- Fetch before changing or moving content. Preserve page IDs, topic children, attachments and user notes. Use schema-backed destination properties; do not modify unrelated gallery settings.
- A moved or newly created child page already adds a visible child-page block. Do not also insert a mention to the same itinerary beside it. After creating/moving, inspect the parent's exact saved content and leave one visible entry per child in simple destination indexes.
- Dashboards may intentionally have both a topic navigation menu and child blocks; keep their roles clear. Do not replicate a navigation menu on a simple one-trip destination page.
- A ZIP export's inaccessible source page ID does not mean all Notion access is broken. Find the requested hub through the connection. Never overwrite an unrelated similarly named page.
- Local creation, Notion publication and visual inspection are separate outcomes. A selected page or a request for a local draft alone does not authorize publishing; use the user's actual instructions. Once publication is requested, carry it through and verify the result.

## Deliver paired visual plans

When asked for concise and detailed diagrams, provide both, based on the same reconciled facts:

1. **Concise route:** stops in order, dates and overnight counts, mode labels, key departure/return deadlines, urgent pending items and a clearly scoped budget.
2. **Detailed itinerary:** chronological daily timeline, practical transfers, overnight name/status, meals/budget and operational reminders.

Reuse the reference palette, typography and card rhythm. Prefer exact editable SVGs with matching PNG previews, not an invented geographic map. A schematic timeline is suitable when accurate map geometry is unavailable. Keep labels away from paths, use mode labels as well as colors, and label the graphic as schematic.

- Keep candidate trains and pending changes visibly provisional in both diagrams; match the native reading pages.
- Supply a text equivalent and editable originals. A large image is a quick reference, not the sole mobile reading surface.
- Render and inspect each final PNG and every exported PDF page for clipping, CJK glyphs, cramped text and bottom-content loss. XML validation alone is not visual review.
- Rendering paths can differ in font metrics. If an SVG cannot be rendered and checked, identify that limit; inspecting a separately drawn PNG does not prove the SVG appearance.
- Include the concise diagram on the trip dashboard and the detailed diagram on the daily itinerary page. Put original SVGs and PDFs in the file area or the established “carry/print” section.

## Upload and export reliability

- Read current connector upload instructions. Prepare each upload, send the required multipart request with all returned headers, check the actual result, then use the returned media source in a page update.
- Never print upload credentials or commit upload URLs, tokens or temporary upload configs. Keep transient configuration private and delete it afterward.
- Do not equate a prepared upload URL with a completed upload. Verify each file separately; do not claim a PDF is attached because the images succeeded.
- Large image-only PDFs can exceed service or workspace limits. Inspect the actual error/status. Compress appropriately while preserving readable text, or provide the smaller original/vector artifact; do not assume all HTTP failures are size failures.
- Distinguish a vector/text PDF from a raster-image PDF. Avoid claiming selectable text or universal font portability without testing.
- Separate a two-page visual export from a two-page A4 text field edition. State the actual page sizes and print scaling; a tall timeline is not automatically A4.
- Refetch when needed to verify media blocks, parentage, duplicate entries or warnings. Do not expose local filesystem paths as downloadable Notion attachments.

## Completion checklist

- [ ] Destination gallery contains a destination card, with the dated trip beneath it.
- [ ] One itinerary entry on the destination index; no accidental mention/child duplicate.
- [ ] Existing Notion visual conventions followed; notes and topic children preserved.
- [ ] Current version decisions traced; impossible connections and stale orders flagged.
- [ ] Nights and partial budget totals reconciled; booking labels retain provenance.
- [ ] Concise and detailed diagrams agree with the reading plan.
- [ ] SVG/PNG/PDF checks distinguish structural validation from actual visual inspection.
- [ ] Every claimed remote attachment and page write succeeded.
