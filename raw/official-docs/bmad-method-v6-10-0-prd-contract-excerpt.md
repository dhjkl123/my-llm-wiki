---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/bmm-skills/2-plan-workflows/bmad-prd/SKILL.md#L22-L50"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/2-plan-workflows/bmad-prd/SKILL.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "22-50"
sha256: b0b97c87761265a8b530fe9120d6ff14878da421cce17081a71d0a37e10e7d6f
---
5. Detect intent: **Create** (no PRD), **Update** (existing PRD), **Validate** (critique only). If ambiguous, ask. For Create intent, before binding a fresh workspace, scan `{workflow.prd_output_path}` for prior in-progress runs (folders matching `{workflow.run_folder_pattern}` whose `prd.md` frontmatter `status` is not `final`); if any exist, offer to resume rather than starting over.

Run `{workflow.activation_steps_append}`.

Activation is complete. If `activation_steps_prepend` or `activation_steps_append` were non-empty, confirm every entry was executed in order before proceeding. Do not begin the main workflow until all activation steps have been completed.

## Intent Modes

**Create.** Bind `{doc_workspace}` to `{workflow.prd_output_path}/{workflow.run_folder_pattern}/`. Write `prd.md` with YAML frontmatter (title, status, created, updated — initial `status: draft`), and seed the memlog with `uv run {project-root}/_bmad/scripts/memlog.py init --workspace {doc_workspace} --field topic="<PRD/product name>"` so subsequent decisions land in a known file. Tell the user the path. Run `## Discovery`, then `## Finalize`.

**Update.** Reconcile the PRD with a change signal. Source-extract against PRD, addendum, `.memlog.md`, and original inputs (extract, don't ingest). If `.memlog.md` is missing, init it with `uv run {project-root}/_bmad/scripts/memlog.py init --workspace {doc_workspace}`, then spawn a one-time bootstrap subagent to reverse-engineer a thin log from the PRD (one `uv run {project-root}/_bmad/scripts/memlog.py append --workspace {doc_workspace} --type decision --text "<recovered decision>"` per recovered decision) before continuing. Surface conflicts with prior decisions before applying. Then `## Finalize`.

**Validate** (or *analyze*). Critique without changing. Load `references/validate.md`.

## Discovery

Order: **Brain dump → Stakes calibration → Working mode → mode-scoped work.** Get to working mode fast — two or three turns, not ten. Users in a hurry must not be held hostage by upstream probing.

**Brain dump.** Always the first move, even when the user opens with paragraphs of context (that is intake, not the dump). Ask for verbal context *and* any existing inputs they want you to read — product brief, research, customer transcripts, competitive analysis, prior PRD draft, design docs. Paths or paste; big docs are fine, you will subagent-extract. A simple "anything else?" surfaces what they almost forgot.

**Research subagents (default).** During Discovery, spawn web-research subagents to ground the picture: what exists in the space, how comparables position themselves, current landscape. Subagent does the search; parent receives a digest.

**Elicitation, not direction.** Discovery pulls the user's vision out; it does not insert yours. Open-ended "tell me about X" beats multiple choice. When you find yourself naming wedges, picking MVP cuts, or proposing phases, stop — you have crossed from elicitation into authoring. Hand the pen back. Infer-and-confirm ("I'm assuming X works like Y — right?") is fine; quizzing the user through a tree of LLM-shaped choices is not.

**Stakes calibration.** One short probe before working mode: hobby / internal / launch — enough to calibrate rigor and section depth. Audience, Existing inputs, and Downstream depth fill in inside the chosen mode, not upstream of the choice.

**Working mode.** Offer the choice in the user's language:

- **Fast path** — I batch remaining gaps into one or two consolidated questions, then draft the full PRD with `[ASSUMPTION]` tags where I inferred. You review and we iterate. The initial quality depends on how much you gave me upfront.
