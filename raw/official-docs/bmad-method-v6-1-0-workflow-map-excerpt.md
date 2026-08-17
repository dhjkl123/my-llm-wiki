---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/docs/reference/workflow-map.md#L22-L82
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: docs/reference/workflow-map.md
excerpt_lines: 22-82
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: 2a5bbffb883f38c973902860e9366fbc1615de8631f4459e83d6c1cbdb15159e
---
## Phase 1: Analysis (Optional)

Explore the problem space and validate ideas before committing to planning.

| Workflow                        | Purpose                                                                    | Produces                  |
| ------------------------------- | -------------------------------------------------------------------------- | ------------------------- |
| `bmad-brainstorming`            | Brainstorm Project Ideas with guided facilitation of a brainstorming coach | `brainstorming-report.md` |
| `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research` | Validate market, technical, or domain assumptions | Research findings |
| `bmad-create-product-brief`     | Capture strategic vision                                                   | `product-brief.md`        |

## Phase 2: Planning

Define what to build and for whom.

| Workflow                    | Purpose                                  | Produces     |
| --------------------------- | ---------------------------------------- | ------------ |
| `bmad-create-prd`    | Define requirements (FRs/NFRs)           | `PRD.md`     |
| `bmad-create-ux-design`  | Design user experience (when UX matters) | `ux-spec.md` |

## Phase 3: Solutioning

Decide how to build it and break work into stories.

| Workflow                                  | Purpose                                    | Produces                    |
| ----------------------------------------- | ------------------------------------------ | --------------------------- |
| `bmad-create-architecture`            | Make technical decisions explicit          | `architecture.md` with ADRs |
| `bmad-create-epics-and-stories`       | Break requirements into implementable work | Epic files with stories     |
| `bmad-check-implementation-readiness` | Gate check before implementation           | PASS/CONCERNS/FAIL decision |

## Phase 4: Implementation

Build it, one story at a time. Coming soon, full phase 4 automation!

| Workflow                   | Purpose                                                                  | Produces                         |
| -------------------------- | ------------------------------------------------------------------------ | -------------------------------- |
| `bmad-sprint-planning` | Initialize tracking (once per project to sequence the dev cycle)         | `sprint-status.yaml`          |
| `bmad-create-story`    | Prepare next story for implementation                                    | `story-[slug].md`             |
| `bmad-dev-story`       | Implement the story                                                      | Working code + tests          |
| `bmad-code-review`     | Validate implementation quality                                          | Approved or changes requested |
| `bmad-correct-course`  | Handle significant mid-sprint changes                                    | Updated plan or re-routing    |
| `bmad-sprint-status`   | Track sprint progress and story status                                   | Sprint status update          |
| `bmad-retrospective`   | Review after epic completion                                             | Lessons learned               |

## Quick Flow (Parallel Track)

Skip phases 1-3 for small, well-understood work.

| Workflow              | Purpose                                    | Produces                                      |
| --------------------- | ------------------------------------------ | --------------------------------------------- |
| `bmad-quick-spec` | Define an ad-hoc change                    | `tech-spec.md` (story file for small changes) |
| `bmad-quick-dev`  | Implement from spec or direct instructions | Working code + tests                          |

## Context Management

Each document becomes context for the next phase. The PRD tells the architect what constraints matter. The architecture tells the dev agent which patterns to follow. Story files give focused, complete context for implementation. Without this structure, agents make inconsistent decisions.

### Project Context

:::tip[Recommended]
Create `project-context.md` to ensure AI agents follow your project's rules and preferences. This file works like a constitution for your project — it guides implementation decisions across all workflows. This optional file can be generated at the end of Architecture Creation, or in an existing project it can be generated also to capture whats important to keep aligned with current conventions.
:::
