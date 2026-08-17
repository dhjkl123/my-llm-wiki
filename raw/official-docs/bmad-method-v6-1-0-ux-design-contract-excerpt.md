---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/2-plan-workflows/create-ux-design/steps/step-01-init.md#L53-L115
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/2-plan-workflows/create-ux-design/steps/step-01-init.md
excerpt_lines: 53-115
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: c8104c0cd73d253ea98eb7bf58568b1feb2595849be37e438b06f003f9b0d360
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
- Research Documents (`*prd*.md`)
- Project Documentation (generally multiple documents might be found for this in the `{product_knowledge}` or `docs` folder.)
- Project Context (`**/project-context.md`)

<critical>Confirm what you have found with the user, along with asking if the user wants to provide anything else. Only after this confirmation will you proceed to follow the loading rules</critical>

**Loading Rules:**

- Load ALL discovered files completely that the user confirmed or provided (no offset/limit)
- If there is a project context, whatever is relevant should try to be biased in the remainder of this whole workflow process
- For sharded folders, load ALL files to get complete picture, using the index first to potentially know the potential of each document
- index.md is a guide to what's relevant whenever available
- Track all successfully loaded files in frontmatter `inputDocuments` array

#### B. Create Initial Document

Copy the template from `{installed_path}/ux-design-template.md` to `{planning_artifacts}/ux-design-specification.md`
Initialize frontmatter in the template.

#### C. Complete Initialization and Report

Complete setup and report to user:

**Document Setup:**

- Created: `{planning_artifacts}/ux-design-specification.md` from template
- Initialized frontmatter with workflow state

**Input Documents Discovered:**
Report what was found:
"Welcome {{user_name}}! I've set up your UX design workspace for {{project_name}}.

**Documents Found:**

- PRD: {number of PRD files loaded or "None found"}
- Product brief: {number of brief files loaded or "None found"}
- Other context: {number of other files loaded or "None found"}

**Files loaded:** {list of specific file names or "No additional documents found"}

Do you have any other documents you'd like me to include, or shall we continue to the next step?

[C] Continue to UX discovery"

## NEXT STEP:

After user selects [C] to continue, ensure the file `{planning_artifacts}/ux-design-specification.md` has been created and saved, and then load `{project-root}/_bmad/bmm/workflows/2-plan-workflows/create-ux-design/steps/step-02-discovery.md` to begin the UX discovery phase.

Remember: Do NOT proceed to step-02 until output file has been updated and user explicitly selects [C] to continue!
