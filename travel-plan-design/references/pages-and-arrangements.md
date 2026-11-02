# Pages and arrangements

## Keep three different questions separate

| Page | Main question | Contents |
| --- | --- | --- |
| Travel plan | What am I doing, when and how? | Visible route diagram; current decisions; day-by-day schedule; transport; overnight names; deadlines; budget and pending confirmations |
| Course/activity | What does this activity require? | Provider evidence; requirements; proposed lessons; costs and inclusions; preparation; safety constraints; enquiry draft |
| Hotels | Which hotel should I choose? | Comparison; reasons and trade-offs; exact dates and stay totals; positions and walk routes; luxury alternatives; editable arrangement ledger |

Other handbook topics can include transport, payments, food, documents, medical information, customs and trip ideas. Use links rather than repeated comparison tables. The itinerary may show hotel decisions and practical transfers, but the course page should not become a hotel decision page.

The itinerary is the current working route. It may still contain pending supplier confirmation; “final route” does not mean every ticket is booked. Keep alternatives in a clearly labeled optional section, not interleaved as if all will happen.

## Current-arrangements ledger

Use `undecided → shortlisted → selected → booked` statuses with explicit labels. Default to undecided unless user evidence establishes another status. The assistant's recommendation must not become the user's selection. A click in the handbook changes a planning record; it does not book a room.

Suggested fields: trip ID/version, check-in/out dates, hotel, status, quoted stay total/currency, rate details, notes and last update. Model dates rather than fixed “night 1” labels when possible. Each overnight date belongs to exactly one stay; checkout day is not another night.

Support single base and split stays where relevant. Derive the itinerary's nightly hotel labels from this ledger. A luxury upgrade should not discard the ordinary base option or silently overwrite existing saved bookings. Show the all-in accommodation delta and moving-day logistics.

## Persistence boundaries

- Validate schema, allowed statuses, dates, finite nonnegative totals and text limits. Render free text with `textContent`, not HTML interpolation.
- Version the schema and migrate old records without dropping user-owned decisions. Provide JSON export/import if arrangements are editable.
- Browser storage does not rewrite the HTML, back it up to disk, or synchronize devices. `file://` storage behavior varies; test actual page transitions.
- When needed, carry a minimal, nonsensitive arrangement object across local-page links in a validated encoded hash. Keep the destination's section anchor intact. Explain that shared links can expose encoded notes; exclude personal booking secrets.
- Preserve state across all top-level navigation paths, including the page selector. Do not update only ordinary links and forget the selector.
- If storage is unavailable, retain an in-memory state and a usable export/transfer fallback. Report limitations plainly.

The bundled navigation accepts optional `window.HotelArrangements.getCurrent()` and `.linkWithState(destination, state)`. Build or adapt the actual editor for the new trip; no hardcoded dates or hotel list are bundled.

## Existing Cebu project reference

The originating workspace is `Philippines_study`, with pages `Philippines_My_Trip.html`, `Philippines_OW_Plan.html`, `Philippines_Hotels.html` and shared `hotel-arrangements.js`. The navigation generator is `scripts/build_handbook_navigation.py`. Inspect these files if working in that project; do not assume they exist elsewhere or copy their personal dates into a new trip. This reference records architecture as of 2026-11-02, not current travel evidence.
