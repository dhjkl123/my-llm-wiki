---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/69cbeb4d07f318180c3d610c511381b9f494e786/src/core-skills/module.yaml"
source_type: official-github-file
ingested: 2026-08-17
retrieved_at: "2026-08-17T15:03:08+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/core-skills/module.yaml"
version: 6.5.0
tag: v6.5.0
commit_sha: 69cbeb4d07f318180c3d610c511381b9f494e786
license: MIT
sha256: 017bb154eb316ed8fb60a6d2ed991bea963354650904037cd5330eaa230d0e14
---
code: core
name: "BMad Core Module"
description: "Core configuration and shared resources"

header: "BMad Core Configuration"
subheader: "Configure the core settings for your BMad installation.\nThese settings will be used across all installed bmad skills, workflows, and agents."

user_name:
  prompt: "What should agents call you? (Use your name or a team name)"
  scope: user
  default: "BMad"
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
