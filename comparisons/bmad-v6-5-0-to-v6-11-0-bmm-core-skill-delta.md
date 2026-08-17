---
title: "BMAD v6.5.0에서 v6.11.0까지 BMM/Core skill 변화"
created: 2026-08-17
updated: 2026-08-17
type: comparison
tags:
  - aidd
  - workflow
  - requirements
  - architecture
  - story
  - implementation
  - review
  - testing
  - automation
  - human-gate
  - governance
  - brownfield
  - versioning
  - comparison
  - provenance
  - experiment
sources:
  - raw/experiments/bmad-method-v6-5-0-bmm-core-skill-inventory.md
  - raw/experiments/bmad-method-v6-5-0-to-v6-10-0-skill-delta.md
  - raw/experiments/bmad-method-v6-10-0-to-v6-11-0-skill-delta.md
  - raw/official-docs/bmad-method-v6-10-0-bmm-module-help-csv.md
  - raw/official-docs/bmad-method-v6-10-0-core-module-help-csv.md
  - raw/official-docs/bmad-method-v6-10-0-bmad-modules-yaml.md
  - raw/official-docs/bmad-method-v6-10-0-prd-skill.md
  - raw/official-docs/bmad-method-v6-10-0-ux-skill.md
  - raw/official-docs/bmad-method-v6-10-0-architecture-skill.md
  - raw/official-docs/bmad-method-v6-10-0-dev-auto-skill.md
  - raw/official-docs/bmad-method-v6-10-0-forge-idea-skill.md
  - raw/official-docs/bmad-method-v6-10-0-spec-skill.md
  - raw/official-docs/bmad-method-v6-11-0-bmm-module-help-csv.md
  - raw/official-docs/bmad-method-v6-11-0-core-module-help-csv.md
  - raw/official-docs/bmad-method-v6-11-0-bmad-modules-yaml.md
  - raw/official-docs/bmad-method-v6-11-0-build-skill.md
  - raw/official-docs/bmad-method-v6-11-0-build-auto-skill.md
  - raw/official-docs/bmad-method-v6-11-0-deep-recon-skill.md
  - raw/official-docs/bmad-method-v6-11-0-project-context-skill.md
  - raw/official-docs/bmad-method-v6-11-0-review-skill.md
  - raw/official-docs/bmad-method-v6-11-0-v6-shims-readme.md
confidence: high
contested: false
contradictions: []
---
# BMAD v6.5.0에서 v6.11.0까지 BMM/Core skill 변화

## 결론

BMAD의 skill catalog는 v6.5.0에서 v6.10.0까지 기존 Phase 1–4 구조를 유지한
채 통합 PRD·UX·Architecture, Spec, Dev Auto와 Forge Idea를 추가했다. v6.11.0은
더 큰 전환으로, active catalog를 `plan`과 `ship` 중심으로 줄이고 과거 ID를
19개의 `v6-shims` root로 분리했다.
^[raw/experiments/bmad-method-v6-5-0-to-v6-10-0-skill-delta.md] ^[raw/experiments/bmad-method-v6-10-0-to-v6-11-0-skill-delta.md]

따라서 물리적 root 수가 46에서 49로 늘었다고 v6.11.0의 기능 표면이 커졌다고
해석하면 안 된다. v6.11.0의 49개 root 중 active root는 30개이고 19개는 v6
호환 shim이다.

## 버전과 freshness

| Version | Tag commit | BMM roots | Core roots | Shims | Active roots |
| --- | --- | ---: | ---: | ---: | ---: |
| 6.5.0 | `69cbeb4d07f318180c3d610c511381b9f494e786` | 30 | 12 | 0 | 42 |
| 6.10.0 | `081e64ee5aab2316b912883f7bee528ee143ce36` | 33 | 13 | 0 | 46 |
| 6.11.0 | `9ce3c397c9b238de96f7365da8019f6f66b059da` | 35 | 14 | 19 | 30 |

- 마지막 검증일: 2026-08-17
- 최신 버전 종속: 예. 최신 설치에서 추천되는 active skill 선택에 영향
- 재검증 조건: 새 stable tag에서 BMM/Core scope tree, module help catalog,
  `v6-shims` 또는 installer registry가 바뀔 때

## 비교 방법

각 `SKILL.md`의 부모 디렉터리를 skill root로 정하고 root 전체의 재귀 Git tree
ID를 비교했다. 이 ID는 `SKILL.md`뿐 아니라 reference, step, template, script와
configuration을 포함한다. 동일 경로·동일 tree ID는 변경 없음으로 판정했고,
다른 경우에만 manifest와 실제 변경 파일을 읽었다. ^[raw/experiments/bmad-method-v6-5-0-bmm-core-skill-inventory.md]

| 비교 | Exact-path 불변 | 변경 | 추가 | 제거 |
| --- | ---: | ---: | ---: | ---: |
| v6.5.0 → v6.10.0 | 4 | 36 | 6 | 2 |
| v6.10.0 → v6.11.0 | 0 | 6 | 43 | 40 |

v6.10.0에서 v6.11.0의 add/remove 수가 큰 이유는 BMM root가 phase-numbered
경로에서 `agents/plan/ship/v6-shims`로 이동했기 때문이다. 이를 모두 독립 신규
기능으로 계산하지 않는다.

## v6.5.0 → v6.10.0

### 추가 및 제거

| 구분 | Skill | 의미 |
| --- | --- | --- |
| 추가 | `bmad-prd` | create/update/validate intent를 한 skill로 통합 |
| 추가 | `bmad-ux` | UX pattern과 design specification 계약 |
| 추가 | `bmad-architecture` | architecture spine 중심 계약 |
| 추가 | `bmad-dev-auto` | 한 번의 unattended development iteration |
| 추가 | `bmad-forge-idea` | persona 기반 idea pressure test |
| 추가 | `bmad-spec` | downstream용 SPEC kernel과 companion 생성 |
| 제거 경로 | `bmad-create-ux-design` | help catalog에서는 `bmad-ux`로 대체 |
| 제거 | `bmad-distillator` | v6.10.0 Core inventory에서 사라짐 |

PRD는 세 개의 create/edit/validate 진입을 하나의 `bmad-prd` intent surface로
노출한다. ^[raw/official-docs/bmad-method-v6-10-0-prd-skill.md]

UX는 `DESIGN.md`와 `EXPERIENCE.md`를 peer contract로 만들고, Architecture는
독립 구현 단위가 따를 invariant spine을 만든다. ^[raw/official-docs/bmad-method-v6-10-0-ux-skill.md] ^[raw/official-docs/bmad-method-v6-10-0-architecture-skill.md]

`bmad-spec`은 다양한 intent를 SPEC kernel과 companion으로 변환하고,
`bmad-dev-auto`는 사람 interaction 없이 intent를 review 가능한 구현으로 만든다. ^[raw/official-docs/bmad-method-v6-10-0-spec-skill.md] ^[raw/official-docs/bmad-method-v6-10-0-dev-auto-skill.md]

`bmad-forge-idea`는 build artifact 생성보다 아직 값싼 단계에서 가정과 결정을
압박 검증하는 Core skill이다. ^[raw/official-docs/bmad-method-v6-10-0-forge-idea-skill.md]

### v6.10.0의 선택 모델

BMM help catalog는 여전히 Planning → Solutioning → Sprint/Story/Dev/Review의
Phase 1–4 흐름을 노출한다. 통합 PRD·UX·Architecture가 권장 ID가 되었지만
Create Story와 Dev Story도 active implementation catalog에 남아 있다. ^[raw/official-docs/bmad-method-v6-10-0-bmm-module-help-csv.md]

Core catalog는 문서 index/shard, 두 editorial reviewer, 두 code reviewer를 각각
독립 skill로 유지하면서 Spec과 Forge Idea를 추가한다. ^[raw/official-docs/bmad-method-v6-10-0-core-module-help-csv.md]

또한 v6.5.0에는 없던 top-level official module registry가 v6.10.0에 존재하며,
`bmad-loop`를 opt-in marketplace module로 등록하고 `bmad-automator`를 deprecated로
표시한다. ^[raw/official-docs/bmad-method-v6-10-0-bmad-modules-yaml.md]

## v6.10.0 → v6.11.0

### Active catalog 통합

| v6.10.0 | v6.11.0 active 선택 | 호환 처리 |
| --- | --- | --- |
| `bmad-quick-dev` | `bmad-build` | old ID shim |
| `bmad-dev-auto` | `bmad-build-auto` | old ID shim |
| `bmad-create-story`, `bmad-dev-story` | `bmad-build` | full workflow shim, v7 제거 예정 |
| `bmad-document-project`, `bmad-generate-project-context` | `bmad-project-context` | setup intent shim |
| market/domain/technical research | `bmad-deep-recon` | type preset shim |
| 개별 review/editorial skills | `bmad-review`와 lens | Core shim |
| readiness, sprint status | `bmad-sprint-planning` | gate/status intent로 통합 |
| Core `bmad-spec` | BMM plan `bmad-spec` | module ownership 이동 |

공식 v6 shim map은 deprecated ID가 v6 중에는 설치되지만 v7에서 제거된다고
명시한다. ^[raw/official-docs/bmad-method-v6-11-0-v6-shims-readme.md]

### Build 중심 실행

`bmad-build`는 user intent, story, bug fix 또는 change request를 하나의 공식
구현 surface로 받는다. `bmad-build-auto`는 같은 모델의 무인 1회 실행이다. 두
skill의 설치 entrypoint는 `uv run ... render_skill.py`로 immutable workflow
snapshot을 만든 뒤 그 출력 경로를 따른다. ^[raw/official-docs/bmad-method-v6-11-0-build-skill.md] ^[raw/official-docs/bmad-method-v6-11-0-build-auto-skill.md]

이 renderer entrypoint는 v6.10.0의 `bmad-dev-auto/SKILL.md`가 workflow와 HALT
규칙을 직접 담던 구조와 다르다. 따라서 v6.11.0 Build 계열은 `uv`와 renderer
성공을 실행 전제에 포함해야 한다.

### Core catalog 축소

`bmad-deep-recon`은 research prompt 작성, 외부 report 처리, 현재 환경에서의
research 실행을 하나의 decision-grade skill로 통합한다. ^[raw/official-docs/bmad-method-v6-11-0-deep-recon-skill.md]

`bmad-review`는 adversarial, edge-case, verification-gap, structure, prose를
설정 가능한 lens로 다루고, `bmad-project-context`는 기존 문서 묶음 대신
repository `AGENTS.md` 안의 검증된 instruction block을 관리한다. ^[raw/official-docs/bmad-method-v6-11-0-review-skill.md] ^[raw/official-docs/bmad-method-v6-11-0-project-context-skill.md]

Core help catalog의 독립 노출은 v6.10.0의 12개에서 v6.11.0의 8개로 줄고,
BMM help도 Create/Dev Story와 독립 readiness/status 등을 추천 경로에서 제거한다. ^[raw/official-docs/bmad-method-v6-11-0-core-module-help-csv.md] ^[raw/official-docs/bmad-method-v6-11-0-bmm-module-help-csv.md]

### Installer module delta

v6.11.0 registry는 BMad Loop의 설명을 whole-epic unattended build/verify/retro로
확장하고 Whiteport Design Studio를 deprecated로 표시한다. 이는 BMM/Core
내장 skill과 외부 installable module을 구분해 해석해야 한다. ^[raw/official-docs/bmad-method-v6-11-0-bmad-modules-yaml.md]

## 버전 선택 기준

- v6.10.0 설치에서는 Phase 1–4와 Create Story/Dev Story ID를 active contract로
  취급한다.
- v6.11.0 신규 설치에서는 `bmad-build`, `bmad-build-auto`,
  `bmad-sprint-planning`, `bmad-project-context`, `bmad-deep-recon`, `bmad-review`를
  우선 선택한다.
- v6.11.0에서 old ID가 실행된다는 사실을 장기 호환 보장으로 해석하지 않는다.
- 물리 root 수가 아니라 help catalog와 shim 여부로 사용자 선택지를 계산한다.
- 세부 workflow 계약은 [[bmad-v6-10-0-workflow-contracts]]와
  [[bmad-v6-11-0-workflow-contracts]], 자동화 gate는
  [[bmad-v6-11-0-automation-and-human-gates]]와 함께 판단한다.

## 알려진 공백

- 비교는 공식 tag의 정적 source와 manifest 기준이며 installer/runtime 실험은
  하지 않았다.
- v6.5.0과 v6.10.0 사이 모든 중간 stable tag의 최초 변경 시점은 아직 매핑하지
  않았다.
- 같은 tree change 안의 문구 수정과 실제 실행 계약 변경은 전체 root 수만으로
  구분할 수 없어, 이번 canonical은 manifest와 중심 skill 원문이 뒷받침하는
  변화만 포함한다.
