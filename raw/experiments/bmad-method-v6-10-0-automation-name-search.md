---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/tree/081e64ee5aab2316b912883f7bee528ee143ce36"
source_type: synthetic-experiment
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
sha256: 558e482f1891a5fc0d4d6bedaa3bd0ddd761ad42f34dce80e7a6c2ca2968fe94
---
# Exact automation-name search

## Protocol

1. Clone the official repository at tag `v6.10.0`.
2. Verify `HEAD` is `081e64ee5aab2316b912883f7bee528ee143ce36`.
3. From the repository root, run:

```text
rg -n "bmad-build-auto|bmad-loop|bmad-dev-auto|bmad-automator" . --glob "*.md" --glob "*.yaml"
```

## Observed result

- `bmad-loop`: found in `bmad-modules.yaml`, `CHANGELOG.md`, and reference documentation.
- `bmad-dev-auto`: found in the workflow map, reference documentation, changelog, and implementation skill files.
- `bmad-automator`: found as a deprecated module replaced by `bmad-loop`.
- `bmad-build-auto`: no exact match in the searched Markdown and YAML files.

## Limitations

This is a bounded name search over one repository tag and selected text-file extensions. A negative result does not prove that the name never existed in another version, fork, issue, discussion, generated package, or unsearched file type.
