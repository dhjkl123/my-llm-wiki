---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/4-implementation/code-review/workflow.md#L36-L62
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/4-implementation/code-review/workflow.md
excerpt_lines: 36-62
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: e710eca1e67b2a5b77298e30f52d528d4837229f3db4ae9186fb62b515c61ae0
---
### Paths

- `installed_path` = `{project-root}/_bmad/bmm/workflows/4-implementation/code-review`
- `sprint_status` = `{implementation_artifacts}/sprint-status.yaml`
- `validation` = `{installed_path}/checklist.md`

### Input Files

| Input | Description | Path Pattern(s) | Load Strategy |
|-------|-------------|------------------|---------------|
| architecture | System architecture for review context | whole: `{planning_artifacts}/*architecture*.md`, sharded: `{planning_artifacts}/*architecture*/*.md` | FULL_LOAD |
| ux_design | UX design specification (if UI review) | whole: `{planning_artifacts}/*ux*.md`, sharded: `{planning_artifacts}/*ux*/*.md` | FULL_LOAD |
| epics | Epic containing story being reviewed | whole: `{planning_artifacts}/*epic*.md`, sharded_index: `{planning_artifacts}/*epic*/index.md`, sharded_single: `{planning_artifacts}/*epic*/epic-{{epic_num}}.md` | SELECTIVE_LOAD |

### Context

- `project_context` = `**/project-context.md` (load if exists)

---

## EXECUTION

<workflow>

<step n="1" goal="Load story and discover changes">
  <action>Use provided {{story_path}} or ask user which story file to review</action>
  <action>Read COMPLETE story file</action>
