---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/9ce3c397c9b238de96f7365da8019f6f66b059da/src/bmm-skills/v6-shims/README.md"
source_type: official-github-file
ingested: 2026-08-17
retrieved_at: "2026-08-17T14:46:34+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/v6-shims/README.md"
version: 6.11.0
tag: v6.11.0
commit_sha: 9ce3c397c9b238de96f7365da8019f6f66b059da
license: MIT
sha256: 05315a8e369f5ebb9e615c1a33fd2b3f85eb92a9455c974cdc7ec7d3ea0d10bf
---
# v6 Deprecation Shims

Skills in this folder are deprecated skills kept for backward compatibility with v6 skill IDs.
Some retain their full workflow, while others forward to the skill that replaced them, passing a
stated intent and pre-resolved customization fields so the target skips its own intent inference.

| Shim                       | Forwards to                          |
| -------------------------- | ------------------------------------ |
| `bmad-quick-dev`           | `bmad-build`                         |
| `bmad-dev-auto`            | `bmad-build-auto`                    |
| `bmad-create-story`        | Retained in full                     |
| `bmad-dev-story`           | Retained in full                     |
| `bmad-create-prd`          | `bmad-prd` (create intent)           |
| `bmad-edit-prd`            | `bmad-prd` (update intent)           |
| `bmad-validate-prd`        | `bmad-prd` (validate intent)         |
| `bmad-create-architecture` | `bmad-architecture` (create intent)  |
| `bmad-market-research`     | `bmad-deep-recon` (market type)      |
| `bmad-domain-research`     | `bmad-deep-recon` (domain type)      |
| `bmad-technical-research`  | `bmad-deep-recon` (technical type)   |
| `bmad-sprint-status`       | `bmad-sprint-planning` (status view) |

Enterprise users may still depend on these IDs, so they ship by default. Removal rides the
v7 cut — never a 6.x minor.

The folder is grouping only: the installer discovers skills recursively and installs each
one under its own `name`, so nesting here does not change any installed path or skill ID.
A future install option will let users include or exclude this folder before it is removed
outright.
