# HTML style and navigation

## Visual language

| Role | Default |
| --- | --- |
| Page | Warm ivory `#f5f4ec` |
| Main text | Dark teal `#163b39` |
| Secondary text | `#5e706c` |
| Hero accent | Sage `#668665` |
| Highlight | Pale lime `#cfec90` |
| Borders | `#dbe2d8` |
| Cards | White, 18px radius, 24–25px padding |
| Typography | Local system sans-serif, CJK fallback, body 16px/1.55 |
| Hero | Short two-line heading, responsive 38–70px, tight line height |
| Layout | Approximately 1100–1200px maximum content width; generous spacing |

Use `assets/handbook-base.css` as the core token/component sheet. Use subdued shadows and clear contrast. English headings may have smaller Chinese labels. Keep source dates and status visible; implementation details do not belong in the travel flow.

Use comparison tables only for parallel information. Wrap wide tables in a horizontally scrollable labeled region; avoid body overflow. On narrow screens collapse grids to one column. Print styles hide navigation and preserve readable content; expand details for printing and restore their state afterward.

## Two-level navigation contract

**Top-level:** one sticky bar remains visible during scrolling. Its page selector names the current page and lets the user switch to every handbook page. Show the current local section when space permits. Include Print/PDF without claiming the browser created a PDF automatically.

**Second-level:** a narrow right-edge “On this page” tab opens the current page's section list. Desktop mouse entry reveals it; mouse exit closes it after a short grace period. “Pinned” keeps it open and reserves space on wide screens. “On hover” restores automatic opening. Clicking works on touch, and keyboard users can reach the panel without hover.

Requirements: active page/section indication, section search, stable anchors, `aria-expanded`, pressed mode state, focus visibility, Escape dismissal, reduced motion support and print cleanup. Clicking a target inside collapsed details must open its ancestor details first. Keyboard focus within the panel must prevent accidental closing. Pointer clicks on the hover-mode button should release focus so it does not keep the panel stuck open.

Persist mode under a handbook-specific storage key; the starter uses `travel-handbook-section-mode`, which should be scoped for independent handbooks. When navigation is generated, rerun the generator twice to verify it does not add duplicate blocks, scripts or IDs.

## Integration precautions

Do not remove every `nav`: local filters and toolbars may be functionally important. Replace only the identified global navigation block. Keep existing IDs on main containers; add a new top anchor to a wrapper instead of duplicating an `id` attribute. Scope layout overrides to direct body children, not every nested `main`.

The starter has a single selected page and working local sections. For a multi-page handbook add only real destination pages to its selector. Keep the section list aligned with actual headings and summaries. Prefer extending an existing index generator to manually duplicating every menu.
