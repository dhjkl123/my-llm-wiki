---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md#L510-L558"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "510-558"
sha256: 5d957e12c82910dcfe85960c7f9a09430794d95bb4760a09e7ba3cf2d8e58396
---
<step n="7" goal="Detect multi-part integration architecture" if="workflow_mode != deep_dive and project has multiple parts">
<action>Analyze how parts communicate:
- Scan integration_scan_patterns across parts
- Identify: REST calls, GraphQL queries, gRPC, message queues, shared databases
- Document: API contracts between parts, data flow, authentication flow
</action>

<action>Create integration_points array with:

- from: source part
- to: target part
- type: REST API, GraphQL, gRPC, Event Bus, etc.
- details: Endpoints, protocols, data formats
  </action>

<action>IMMEDIATELY write integration-architecture.md to disk</action>
<action>Validate document completeness</action>

<template-output>integration_architecture</template-output>

<action>Update state file:

- Add to completed_steps: {"step": "step_7", "status": "completed", "timestamp": "{{now}}", "summary": "Integration architecture documented"}
- Update current_step = "step_8"
  </action>
  <action>PURGE integration details, keep only: "{{integration_count}} integration points"</action>
  </step>

<step n="8" goal="Generate architecture documentation for each part" if="workflow_mode != deep_dive">
<action>For each part in project_parts:
  - Use matched architecture template from Step 3 as base structure
  - Fill in all sections with discovered information:
    * Executive Summary
    * Technology Stack (from Step 3)
    * Architecture Pattern (from registry match)
    * Data Architecture (from Step 4 data models scan)
    * API Design (from Step 4 API scan if applicable)
    * Component Overview (from Step 4 component scan if applicable)
    * Source Tree (from Step 5)
    * Development Workflow (from Step 6)
    * Deployment Architecture (from Step 6)
    * Testing Strategy (from test patterns)
</action>

<action if="single part project">
  - Generate: architecture.md (no part suffix)
</action>

<action if="multi-part project">
