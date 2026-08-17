---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/bmm-skills/2-plan-workflows/bmad-ux/SKILL.md#L27-L55"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/2-plan-workflows/bmad-ux/SKILL.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "27-55"
sha256: 3cc2114f4ee58664b0faaca328901d433c32c6355ac43619916909b2c72fe19d
---
## Sources

UX may lead, follow, or stand alone. Inherit `sources:` by reference; the spines hold design and experience decisions, not duplicates of upstream product content.

## On Activation

1. Resolve customization: `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`. On failure, read `{skill-root}/customize.toml` directly and use defaults.
2. Run `{workflow.activation_steps_prepend}`. Treat `{workflow.persistent_facts}` as foundational context (entries prefixed `file:` are loaded). `{workflow.external_sources}` is an org-configured registry of internal tools; consult them alongside generic web research on the same triggers, org tools preferred when their directive matches.
3. Load `{project-root}/_bmad/bmm/config.yaml` (+ `config.user.yaml` if present). Resolve `{user_name}`, `{communication_language}`, `{document_output_language}`, `{planning_artifacts}`, `{project_name}`, `{date}`. Missing keys → neutral defaults; never block.
4. If headless, follow `references/headless.md` for the whole run. Otherwise greet the user **by name** using `{user_name}` and **in their language** using `{communication_language}` — and stay in `{communication_language}` for every turn. In the greeting, let the user know `bmad-party-mode` and `bmad-advanced-elicitation` are always available. Then scan for misroute on the first message: PRD → `bmad-prd`; architecture → `bmad-architecture`; game UX → BMad GDS; agent/skill → `bmad-workflow-builder`; brief → `bmad-product-brief`.
5. Detect intent: **Create**, **Update**, **Validate**. For Create, before binding a fresh workspace, scan `{workflow.ux_output_path}` for prior in-progress runs (folders matching `{workflow.run_folder_pattern}` whose `DESIGN.md` frontmatter `status` is not `final`) and offer to resume rather than starting over.

Run `{workflow.activation_steps_append}`.

Activation is complete. If `activation_steps_prepend` or `activation_steps_append` were non-empty, confirm every entry was executed in order before proceeding. Do not begin the main workflow until all activation steps have been completed.

## Modes

**Create.** Bind `{doc_workspace}` to `{workflow.ux_output_path}/{workflow.run_folder_pattern}/`. Create `.working/` and `imports/`; seed the memlog with `uv run {project-root}/_bmad/scripts/memlog.py init --workspace {doc_workspace} --field topic="<product/UX>"`; create `DESIGN.md` (frontmatter only) and `EXPERIENCE.md` (frontmatter only). Run Discovery → Finalize.

**Update.** Read spines + memlog + sources. If `.memlog.md` is missing, init it with `uv run {project-root}/_bmad/scripts/memlog.py init --workspace {doc_workspace}` — this update is entry one. Surface conflicts with prior decisions. Run Finalize.

**Validate.** See `references/validate.md`.

## Discovery

**Capture; do not author.** The spines are distilled at Finalize toward the memlog. Decisions → `.memlog.md` (canonical), each appended via `uv run {project-root}/_bmad/scripts/memlog.py append --workspace {doc_workspace} --type <decision|change|override|assumption|event> --text "…"` — never hand-edited; a resume reloads it. Creative-tool artifacts → `.working/`. User-supplied visuals (Figma, sketches, brand decks, image folders) → `imports/`, one `memlog.py append` per item. Spines win on conflict.

**Source scan.** Glob `{planning_artifacts}/` for candidate input paths; surface paths only — never read content in the parent. User confirms which apply or adds others; subagent-extracts on confirm.
