# Wiki Log

> Chronological record of wiki actions. This file is append-only: add entries at
> the end and never rewrite or remove an earlier entry.
>
> Entry heading format: `## [YYYY-MM-DD] <action> | <subject>`
>
> Allowed actions: `ingest`, `create`, `update`, `query`, `lint`, `archive`,
> `delete`, `map`, and `repair`.
>
> Each entry lists every affected repository-relative path. After 500 entries,
> rotate the completed file to `log-YYYY.md` and begin a new `log.md`; preserve the
> completed file unchanged.

## [2026-07-21] ingest | 2nd-Brain 개인지식 관리 원본 배치

- Selection: `understand-chat` identified the 2nd-Brain PKM core subgraph and its one-hop canonical neighbors; their leading frontmatter referenced 13 unique raw sources.
- Created:
  - `raw/notebooklm/2026-07-16-all-notes.md`
  - `raw/notebooklm/codegraph-github.md`
  - `raw/notebooklm/graphify-github.md`
  - `raw/notebooklm/llm-wiki-skill-github.md`
  - `raw/notebooklm/llm-wiki-zotero-notebooklm-youtube.md`
  - `raw/notebooklm/notebooklm-py-github.md`
  - `raw/notebooklm/understand-anything-github.md`
  - `raw/notebooklm/zotero-mcp-github.md`
  - `raw/web/NomaDamasslides-grab Best harness + editor + linter for generating slides in Claude Code  Codex - Claude Design Open Source Alternative.md`
  - `raw/web/stablyaiorca Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile..md`
  - `raw/youtube/📺 How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md`
  - `raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md`
  - `raw/youtube/📺 Orca Is the Free Cursor Killer Nobody's Talking About!.md`
- Updated: `SCHEMA.md`, `AGENTS.md` to register importer-preserved raw directories and legacy hash-coverage handling.
- Integrity: all 13 target files are byte-identical to the source vault; all 8 recorded post-frontmatter body hashes match; 5 legacy web/video captures have no recorded `sha256` and retain their original missing final LF as explicit coverage and format gaps.
- Canonical state: unchanged at 0 pages; `index.md` was not modified.

## [2026-07-21] lint | 0 issues found

- Raw files in the imported source set: 13.
- Source/target byte-identical files: 13.
- Recorded post-frontmatter body hashes checked and matched: 8.
- Documented legacy hash-coverage and final-LF format gaps: 5.
- Invalid UTF-8, BOM, CRLF, body-hash drift, missing ingest-log paths, and unregistered importer directories: 0.
- Canonical pages and index entries: 0; no canonical navigation update was required.

## [2026-07-21] create | 2nd-Brain canonical 지식 코어

- Evidence: the existing 13-file raw source set was mapped to eight central, reusable PKM subjects; no raw record was duplicated or mutated.
- Created:
  - `concepts/ai-knowledge-workflow.md`
  - `concepts/ai-personal-knowledge-management.md`
  - `concepts/llm-wiki.md`
  - `concepts/research-feedback-loop.md`
  - `concepts/second-brain-research-workflow.md`
  - `comparisons/knowledge-tool-roles.md`
  - `queries/notebooklm-query-compounding.md`
  - `queries/ua-knowledge-graph-workflow.md`
- Updated:
  - `SCHEMA.md`
  - `index.md`
  - `log.md`
- Navigation: the eight-page graph uses only resolvable canonical wikilinks, with at least two distinct non-self links per page.
- Provenance: every source and claim marker resolves to an existing repository-relative raw Markdown path.

## [2026-07-21] lint | 0 issues found

- Canonical pages: 8 total (5 concepts, 1 comparison, and 2 queries); all required frontmatter fields, types, dates, confidence values, contestation fields, and contradiction lists are valid.
- Taxonomy and navigation: 9 registered tags, 8 exact alphabetical index entries, 33 canonical links, minimum 3 outbound links per page, and minimum 2 inbound links per page.
- Provenance: 27 source references and 17 claim-level markers resolve to existing raw Markdown records; no marker is absent from its page source list.
- Raw integrity: 13 Markdown records checked, 8 recorded body hashes matched, and 5 importer-preserved legacy hash/final-LF coverage gaps remain documented.
- Formatting, duplicate slugs, broken links, self-links, orphan pages, source drift, and lint warnings: 0.

## [2026-07-21] repair | lint source-reference count correction

- Correction: the immediately preceding lint entry reports 27 source references, but the measured canonical frontmatter total is 30.
- Unchanged measurements: 17 claim-level markers, 33 canonical links, 8 canonical pages, and 0 lint errors or warnings.
- Updated: `log.md` only; no raw or canonical page was changed.

## [2026-07-29] delete | canonical wiki 및 지식그래프 초기화

- Preserved: `raw/` 아래 원본 Markdown 13개는 변경하지 않음.
- Deleted canonical pages:
  - `concepts/ai-knowledge-workflow.md`
  - `concepts/ai-personal-knowledge-management.md`
  - `concepts/llm-wiki.md`
  - `concepts/research-feedback-loop.md`
  - `concepts/second-brain-research-workflow.md`
  - `comparisons/knowledge-tool-roles.md`
  - `queries/notebooklm-query-compounding.md`
  - `queries/ua-knowledge-graph-workflow.md`
- Deleted derived graph state:
  - `.ua/knowledge-graph.json`
  - `.ua/meta.json`
- Updated:
  - `index.md`
  - `log.md`
- Canonical state: 0 pages; 새 canonical 문서 생성과 이후 지식그래프 재생성을 위한 초기 상태.

## [2026-07-29] delete | raw 원본 자료 초기화

- Deleted raw source records:
  - `raw/notebooklm/2026-07-16-all-notes.md`
  - `raw/notebooklm/codegraph-github.md`
  - `raw/notebooklm/graphify-github.md`
  - `raw/notebooklm/llm-wiki-skill-github.md`
  - `raw/notebooklm/llm-wiki-zotero-notebooklm-youtube.md`
  - `raw/notebooklm/notebooklm-py-github.md`
  - `raw/notebooklm/understand-anything-github.md`
  - `raw/notebooklm/zotero-mcp-github.md`
  - `raw/web/NomaDamasslides-grab Best harness + editor + linter for generating slides in Claude Code  Codex - Claude Design Open Source Alternative.md`
  - `raw/web/stablyaiorca Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile..md`
  - `raw/youtube/📺 How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md`
  - `raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md`
  - `raw/youtube/📺 Orca Is the Free Cursor Killer Nobody's Talking About!.md`
- Created empty directory placeholders:
  - `raw/notebooklm/.gitkeep`
  - `raw/web/.gitkeep`
  - `raw/youtube/.gitkeep`
- Updated:
  - `log.md`
- Result: raw source records 0, canonical pages 0, derived knowledge-graph state 0.

## [2026-08-03] ingest | BMAD v6.1.0 공식 근거 및 명칭 검색 실험

- Scope: official repository tag `v6.1.0`, commit `521f1e15ca819b855571da5e13623afdee4a2122`.
- Created source directories:
  - `raw/official-docs/`
  - `raw/releases/`
  - `raw/github-issues/`
  - `raw/examples/`
  - `raw/experiments/`
- Created official source records:
  - `raw/official-docs/bmad-method-v6-1-0-architecture-contract-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-code-review-decision-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-code-review-input-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-create-prd-contract-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-create-story-handoff-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-create-story-inputs-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-dev-story-gates-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-dev-story-input-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-epics-confirmation-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-epics-inputs-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-monorepo-detection-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-readiness-gate-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-sprint-planning-input-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-sprint-planning-output-excerpt.md`
  - `raw/official-docs/bmad-method-v6-1-0-workflow-map-excerpt.md`
  - `raw/releases/bmad-method-v6-1-0-release.md`
- Created reproducible experiment:
  - `raw/experiments/bmad-method-v6-1-0-automation-name-search.md`
- Updated contract and support documents:
  - `SCHEMA.md`
  - `docs/initial-research-backlog.md`
- Integrity: all 17 new raw Markdown records have SHA-256 over exact post-frontmatter body bytes; no existing raw body was modified.

## [2026-08-03] create | BMAD v6.1.0 AIDD workflow 첫 지식 세트

- Created canonical pages:
  - `concepts/bmad-msa-multi-repository-boundaries.md`
  - `comparisons/bmad-v6-1-0-automation-and-human-gates.md`
  - `queries/bmad-v6-1-0-workflow-contracts.md`
- Updated:
  - `index.md`
  - `log.md`
- Version boundary: “BMAD 6.10” is provisionally treated as official `v6.1.0`; no `v6.10` tag was found.
- Confidence boundary: exact-name absence and multi-repository inference remain `low`; official single-version workflow contracts are `medium`.
- Navigation: each of the three pages links to the other two active canonical pages.

## [2026-08-03] ingest | BMAD v6.1.0 UX Design contract 보강

- Created:
  - `raw/official-docs/bmad-method-v6-1-0-ux-design-contract-excerpt.md`
- Updated:
  - `queries/bmad-v6-1-0-workflow-contracts.md`
  - `log.md`
- Integrity: the new raw body matches source lines 53-115 at the pinned commit and its post-frontmatter SHA-256 matches.
- Canonical effect: replaced the UX contract research gap with verified optional inputs, output path, and initial human confirmation gate; page confidence remains `medium`.

## [2026-08-03] repair | UX contract canonical index 동기화

- Updated:
  - `index.md`
  - `log.md`
- Repair: synchronized the query summary with the newly verified UX workflow contract; canonical count and target path are unchanged.

## [2026-08-03] update | AIDD Workflow Evidence Wiki 프로젝트 안내

- Updated:
  - `AGENTS.md`
  - `README.ko.md`
  - `log.md`
- Orientation: renamed and described the project as a public-evidence AIDD workflow decision wiki, linked the pilot knowledge set, and synchronized the documented raw/canonical counts and source directories.

## [2026-08-03] lint | BMAD v6.1.0 초기 지식 세트 0 issues

- Canonical: 3 pages, 26 source references, 26 claim-level markers, and 6 resolvable non-self canonical links; every page has two distinct outbound targets.
- Index: 3 unique entries and declared total 3, matching the filesystem by type.
- Taxonomy: all 18 registered tags are used; no unregistered or unused tag remains.
- Raw integrity: 18 Markdown records checked and all post-frontmatter SHA-256 values match.
- Source fidelity: 16 official GitHub excerpts byte-match their declared line ranges at commit `521f1e15ca819b855571da5e13623afdee4a2122`; the official release body matches the GitHub API capture after LF normalization.
- Format: canonical and new raw files are UTF-8, LF, no BOM, and final-newline terminated; canonical pages remain below the 200-line split threshold.
- Provenance, frontmatter fields, type-directory fit, broken links, missing sources, marker/source disagreement, pending placeholders, index drift, and whitespace errors: 0.
- Updated: `log.md` only.

## [2026-08-03] ingest | BMAD v6.10.0 공식 근거 재수집

- Pinned official tag `v6.10.0` to commit
  `081e64ee5aab2316b912883f7bee528ee143ce36`.
- Created 18 immutable raw records: 16 official GitHub file excerpts, one official
  release capture, and one reproducible exact-name search experiment under
  `raw/official-docs/`, `raw/releases/`, and `raw/experiments/`.
- Preserved all 18 prior v6.1.0 raw records unchanged as version history.
- Integrity: each new record records a post-frontmatter SHA-256; commit permalinks
  and explicit excerpt line boundaries are used for GitHub files.

## [2026-08-03] update | BMAD v6.10.0 활성 지식 세트 교체

- Created:
  - `queries/bmad-v6-10-0-workflow-contracts.md`
  - `comparisons/bmad-v6-10-0-automation-and-human-gates.md`
- Updated:
  - `concepts/bmad-msa-multi-repository-boundaries.md`
  - `docs/initial-research-backlog.md`
  - `README.ko.md`
  - `AGENTS.md`
  - `index.md`
  - `log.md`
- Deleted the uncommitted, incorrectly targeted active pages
  `queries/bmad-v6-1-0-workflow-contracts.md` and
  `comparisons/bmad-v6-1-0-automation-and-human-gates.md`; their raw evidence
  remains immutable and available.
- Decision change: v6.10.0 officially contains `bmad-dev-auto` and opt-in
  `bmad-loop`; `bmad-automator` is deprecated, while `bmad-build-auto`
  remains unconfirmed with `low` confidence.

## [2026-08-03] ingest | BMAD v6.10.0 Epics 및 readiness 계약 보강

- Created:
  - `raw/official-docs/bmad-method-v6-10-0-epics-prerequisites-excerpt.md`
  - `raw/official-docs/bmad-method-v6-10-0-readiness-input-gate-excerpt.md`
- Updated:
  - `queries/bmad-v6-10-0-workflow-contracts.md`
  - `docs/initial-research-backlog.md`
  - `AGENTS.md`
  - `log.md`
- Canonical effect: verified PRD/Architecture/conditional UX prerequisites,
  `epics.md` creation, whole/sharded duplicate handling, and the human input
  selection gate.

## [2026-08-03] repair | Epics excerpt trailing blank line 복원

- Restored the source line 83 blank line in
  `raw/official-docs/bmad-method-v6-10-0-epics-prerequisites-excerpt.md` after a
  frontmatter hash patch had inadvertently trimmed it.
- Verification target: the body again byte-matches lines 45–83 at the pinned
  commit and the originally recorded SHA-256.

## [2026-08-03] repair | Epics excerpt provenance boundary 정정

- Correction to the immediately preceding repair entry: the patch mechanism did
  not retain source line 83, which is an empty line.
- The immutable nonblank body was kept unchanged; its declared boundary is now
  lines 45–82 and its SHA-256 was synchronized to those exact body bytes.

## [2026-08-03] lint | BMAD v6.10.0 재수집 지식 세트 0 issues

- Canonical: 3 pages, 25 source references, 24 claim-level markers, and 6
  resolvable non-self links; every page has two distinct outbound targets and is
  below the 200-line split threshold.
- Index: 3 unique entries and declared total 3, matching the filesystem by type.
- Taxonomy: all 18 registered tags are used; no unregistered or unused tag remains.
- Raw integrity: 38 Markdown records checked and every post-frontmatter SHA-256
  matches; all 18 v6.10.0 official excerpts byte-match their declared line ranges.
- Release fidelity: the v6.10.0 release body matches the official GitHub API body
  after LF normalization.
- Format: checked files are UTF-8, LF, no BOM, and final-newline terminated.
- Provenance, required fields, type-directory fit, broken links, missing sources,
  marker/source disagreement, pending canonical angle tokens, index drift, and
  whitespace errors: 0.
- Updated: `log.md` only.

## [2026-08-04] repair | BMAD v6.10.0 감사 finding 교정

- Created:
  - `raw/releases/bmad-method-v6-10-0-release-api-2026-08-04.md`
  - `raw/official-docs/bmad-method-v6-10-0-epics-prerequisites-excerpt-2026-08-04.md`
  - `raw/official-docs/bmad-method-v6-10-0-prd-reviewer-gate-excerpt.md`
  - `raw/official-docs/bmad-method-v6-10-0-create-story-selection-excerpt.md`
  - `raw/official-docs/bmad-method-v6-10-0-dev-story-input-excerpt.md`
  - `raw/official-docs/bmad-method-v6-10-0-code-review-input-excerpt.md`
  - `raw/official-docs/bmad-method-main-5247108-package-version-excerpt.md`
  - `raw/official-docs/bmad-method-main-5247108-build-auto-skill.md`
  - `raw/official-docs/bmad-method-main-5247108-dev-auto-shim.md`
- Updated:
  - `comparisons/bmad-v6-10-0-automation-and-human-gates.md`
  - `queries/bmad-v6-10-0-workflow-contracts.md`
  - `docs/initial-research-backlog.md`
  - `AGENTS.md`
  - `index.md`
  - `log.md`
- Raw integrity incident: the earlier epics excerpt had been mutated after capture;
  it remains untouched for audit history and is no longer canonical evidence. The
  replacement was freshly captured from pinned commit lines 45-82.
- Release fidelity: the prior release record remains untouched and is no longer
  canonical evidence. The replacement preserves the GitHub API body's leading LF,
  normalizes line endings to LF, and appends one documented final LF required by
  the wiki Markdown format.
- Version boundary: `v6.10.0` tag retains `bmad-dev-auto`; official main commit
  `5247108ba3f45b2e9731fa41919029b3d2623023` provides `bmad-build-auto` and a
  deprecated `bmad-dev-auto` redirect shim while `package.json` declares 6.10.0.
- Source coverage: added pinned excerpts for the PRD reviewer gate, story selection,
  dev-story input discovery, and code-review diff/spec context.
- MVP policy: clean worktree is mandatory when VCS exists; bmad-loop setup is an
  activation prerequisite, and the general story chain's retry/re-entry/merge
  behavior is explicitly an external orchestrator policy rather than an official
  combined workflow.

## [2026-08-04] lint | BMAD 감사 교정 후 validator PASS

- Command: `python scripts/validate_wiki.py`
- Result: `PASS`, 0 errors and 5 warnings.
- Canonical: 3 pages, 32 source references, 33 claim-level markers, 6 resolvable
  non-self links, and no index drift.
- Raw integrity: 47 Markdown records checked; every recorded post-frontmatter
  SHA-256 matches.
- Warning disposition: two historical deleted-path log references are not
  verifiable from the current diff; three sensitive-keyword matches are ordinary
  prose in `AGENTS.md` and immutable official release text, not credentials.
- Updated: `log.md` only.

## [2026-08-17] ingest | BMAD v6.11.0 공식 근거 수집

- Pinned official tag `v6.11.0` to commit
  `9ce3c397c9b238de96f7365da8019f6f66b059da`.
- Created one immutable GitHub release capture at
  `raw/releases/bmad-method-v6-11-0-release-api-2026-08-17.md`.
- Created eight immutable, commit-pinned complete official files under
  `raw/official-docs/`: workflow map, Build workflow, Build Auto reference,
  sprint-planning skill and readiness gate, project-context skill, review skill,
  and the v6 shim map.
- Integrity: all nine records include SHA-256 over their exact post-frontmatter
  body; official GitHub file bodies were captured from raw commit permalinks.
- Version boundary: v6.10.0 records remain unchanged and are not merged into
  unqualified v6.11.0 facts.

## [2026-08-17] create | BMAD v6.11.0 활성 지식 보강

- Created:
  - `queries/bmad-v6-11-0-workflow-contracts.md`
  - `comparisons/bmad-v6-11-0-automation-and-human-gates.md`
- Updated:
  - `concepts/bmad-msa-multi-repository-boundaries.md`
  - `docs/initial-research-backlog.md`
  - `README.ko.md`
  - `AGENTS.md`
  - `index.md`
  - `log.md`
- Canonical effect: retained the v6.10.0 pages as version history and added
  separate v6.11.0 decisions for the Build-only Phase 4 path, readiness
  integration, Build Auto state contract, review lenses, and v6 shim migration.

## [2026-08-17] lint | BMAD v6.11.0 수집 후 validator PASS

- Command: `python scripts/validate_wiki.py`
- Result: `PASS`, 0 errors and 6 warnings.
- Canonical: 5 pages, 45 source references, 48 claim-level markers, 10
  resolvable non-self wikilinks, and no index drift.
- Raw integrity: 56 Markdown records checked; every recorded post-frontmatter
  SHA-256 matches.
- Warning disposition: two historical deleted-path log references remain
  unverifiable from the current diff; four sensitive-keyword matches are ordinary
  prose about token ranges or immutable release text, not credentials.
- Updated: `log.md` only.

## [2026-08-17] lint | BMAD v6.11.0 최종 로그 포함 validator PASS

- Command: `python scripts/validate_wiki.py`
- Result: `PASS`, 0 errors and 7 warnings after including the preceding lint
  record itself.
- Warning disposition: two historical deleted-path references are not verifiable
  from the current diff; five keyword matches are ordinary prose or immutable
  release text and contain no credential material.
- Updated: `log.md` only.

## [2026-08-17] ingest | BMAD v6.5.0 BMM/Core skill 기준선 수집

- Pinned official tag `v6.5.0` to commit
  `69cbeb4d07f318180c3d610c511381b9f494e786`.
- Created five immutable official GitHub file records: `package.json`, BMM/Core
  `module.yaml`, and BMM/Core `module-help.csv`.
- Created `raw/releases/bmad-method-v6-5-0-release-api-2026-08-17.md` from the
  official GitHub release API body.
- Created reproducible inventory
  `raw/experiments/bmad-method-v6-5-0-bmm-core-skill-inventory.md` with 42 skill
  roots, recursive Git tree IDs, file counts, protocol, delta rules, and limits.
- Baseline: BMM has 30 skill roots and scope tree
  `bde383035df88f2e252e83dc76af7acfe39aeed1`; Core has 12 and scope tree
  `dc5d00bf44f96271fee315555838c884a56ac89f`.
- Integrity: all seven records include SHA-256 over their exact post-frontmatter
  body; official file bodies use commit permalinks.

## [2026-08-17] create | BMAD v6.5.0 BMM/Core skill 기준선

- Created:
  - `queries/bmad-v6-5-0-bmm-core-skill-catalog.md`
- Updated:
  - `docs/initial-research-backlog.md`
  - `README.ko.md`
  - `AGENTS.md`
  - `index.md`
  - `log.md`
- Canonical effect: separated physical module ownership from help-catalog
  exposure, cataloged 30 BMM and 12 Core skill roots, and established a policy
  that unchanged recursive skill trees cause no repository update.

## [2026-08-17] repair | BMAD v6.5.0 기준선 형식 및 연결 교정

- Removed one patch-introduced trailing blank line from each of the seven new raw
  bodies, restoring their recorded upstream or experiment SHA-256 values.
- Reordered the query index entries using the validator's lexical ordering.
- Added an inbound canonical link from
  `queries/bmad-v6-11-0-workflow-contracts.md` to the v6.5.0 skill baseline.
- Updated:
  - `queries/bmad-v6-11-0-workflow-contracts.md`
  - `index.md`
  - `log.md`

## [2026-08-17] lint | BMAD v6.5.0 skill 기준선 validator PASS

- Command: `python scripts/validate_wiki.py`
- Result: `PASS`, 0 errors and 8 warnings.
- Canonical: 6 pages, 52 source references, 57 claim-level markers, 14
  resolvable non-self wikilinks, and no index drift.
- Raw integrity: 63 Markdown records checked; every recorded post-frontmatter
  SHA-256 matches.
- Warning disposition: two historical deleted-path references are not verifiable
  from the current diff; six keyword matches are ordinary prose or immutable
  source text and contain no credential material.
- Updated: `log.md` only.

## [2026-08-17] ingest | BMAD v6.10.0 및 v6.11.0 skill delta 수집

- Compared every BMM/Core skill root using recursive Git tree IDs for
  `v6.5.0 → v6.10.0` and `v6.10.0 → v6.11.0`.
- Created two reproducible delta records under `raw/experiments/` with protocol,
  scope trees, counts, and complete unchanged/changed/added/removed path tables.
- v6.5.0→v6.10.0: 42→46 roots; 4 exact-path unchanged, 36 changed, 6 added,
  and 2 removed.
- v6.10.0→v6.11.0: 46→49 physical roots; 0 exact-path unchanged, 6 changed,
  43 added, and 40 removed because BMM moved to agents/plan/ship/v6-shims and
  Core consolidated skills.
- Created 12 immutable v6.10.0 records: package and five registries/manifests,
  plus PRD, UX, Architecture, Dev Auto, Forge Idea, and Spec skill files.
- Created 9 immutable v6.11.0 records: package and five registries/manifests,
  plus Build, Build Auto, and Deep Recon skill files.
- Reused the previously captured v6.11.0 Project Context, Review, Sprint Planning,
  and v6 shim records instead of duplicating unchanged evidence paths.
- Integrity: all 23 new records carry SHA-256 over their exact post-frontmatter
  body and official files use commit permalinks.

## [2026-08-17] create | BMAD v6.5.0부터 v6.11.0 skill 변화 비교

- Created:
  - `comparisons/bmad-v6-5-0-to-v6-11-0-bmm-core-skill-delta.md`
- Updated:
  - `queries/bmad-v6-5-0-bmm-core-skill-catalog.md`
  - `docs/initial-research-backlog.md`
  - `README.ko.md`
  - `AGENTS.md`
  - `index.md`
  - `log.md`
- Canonical effect: separated physical roots, active help-catalog entries, and
  compatibility shims; recorded v6.10.0 additions and v6.11.0 Build, renderer,
  research/review consolidation, and migration choices.

## [2026-08-17] lint | BMAD v6.10.0 및 v6.11.0 skill delta validator PASS

- Command: `python scripts/validate_wiki.py`
- Result: `PASS`, 0 errors and 9 warnings.
- Canonical: 7 pages, 73 source references, 78 claim-level markers, 18
  resolvable non-self wikilinks, no index drift, and every page at or below the
  200-line split threshold.
- Raw integrity: 86 Markdown records checked; every recorded post-frontmatter
  SHA-256 matches.
- Warning disposition: two historical deleted-path references are not verifiable
  from the current diff; seven keyword matches are ordinary prose or immutable
  source text and contain no credential material.
- Updated: `log.md` only.

## [2026-08-17] ingest | BMAD v6.5.0부터 v6.11.0까지 커뮤니티 의견 표본

- Registered `raw/community/` for immutable public-post metadata and bounded
  excerpts; community evidence supports reception claims, not shipped behavior.
- Captured eight public GitHub Issue positions and five DEV Community articles
  without account handles, using original URLs, publication timestamps, explicit
  version fields when present, and short opinion excerpts.
- Captured the official stable release timeline for v6.5.0, v6.6.0, v6.7.0,
  v6.7.1, v6.8.0, v6.9.0, v6.10.0, and v6.11.0 from the GitHub Releases API.
- Version assignment policy: explicit mention wins; otherwise use the latest
  stable release published at or before the post timestamp and mark it inferred.
- Created:
  - `raw/releases/bmad-method-v6-5-to-v6-11-release-timeline-api-2026-08-17.md`
  - `raw/community/bmad-method-github-opinions-v6-5-to-v6-11-2026-08-17.md`
  - `raw/community/bmad-method-devto-opinions-v6-6-to-v6-10-2026-08-17.md`
- Updated:
  - `SCHEMA.md`
  - `log.md`

## [2026-08-17] create | BMAD v6.5.0부터 v6.11.0까지 커뮤니티 의견 변화

- Created:
  - `comparisons/bmad-v6-5-0-to-v6-11-0-community-opinions.md`
- Updated:
  - `queries/bmad-v6-11-0-workflow-contracts.md`
  - `index.md`
  - `log.md`
- Canonical effect: kept every intermediate stable release as a separate
  collection unit, separated explicit from timestamp-inferred assignments, and
  recorded platform and sampling biases instead of treating the sample as a
  population sentiment score.

## [2026-08-17] lint | BMAD 버전별 커뮤니티 의견 validator PASS

- Command: `python scripts/validate_wiki.py`
- Result: `PASS`, 0 errors and 10 warnings.
- Canonical: 8 pages, 76 source references, 81 claim-level markers, 22
  resolvable non-self wikilinks, no index drift, and every page at or below the
  200-line split threshold.
- Raw integrity: 89 Markdown records checked; every recorded post-frontmatter
  SHA-256 matches.
- Warning disposition: two historical deleted-path references remain
  unverifiable; the remaining keyword matches are ordinary prose or immutable
  source text and contain no credentials.
- Updated: `log.md` only.

## [2026-08-17] ingest | Reddit·YouTube·LinkedIn BMAD 의견 보강

- Added five Reddit positions from the v6.6.0 and v6.10.0 publication windows,
  four public YouTube comments on the v6.10 Loop livestream, and two public
  LinkedIn comments on the v6.10 three-flows announcement.
- Omitted account handles and profile data; retained original public URLs,
  publication displays, stable comment IDs where available, and bounded excerpts.
- Discord exposed its public invite but not searchable message content without
  authentication; Threads returned no reproducible qualifying public result.
- Created:
  - `raw/community/bmad-method-reddit-opinions-v6-6-and-v6-10-2026-08-17.md`
  - `raw/community/bmad-method-youtube-v6-10-loop-comments-2026-08-17.md`
  - `raw/community/bmad-method-linkedin-v6-10-loop-comments-2026-08-17.md`
- Updated:
  - `log.md`

## [2026-08-17] update | BMAD 커뮤니티 후보 6곳 커버리지 보강

- Updated:
  - `comparisons/bmad-v6-5-0-to-v6-11-0-community-opinions.md`
  - `index.md`
  - `log.md`
- Canonical effect: expanded the sample from 13 to 24 positions across five
  publicly collectible platforms and recorded Discord as an authentication
  boundary rather than silently treating it as searched or empty.

## [2026-08-17] lint | BMAD 커뮤니티 후보 6곳 보강 validator PASS

- Command: `python scripts/validate_wiki.py`
- Result: `PASS`, 0 errors and 10 warnings.
- Canonical: 8 pages, 79 source references, 84 claim-level markers, 22
  resolvable non-self wikilinks, no index drift, and all pages below the
  200-line split threshold.
- Raw integrity: 92 Markdown records checked; every recorded post-frontmatter
  SHA-256 matches.
- Warning disposition: two historical deleted-path references remain
  unverifiable; the remaining keyword matches are ordinary prose or immutable
  source text and contain no credentials.
- Updated: `log.md` only.
