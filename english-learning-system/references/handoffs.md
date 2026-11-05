# Shared handoffs and recovery

Use this contract for combined tasks. It is a conceptual record, not a required local file or a new database. Keep evidence in the workflow's authorized destination; quizzes and review tasks use the Notion connector only. Never publish private records in this package.

## Carry between stages

- Source identity and accessible original content; original learning date and timezone, not edit or catch-up date.
- Current task, topic, attempt and source scope; complete originals and learner corrections, editorial additions and selected expressions separately.
- Authorship: independent, prompted retry, quoted/model reading, other speaker or uncertain. Record text/audio/ASR availability and coverage gaps.
- Requested operations, existing authorization and applicable cadence; verified rules and target identities.
- Existing record/task/quiz IDs, actual review events, completed writes and pending stages. Use source identity plus operation/date/event to avoid duplicate writes; inspect current schema before choosing keys.

## Ownership

| Stage | Owner | Handoff |
| --- | --- | --- |
| Feedback and source preparation | Relevant practice workflow | Originals, corrections, chunks and evidence limits |
| Vocabulary/Speaking/Listening/Writing archive | Memo workflow | Verified Memo identity, original dates and coverage |
| Selected sentence archive and deliberate sentence-practice evidence | Natural Sentences | Verified sentence record and review event; no automatic harvesting |
| Due/overdue/extra review tasks | Review workflow | Existing source/date/node identities and selected/deferred tasks |
| Test construction, marking and reinforcement | Quiz workflow | Frozen rubric, preserved first attempt and source-linked results |
| Progress synthesis and next priorities | Coordinator/learner workflow | Dated comparisons and limited claims; no status inference |

The feedback workflow may request a Vocabulary write when authorized; the Memo writer performs it once. Speaking and Listening archives retain their own selected language; do not automatically duplicate those into Vocabulary or Natural Sentences. A direct request may authorize a deliberate cross-link or extra archive.

Creating a review task, marking it complete, logging a meaningful sentence review and promoting sentence status are distinct. The review scheduler never edits Sentence Library learning fields. Natural Sentences may record an actual authorized practice event once; preserve learner-owned completion and status. Quiz grading does not mark the source mastered or the review complete.

## Order and retries

Gather source and live rules → coach if requested → write requested archive → verify → reconcile authorized review tasks → generate/grade requested assessment from verified sources. Skip inapplicable steps; an existing source can go directly to review or assessment.

A new correction after archival updates the relevant source/Memo without losing the first attempt. Do not retroactively change a frozen published rubric; label amendments and preserve attempts according to current quiz rules.

Before retrying an ambiguous create, enumerate the target for its identity. Before retrying an update or review increment, inspect the existing content/event. Count only verified operations; keep independent stages moving when safe, but do not build on an unverified write. Do not advance recovery checkpoints across unread or unreconciled sources.

No-op requires a complete relevant read and comparison. State missing coverage separately. Do not generate empty records, silently fill missing history, or recreate schedules to compensate for unavailable sources.
