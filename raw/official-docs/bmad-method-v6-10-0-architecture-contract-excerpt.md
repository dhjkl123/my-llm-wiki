---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/bmm-skills/3-solutioning/bmad-architecture/SKILL.md#L27-L31"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/3-solutioning/bmad-architecture/SKILL.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "27-31"
sha256: a1b2944f4dcc16c62a1e74b239eee9088679459a90cbe5aa78ddebe3e87a0957
---
## Read the input to know the job

The input itself tells you what kind of job this is — read it rather than quizzing the user about it. A spec package (`SPEC.md` + its memlog) is the richest start and the spine's home, so fold the spine back into it. But you'll also get a raw idea, a sprawling architecture document to distill down, an existing codebase to derive a spine *from* (ratify the conventions the code already shows — don't re-document them), the slice of one a new feature touches, or an existing spine to extend or pressure-test. Prefer a `.memlog.md` over re-reading the source it came from. Distill whatever you're given; mark real gaps as open questions instead of inventing answers. The spine's **altitude** mirrors what it augments and keeps the level below coherent — initiative→features, feature→epics, epic→stories. Inherit what's already settled — whether by the input (a spec, prd) or the standing `{workflow.persistent_facts}` — silently; don't re-decide or re-ask it. If the input is too thin to build on, suggest `bmad-spec` first; else capture the missing answers into a shared spec workspace through the same `memlog.py`, so `bmad-spec` can later derive `SPEC.md` without drift.

**Inheriting a parent spine** (e.g. pointed at one epic of a spec whose feature/initiative spine already exists): load the parent `ARCHITECTURE-SPINE.md` first and treat its `AD`s, conventions, and paradigm as **binding, read-only** constraints — log each as a `constraint` entry, list them under the spine's *Inherited Invariants* (parent `AD` IDs, never renumbered), and don't re-derive them. Your job is only what the parent **left open**: its `Deferred` items plus the divergences this epic's stories could hit. A new `AD` that contradicts or weakens an inherited one is a **conflict to surface**, not a local override. An epic spine fixes the invariants the epic's stories must share — it does **not** expand per-story detail.
