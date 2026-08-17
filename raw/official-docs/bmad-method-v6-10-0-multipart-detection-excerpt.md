---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md#L160-L180"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "160-180"
sha256: 7180689b8ff6284cb5cd7c71775bbf37b8cc13ba768d97140be92e560759dcc1
---
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
