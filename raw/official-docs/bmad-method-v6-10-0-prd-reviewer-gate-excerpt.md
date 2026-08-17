---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/bmm-skills/2-plan-workflows/bmad-prd/SKILL.md#L48-L91"
source_type: official-github-file-excerpt
ingested: 2026-08-04
retrieved_at: "2026-08-04T11:37:44+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/2-plan-workflows/bmad-prd/SKILL.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "48-91"
sha256: f7e17a8847b2d52f9dd693937162fa2c66dc33df82eac572c30352b802b292e8
---
**Working mode.** Offer the choice in the user's language:

- **Fast path** — I batch remaining gaps into one or two consolidated questions, then draft the full PRD with `[ASSUMPTION]` tags where I inferred. You review and we iterate. The initial quality depends on how much you gave me upfront.
- **Coaching path** — we walk PM-thinking sections together. Once chosen, I ask which entry point fits: **Vision + Features** (capability-first — for enterprise, dev products, internal tools, anyone who thinks in features), **Journey-led** (user-first — for consumer, UX-heavy, multi-stakeholder products; journeys with named protagonists carry persona context inline, no standalone persona section), or *let me suggest* based on what I heard. The chosen entry sets the section order.

The workspace persists; stop and resume freely.

**Concern scan.** As you read what the user gave you, name the concerns this product actually carries — compliance, integration density, operational SLAs, hardware constraints, public-API contracts, monetization, data governance, whatever applies. The list is open; recognize what's there, do not classify into a fixed shape. These concerns drive which template sections to pull in from the Adapt-In Menu and which to invent when no cluster names them.

**Form-factor.** If not stated in sources, probe — mobile / web / desktop / multi-surface / hardware / API.

**User Journeys are captured, not authored.** When UJs are warranted (consumer / multi-stakeholder B2B / meaningful UX — drop or downscale for internal tooling with a single operator role, regulatory-only updates, hobby/solo, pure technical PRDs), prompt the user to narrate a real session with a named protagonist (Mary, mom of three — not "the user") — what the person does, in what order, where it lands — then structure the answer into UJ-N form and confirm. Persona context lives inline at the moments that matter; no standalone persona section.

## PRD Discipline

**Shape.** Features grouped; FRs nested with globally numbered stable IDs. Cross-cutting NFRs in their own section; skip traceability matrices. Capabilities, not implementation — tech choices live in `addendum.md`. Treat `{workflow.prd_template}` as expert prior knowledge, not a checklist. The **Essential Spine** is the expected default — present it unless the product genuinely doesn't need a section, and when you drop one, do so for a reason a reviewer would agree with. The **Adapt-In Menu** is conditional: pull in the clusters the product's concerns need to best define the requirements. When the product carries a concern the menu doesn't name, invent the section — name it well, decide what belongs in it, place it where it serves the reader or the PRD. Reorder and combine for readability. Never include a section because it appears; never skip a concern because no template section covered it. Counter-metrics named when Success Metrics exist.

**Extract, don't ingest.** Source documents go to subagents for extraction; the parent assembles from extracts. Only load source documents into the parent context wholesale when no subagents are available.

**Length scales with stakes.** Hobby / solo PRDs aim for about two pages. Internal tools land around five to eight. Launch and chain-top PRDs run as long as their FRs and concerns require. Whatever the length, detail that doesn't earn its place in the PRD's main narrative belongs in `addendum.md` — moving overflow there is correct; padding the PRD to look thorough is not.

## Reviewer Gate

Used by the Validate intent and at Finalize step 3.

Assemble the menu: rubric walker against `{workflow.validation_checklist_template}` (the PRD quality rubric) + each entry in `{workflow.finalize_reviewers}` + any ad-hoc reviewers the artifact warrants. Stakes-calibrated — hobby/solo may run quietly or skip; higher stakes get the explicit all/subset/skip menu.

Dispatch entries as parallel subagents against `prd.md` (and `addendum.md` if present) using the standard prefix convention (`skill:` / `file:` / plain text). Each writes its full review to `{doc_workspace}/review-{slug}.md` and returns ONLY a compact summary (verdict, top 2-5 findings, file path) — the parent never holds full review text. The rubric walker uses the prompt and output format in `references/validate.md`. If subagents are unavailable, run sequentially: write the file *before* anything else, then flush the review from working context.

Surface findings tiered, never dumped. Lead with a one-sentence gate verdict, then walk critical + high findings; medium/low roll into a single tail ("plus N more in {file}"). Read the full `review-{slug}.md` only when the user drills into a specific finding. Per finding: autofix, discuss, defer to open items, or ignore.

Under Validate intent, the parent additionally runs the synthesis pipeline in `references/validate.md` — folding every selected reviewer's output into a single HTML + markdown report and opening the HTML.

## Finalize

Tell the user the sequence in one sentence, then walk it. Polish goes last so it does not redo work after reviewer fixes.

1. **Memlog audit.** Walk `.memlog.md` with the user; each entry captured in PRD, in addendum, or set aside.
2. **Input reconciliation.** Subagent per user-supplied input against `prd.md` + `addendum.md`. Each writes its extract to `{doc_workspace}/reconcile-{slug}.md` and returns ONLY a compact summary (input name, gaps 2-5, file path). Surface gaps — especially qualitative ideas (tone, voice, feel) the FR structure silently drops. Must happen before polish.
3. **Reviewer pass.** Run `## Reviewer Gate`. Resolve before polish.
4. **Triage open items.** All Open Questions, `[ASSUMPTION]` tags, `[NOTE FOR PM]` callouts. Phase-blockers (would make the PRD unsafe for UX/architecture/epics) surfaced one at a time and resolved; non-blockers deferred with owner + revisit condition logged via `memlog.py append`. If phase-blocker count is high, flag it.
5. **Polish.** Apply `{workflow.doc_standards}` to `prd.md` and `addendum.md` in declared order (structural passes before prose — prose should not polish soon-to-be-cut text). Parallelize across documents, sequential within.
6. **External handoffs.** Execute `{workflow.external_handoffs}`; surface returned URLs/IDs. Skip and flag unavailable tools.
7. **Close.** Set `prd.md` frontmatter `status: final` and `updated` to `{date}` so future invocations distinguish this PRD from in-progress drafts. Record finalization via `uv run {project-root}/_bmad/scripts/memlog.py append --workspace {doc_workspace} --type event --text "PRD finalized"`. Share artifact paths. Common next: `bmad-ux`, `bmad-architecture`, `bmad-create-epics-and-stories`; invoke `bmad-help` for authoritative routing.
