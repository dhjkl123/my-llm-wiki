---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/9ce3c397c9b238de96f7365da8019f6f66b059da/src/core-skills/module.yaml"
source_type: official-github-file
ingested: 2026-08-17
retrieved_at: "2026-08-17T15:11:24+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/core-skills/module.yaml"
version: 6.11.0
tag: v6.11.0
commit_sha: 9ce3c397c9b238de96f7365da8019f6f66b059da
license: MIT
sha256: 75cb5eccdd193b3282a948f57b27273112aabd619eb29fcca442d33003a914fb
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

# The one directory created at install time. Everything else (module artifact
# folders, project knowledge) is created lazily by the first skill that writes there.
directories:
  - "{output_folder}"
