---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/3-solutioning/check-implementation-readiness/steps/step-01-document-discovery.md#L51-L164
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/3-solutioning/check-implementation-readiness/steps/step-01-document-discovery.md
excerpt_lines: 51-164
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: c0b5a020908750401412b969faaf671db1fe0f480e4ab3cb147b112ab22ccd4c
---
"Beginning **Document Discovery** to inventory all project files.

I will:

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

Initialize {outputFile} with {templateFile}.

### 6. Present Findings and Get Confirmation

Display findings and ask:
"**Document Discovery Complete**

[Show organized file list]

**Issues Found:**

- [List any duplicates requiring resolution]
- [List any missing documents]

**Required Actions:**

- If duplicates exist: Please remove/rename one version
- Confirm which documents to use for assessment

**Ready to proceed?** [C] Continue after resolving issues"

### 7. Present MENU OPTIONS

Display: **Select an Option:** [C] Continue to File Validation

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed with 'C' selection
- If duplicates identified, insist on resolution first
- User can clarify file locations or request additional searches

#### Menu Handling Logic:

- IF C: Save document inventory to {outputFile}, update frontmatter with completed step and files being included, and then read fully and follow: {nextStepFile}
- IF Any other comments or queries: help user respond then redisplay menu

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and document inventory is saved will you load {nextStepFile} to begin file validation.
