---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/3-solutioning/create-architecture/steps/step-01-init.md#L53-L100
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/3-solutioning/create-architecture/steps/step-01-init.md
excerpt_lines: 53-100
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: fd76e06b2f7bcc2aa67deec5e28d5f561b3887694b53136c45f1aec70a6357ec
---
If no document exists or no `stepsCompleted` in frontmatter:

#### A. Input Document Discovery

Discover and load context documents using smart discovery. Documents can be in the following locations:
- {planning_artifacts}/**
- {output_folder}/**
- {product_knowledge}/**
- docs/**

Also - when searching - documents can be a single markdown file, or a folder with an index and multiple files. For Example, if searching for `*foo*.md` and not found, also search for a folder called *foo*/index.md (which indicates sharded content)

Try to discover the following:
- Product Brief (`*brief*.md`)
- Product Requirements Document (`*prd*.md`)
- UX Design (`*ux-design*.md`) and other
- Research Documents (`*research*.md`)
- Project Documentation (generally multiple documents might be found for this in the `{product_knowledge}` or `docs` folder.)
- Project Context (`**/project-context.md`)

<critical>Confirm what you have found with the user, along with asking if the user wants to provide anything else. Only after this confirmation will you proceed to follow the loading rules</critical>

**Loading Rules:**

- Load ALL discovered files completely that the user confirmed or provided (no offset/limit)
- If there is a project context, whatever is relevant should try to be biased in the remainder of this whole workflow process
- For sharded folders, load ALL files to get complete picture, using the index first to potentially know the potential of each document
- index.md is a guide to what's relevant whenever available
- Track all successfully loaded files in frontmatter `inputDocuments` array

#### B. Validate Required Inputs

Before proceeding, verify we have the essential inputs:

**PRD Validation:**

- If no PRD found: "Architecture requires a PRD to work from. Please run the PRD workflow first or provide the PRD file path."
- Do NOT proceed without PRD

**Other Input that might exist:**

- UX Spec: "Provides UI/UX architectural requirements"

#### C. Create Initial Document

Copy the template from `{installed_path}/architecture-decision-template.md` to `{planning_artifacts}/architecture.md`

#### D. Complete Initialization and Report
