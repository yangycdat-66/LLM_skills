# Handoff contracts

Read only for an archival or review operation. Current user instructions and live rules override these defaults. A handoff is an instruction boundary, not permission to launch another agent.

## Dictation → english-memo

Provide:

- Verified source identity, original exercise date, material/test/part/scope and current rules.
- Ordered original block IDs/rich text; complete human comment/discussion IDs, anchors and exact correction wording; any missing evidence.
- Exact body-code and comment-code selections with occurrence provenance and counts, normalized forms separately, and a material source snapshot/fingerprint.
- Original-block → reconstruction mapping, merge groups, changed spans, unresolved wording and practice-page verification result.
- Existing same-date/category Memo identity and full content, or parent/title/source-ID duplicate-check evidence before creation.
- Explicit archival/review authorization already established in the conversation; do not infer ongoing permission from a source URL.

Have `english-memo` merge one dated Listening Memo under the verified English Memo root. Preserve user notes, review checks and unrelated chapters. Include concise takeaways; original → user correction → explanation/relisten mapping; user-selected expressions with raw mark, meaning, reusable pattern, editorial example, reuse/relisten cue and active recall; relevant vocabulary, chunks/contrasts, grammar/prepositions, evidence-bounded listening diagnosis and IELTS transfer. Keep a full original snapshot in a native toggle, native source-page mentions and real tables. Apply the current Notion authoring convention and Listening native icon/TOC without imposing Vocabulary's separate template.

Include short D1/D3/D7/D15/D30 content prompts and source gaps. These prompts explain what to practise, not a second completion tracker. Keep actual completion in the existing review database. Distinguish user corrections, editorial suggestions and verified reference facts. Do not label a reconstruction as an official transcript or imply that a partial Part covers a complete test.

Verify all source selections and comments are covered, the parent/title/date/source are correct, and user-owned content survived. Return the verified Memo ID and URL with the source date for scheduling. On Memo update alone, do not move review dates or reset checks.

## Listening Memo → english-review

Supply the verified Memo identity, original exercise date, category `Listening`, existing review authorization and any known task identities. Read current review rules, live schema/views, ledger and relevant existing rows before mutations.

- Register the whole Memo at fixed D1/D3/D7/D15/D30 dates, using the configured timezone's calendar days. Retain original learning/due dates when the Memo is edited or a review is late.
- Use the established identity convention: compact Memo UUID + `|` + node + `|` + original due date. Query before creating; normalize connector escaping of pipes when comparing identifiers.
- Treat Listening as one Memo, exempt from any per-day Natural Sentences quota. Do not create five tasks for every expression or a parallel review database.
- Keep existing checked state, feedback, actual completion date, notes and partial progress. New records start unchecked/待反馈, never as completed or mastered; use the native Memo mention in 学习页面.
- Update the current equivalents of the new-source registration and Memo/source ledger with category, learning date, earliest actually unfinished node, due date and actual completed count. Ledger headings may have changed; adapt to the live structure rather than restoring obsolete sections or altering unrelated daily batches.
- Preserve the current daily/overdue/completed/all views and feedback-practice rules. Do not change the morning automation or global scheduling arrangement. Use `english-review`'s own evidence/timing rules for 忘记/模糊 extra practice.
- Read back task dates/identities, source mentions, learner fields and ledger entries before marking review integration successful. If a task creation outcome is unknown, query first and resume missing rows only.

Review coverage is not proof the learner has completed the source or mastered its contents.
