---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/tree/521f1e15ca819b855571da5e13623afdee4a2122
source_type: synthetic-experiment
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: .
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: e1beeec46cb1315bb4d35475c1a8083793dfc6b2c5d0904467cfcb303c6341f3
---
# BMAD v6.1.0 automation-name search

## Purpose

Test whether the exact names `bmad-build-auto`, `bmad-loop`, or `bmad-dev-auto`
occur in the tracked files or tracked paths of the official v6.1.0 tag.

## Environment and scope

- Run date: 2026-08-03
- Git client: local command-line Git on Windows
- Repository: `https://github.com/bmad-code-org/BMAD-METHOD.git`
- Tag: `v6.1.0`
- Resolved commit: `521f1e15ca819b855571da5e13623afdee4a2122`
- Scope: every tracked file and path at the tag
- Matching: case-insensitive for file content; case-insensitive path filtering

## Protocol

```powershell
git clone --depth 1 --branch v6.1.0 https://github.com/bmad-code-org/BMAD-METHOD.git [temporary-directory]
git -C [temporary-directory] rev-parse HEAD
git -C [temporary-directory] grep -n -i -E 'bmad-build-auto|bmad-loop|bmad-dev-auto' v6.1.0 -- .
git -C [temporary-directory] ls-tree -r --name-only v6.1.0 | Select-String -Pattern 'build-auto|bmad-loop|dev-auto'
git -C [temporary-directory] grep -n -i 'full phase 4 automation' v6.1.0 -- docs/reference/workflow-map.md
```

## Observed output

```text
rev-parse:
521f1e15ca819b855571da5e13623afdee4a2122

content search:
(no matches; git grep exit code 1)

path search:
(no matches; match count 0)

workflow-map control search:
v6.1.0:docs/reference/workflow-map.md:53:Build it, one story at a time. Coming soon, full phase 4 automation!
```

## Interpretation and limitation

The three exact names are not present in the bounded official v6.1.0 snapshot.
This does not prove absence from another tag, the `next` channel, a module in a
different repository, a fork, generated installation output, an issue, or a
Discussion. Any cross-version existence claim requires those scopes to be searched
separately. Confidence for the negative claim remains low.
