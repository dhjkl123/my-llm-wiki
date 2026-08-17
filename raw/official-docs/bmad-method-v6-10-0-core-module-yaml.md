---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/src/core-skills/module.yaml"
source_type: official-github-file
ingested: 2026-08-17
retrieved_at: "2026-08-17T15:11:24+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/core-skills/module.yaml"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
sha256: 46f8972746f0d4e49358fdf94b0c1ba856fd7a8eb66abc75d5aaff0624540479
---
code: core
name: "BMad Core Module"
description: "Shared utilities across modules"

header: "BMad Core Configuration"
subheader: "Configure the core settings for your BMad installation.\nThese settings will be used across all installed bmad skills, workflows, and agents."

user_name:
  prompt: "What should agents call you? (Use your name or a team name)"
  scope: user
  default: "BMad"
  result: "{value}"

project_name:
  prompt: "What is your project called?"
  default: "{directory_name}"
  result: "{value}"

communication_language:
  prompt: "What language should agents use when chatting with you?"
  scope: user
  default: "English"
  result: "{value}"

document_output_language:
  prompt: "Preferred document output language?"
  default: "English"
  result: "{value}"

output_folder:
  prompt: "Where should output files be saved?"
  default: "_bmad-output"
  result: "{project-root}/{value}"
