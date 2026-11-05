---
name: english-memo
description: Create or incrementally update the user's Notion English Memo for Vocabulary, Speaking, Listening, or Writing from actual learning evidence. Use for daily memo generation, consolidation, or source-backed repair; follow the current category rules, preserve originals and user edits, and verify Notion writes. Do not use for review-list scheduling or quiz generation.
---

# English Memo in Notion

Use the Notion connector, plus the user's Notion authoring workflow when available. The user controls their own learning status and summaries. This skill organizes evidence; it does not invent learning, change completion, or populate other categories. Coordinate vocabulary sync with `english-learner` so the same material is archived only once. Use `english-review` for the separate review scheduler and `english-quiz-system` for quizzes.

## Discover and verify current rules

1. Find the user's `English Memo` root and `ChatGPT English Memo rules` through the connected Notion workspace (or the user's private English-learner configuration). Verify parentage and read the complete current rules. For Speaking also read `IELTS Speaking Practice System — Version 1.1`; for Listening read `雅思听写训练方法与整理规则`. Discover any newer category rules and apply the latest explicit user instruction over these defaults. Do not publish private page IDs or learning records in the skill.
2. Determine category, actual learning date in the learner’s configured timezone, sources, and whether an existing same-date/category page already exists. Do not use edit date as learning date. Search exact title and verify its parent; inspect all current content, nested toggles and user edits before changing it. If duplicate pages, truncated content, unresolved source identity or conflicting rules prevent safe merging, stop that write and report the gap. No empty memo when no material is available.
3. Work from supplied accessible original evidence, not search snippets or summaries as if verbatim. Inventory actual original messages, questions, attempts, corrections, source pages and comments; mark date and ASR uncertainty. Reconcile in learning order and preserve prior material. Never claim unavailable source text, audio, answers or performance is verified.
4. Use title `YYMMDD - English Memo - Category` beneath the verified root; use the category's established native icon and native table of contents when appropriate. Incrementally merge with existing page; preserve content and user edits. Verify all changed blocks, nested content, title, icon, parent and source coverage by reading back. Report date, changes, link and any specific gaps or failed writes. Treat truncated/unknown blocks and failed discussion retrieval as incomplete.

## Vocabulary

Current V2.1: 📚; native TOC; sections in order, omitting empty ones: (1) core expression table, at most 10, with number, expression, Chinese recall cue, natural example, usage; bold expression; (2) real original wording, correction and reason, distinguishing mistakes from optional alternatives; (3) complete selected vocabulary in learning order: item/part of speech, IPA, Chinese meaning, etymology/formation, collocations, example; (4) distinctions and examples; (5) actual spelling errors, correct spelling, review priority, memory cue. Merge duplicates. Do not add source numbering, register column, raw chat transcript, date or routine process reports. Put material usage limits within the item. Mark newly added teaching examples/explanations as editorial; uncertain etymology as unverified or mnemonic.

Select worthwhile new expressions, meanings and substantive corrections suited to the learner; do not list every encountered basic word or infer mastery. Use only the bound conversation's original messages, not cross-session snippets; configuration is not learning. Include items from the actual local learning day, including after 23:00. Mark specific coverage gaps briefly at the end when needed.

## Speaking

🎙️. Apply V1.1 in this order: (1) 3–5 worthwhile chunks, flag three priorities when available, table chunk/Chinese use/topic example; (2) 3–5 issues prioritized by impact, table actual expression with question/attempt, correction, reason/action, then one next practice target; (3) questions and complete original answers and one final speakable polished version per question in native toggles. Preserve every original attempt, errors, code-switching, self-corrections, endings and prior validated versions in practice order; label reading versus independent attempts and newly supplied examples or rewrites. Place detailed feedback, historical versions and completeness/source evidence in additional toggles. Show a visible partial-archive warning when needed. Preserve the user's meaning without invented experiences.

A transcript or ASR is not verified audio: do not infer pronunciation, actual fluency, independent mastery or a full band score. Short drills/reading need not be forced into a complete answer or full assessment. Same-topic ongoing work updates the existing page; preserve all attempts.

## Listening

Use the current `english-dictation-practice` skill when the task includes dictation coaching, source-page reconstruction, source/comment inventory or a daily dictation check. That workflow owns source integrity and hands off the verified evidence package; this skill owns the Listening Memo. For a Memo-only request, preserve a valid source reconstruction and avoid rerunning unrelated stages. Follow the system’s bundled dictation fallback when the dedicated installed skill is unavailable.

🎧. Read the actual practice page, original dictation, user code marks and all user correction discussions, including resolved ones when accessible. Separate user's code marks in originals/comments (all deserve accumulation even if correct) from code in the generated green reconstruction (changed text only). One daily memo merges same-day practice sources in separate sections; preserve source links, originals, corrections, vocabulary/chunks, Chinese meaning, examples, distinctions and practical review cues. Keep editorial examples separate from alleged audio; don't invent official transcript, answer key, IELTS score or causes of listening difficulty.

When the user has authorized the listening workflow's practice-page update, preserve originals/comments and consolidate one light-green full corrected passage below the original, numbering sentences and marking only changes as code. Distinguish uncertain reconstruction. Do not imply a 23:00 automation was created or executed. Review reminders use original practice date and the existing review system; do not create a parallel task system.

## Writing

No separately authoritative writing rule was located in the inspected main rules; search for and follow any current dedicated rules before using this fallback. Existing examples preserve task/context, the complete accessible user answer, an explicitly labeled polished version, detailed corrections, grammar and useful phrases, plus specific source gaps. Preserve the learner's actual text and distinguish original historical feedback from newly written suggestions. Only assess criteria supported by the actual sample; a single sentence cannot support a full essay score. Never fabricate unseen questions, earlier drafts or progress.
