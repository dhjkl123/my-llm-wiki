---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/docs/reference/workflow-map.md#L52-L100"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "docs/reference/workflow-map.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "52-100"
sha256: 46defd0cc3a2ecab6b3279787d04f1a729ea76c019230b0f09a83493e34ff6c4
---

:::tip[Three intents in one skill]
`bmad-prd` handles the full PRD lifecycle. State your intent when invoking or the skill will ask:

- **Create** — new PRD from scratch via coached discovery; produces `prd.md`, `addendum.md`, and `.memlog.md`
- **Update** — reconcile an existing PRD with a change signal, surfacing conflicts before applying changes
- **Validate** — critique a PRD against a configurable checklist and produce a structured HTML findings report
:::

:::tip[Upstream: `bmad-product-brief`]
`bmad-product-brief` (Phase 1) produces a `product-brief.md` that `bmad-prd` can source-extract during Discovery, reducing re-explanation and keeping the two documents aligned. Neither skill requires the other — start with `bmad-prd` directly if you already know what you're building.
:::

## Phase 3: Solutioning

Decide how to build it and break work into stories.

| Workflow                              | Purpose                                    | Produces                    |
|---------------------------------------|--------------------------------------------|-----------------------------|
| `bmad-architecture`            | Make technical decisions explicit          | `ARCHITECTURE-SPINE.md` is the spine by default but can hydrate to your desired output or presentation needs also |
| `bmad-create-epics-and-stories`       | Break requirements into implementable work | Epic files with stories     |
| `bmad-check-implementation-readiness` | Gate check before implementation           | PASS/CONCERNS/FAIL decision |

## Phase 4: Implementation

Build it, one story at a time. Phase 4 epic and story automation is now available also. So you can choose how you want to stay in the loop. You can choose the full flow, or go right to quick flow.

| Workflow               | Purpose                                                                       | Produces                                             |
|------------------------|-------------------------------------------------------------------------------|------------------------------------------------------|
| `bmad-sprint-planning` | Initialize tracking (once per project to sequence the dev cycle)              | `sprint-status.yaml`                                 |
| `bmad-create-story`    | Prepare next story for implementation                                         | `story-[slug].md`                                    |
| `bmad-dev-story`       | Implement the story                                                           | Working code + tests                                 |
| `bmad-code-review`     | Validate implementation quality                                               | Approved or changes requested                        |
| `bmad-correct-course`  | Handle significant mid-sprint changes                                         | Updated plan or re-routing                           |
| `bmad-sprint-status`   | Track sprint progress and story status                                        | Sprint status update                                 |
| `bmad-retrospective`   | Review after epic completion                                                  | Lessons learned                                      |

## Quick Flow (Parallel Track)

Skip phases 1-3 for small, well-understood work.

| Workflow         | Purpose                                                                   | Produces           |
|------------------|---------------------------------------------------------------------------|--------------------|
| `bmad-quick-dev` | Unified quick flow — clarify intent, plan, implement, review, and present | `spec-*.md` + code |
| `bmad-dev-auto`  | Runs one unattended development-loop iteration — small intent in, code out | `spec-*.md` + code |

For the reference on unattended development loops with `bmad-dev-auto`, see [Autonomous Development Loops](./dev-auto.md).

## Context Management
