---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/2-plan-workflows/create-prd/steps-c/step-01-init.md#L85-L160
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/2-plan-workflows/create-prd/steps-c/step-01-init.md
excerpt_lines: 85-160
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: 9497d82b0c79b62c75cbe108faff9f4c031f61e25d941ead5c5ecf6919da5e9b
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
- Research Documents (`/*research*.md`)
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

**Document Setup:**

- Copy the template from `{prdTemplate}` to `{outputFile}`
- Initialize frontmatter with proper structure including inputDocuments array.

#### C. Present Initialization Results

**Setup Report to User:**

"Welcome {{user_name}}! I've set up your PRD workspace for {{project_name}}.

**Document Setup:**

- Created: `{outputFile}` from template
- Initialized frontmatter with workflow state

**Input Documents Discovered:**

- Product briefs: {{briefCount}} files {if briefCount > 0}✓ loaded{else}(none found){/if}
- Research: {{researchCount}} files {if researchCount > 0}✓ loaded{else}(none found){/if}
- Brainstorming: {{brainstormingCount}} files {if brainstormingCount > 0}✓ loaded{else}(none found){/if}
- Project docs: {{projectDocsCount}} files {if projectDocsCount > 0}✓ loaded (brownfield project){else}(none found - greenfield project){/if}

**Files loaded:** {list of specific file names or "No additional documents found"}

{if projectDocsCount > 0}
📋 **Note:** This is a **brownfield project**. Your existing project documentation has been loaded. In the next step, I'll ask specifically about what new features or changes you want to add to your existing system.
{/if}

Do you have any other documents you'd like me to include, or shall we continue to the next step?"

### 4. Present MENU OPTIONS

Display menu after setup report:

"[C] Continue - Save this and move to Project Discovery (Step 2 of 11)"

#### Menu Handling Logic:

- IF C: Update output file frontmatter, adding this step name to the end of the list of stepsCompleted, then read fully and follow: {nextStepFile}
- IF user provides additional files: Load them, update inputDocuments and documentCounts, redisplay report
- IF user asks questions: Answer and redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
