---
name: travel-plan-design
description: Create and maintain a personal travel handbook with evidence-based itineraries, hotel decisions, activity or course pages, editable route diagrams, and a consistent HTML design. Use for HTML/source organization, SVG quick views, PDF print editions and Notion mobile reading, and when planning or reorganizing a trip handbook, updating its itinerary and hotel arrangements, or extending its navigation and visual style. Captures the user's Cebu handbook workflow but adapts to other destinations. Do not use for an isolated travel fact, a booking transaction alone, or an unrelated website.
---

# Travel plan design

Turn constraints and research into a usable personal handbook. Preserve the user's decisions and existing content while making the current plan easy to find and update. Produce working files, not only a proposed structure.

## Start from the existing work

1. Before any edits, fetch the configured GitHub upstream and ensure the local project includes its newest commit, preserving uncommitted work. Follow [Notion reconciliation](references/notion-sync.md) for the Git preflight and automatic checks for Notion edits. Then inspect project instructions, existing HTML, shared assets, generators and saved arrangement state. Read the current page before changing it. Identify the source of generated sections and edit that source when possible.
2. Recover dates, local time zones, hard deadlines, accommodation nights, budget, interests and decisions from the conversation and current files. Ask only for consequential missing information; continue independent work. Do not ask the user to repeat established preferences.
3. Back up files affected by a structural migration. Preserve page-specific controls, stable anchors, diagrams, original evidence and user-owned state. Do not replace a working handbook with the starter template.

For scratch exports, destination-gallery placement, matching an existing Notion handbook, paired diagrams and upload checks, read [Draft reconciliation and publication lessons](references/publication-and-draft-lessons.md).

## Plan from constraints to decisions

Read [Planning and evidence](references/planning-and-evidence.md) for research, transport arithmetic and activity constraints. Build the timeline backward from hard deadlines, then check the whole journey forward. A feasible timetable is not a confirmed reservation.

Read [Pages and arrangements](references/pages-and-arrangements.md) before splitting pages or adding hotel choices. Keep the selected working itinerary, course details and hotel comparison in their own pages, with a shared current-arrangements summary. Treat “considering” as a shortlist, not consent to select or book.

Use current primary sources for volatile claims; separate user decisions, sourced facts, quotes, estimates, anecdotes and pending confirmations. Link the evidence beside the claim. Do not reuse the Cebu example's old prices, dates, suppliers or medical guidance as current facts for another trip.

## Build the handbook

For maintained HTML, SVG, PDF and Notion outputs, follow [Artifact workflow](references/artifact-workflow.md). Keep HTML/source links canonical, SVG concise, PDF printable, and Notion readable on phones with separate notes. Automatically check and reconcile clear Notion plan changes during active project work using [Notion reconciliation](references/notion-sync.md); rebuild affected artifacts and retain unresolved conflicts for review.

Read [HTML style and navigation](references/html-style.md). Match the existing warm ivory, dark teal and sage style unless the user requests another direction.

- Keep a visible, editable route diagram near the top of the itinerary. Read [Route diagrams](references/route-diagrams.md) before changing it. Reorganization must not delete or hide it.
- Use one sticky top-level page menu showing the current page, plus a right-side section menu with hover and pinned modes. Avoid duplicate global navigation rows. Keep local search, touch/click and keyboard access.
- For a new handbook, copy `assets/page-template.html`, `assets/handbook-base.css`, `assets/handbook-navigation.css`, `assets/handbook-navigation.js` and `assets/route-template.svg` into its output folder. Replace demonstration text, dates, route geometry, page options and section anchors. The starter is a single-page demonstration, not an itinerary recommendation.
- For an existing handbook, reuse its assets and generator; use the bundled assets as a reference. The optional `window.HotelArrangements` integration in the navigation script is an adapter, not a bundled hotel editor.
- Keep readable summaries above detailed evidence. Use tables for comparisons, collapsible details for supporting material, and clear time/deadline callouts. Do not collapse the route or current decisions.

## Verify and deliver

Read [Validation and known pitfalls](references/validation.md). Check night coverage, transfer arithmetic, link targets, unique IDs, state preservation and navigation. Render and inspect the changed page at desktop and narrow widths when tools allow; inspect exported diagrams separately. If visual inspection is blocked, report it rather than claiming appearance is verified.

Deliver links to the actual changed files, explain what changed and what was tested, and identify remaining confirmations. Do not send supplier messages, book, pay or publish without applicable authorization. Draft enquiries locally when needed.

## Maintain this skill

When the user asks to accumulate a new lesson, update the relevant reference or reusable asset rather than copying another trip's entire history into this file. Preserve the distinction between reusable rules and dated examples. After asset changes, rerun the relevant checks in `evals/evals.json`; distinguish recorded test prompts from tests actually executed.
