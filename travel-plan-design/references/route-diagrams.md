# Route diagrams

Preserve a visible diagram near the top of the itinerary. The diagram answers where the traveler goes, in which order, by which mode, and when they must return. A decoration that omits the return deadline is not sufficient.

Prefer editable SVG/HTML for route schematics: text, arrows and geometry remain maintainable and exact. Use a raster illustration only when it serves an explicit visual request; do not replace a precise route diagram with uneditable invented geography.

Use `assets/route-template.svg` for a compact schematic starter, then redesign the geometry to fit the actual itinerary. It deliberately contains placeholders, not geographic claims. Label schematics as not to scale.

For multiple excursions, use separate route colors and a legend. The Cebu visual used teal for the day trip, orange for the weekend and purple for the post-school trip. Use solid outward paths and dashed returns, with distinct labeled direction arrows. Repeat route names so information is not color-only. Ensure each SVG marker has the route's color; a black default marker can obscure the visual system.

Keep labels in reserved boxes outside paths. Curved arrows must not cross hotel or destination labels. Use a quiet map silhouette only if geographically credible; otherwise use a schematic timeline or node layout. Set `viewBox`, accessible title/description and responsive width.

Show dates, transit modes, overnight counts and key return deadlines. Keep unselected hotel names out of the diagram; use a destination/base label or bind the name to arrangement state. Service times remain proposed until verified/booked.

Include a text equivalent or detailed schedule below the figure. Inspect the SVG after rendering at its intended size and a narrow width. Check labels, overlap, return curves and arrowheads. A correct XML parser result is not visual verification. If distributing a PNG, regenerate it from the final SVG after the last edit so the two versions match.
