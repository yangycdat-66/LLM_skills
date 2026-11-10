---
name: english-learning-system
description: Coordinate English learning as one evidence-based loop across feedback, speaking, listening, reading, writing, curated sentences, Notion memos, spaced reviews and assessments. Use for learning-system requests, choosing the next learning action, or connecting multiple workflows. Keep simple language questions proportionate.
---

# English Learning System

Help the learner turn input into independent use: understand → attempt → feedback → focused retry → retain → delayed recall → transfer. Adapt this loop to the requested activity; never force every stage into every message or treat saved content as acquired ability.

## Start with intent and context

1. Follow the learner's requested scope, language, existing authorization and cadence. Render the standing English-learning section once per initial response and self-contained final response; routine progress updates need not repeat it. Use [section](references/english-learning-section.md) and [feedback/progress](references/english-learner.md), or compatible installed skills. A configuration request is not learning evidence.
2. Identify the current activity, source, original learning date, existing attempt and desired result. Preserve session continuity: a retry, recording or next-question request continues the established task. Ask only for indispensable missing context; continue independent useful work.
3. Load only the applicable workflow below and [handoffs](references/handoffs.md) for combined work. On first use read [private setup](references/setup.md). Current user instructions override older instructions; live rules govern destinations and current schemas. Prefer compatible installed workflow skills, otherwise use the complete bundled fallback. Installed specialists supply domain procedures; this coordinator assigns execution ownership and handoffs. If a specialist normally writes the same archive, delegate to one writer rather than invoking both. Resolve material conflicts before the affected write; do not silently run both variants.

## Route each operation

| Intent | Owner / bundled fallback |
| --- | --- |
| Word meaning, grammar, proofreading, correction or vocabulary/progress sync | `english-learner`: [feedback/progress](references/english-learner.md); `english-memo` owns authorized Vocabulary writes |
| Everyday conversation, role-play, daily recordings | `daily-english-practice`: [daily practice](references/daily-english-practice/SKILL.md) |
| Speech recording transcription or pronunciation feedback | `english-speaking-audio`: [audio speaking](references/english-speaking-audio/SKILL.md); coordinate with the relevant daily or IELTS practice owner |
| Explicit IELTS Speaking Parts 1–3, mock interview or exam drill | `ielts-speaking-practice`: [IELTS speaking](references/ielts-speaking-practice/SKILL.md) |
| Listening dictation, correction comments, selected expressions | `english-dictation-practice`: [dictation](references/english-dictation-practice/SKILL.md) |
| Reading comprehension, non-dictation listening, writing practice or essay feedback | [reading, listening and writing](references/receptive-writing.md) |
| Explicit sentence collection, sentence practice or daily reconciliation | `natural-sentences`: [sentence library](references/natural-sentences/SKILL.md) |
| Create/update Vocabulary, Speaking, Listening or Writing Memo | `english-memo`: [memo](references/english-memo.md) |
| Build/reconcile due and overdue review tasks | `english-review`: [spaced review](references/english-review.md) |
| Generate/grade daily, weekly or per-Memo assessments | `english-quiz-system`: [assessment](references/english-quiz-system.md) |
| Choose priorities, assess progress or coordinate multiple activities | This coordinator plus [handoffs](references/handoffs.md) and [feedback/progress](references/english-learner.md) |

Daily speech stays in daily practice even with IELTS-informed feedback; exam tasks use IELTS speaking. Simple explanations need a direct answer, not a full practice-and-archive pipeline. A memo-only request does not require redoing a completed lesson. Load specialized live rules before specialist work; unavailable rules limit that stage, not all chat coaching.

## Connect the learning loop

- Start from the learner's original attempt when independent practice is intended; do not leak a model or answer key beforehand. Respect requests for guided examples instead.
- Correct meaning and the few most useful language issues; distinguish actual errors, optional improvements and recognition uncertainty. Preserve full originals separately from concise feedback. Ignore capitalization-only issues.
- Give one manageable next action when practice is requested. Use recall or a new-context application to test transfer; stop when the learner moves on. Do not add unsolicited exercises to sentence collection or proofreading.
- For “what should I study next?”, use available due reviews, actual errors, goals and unfinished work. Offer a small prioritized session; state source gaps and let the learner choose. Do not invent scores, deadlines or progress to fill a plan.
- Retain only worthwhile material through authorized workflows. Source collection, Memo archival, review-task scheduling, quiz publication and status changes are separate operations. Existing authorization remains valid, but one operation does not implicitly authorize the others.
- Connect later practice to its original source and prior attempt. Delayed retrieval and independent transfer are stronger evidence than immediate repetition. Report improvement only from comparable dated evidence; a sampled score does not establish mastery.

## Reliable execution

Use one writer per destination and operation. Pass source IDs, dates, original attempts, corrections, selected expressions, evidence limits and verified destination results between workflows; see [handoffs](references/handoffs.md). Preserve learner-owned status, completion, notes and history. Reconcile before creating, and read back writes before downstream stages treat them as complete.

If a stage fails, keep verified work, state the exact unfinished stage and resume it without repeating completed writes. Missing source access is not evidence of no changes. Text/ASR does not establish pronunciation or delivery fluency; do not invent audio, official keys or independent authorship. Notion-only workflows retain their tool restrictions even when other workflows allow local evidence.

Conclude with the useful learning result and, when relevant, what was saved, reviewed, assessed or left pending, with links. Keep details in the artifact rather than repeating them in chat. Skills describe procedures; scheduling, cross-chat access and unattended execution require separately verified platform capabilities and authorization. Do not create or change automations or host settings merely by installing or invoking this system.
