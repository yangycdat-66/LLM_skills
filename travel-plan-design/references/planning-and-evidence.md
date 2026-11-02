# Planning and evidence

## Inputs and outputs

Record the trip year, dates, time zones, school/work release times, return curfew, flight departure, latest acceptable airport arrival, number of nights, preferred start time, baggage, spending range and activity interests. Separate hard constraints from preferences. If exact dates are inferred, label the assumption and verify weekday alignment.

Build a small constraint ledger before recommending a route:

| Constraint | Value | Status/source | Consequence |
| --- | --- | --- | --- |
| Airport arrival | User's deadline | User decision | Work backward through port, baggage and road transfers |
| Departure preference | Preferred hotel pickup | Preference | Show feasibility and loss of margin |
| Hotel nights | Check-in through checkout | Date arithmetic | Assign each night exactly once |
| Activity | Course or excursion | Availability pending | Protect required training/rest time |

## Evidence labels

- **User decision:** explicitly chosen constraint or arrangement; preserve until changed.
- **Verified source:** official operator, airline, government, provider or authoritative safety source; record checked date and applicable travel dates.
- **Quote snapshot:** exact occupancy, dates, currency, room/rate, fees, cancellation and inclusions; unknown fields remain unknown. Price and inventory can change.
- **Planning estimate:** travel allowance or reserve, with a range and assumptions. Do not dress an estimate as a departure time or supplier quote.
- **Traveler account:** useful experience, not proof of current schedules, fees, access or safety.
- **Pending confirmation:** concise actionable question and responsible provider.

Prefer connected service tools where suitable. Search official sources for current requirements and schedules. Do not treat a stale timetable as future inventory, a map label as a walkable route, or a connector's generated answer as verified fact. Store source links and checked dates with the relevant claim. Never include sensitive booking codes or passport data in public assets or URL state.

## Time arithmetic

For every leg include departure point, actual terminal, mode, pickup time, journey duration, transfer/check-in/baggage time, arrival range and booking status. Distinguish road time from door-to-door time. Add durations across midnight with date-aware calculations; normalize time zones before comparing.

Work backward from the binding deadline and then calculate forward. Report earliest/latest planning arrivals and remaining margin. Test a plausible delay; if it breaches the deadline, call the connection tight. A ferry cancellation is qualitatively different from a short delay. Offer a practical alternative such as returning the previous day, while keeping the user's preferred route visibly selected if that is their decision. Do not silently substitute your preferred plan.

Exact schedule columns may contain proposed clock times, but each unbooked service must be explicitly marked proposed or pending. Keep the provider's actual cutoff separate from the user's preferred preparation time.

## Courses and water activities

Check ability, relevant qualifications and provider prerequisites. Course completion depends on demonstrated skills, weather and instructor assessment. Do not compress training to protect hotel checkout or a flight.

For scuba, verify current authoritative flying-after-diving guidance and provider requirements. Record actual last surfacing and the **first takeoff**, calculate the interval, and follow stricter individual restrictions. A calculated interval is not medical clearance. Do not invent a universal safe interval in a reusable template. Separate snorkeling, scuba and breath-hold activities in the schedule.

## Budget and hotels

Calculate each quoted stay total divided by its own nights. Search split stays for their actual date ranges; do not scale an unrelated average nightly price. Distinguish currency conversion assumptions from settlement. Keep contingency reserves separate from supplier prices.

Evaluate hotel value against usable time: a late check-in after training and early checkout may make a luxury night mostly an evening. Include checkout, luggage storage, moving time and check-in in the schedule. Label above-budget upgrades as options requiring a user decision.

Walking estimates need correct entrances and routed paths; straight-line distance is a lower bound. State whether distance is routed, approximate or unverified. Include realistic walking allowance and a transport fallback for heat, rain, darkness or equipment.
