---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/docs/reference/workflow-map.md#L31-L51"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "docs/reference/workflow-map.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "31-51"
sha256: e676c0e1991bdda560d1a9dd12415ed7eaddf63a81d09f137d5eefd8884abcaf
---
## Phase 1: Analysis (Optional)

Explore the problem space and validate ideas before committing to planning. [**Learn what each tool does and when to use
it**](../explanation/analysis-phase.md).

| Workflow                                                                  | Purpose                                                                    | Produces                  |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------|---------------------------|
| `bmad-brainstorming`                                                      | Brainstorm Project Ideas with guided facilitation of a brainstorming coach | `brainstorm.html` keepsake plus an optional `brainstorm-intent.md` |
| `bmad-forge-idea` | Pressure-test an idea until it hardens, proves out, or dies cheaply | `forge-report.html` every run; `forged-idea.md` when an idea hardens |
| `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research` | Validate market, technical, or domain assumptions                          | Research findings         |
| `bmad-product-brief`                                                      | Capture strategic vision — best when your concept is clear                 | `brief.md` + `addendum.md`, plus any desired HTML or presentation output       |
| `bmad-prfaq`                                                              | Working Backwards — stress-test your product concept customer-first             | `prfaq-{project}.md`      |

## Phase 2: Planning

Define what to build and for whom.

| Workflow                | Purpose                                                                             | Produces                                          |
|-------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------|
| `bmad-prd`              | Create, update, or validate a PRD — facilitated discovery, three intents in one skill | Create/Update: `prd.md`, `addendum.md`, `.memlog.md`; Validate: `validation-report.html` + `.md` |
| `bmad-ux`               | Design user experience (when UX matters) — DESIGN.md (visual) + EXPERIENCE.md (behavioral) spine pair | `DESIGN.md`, `EXPERIENCE.md`, `.memlog.md`  |
