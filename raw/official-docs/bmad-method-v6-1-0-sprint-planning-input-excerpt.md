---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/4-implementation/sprint-planning/workflow.md#L36-L48
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/4-implementation/sprint-planning/workflow.md
excerpt_lines: 36-48
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: e07ce19ba6c83955843f0453c1823556b5b6bd968941404124465c399eca8cf7
---
- `epics_location` = `{planning_artifacts}`
- `epics_pattern` = `*epic*.md`
- `status_file` = `{implementation_artifacts}/sprint-status.yaml`

### Input Files

| Input | Path | Load Strategy |
|-------|------|---------------|
| Epics | `{planning_artifacts}/*epic*.md` (whole) or `{planning_artifacts}/*epic*/*.md` (sharded) | FULL_LOAD |

### Context

- `project_context` = `**/project-context.md` (load if exists)
