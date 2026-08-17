# Wiki Schema

## Domain contract

**Domain:** 공개 근거를 이용한 AIDD 개발 워크플로 의사결정 지식베이스.

**Primary audience:**

- 코딩 에이전트를 개발 프로세스에 도입하려는 개발자
- 백엔드 및 플랫폼 엔지니어
- PL, BA, Tech Lead
- AIDD 방법론 또는 개발 표준을 설계하는 담당자

Canonical pages are decision support, not feature encyclopedia entries. A page is
canonical only when it satisfies at least one of these conditions:

- provides a reusable decision criterion;
- compares or synthesizes multiple sources;
- makes a workflow's required inputs, optional inputs, outputs, or gates explicit;
- separates adoption conditions from non-adoption conditions;
- explains how a version change alters a decision; or
- records a difference between official documentation and a reproducible result.

Public official documentation, official repositories and releases, official
examples, public issues or discussions, public reproducible test projects,
bounded captures of public community posts, and this wiki's synthetic examples
or experiments are allowed. Community posts support claims about reported
experience or reception only; they do not establish shipped behavior. Internal documents,
identifiable customer or organization data, private source code, credentials,
personal work records, unattributed summaries, search snippets, and unsupported AI
guesses are prohibited.

## Repository orientation

This repository root is the wiki root. Every wiki operation resolves paths from the
current project root; no database, hosted service, or separate vault is required.
Before curating, read this file, `index.md`, and the most recent entries in `log.md`.

## Three layers

1. **Layer 1 — raw immutable source evidence:** Markdown source records live under
   `raw/`. Their captured body is immutable except for the two narrow metadata
   operations defined below.
2. **Layer 2 — canonical pages:** Curated pages live only in `entities/`,
   `concepts/`, `comparisons/`, and `queries/`. These pages synthesize and connect
   raw evidence; they never replace it.
3. **Layer 3 — schema, navigation, and log metadata:** `SCHEMA.md` defines the
   contract, `index.md` is the complete canonical catalog, and `log.md` is the
   append-only action history.

Zero canonical pages is a valid wiki state. The initial repository deliberately
contains no raw source record and no canonical page.

## Directory roles

| Path | Role |
| --- | --- |
| `inbox/` | Temporary intake awaiting classification and capture; not canonical evidence. |
| `raw/articles/` | Immutable captured article or clipping Markdown. |
| `raw/notebooklm/` | Immutable importer-preserved NotebookLM source records and source identifiers. |
| `raw/papers/files/` | Optional copied paper attachments; initially only the empty `.gitkeep` placeholder is allowed. |
| `raw/transcripts/` | Immutable captured transcript Markdown. |
| `raw/web/` | Immutable importer-preserved web captures whose existing provenance paths must remain stable. |
| `raw/youtube/` | Immutable importer-preserved video metadata and transcript captures. |
| `raw/official-docs/` | Immutable complete files or explicitly bounded excerpts from official documentation and official repositories. |
| `raw/releases/` | Immutable official release notes and CHANGELOG captures. |
| `raw/github-issues/` | Immutable public issues and discussions from an official repository, including visible comments needed for context. |
| `raw/examples/` | Immutable official examples or public reproducible example projects with a verified public license. |
| `raw/experiments/` | Immutable protocols and results from reproducible synthetic experiments performed for this wiki. |
| `raw/community/` | Immutable metadata and bounded excerpts from publicly accessible community posts. |
| `entities/` | Canonical pages whose exact `type` is `entity`. |
| `concepts/` | Canonical pages whose exact `type` is `concept`. |
| `comparisons/` | Canonical pages whose exact `type` is `comparison`. |
| `queries/` | Canonical filed syntheses whose exact `type` is `query`. |
| `_archive/` | Fully superseded canonical pages removed from active navigation. |

## File and frontmatter rules

- Markdown is UTF-8, uses LF line endings, and has no byte-order mark.
- Canonical file names use lowercase words separated by hyphens and end in `.md`;
  imported raw file names and relative paths are preserved exactly.
- Frontmatter, when required, starts at byte zero with `---` followed by LF.
- Every canonical page has these fields: `title`, `created`, `updated`, `type`,
  `tags`, `sources`, `confidence`, `contested`, and `contradictions`.
- Canonical `type` is exactly one of `entity`, `concept`, `comparison`, or `query`,
  and it must match the containing directory.
- `created` and `updated` are calendar dates. Preserve `created`; change `updated`
  whenever the page content or metadata changes.
- `confidence` is exactly `high`, `medium`, or `low`. Use `high` only for evidence
  supported across multiple sources.
- `contested` is a YAML boolean. When it is `true`, describe unresolved positions
  with dates and provenance in the body. `contradictions` is a list of canonical
  page slugs whose claims conflict; use an empty list when there is no conflict.

Templates live outside canonical directories and are not pages. All angle-bracket
tokens in a copied template must be replaced or removed before the copy can become
a valid source record or canonical page.

## Tag taxonomy

- Every tag used by a canonical page must first be registered in this section.
- Register a tag before using it, and keep its spelling stable.
- Add only tags that fit the chosen wiki domain; do not seed domain tags here.

Keep the active taxonomy between 10 and 20 tags. Do not register speculative tags
that no canonical page uses.

### Registered tags

- `aidd`: AI-driven development methods and decisions.
- `workflow`: ordered development processes and feedback loops.
- `requirements`: requirement and PRD artifacts.
- `architecture`: solution design, ADRs, and technical constraints.
- `story`: implementation-ready story artifacts and lifecycle.
- `implementation`: code-producing workflow stages.
- `review`: implementation review and remediation stages.
- `testing`: test generation, execution, and quality evidence.
- `automation`: deterministic or agent-driven workflow automation.
- `human-gate`: explicit human confirmation, approval, or escalation points.
- `governance`: policy, accountability, and change control.
- `brownfield`: workflows for an existing codebase or system.
- `msa`: microservice architecture boundaries and coordination.
- `multi-repository`: workflows spanning more than one repository.
- `versioning`: version-scoped claims and migration effects.
- `comparison`: explicit side-by-side analysis of workflows or methods.
- `provenance`: source traceability and claim lineage.
- `experiment`: reproducible synthetic verification and observed behavior.

## AIDD source-record contract

New source records in the five AIDD source directories use lowercase kebab-case
filenames. Prefer `{project}-{tag-or-version}-{subject}.md`; append the retrieval
date or abbreviated commit only when needed to distinguish captures. Original
repository paths are recorded in metadata rather than recreated as nested paths.

Every new AIDD raw Markdown record starts at byte zero with YAML frontmatter and,
where the value exists in the source, records:

- `source_url`: canonical public URL; GitHub file URLs should be commit permalinks.
- `source_type`: one of `official-doc`, `official-github-file`,
  `official-github-file-excerpt`, `official-release`, `official-github-issue`,
  `official-example`, or `synthetic-experiment`.
- `ingested`: capture date as `YYYY-MM-DD`.
- `retrieved_at`: RFC 3339 timestamp with offset.
- `repository`: canonical `owner/repository` name for repository sources.
- `document_path`: repository-relative source path when applicable.
- `version`: product version exactly as published.
- `tag`: exact Git tag when verified.
- `commit_sha`: full 40-character commit SHA when verified.
- `license`: source license identifier when verified.
- `sha256`: lowercase SHA-256 of the exact post-frontmatter body bytes.

Do not invent absent values. An excerpt record must also state `excerpt_lines` or
an equivalent stable boundary and must preserve the selected source text exactly.
Its `sha256` covers only the captured excerpt body. A GitHub issue record preserves
the captured issue body and included public comments in visible order.

The body established at first capture is immutable under the general raw-integrity
rules. Recollection never overwrites a prior body. If bytes or upstream content
drift, create a new dated or commit-qualified record, retain both records, and
describe the drift in `log.md` and the affected canonical page. A same-commit byte
difference is an integrity incident; a different commit is version drift.

Directory-specific allowed inputs are:

- `raw/official-docs/`: official documentation pages, complete official repository
  files, and explicitly bounded verbatim excerpts.
- `raw/releases/`: official GitHub Release bodies and official CHANGELOG sections.
- `raw/github-issues/`: public issues or discussions in the official repository;
  issue claims remain lower-confidence than shipped files or reproducible behavior.
- `raw/examples/`: official examples or public reproducible projects whose license
  and exact tag or commit are recorded.
- `raw/experiments/`: synthetic fixtures, commands, environment assumptions,
  observed output, and limitations sufficient for another person to repeat the run.

## Version and freshness policy

Each version-sensitive canonical page identifies the product, verified version,
tag or commit, last verification date, whether the conclusion is latest-version
dependent, and concrete revalidation triggers. Never merge claims from different
versions into one unqualified current fact. Fast-changing documentation requires a
retrieval date plus a verified version, tag, or commit. Revalidate when a referenced
tag changes, a new stable release changes the named workflow inventory or contract,
or a cited file is moved or materially edited.

For community opinion assignment, an explicit product version in the post wins.
Otherwise infer the version from the post's original publication timestamp and
the latest stable release published at or before that instant. Preserve both the
assigned version and `version_basis: explicit` or `version_basis: inferred` in
the canonical synthesis. Intermediate stable releases are independent collection
units; never collapse a time span merely because only its endpoints have existing
canonical pages. Leave a post unassigned when its timestamp is ambiguous, it
describes multiple versions, or surrounding context indicates an older version.

## Public community source contract

Community captures live under `raw/community/` and use
`source_type: public-community-post-collection`. Each record identifies the
platform, API or public page URL, retrieval time, selection boundary, captured
fields, and capture mode. Prefer a stable public API projection. When no stable
projection exists, preserve only the metadata and short excerpts necessary to
support the opinion classification; do not mirror whole posts merely for
convenience.

- Preserve the original post URL and publication timestamp for every item.
- Omit account handles and other identifying profile data unless identity is
  essential to evaluating a disclosed project affiliation.
- Distinguish author opinion, reported observation, reproduction evidence, and
  maintainer response. Only the first two are community reception.
- Record zero qualifying samples as a coverage gap, not as neutral sentiment.
- Treat edits, deletions, inaccessible pages, engagement counts, and platform
  search ranking as unstable. Recollection creates a new dated record.
- Community evidence is `low` confidence for population-wide claims even when
  several posts agree. It may raise confidence only about the existence of the
  captured positions, not their representativeness or product correctness.

## Confidence policy

- `high`: independent official evidence agrees, or official evidence and a
  reproducible experiment agree.
- `medium`: one official source directly supports the claim, or several indirect
  official sources agree.
- `low`: the claim depends on an issue, Discussion, inference, absence search, or
  version mismatch.

A feature described in only one official README is not automatically `high`.
Negative existence claims remain `low` even after a bounded repository search and
must state the searched repository, tag or commit, paths, and terms.

## Raw source integrity

Initial capture establishes an immutable raw record. The `sha256` field is the
SHA-256 digest of the exact post-frontmatter body bytes: every byte after the LF
that terminates the closing `---` delimiter through end of file. For a Zotero
record this includes the readable Zotero metadata block, extracted-text suffix,
and the normalized final LF.

Byte-identical records copied from a trusted legacy vault may lack a recorded
`sha256`. Preserve those files exactly, record the whole-file source/target hash
comparison in `log.md`, and report the missing field as a hash-coverage gap rather
than source drift. Do not add frontmatter merely to normalize a legacy capture.
A trusted legacy copy may also retain its original missing final LF. Treat that as
a documented format gap, not permission to alter the immutable raw bytes.

Only these raw-record mutations are allowed:

1. **Zotero metadata repair:** replace raw frontmatter and the readable Zotero
   metadata block only, prove the extracted-text suffix remains byte-exact, and
   recompute `sha256` over the resulting complete post-frontmatter body.
2. **NotebookLM mapping:** change only byte-zero leading frontmatter, preserve
   every body byte, and preserve the existing `sha256` scalar byte-for-byte.

No other edit to a captured raw body is allowed. Corrections and interpretations
belong in canonical pages. A copied attachment does not substitute for its raw
Markdown record or for Zotero parent metadata.

## Provenance

- Every canonical `sources` item is an exact repository-relative path to an
  existing raw Markdown record under a source directory registered in the table
  above, including importer-preserved `raw/notebooklm/`, `raw/web/`, and
  `raw/youtube/` paths.
- Assets and attachments may support a raw record but are not canonical `sources`
  entries by themselves.
- Never invent, approximate, or retain a source path that does not resolve.
- Where a synthesized paragraph needs claim-level attribution, append a marker of
  the form `^[raw/<source-kind>/<source-file>.md]`. Use markers for multi-source
  synthesis, contested claims, or wherever the frontmatter list alone is
  ambiguous. Each marker must resolve to a path already listed in `sources`.

## Canonical link validity

Explicit Obsidian `[[wikilinks]]` connect canonical pages. When the canonical set
is nonempty, every canonical page must contain at least two distinct, resolvable,
non-self links to other canonical pages. Targets must resolve to active Markdown
pages in one of the four canonical directories.

Therefore a one-page or two-page canonical set is invalid. A three-page set can be
valid only when every page satisfies the same two-target rule. Links to templates,
raw records, archived pages, headings in the same page, or missing targets do not
count toward the minimum.

## Page thresholds and maintenance

- Create a canonical page when its subject appears in at least two raw sources or
  is central to one source.
- Add evidence to an existing page when the subject is already covered.
- Do not create pages for passing mentions, minor details, or out-of-domain items.
- Split a canonical page when it grows beyond roughly 200 lines, preserving links
  and provenance in both resulting pages.
- Archive a page only when it is fully superseded. Move it under `_archive/`,
  remove it from `index.md`, update active links, and append the archive to
  `log.md`.

## Index and log synchronization

For every canonical create, update, filed query, archive, or delete operation:

1. Update `index.md` in the same operation. List every active canonical page once
   under its matching type, sort entries alphabetically, keep a one-line summary,
   and make the total equal the filesystem canonical-page count.
2. Append one entry to `log.md` in the defined heading format. Record the action,
   subject, and every repository-relative file created, updated, archived, or
   deleted.
3. Never list raw records, templates, or archived pages as active canonical index
   entries. Never rewrite or remove prior log entries.

When an index section exceeds 50 entries, divide it into stable subsections. When
the full index exceeds 200 entries, add a thematic navigation map without changing
the canonical count. Rotate the log only under its policy in `log.md`.
