---
name: english-learning-system
description: Coordinate the user's English-learning feedback, progress evidence, Notion memos, spaced reviews, and daily, weekly or full-Memo quizzes. Use for an English learning system request or a combination of these workflows.
---

# English Learning System

Coordinate the requested learning workflows without turning a request for one into permission to run all of them. For every-message feedback, follow the user's standing instructions and the dedicated `english-learning-section` skill when available, or its [bundled fallback](references/english-learning-section.md). If the existing `english-learner` skill is active, render the section only once.

## Choose workflows

Read the corresponding bundled reference for each requested operation. If a compatible installed skill with the same name exists, use its current instructions instead of the bundled guidance; later user instructions and live Notion rules take precedence. The references are portable fallbacks, not independent background agents.

| User intent | Workflow | Bundled reference |
| --- | --- | --- |
| Feedback, local progress records or authorized vocabulary sync | `english-learner` | [learner](references/english-learner.md) |
| Create or update an evidence-backed Vocabulary, Speaking, Listening or Writing Memo | `english-memo` | [memo](references/english-memo.md) |
| Reconcile the spaced review list | `english-review` | [review](references/english-review.md) |
| Generate or grade a daily, weekly or full-Memo quiz | `english-quiz-system` | [quiz](references/english-quiz-system.md) |

For a combined request, follow the relevant workflows in evidence order: gather originals and current rules, update a requested memo, reconcile a requested review, then generate or grade a requested quiz. Do only applicable stages. Coordinate vocabulary archiving so the same material is synced once; check existing pages and identities before each write. Respond to the actual task as well as providing feedback.

## Common boundaries

- On first use of a workflow, read [private setup](references/setup.md) and discover or ask for the settings needed for that workflow. Reuse existing verified settings; do not demand all settings upfront.
- Discover and verify the user's Notion destinations and current rules; keep private configuration and page IDs outside this shareable folder. Follow the specific workflow's connector restrictions. If unavailable or incomplete, report the precise gap rather than inventing live state.
- Keep original attempts, user edits, notes, status, completion and independent summaries under the learner's control. Link evidence, use the actual learning date, distinguish quotations, ASR and editorial suggestions, and qualify unsupported claims. Do not infer pronunciation or fluency from text.
- Read back and verify authorized writes; do not create duplicates, empty records, schedules or automation by implication. The system coordinates instructions, not a background service.
- For installation or host compatibility, follow the host's documented skill discovery mechanism. A skill alone cannot guarantee a section on every turn: persistent user/project instructions or host-supported auto-loading are needed, and explicit later user instructions override them. Do not change host configuration unless the user authorizes it.
