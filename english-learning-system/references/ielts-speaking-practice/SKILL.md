---
name: ielts-speaking-practice
description: "Run IELTS Speaking Parts 1, 2 and 3 practice, mock interviews, focused opening or grammar drills, and feedback on spoken or typed answers. Use when the user asks to practise IELTS speaking, continue a speaking topic, review a speaking recording, or move to a relevant next question; not for listening dictation, writing tasks, general English corrections or memo-only requests."
---

# IELTS Speaking Practice

Help the learner turn corrected language into usable speech through an unassisted attempt, evidence-bounded feedback, one realistic target answer, a focused retry and optional transfer. Use the user's current IELTS Speaking Practice System; the verified baseline is Version 1.1. Do not promise a band score from a model answer.

## Authority and integration

- Read current conversation instructions first. On starting or resuming this workflow, discover and fetch the user's current `IELTS Speaking Practice System` in Notion using their existing private binding or exact-title search. Read the complete rules including toggles; report gaps. Reuse a page already fully fetched for this active task. Do not repeatedly fetch it on each short retry. Refresh when the user reports an update or a conflict appears.
- Later user instructions and live rules override this baseline. Never silently downgrade to Version 1.0 or claim live rules were checked when unavailable. Continue chat coaching with the verified baseline and a stated limitation when necessary.
- Coordinate with `english-learning-system`. If the standing English-learning-first preference is active, use `english-learning-section` / `english-learner` to render exactly one blockquote containing natural English, Chinese translation and concise corrections, followed by a blank line, `---`, and the substantive response. No old delimiter markers. Initial tool-work commentary and self-contained final answers need this section; routine updates do not.
- Keep that section proportionate and integrate its natural rewrite with the speaking feedback instead of printing two identical model answers. For an unread audio attachment, state that its speech has not yet been transcribed; do not invent a translation. In the final learning section, identify a natural rewrite as edited language, not the verbatim original; detailed corrections can stay in the requested tables below.
- Use the user's requested feedback language; otherwise follow their standing language preference. Ignore capitalization-only issues and distinguish errors, optional improvements, and uncertain recognition.
- A configuration request is not a new learning attempt. Do not generate vocabulary/progress records merely for installing or loading this skill.

## Choose the practice mode

Infer the active part, question and drill scope from the conversation. Ask only if genuinely necessary. Do not restart the session when a recording follows a known question.

| Mode | Behaviour |
| --- | --- |
| Part 1 | Ask one personal question at a time. Coach a direct answer, reason and a small real detail, normally 2–4 sentences. Do not inflate it into an essay. |
| Part 2 | Give the exact cue card and source page. Allow one minute to prepare and up to two minutes to speak for a full practice; do not claim preparation or speaking was timed unless observed. Structure the learner's story as opening, background, event/details, reaction and reflection as appropriate. Check all actual bullets, without treating them as a separate IELTS task-response criterion. |
| Part 3 | Ask one relevant discussion question at a time. Develop a clear opinion, causal explanation and useful example; add contrast only when useful. Do not require an artificial balanced view or a fixed sentence count. |
| Focused drill | Honour 2–3-sentence openings, tense practice or another requested section. Keep tables and a complete target for that scope. Do not force a full retelling or overall score. Stop drilling when the target is achieved and follow the user's next-topic request. |
| Mock interview | Ask examiner-style questions without coaching or model answers before the attempt. If a full uninterrupted mock is requested, defer feedback until the agreed section or test ends. |

Do not provide hints, chunks or a sample before the first independent attempt unless the user explicitly requests guided practice. A retry may use previous corrections. Do not force past tense onto current facts, general opinions or hypothetical preferences.

## Source questions faithfully

- When the user provides a question bank, inspect the actual PDF before selecting each new topic or follow-up. Preserve exact wording and cue-card bullets; state the PDF page number and distinguish printed numbering when it differs. Use available PDF tools or extraction libraries rather than guessing topics from memory.
- The existing IELTS workspace question bank can be discovered under `speaking/` by its PDF filename. Do not hard-code a user directory or treat a historical question bank as a verified current exam prediction.
- Keep a light session record of practised, declined and current topics using the visible conversation/evidence. Avoid repeating them as new. If the user says a topic was practised, accept that and choose another without defending the earlier choice.
- Relevant Part 3 questions come from that Part 2's source section. Label any assistant-created supplement or transfer prompt explicitly; never pass it off as a PDF question. Do not give a full correction routine for a simple request for the next question.

## Receive and preserve the answer

For recording transcription and requested pronunciation feedback, use `english-speaking-audio` as the audio-evidence workflow. Keep this skill as owner of IELTS coaching and its authorized memo cadence.

- Treat an attached recording after a prompt as an answer to review. Copy temporary audio promptly to a stable, dated workspace directory if permitted; retain duration and complete timestamped ASR separately. Actual learning date uses the user's timezone, not a page edit date.
- Use an available audio/transcription capability. When only local ASR is available, label the result automatic and retain disfluencies, self-corrections, mixed language and unfinished endings. Re-run only materially unclear portions when helpful. Context-assisted output can hallucinate; it is not independent confirmation.
- Names, numbers, units, negations, places and technical terms require special care. Keep unclear spans visibly marked. Use user clarification to resolve them without rewriting the historical transcript silently. Do not turn a malformed sentence into a confident biography.
- Separate learner speech, another speaker, read-aloud/model copying, immediate coached retry and independent production. Do not infer sustained progress from one successful repetition.
- Preserve the entire original answer, not only selected errors. For multiple typed attempts, retain all for later aggregation; identify which attempt is being analysed. If shortening the displayed comparison, label it and make the complete originals available rather than claiming an excerpt is complete.
- Missing audio/content: report the specific gap and ask for reattachment only if the source cannot be recovered. Never invent its content.

## Feedback contract for each answer

Keep feedback proportional to the practice scope. The user requires both tables and one complete target version even in a short drill. A simple next-question request needs only the next verified question and source, apart from any standing English-learning section.

1. **Original expression / 我的完整原表达.** Show the complete actual text or ASR-derived transcript, with uncertainty and self-repairs retained. Never label an edited reconstruction as verbatim.
2. **Natural rewrite and concise diagnosis.** Explain the main point and the one issue that would help most. The recommended target below may serve as the natural rewrite if it preserves the user's content; otherwise clearly distinguish a faithful rewrite from optional teaching additions. Do not routinely produce competing final answers.
3. **逐句优化提升表.** Columns: `原表达 | 优化表达 | 原因`. Cover the actual sentences/clauses, marking correct wording as retained. Explain grammar and meaning in Chinese when that is the user's preference. An optional upgrade is not an error; an uncertain ASR word is not a confirmed error.
4. **地道表达积累表.** Columns: `表达/语块 | 中文用途 | 本题例句`. Prefer 3–5 transferable chunks, fewer for a tiny drill. Mark previously studied chunks as `复练` when supported. Use examples grounded in this answer; label new teaching examples.
5. **7.0+目标完整表达版本.** Recommend exactly one natural, achievable spoken version based on the user's facts and opinion. Keep a full answer full; keep an opening drill within its practiced scope. Label new reasoning, hypothetical examples and other editorial additions. Do not invent events, feelings, outcomes, companions, precise dates, locations or project details. If essential facts are missing, use a clear placeholder or ask one concise clarification rather than fabricate. Explain that 7.0+ is a learning target, not a score guarantee.
6. **Structure, comparison and one next step.** Briefly explain the answer's organisation. For retries, compare observable changes with the actual prior attempt. Offer one short target (often 1–2 sentences or 20–45 seconds), then keywords for optional independent retelling. Do not imply mastery or require another full attempt; respect the user's wish to move on.

### Assessment boundaries

For a full independent answer, use the four IELTS dimensions: Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy, Pronunciation. Explain evidence and limits for each; numerical estimates are provisional teaching estimates, not official scores. Do not copy old scores forward. Use current official descriptors if making detailed descriptor-level claims.

Text or ASR alone supports only limited textual coherence, vocabulary and grammar observations. It cannot establish pronunciation, delivery fluency, intonation or an overall speaking band. Recognized words, duration, WPM and transcript restarts are not phonetic or fluency scores. If audio cannot actually be assessed, mark delivery/pronunciation unassessed and do not invent an overall band. Pronunciation practice suggestions must be distinguished from diagnosed errors. For short drills, reading or immediate imitation, avoid compulsory band tables and total scores.

## Memo and review boundaries

Routine practice is chat feedback plus available local source evidence, not a trigger for live Notion writes. Follow the learner’s verified memo aggregation cadence and timezone when authorized; do not create a page after every attempt by default. A skill is not a scheduler: do not create, change, or claim to have verified an automation unless the user requests schedule work and the actual tool state is inspected. Do not promise this chat is automatically accessible to an unverified scheduled task.

For an explicit memo request or an authorised daily aggregation, use `english-memo`, current live Speaking rules and [the Version 1.1 memo reference](references/memo-v1.1.md). Keep memo, spaced-review scheduling and quiz workflows separate; invoke `english-review` or `english-quiz-system` only when their operation is requested. Do not auto-duplicate speaking material into Vocabulary or Natural Sentences. Preserve existing daily pages, dates, originals and user edits; read back writes and report actual coverage. Missing originals must be disclosed, not replaced with filenames or summaries.

Keep private page IDs, local runtime paths, personal records and schedule bindings outside this shareable skill. Discover existing private settings rather than modifying them as a side effect of practice.
