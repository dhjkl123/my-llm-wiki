---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/9ce3c397c9b238de96f7365da8019f6f66b059da/src/bmm-skills/ship/bmad-build/SKILL.md"
source_type: official-github-file
ingested: 2026-08-17
retrieved_at: "2026-08-17T15:11:24+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/ship/bmad-build/SKILL.md"
version: 6.11.0
tag: v6.11.0
commit_sha: 9ce3c397c9b238de96f7365da8019f6f66b059da
license: MIT
sha256: bce4778d8d275095ca1836733337163c1bf11a5a62e6585b951de458a5ac2c8e
---
---
name: bmad-build
description: 'Implements any user intent, requirement, story, bug fix or change request by producing clean working code artifacts that follow the project''s existing architecture, patterns and conventions. Use when the user wants to build, fix, tweak, refactor, add or modify any code, component or feature.'
---

Run the following command exactly once without changing the current working directory. Replace `{project-root}` with the absolute path to the project root and `{skill-root}` with the absolute path to this skill's directory:

```bash
uv run --no-cache "{project-root}/_bmad/scripts/render_skill.py" --project-root "{project-root}" --skill "{skill-root}"
```

- On success, read and follow the one absolute `workflow.md` instruction printed to stdout.
- On failure (including `uv` being unavailable), report the command output and HALT. Do not run any workflow source directly.
