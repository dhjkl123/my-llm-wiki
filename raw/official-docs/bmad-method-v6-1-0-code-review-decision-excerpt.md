---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/4-implementation/code-review/workflow.md#L180-L265
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/4-implementation/code-review/workflow.md
excerpt_lines: 180-265
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: 0cdbe31e6e11f9005d91691cf1e21051fdd2945f449d7a0218a6f8ecbfe9e507
---
  <ask>What should I do with these issues?

    1. **Fix them automatically** - I'll update the code and tests
    2. **Create action items** - Add to story Tasks/Subtasks for later
    3. **Show me details** - Deep dive into specific issues

    Choose [1], [2], or specify which issue to examine:</ask>

  <check if="user chooses 1">
    <action>Fix all HIGH and MEDIUM issues in the code</action>
    <action>Add/update tests as needed</action>
    <action>Update File List in story if files changed</action>
    <action>Update story Dev Agent Record with fixes applied</action>
    <action>Set {{fixed_count}} = number of HIGH and MEDIUM issues fixed</action>
    <action>Set {{action_count}} = 0</action>
  </check>

  <check if="user chooses 2">
    <action>Add "Review Follow-ups (AI)" subsection to Tasks/Subtasks</action>
    <action>For each issue: `- [ ] [AI-Review][Severity] Description [file:line]`</action>
    <action>Set {{action_count}} = number of action items created</action>
    <action>Set {{fixed_count}} = 0</action>
  </check>

  <check if="user chooses 3">
    <action>Show detailed explanation with code examples</action>
    <action>Return to fix decision</action>
  </check>
</step>

<step n="5" goal="Update story status and sync sprint tracking">
  <!-- Determine new status based on review outcome -->
  <check if="all HIGH and MEDIUM issues fixed AND all ACs implemented">
    <action>Set {{new_status}} = "done"</action>
    <action>Update story Status field to "done"</action>
  </check>
  <check if="HIGH or MEDIUM issues remain OR ACs not fully implemented">
    <action>Set {{new_status}} = "in-progress"</action>
    <action>Update story Status field to "in-progress"</action>
  </check>
  <action>Save story file</action>

  <!-- Determine sprint tracking status -->
  <check if="{sprint_status} file exists">
    <action>Set {{current_sprint_status}} = "enabled"</action>
  </check>
  <check if="{sprint_status} file does NOT exist">
    <action>Set {{current_sprint_status}} = "no-sprint-tracking"</action>
  </check>

  <!-- Sync sprint-status.yaml when story status changes (only if sprint tracking enabled) -->
  <check if="{{current_sprint_status}} != 'no-sprint-tracking'">
    <action>Load the FULL file: {sprint_status}</action>
    <action>Find development_status key matching {{story_key}}</action>

    <check if="{{new_status}} == 'done'">
      <action>Update development_status[{{story_key}}] = "done"</action>
      <action>Update last_updated field to current date</action>
      <action>Save file, preserving ALL comments and structure</action>
      <output>✅ Sprint status synced: {{story_key}} → done</output>
    </check>

    <check if="{{new_status}} == 'in-progress'">
      <action>Update development_status[{{story_key}}] = "in-progress"</action>
      <action>Update last_updated field to current date</action>
      <action>Save file, preserving ALL comments and structure</action>
      <output>🔄 Sprint status synced: {{story_key}} → in-progress</output>
    </check>

    <check if="story key not found in sprint status">
      <output>⚠️ Story file updated, but sprint-status sync failed: {{story_key}} not found in sprint-status.yaml</output>
    </check>
  </check>

  <check if="{{current_sprint_status}} == 'no-sprint-tracking'">
    <output>ℹ️ Story status updated (no sprint tracking configured)</output>
  </check>

  <output>**✅ Review Complete!**

    **Story Status:** {{new_status}}
    **Issues Fixed:** {{fixed_count}}
    **Action Items Created:** {{action_count}}

    {{#if new_status == "done"}}Code review complete!{{else}}Address the action items and continue development.{{/if}}
  </output>
