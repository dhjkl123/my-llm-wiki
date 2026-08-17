---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/3-solutioning/create-epics-and-stories/steps/step-01-validate-prerequisites.md#L65-L96
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/3-solutioning/create-epics-and-stories/steps/step-01-validate-prerequisites.md
excerpt_lines: 65-96
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: d29cc01c3383865a08824ee16cef82576a8d81ebc985b7f9c51578fd8b11ef1f
---
Welcome {user_name} to comprehensive epic and story creation!

**CRITICAL PREREQUISITE VALIDATION:**

Verify required documents exist and are complete:

1. **PRD.md** - Contains requirements (FRs and NFRs) and product scope
2. **Architecture.md** - Contains technical decisions, API contracts, data models
3. **UX Design.md** (if UI exists) - Contains interaction patterns, mockups, user flows

### 2. Document Discovery and Validation

Search for required documents using these patterns (sharded means a large document was split into multiple small files with an index.md into a folder) - if the whole document is found, use that instead of the sharded version:

**PRD Document Search Priority:**

1. `{planning_artifacts}/*prd*.md` (whole document)
2. `{planning_artifacts}/*prd*/index.md` (sharded version)

**Architecture Document Search Priority:**

1. `{planning_artifacts}/*architecture*.md` (whole document)
2. `{planning_artifacts}/*architecture*/index.md` (sharded version)

**UX Design Document Search (Optional):**

1. `{planning_artifacts}/*ux*.md` (whole document)
2. `{planning_artifacts}/*ux*/index.md` (sharded version)

Before proceeding, Ask the user if there are any other documents to include for analysis, and if anything found should be excluded. Wait for user confirmation. Once confirmed, create the {outputFile} from the {epicsTemplate} and in the front matter list the files in the array of `inputDocuments: []`.

### 3. Extract Functional Requirements (FRs)
