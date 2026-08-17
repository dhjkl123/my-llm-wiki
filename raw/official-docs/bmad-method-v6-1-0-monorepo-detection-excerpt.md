---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/521f1e15ca819b855571da5e13623afdee4a2122/src/bmm/workflows/document-project/workflows/full-scan-instructions.md#L150-L185
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
document_path: src/bmm/workflows/document-project/workflows/full-scan-instructions.md
excerpt_lines: 150-185
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: 0a90d9743ce31a646cadebdb8c29f9e064d3bcbfb2d7b511505169acb1e534ab
---
<step n="1" goal="Detect project structure and classify project type" if="workflow_mode != deep_dive">
<action>Ask user: "What is the root directory of the project to document?" (default: current working directory)</action>
<action>Store as {{project_root_path}}</action>

<action>Scan {{project_root_path}} for key indicators:

- Directory structure (presence of client/, server/, api/, src/, app/, etc.)
- Key files (package.json, go.mod, requirements.txt, etc.)
- Technology markers matching detection_keywords from project-types.csv
  </action>

<action>Detect if project is:

- **Monolith**: Single cohesive codebase
- **Monorepo**: Multiple parts in one repository
- **Multi-part**: Separate client/server or similar architecture
  </action>

<check if="multiple distinct parts detected (e.g., client/ and server/ folders)">
  <action>List detected parts with their paths</action>
  <ask>I detected multiple parts in this project:
  {{detected_parts_list}}

Is this correct? Should I document each part separately? [y/n]
</ask>

<action if="user confirms">Set repository_type = "monorepo" or "multi-part"</action>
<action if="user confirms">For each detected part: - Identify root path - Run project type detection using key_file_patterns from documentation-requirements.csv - Store as part in project_parts array
</action>

<action if="user denies or corrects">Ask user to specify correct parts and their paths</action>
</check>

<check if="single cohesive project detected">
  <action>Set repository_type = "monolith"</action>
  <action>Create single part in project_parts array with root_path = {{project_root_path}}</action>
