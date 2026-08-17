---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/bmm-skills/3-solutioning/bmad-check-implementation-readiness/steps/step-01-document-discovery.md#L49-L120"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/3-solutioning/bmad-check-implementation-readiness/steps/step-01-document-discovery.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "49-120"
sha256: 51771572b024faad9a734ebe6ceb7243ea081603d56620dce23ec150429ec417
---

1. Search for all required documents (PRD, Architecture, Epics, UX)
2. Group sharded documents together
3. Identify any duplicates (whole + sharded versions)
4. Present findings for your confirmation"

### 2. Document Search Patterns

Search for each document type using these patterns:

#### A. PRD Documents

- Whole: `{planning_artifacts}/*prd*.md`
- Sharded: `{planning_artifacts}/*prd*/index.md` and related files

#### B. Architecture Documents

- Whole: `{planning_artifacts}/*architecture*.md`
- Sharded: `{planning_artifacts}/*architecture*/index.md` and related files

#### C. Epics & Stories Documents

- Whole: `{planning_artifacts}/*epic*.md`
- Sharded: `{planning_artifacts}/*epic*/index.md` and related files

#### D. UX Design Documents

- Whole: `{planning_artifacts}/*ux*.md`
- Sharded: `{planning_artifacts}/*ux*/index.md` and related files

### 3. Organize Findings

For each document type found:

```
## [Document Type] Files Found

**Whole Documents:**
- [filename.md] ([size], [modified date])

**Sharded Documents:**
- Folder: [foldername]/
  - index.md
  - [other files in folder]
```

### 4. Identify Critical Issues

#### Duplicates (CRITICAL)

If both whole and sharded versions exist:

```
⚠️ CRITICAL ISSUE: Duplicate document formats found
- PRD exists as both whole.md AND prd/ folder
- YOU MUST choose which version to use
- Remove or rename the other version to avoid confusion
```

#### Missing Documents (WARNING)

If required documents not found:

```
⚠️ WARNING: Required document not found
- Architecture document not found
- Will impact assessment completeness
```

### 5. Add Initial Report Section

Initialize {outputFile} with ../templates/readiness-report-template.md.
