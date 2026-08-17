---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/3-solutioning/create-epics-and-stories/steps/step-01-validate-prerequisites.md#L223-L255
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/3-solutioning/create-epics-and-stories/steps/step-01-validate-prerequisites.md
excerpt_lines: 223-255
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: c8b54afc57a4e3bc87a97f2695efc0da85473100e5ece89c706b2d0bc83f99bf
---
### 9. Get User Confirmation

Ask: "Do these extracted requirements accurately represent what needs to be built? Any additions or corrections?"

Update the requirements based on user feedback until confirmation is received.

## CONTENT TO SAVE TO DOCUMENT:

After extraction and confirmation, update {outputFile} with:

- Complete FR list in {{fr_list}} section
- Complete NFR list in {{nfr_list}} section
- All additional requirements in {{additional_requirements}} section
- UX Design requirements in {{ux_design_requirements}} section (if UX document exists)

### 10. Present MENU OPTIONS

Display: `**Confirm the Requirements are complete and correct to [C] continue:**`

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- User can chat or ask questions - always respond and then end with display again of the menu option

#### Menu Handling Logic:

- IF C: Save all to {outputFile}, update frontmatter, then read fully and follow: {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#10-present-menu-options)

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and all requirements are saved to document and frontmatter is updated, will you then read fully and follow: {nextStepFile} to begin epic design step.
