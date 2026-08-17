---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/4-implementation/dev-story/workflow.md#L413-L450
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/4-implementation/dev-story/workflow.md
excerpt_lines: 413-450
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: cfed013b8b902a94e81d97fb77eacab0e21e901fb50232746eade31062f81e2c
---
    <!-- Final validation gates -->
    <action if="any task is incomplete">HALT - Complete remaining tasks before marking ready for review</action>
    <action if="regression failures exist">HALT - Fix regression issues before completing</action>
    <action if="File List is incomplete">HALT - Update File List with all changed files</action>
    <action if="definition-of-done validation fails">HALT - Address DoD failures before completing</action>
  </step>

  <step n="10" goal="Completion communication and user support">
    <action>Execute the enhanced definition-of-done checklist using the validation framework</action>
    <action>Prepare a concise summary in Dev Agent Record → Completion Notes</action>

    <action>Communicate to {user_name} that story implementation is complete and ready for review</action>
    <action>Summarize key accomplishments: story ID, story key, title, key changes made, tests added, files modified</action>
    <action>Provide the story file path and current status (now "review")</action>

    <action>Based on {user_skill_level}, ask if user needs any explanations about:
      - What was implemented and how it works
      - Why certain technical decisions were made
      - How to test or verify the changes
      - Any patterns, libraries, or approaches used
      - Anything else they'd like clarified
    </action>

    <check if="user asks for explanations">
      <action>Provide clear, contextual explanations tailored to {user_skill_level}</action>
      <action>Use examples and references to specific code when helpful</action>
    </check>

    <action>Once explanations are complete (or user indicates no questions), suggest logical next steps</action>
    <action>Recommended next steps (flexible based on project setup):
      - Review the implemented story and test the changes
      - Verify all acceptance criteria are met
      - Ensure deployment readiness if applicable
      - Run `code-review` workflow for peer review
      - Optional: If Test Architect module installed, run `/bmad:tea:automate` to expand guardrail tests
    </action>

    <output>💡 **Tip:** For best results, run `code-review` using a **different** LLM than the one that implemented this story.</output>
