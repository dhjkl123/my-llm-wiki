---
title: "BMAD v6.10.0 workflow 및 artifact 계약"
created: 2026-08-03
updated: 2026-08-04
type: query
tags:
  - aidd
  - workflow
  - requirements
  - architecture
  - story
  - implementation
  - human-gate
  - versioning
  - provenance
sources:
  - raw/official-docs/bmad-method-v6-10-0-planning-map-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-workflow-map-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-prd-contract-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-ux-contract-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-architecture-contract-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-epics-prerequisites-excerpt-2026-08-04.md
  - raw/official-docs/bmad-method-v6-10-0-readiness-input-gate-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-create-story-inputs-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-create-story-handoff-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-dev-story-gates-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-code-review-human-gates-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-dev-auto-reference-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-prd-reviewer-gate-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-create-story-selection-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-dev-story-input-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-code-review-input-excerpt.md
confidence: medium
contested: false
contradictions: []
---
# BMAD v6.10.0 workflow 및 artifact 계약

## 결론

BMAD v6.10.0은 제품 계획 경로와 story 중심 구현 경로에 더해, 작은 단일
intent를 `spec-*.md`로 고정하고 계획·구현·리뷰까지 한 번 무인 실행하는
`bmad-dev-auto`를 제공한다. 전통 경로는 `PRD → Architecture → Epics & Stories
→ Readiness → Sprint/Story → Dev → Review`, Quick Flow는 `bmad-quick-dev` 또는
`bmad-dev-auto`다. ^[raw/official-docs/bmad-method-v6-10-0-workflow-map-excerpt.md]

## 버전과 freshness

- 대상: BMad Method/BMM
- 확인 버전/tag: `6.10.0` / `v6.10.0`
- commit: `081e64ee5aab2316b912883f7bee528ee143ce36`
- 마지막 검증일: 2026-08-03
- 최신 버전 종속: 예
- 재검증 조건: 새 stable release가 workflow 명칭·상태 machine·산출물을
  변경하거나 인용 파일이 이동·수정될 때

## Planning 및 Solutioning contract

| Workflow | 필수 입력 | 선택 입력 | 출력 | Gate |
| --- | --- | --- | --- | --- |
| `bmad-prd` | Create/Update/Validate intent, 사용자의 product context와 결정 | Product Brief, research, transcript, prior PRD, design docs | Create/Update: `prd.md`, `addendum.md`, `.memlog.md`; Validate: HTML+MD report | intent가 모호하면 질문; Create는 Fast/Coaching 방식과 최종 사용자 검토 |
| `bmad-ux` | Create/Update/Validate intent, UX 결정 | planning artifacts, Figma·sketch·brand 자료 | `DESIGN.md`, `EXPERIENCE.md`, `.memlog.md` | 발견 경로를 읽기 전에 사용자가 적용 대상을 확인 |
| `bmad-architecture` | spine을 만들 만큼 충분한 spec·idea·codebase·기존 architecture 중 하나 | parent spine, persistent facts, memlog | `ARCHITECTURE-SPINE.md` | 입력이 너무 얇으면 `bmad-spec`; 상위 spine과 충돌하면 표면화 |
| `bmad-create-epics-and-stories` | PRD, Architecture | UI가 있으면 UX contract, 추가 문서 | `epics.md` | 발견 문서 포함·제외를 사람이 확인 |
| `bmad-check-implementation-readiness` | PRD, Architecture, Epics; UI가 있으면 UX | whole 또는 sharded 문서 | readiness report, PASS/CONCERNS/FAIL | 중복 형식과 입력 목록을 사람이 확인 |

공식 map은 PRD와 UX의 산출물을 명시한다. PRD는 Product Brief 없이도 시작할
수 있고 Create/Update/Validate를 한 skill에서 처리한다.
^[raw/official-docs/bmad-method-v6-10-0-planning-map-excerpt.md]

PRD Create의 핵심 입력은 사용자의 brain dump이며 기존 문서는 선택 입력이다.
Agent는 사용자 vision을 임의로 저작하지 않고 누락을 확인해야 한다.
^[raw/official-docs/bmad-method-v6-10-0-prd-contract-excerpt.md]

Create는 Fast/Coaching path를 선택하고 Finalize에서 reviewer pass와 사용자
결정 정리를 거쳐 `status: final`로 닫는다.
^[raw/official-docs/bmad-method-v6-10-0-prd-reviewer-gate-excerpt.md]

UX는 upstream 내용을 복제하지 않고 source reference를 상속한다. 후보 경로는
사람이 확인한 뒤 subagent가 추출한다.
^[raw/official-docs/bmad-method-v6-10-0-ux-contract-excerpt.md]

Architecture는 PRD만을 절대 필수로 보지 않는다. 충분한 spec, raw idea, 기존
codebase 또는 spine도 입력이 될 수 있다. 상위 spine의 결정은 하위 epic
spine에서 read-only constraint다.
^[raw/official-docs/bmad-method-v6-10-0-architecture-contract-excerpt.md]

Epics workflow는 PRD와 Architecture를 필수로 확인하고, UI가 있으면 UX spine
pair를 하나의 contract로 취급한다. 발견 문서의 포함·제외를 사용자가 확인한
뒤 `epics.md`를 만든다.
^[raw/official-docs/bmad-method-v6-10-0-epics-prerequisites-excerpt-2026-08-04.md]

Readiness는 PRD, Architecture, Epics, UX를 찾고 whole/sharded 중복을 critical
issue로 표시해 사용자가 사용할 버전을 선택하게 한다.
^[raw/official-docs/bmad-method-v6-10-0-readiness-input-gate-excerpt.md]

## Implementation contract

| Workflow | 필수 입력 | 선택 입력 | 출력·상태 | 정지 조건 |
| --- | --- | --- | --- | --- |
| `bmad-create-story` | story 선택, Epic context | PRD·Architecture·UX fallback, sprint status | story file, `ready-for-dev` | story 선택·입력 확인 실패 |
| `bmad-dev-story` | `ready-for-dev` story | project context, sprint status | code/tests, story `review` | 미완료 task, regression, File List 또는 DoD 실패 |
| `bmad-code-review` | 변경 diff; story가 있으면 story/spec | project context와 sprint status | `done` 또는 `in-progress` | decision/patch 처리 방법을 사람이 선택할 때 HALT |
| `bmad-dev-auto` | 하나의 coherent invocation intent; synchronous subagent 기능 | ticket/story, intent/spec path, planning artifacts, project context, VCS | slug 기반 spec 파일, code, terminal `done`/`blocked`, 선택적 local commit | intent/spec/검증 gap, subagent 부재, review loop 비수렴 |

Create Story는 Epic을 주 context로 사용하고 PRD·Architecture·UX를 fallback으로
선택 로드한다. 명시적 story 식별자를 받거나 sprint status에서 첫 backlog
story를 선택하며, 출력은 checklist 적용 후 `ready-for-dev`다.
^[raw/official-docs/bmad-method-v6-10-0-create-story-inputs-excerpt.md]
^[raw/official-docs/bmad-method-v6-10-0-create-story-selection-excerpt.md]
^[raw/official-docs/bmad-method-v6-10-0-create-story-handoff-excerpt.md]

Dev Story는 명시적 story path 또는 sprint status의 첫 `ready-for-dev` story를
입력으로 고른다. 모든 task와 AC, 필요한 unit/integration/E2E test, regression,
lint/static analysis, File List를 검사한 뒤에만 `review`로 전이한다.
^[raw/official-docs/bmad-method-v6-10-0-dev-story-input-excerpt.md]
^[raw/official-docs/bmad-method-v6-10-0-dev-story-gates-excerpt.md]

일반 Code Review는 명시적 PR/commit/branch/spec/diff나 현재 Git 상태에서 diff를
구성하고, story/spec context 유무를 확인한다. 모호한 finding과 patch 적용
방식을 사용자에게 묻고 멈춘다. 해결되면 `done`, action item이나 미해결 문제가
남으면 `in-progress`다.
^[raw/official-docs/bmad-method-v6-10-0-code-review-input-excerpt.md]
^[raw/official-docs/bmad-method-v6-10-0-code-review-human-gates-excerpt.md]

Dev Auto는 prompt, ticket/story, intent file 또는 기존 spec을 받아 spec 상태에
따라 resume한다. VCS가 있으면 깨끗한 worktree가 필요하고 완료 시 commit하지만
push하지 않는다. ^[raw/official-docs/bmad-method-v6-10-0-dev-auto-reference-excerpt.md]

## 선택 기준

- 공통 NFR, 여러 stakeholder, architecture 의사결정이 크면 전체 planning
  경로와 readiness gate를 사용한다.
- 범위가 작고 intent와 검증 기준이 닫혀 있으면 `bmad-dev-auto`를 고려한다.
- intent가 모호하거나 migration·보안·cross-repo 계약 승인처럼 사람 판단이
  필요하면 무인 workflow에 넘기지 않는다.
- 자동화와 승인 선택은 [[bmad-v6-10-0-automation-and-human-gates]], 서비스
  경계는 [[bmad-msa-multi-repository-boundaries]]와 함께 판단한다.

## 알려진 공백

- 이번 재수집은 공식 tag의 contract 정적 검증이며 실제 설치·실행은 하지 않았다.
- Sprint planning의 세부 입력과 상태 전이는 후속 보강 대상이다.
- 설치 환경별 subagent 및 VCS 동작 차이는 synthetic experiment가 필요하다.
