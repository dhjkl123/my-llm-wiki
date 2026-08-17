---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/5247108ba3f45b2e9731fa41919029b3d2623023/src/bmm-skills/ship/bmad-build-auto/SKILL.md#L1-L13"
source_type: official-github-file-excerpt
ingested: 2026-08-04
retrieved_at: "2026-08-04T11:37:44+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "src/bmm-skills/ship/bmad-build-auto/SKILL.md"
version: 6.10.0
commit_sha: 5247108ba3f45b2e9731fa41919029b3d2623023
license: MIT
excerpt_lines: "1-13"
sha256: ea6931f8210e92f7d9cfb845040d557d4d8c02eced3acc3d77bd2fcc4fffc235
---
---
name: bmad-build-auto
description: 'One iteration of an unattended development loop. Use when invoked by name.'
---

Run the following command exactly once without changing the current working directory. Replace `{project-root}` with the absolute path to the project root and `{skill-root}` with the absolute path to this skill's directory:

```bash
uv run --no-cache "{project-root}/_bmad/scripts/render_skill.py" --project-root "{project-root}" --skill "{skill-root}"
```

- On success, read and follow the one absolute `workflow.md` instruction printed to stdout.
- On failure (including `uv` being unavailable), report the command output and HALT. Do not run any workflow source directly.
