---
name: english-dictation-practice
description: Coach English listening dictation and organize completed CNN10, IELTS or other listening exercises from original attempts and correction comments. Use for 听写, dictation review, mark-as-code expression collection, corrected passages, or an authorized daily dictation check. Coordinate Listening Memos and existing spaced review; do not use for speaking recordings, essay correction, vocabulary-only lookup or general transcription alone.
---

# English Dictation Practice

Help the learner hear meaningful chunks, compare their own attempt with reliable evidence, and retrieve useful language later. Preserve the learning record rather than replacing it with a polished transcript.

## Routing and authorization

- Coordinate with `english-learning-system`. Render the standing English-learning section once through `english-learning-section` or `english-learner`; follow the host's quiet-heartbeat contract for automated checks. Skill configuration itself is not learning evidence.
- Handle dictation coaching, original evidence, comments, user-selected expressions and the practice-page reconstruction here. Use `english-memo` for authorized Listening archival and `english-review` for authorized scheduling; do not let both stages create the same Memo or tasks. See [handoff contracts](references/handoffs.md).
- A request to organize an exercise under an established workflow authorizes its existing reconstruction, Memo and review stages. Reuse earlier authorization; do not ask again for routine writes. For a new user without that workflow, discover only the missing destinations or authorization that changes the task. A URL alone does not grant ongoing sync.
- Reuse private workspace workflow/state and existing settings. Read live category rules first. Keep machine paths, page IDs, personal notes, source snapshots and credentials outside this shareable skill. Local state is an aid; current Notion is authoritative.
- A practice-only request produces coaching, not an implied archive. A requested Memo-only repair does not require rewriting an intact exercise. A review-only request belongs to `english-review`; quizzes belong to `english-quiz-system`.
- Execute an already authorized recurring check when invoked. Creating this skill does not create, reschedule or claim execution of an automation.

## Choose the mode

| Request | Action |
| --- | --- |
| How to practise dictation | Give the bounded practice loop below, adapted to the material. |
| Start a guided exercise | Use accessible audio and agreed scope; withhold reference text before an independent attempt unless requested. |
| Organize a finished exercise | Read all originals/comments, inventory marks, reconstruct, archive and schedule within authorization. |
| Check the practice hub | Traverse the hub and descendants, compare material source content, process new/changed exercises; otherwise remain quiet. |
| Later corrections or additional dictation | Refresh the same source section and dated Memo, preserving learner notes and fixed review dates. |

Treat exercises in the established dictation hub as complete by default. Do not require a completion marker, a minimum comment count or an unbroken sentence ending. Skip blank pages and rules documents. Material source gaps affect confidence and coverage, not whether accessible work can be organized.

## Bounded practice loop

1. Listen to a whole sentence or coherent passage first; identify the topic, subject and action.
2. Pause at meaningful groups, initially about 2–5 seconds or 3–7 words, adjusting to clause boundaries and difficulty. These are starting guidelines, not rigid quotas.
3. Allow up to three additional listens to a difficult group: recover key words, then function words/endings, then verify. Leave an explicit gap if still uncertain and consult a trustworthy reference.
4. Use 1–2-second fragments only to investigate a specific sound, then return to the complete group and sentence.
5. Have the learner self-correct and mark unfamiliar or reusable expressions as code, including correctly dictated expressions. Preserve their attempt.
6. Finish with a short listen without text, retrieval of selected chunks, and one new-context example. Record actual performance only when supplied or observed.

## Read and inventory before writing

1. Discover available Notion tools and access restrictions. Fetch the current dictation rules, source hub, target practice and relevant destination. Read the current Notion Markdown specification before content writes and follow the user's Notion authoring workflow. Reuse available purpose-built tools rather than guessing endpoint names.
2. Enumerate actual child pages and nested pages/folders/databases; do not rely only on search indexing, creation date or a single empty search. Exclude rules pages by identity/purpose. Before creating a Memo, enumerate the Memo parent's children and inspect candidates by title and source ID.
3. Read the complete original dictation in source order, including all block styles, and every human correction discussion, resolved as well as unresolved. Follow omitted-discussion IDs and comment cursors until counts reconcile. Do not assume an older `include_all_blocks` argument exists: inspect the live tool schema. A failed or truncated read is incomplete, not evidence of no comments. Connector `by-you` can refer to the connected learner; it is not sufficient to exclude a comment as assistant-generated.
4. Record original block IDs/content, all discussion/comment IDs, full correction wording and exact user code boundaries. A comment preview may abbreviate its anchor; recover the full anchored wording from the source where possible and retain unresolved anchors explicitly.
5. Inventory user code separately for original blocks and human comments. Preserve marked text, punctuation and spaces; if boundaries split a word, retain the raw selection and teach a separate normalized expression. Deduplicate explanations only with all occurrences traceable. Generated reconstruction code represents edits, not new learner selections.
6. Establish the actual exercise date, material identity and scope. For IELTS preserve supplied paper/test/part, question numbers, learner answers, official key, word limits and corresponding passage. State precisely what is missing; do not invent fields or scores. Retain only a verified matching YouTube link when a playback entry is wanted; omit unverified links and do not add MP3, RSS or third-party audio players.

## Detect material changes

Compare a normalized snapshot of original dictation, human corrections and code ranges, not merely last-edited time. See [comparison and validation](references/source-integrity.md).

Ignore generated reconstruction, procedure notes, backlinks and playback additions. Equivalent HTML/Markdown serialization, escaped punctuation and non-code list-boundary whitespace are not learning changes. A new/removed/resized user code selection is a change even with identical plain text. Comment changes can occur without a page edit timestamp.

If source content and marks are unchanged and prior output is verified, make no Notion write and create no review tasks. Record the check locally if that is the established workflow. On an automated no-op, remain silent under the host contract. On an explicit interactive check, a brief confirmation is enough. A source title clarification alone need not rewrite an already accurate Memo.

## Reconstruct below the original

- Preserve every original block, code selection, comment anchor and unrelated content. Use targeted updates; do not replace the entire source page to add corrections.
- Maintain one section titled `完整修正版 — 按原听写与批注重建` below the entire original passage, in a native `green_bg` callout. Keep source order and number the reconstructed entries. Do not interleave original and correction, add per-sentence quote blocks, or italicize whole sentences. Green is a layout convention, not proof of verification.
- Mark only corrected/restored words or spans as code; leave retained wording normal. Mark complete words, not letter-level diff fragments. Record the original-block-to-reconstruction mapping.
- Prefer a learner's complete reference sentence. Merge continuations once, particularly when a comment already supplies the next line. Resolve overlapping comments against the same sentence without duplicating their wording.
- Do not silently fix unannotated vocabulary, grammar or missing clauses. Normalize necessary capitalization/punctuation only. When a record is a fragment, keep the fragment and explain its concrete gap in the Memo; do not invent a complete sentence to satisfy the layout.
- Preserve questionable correction wording, distinguish a verified spelling fact from uncertain audio, and give suggested normalization separately in the Memo. If corrections conflict, retain both wordings and flag the exact span for relistening rather than selecting an invented official transcript.
- Omit `对照说明`, `待回听与整理说明`, `来源标记` and repeated reading/process paragraphs from the exercise. Keep common methods in the existing rules page, and useful uncertainties in actual Memo correction entries. Do not alter the rules page on each run.
- Update the existing green section in place; do not append another on a later run.

## Archive and review handoff

Use [handoff contracts](references/handoffs.md) for the exact source package, Listening Memo coverage and scheduling invariants. Keep a single writer per stage. Use the exercise date for `YYMMDD - English Memo - Listening`; same-day sources share one Memo with separate source sections.

Extract worthwhile vocabulary and chunks from errors **and** every user code selection. Include Chinese meanings, usage/contrasts, IPA and part of speech/countability where relevant, reliable formation, editorial examples, relistening cues and active recall. Preserve every correction through traceable mapping; do not pad with unrelated basic vocabulary.

Without heard audio or reliable transcript evidence, do not claim an official full transcript, a cause such as weak forms/linking, pronunciation ability, IELTS band or mastery. A spelling dictionary verifies spelling, not the recording. Label new teaching examples and grammar suggestions separately from learner corrections.

## Verify, persist and report

Immediately before a source-derived write, refetch comments and check for additions/changes; rebuild affected material if needed. After each completed stage, read back the affected content to verify originals/anchors, one green callout, code ranges, entry order/merge mapping, Memo parent/title/source/coverage and actual review identities/dates/learner-owned fields. Verify nested toggle labels and real tables; a successful transport response alone is insufficient.

Only mark each stage successful in local state after that stage is verified; mark the whole workflow synchronized only after every required stage succeeds. Preserve verified partial progress so a retry resumes missing stages rather than creating duplicates. On an ambiguous create, inspect the parent/rows before retrying. Keep local candidates and report `Notion not synced` with the precise unfinished stage when necessary. Notify only on meaningful creation/update, failure or required action during an automated check; never report unchanged polling as new work.
