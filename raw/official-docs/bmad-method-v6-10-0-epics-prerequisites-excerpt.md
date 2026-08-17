---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/bmm-skills/3-solutioning/bmad-create-epics-and-stories/steps/step-01-validate-prerequisites.md#L45-L82"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/3-solutioning/bmad-create-epics-and-stories/steps/step-01-validate-prerequisites.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "45-82"
sha256: 34c7b7e32e5abc6189c9f2cfb19c817a8b56ca3ed95ca2137487544192e87985
---
**CRITICAL PREREQUISITE VALIDATION:**

Verify required documents exist and are complete:

1. **PRD.md** - Contains requirements (FRs and NFRs) and product scope
2. **Architecture.md** - Contains technical decisions, API contracts, data models
3. **UX design contract** (if UI exists) - Contains visual identity, interaction patterns, mockups, and user flows

### 2. Document Discovery and Validation

Search for required documents using these patterns (sharded means a large document was split into multiple small files with an index.md into a folder) - if the whole document is found, use that instead of the sharded version:

**PRD Document Search Priority:**

1. `{planning_artifacts}/*prd*.md` (whole document)
2. `{planning_artifacts}/*prd*/index.md` (sharded version)

**Architecture Document Search Priority:**

1. `{planning_artifacts}/*architecture*.md` (whole document)
2. `{planning_artifacts}/*architecture*/index.md` (sharded version)

**UX Design Document Search (Optional):**

1. `{planning_artifacts}/ux-designs/ux-*/DESIGN.md` and `{planning_artifacts}/ux-designs/ux-*/EXPERIENCE.md` (bmad-ux spine pair)
2. `{planning_artifacts}/*ux*.md` (legacy whole document)
3. `{planning_artifacts}/*ux*/index.md` (legacy sharded version)

For each matching bmad-ux run folder, treat `DESIGN.md` and `EXPERIENCE.md` as one UX design contract:

- Confirm and load both files together. `DESIGN.md` owns visual identity and design tokens; `EXPERIENCE.md` owns information architecture, behavior, states, interactions, accessibility, and journeys.
- Add both files to the `inputDocuments: []` frontmatter array.
- If only one spine exists, report the incomplete pair and ask whether the user wants to include the partial UX handoff.
- If multiple run folders match, show each run folder with the spine frontmatter `status` and `updated` values when available, then ask the user which UX design contract to include.

Before proceeding, Ask the user if there are any other documents to include for analysis, and if anything found should be excluded. Wait for user confirmation. Once confirmed, create the {planning_artifacts}/epics.md from the ../templates/epics-template.md and in the front matter list the files in the array of `inputDocuments: []`.

### 3. Extract Functional Requirements (FRs)
