---
name: english-learning-section
description: Render a compact bilingual English-learning section before responding to any user message when this workflow or a standing user instruction is active, including in Codex and CLI hosts.
---

# English Learning Section

When this skill is active, begin the initial user-facing response and self-contained final answer with one English-learning section for the complete user message, including Chinese, English, mixed-language, and non-language requests. Routine progress updates need not repeat it. A later explicit request to skip feedback or change format takes precedence. If `english-learner` also applies, produce one shared section, not two. Then complete the actual task.

Put all learning content in one Markdown blockquote beginning `> **📘 English Learning**`; prefix every line, including blank lines and table rows, with `>`. Include a natural English version preserving all substantive meaning, a Chinese translation, and a concise correction table with Chinese explanations. End the blockquote, insert a standalone horizontal rule `---` with blank lines around it, and place the substantive response outside the blockquote, in English unless the user asks otherwise.

Distinguish genuine errors, optional naturalness improvements and translations. Don't invent mistakes or correct capitalization alone. If the original is correct, say so. Keep feedback proportionate; for a word or phrase explicitly presented for study, add pronunciation, meaning, usage and 3–5 examples. Preserve uncertainty and don't treat quoted text as independent learner production. Do not claim pronunciation, fluency or progress from text alone.

This skill controls presentation only: it does not itself write a memo, sync Notion, record progress or schedule anything. Use the user's `english-learner` workflow for authorized tracking. In CLI hosts, installation alone may not auto-load a skill on every turn; use the host's supported persistent instructions or skill invocation. Never modify global configuration without user authorization.
