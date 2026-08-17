---
title: "BMAD v6.5.0 BMM 및 Core 스킬 기준선"
created: 2026-08-17
updated: 2026-08-17
type: query
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
  - governance
  - brownfield
  - versioning
  - provenance
  - experiment
sources:
  - raw/releases/bmad-method-v6-5-0-release-api-2026-08-17.md
  - raw/official-docs/bmad-method-v6-5-0-package-json.md
  - raw/official-docs/bmad-method-v6-5-0-bmm-module-yaml.md
  - raw/official-docs/bmad-method-v6-5-0-bmm-module-help-csv.md
  - raw/official-docs/bmad-method-v6-5-0-core-module-yaml.md
  - raw/official-docs/bmad-method-v6-5-0-core-module-help-csv.md
  - raw/experiments/bmad-method-v6-5-0-bmm-core-skill-inventory.md
confidence: high
contested: false
contradictions: []
---
# BMAD v6.5.0 BMM 및 Core 스킬 기준선

## 결론

BMAD v6.5.0의 공식 저장소에는 `src/bmm-skills` 아래 30개, `src/core-skills`
아래 12개, 총 42개의 `SKILL.md` root가 있다. BMM은 제품 발견부터 story 구현과
회고까지의 AIDD lifecycle 및 여섯 agent를 제공하고, Core는 공통 설정,
brainstorming, multi-agent 협업, 문서 분할·검토·요약·customization 도구를
제공한다. ^[raw/experiments/bmad-method-v6-5-0-bmm-core-skill-inventory.md]

이 페이지는 v6.5.0을 이후 버전의 delta 기준선으로 사용한다. 같은 skill 경로의
재귀 Git tree ID가 같으면 그 버전에서는 새 raw나 canonical update를 만들지
않는다. Tree ID가 다르거나 경로·registry가 바뀐 경우에만 변경 파일과 실행 계약을
추가 수집한다.

## 버전과 freshness

- 대상: BMad Method BMM/Core skills
- 확인 버전/tag: `6.5.0` / `v6.5.0`
- commit: `69cbeb4d07f318180c3d610c511381b9f494e786`
- 마지막 검증일: 2026-08-17
- 최신 버전 종속: 아니오. 후속 버전 비교를 위한 역사적 기준선
- 재검증 조건: tag가 이동하는 integrity incident, inventory 절차 변경 또는
  비교 대상 버전의 BMM/Core scope tree ID 변화

`package.json`도 product version을 `6.5.0`으로 선언하므로 tag와 package
version이 일치한다. ^[raw/official-docs/bmad-method-v6-5-0-package-json.md]

## 두 카탈로그를 구분하는 법

| 관점 | 근거 | 의미 |
| --- | --- | --- |
| 물리적 설치 소스 | `src/bmm-skills`, `src/core-skills`의 `SKILL.md` root | 어느 module tree가 skill 구현을 소유하는지 |
| 사용자 노출 카탈로그 | 각 `module-help.csv` | display name, menu code, phase, 순서, 필수 여부와 output |
| module 설정 | 각 `module.yaml` | 설치 시 받는 설정, 출력 경로, agent roster |

BMM의 help catalog에는 Core가 소유하는 `bmad-brainstorming`도 Phase 1 항목으로
노출된다. 따라서 help 행 수를 BMM 물리 skill 수로 해석하면 안 된다.
^[raw/official-docs/bmad-method-v6-5-0-bmm-module-help-csv.md]
^[raw/official-docs/bmad-method-v6-5-0-core-module-help-csv.md]

## BMM skill 기준선

### Agent 6개

| 단계 | Skill | 역할 |
| --- | --- | --- |
| Analysis | `bmad-agent-analyst` | business analysis와 stakeholder 관점 |
| Analysis | `bmad-agent-tech-writer` | 기술 문서 작성·검증·설명·diagram |
| Planning | `bmad-agent-pm` | 제품 요구사항과 user value |
| Planning | `bmad-agent-ux-designer` | UX 설계와 사용자 흐름 |
| Solutioning | `bmad-agent-architect` | 기술 결정과 architecture |
| Implementation | `bmad-agent-dev` | story 구현과 test discipline |

공식 BMM module 설정은 이 여섯 agent의 code, persona와 team을 등록하고,
`planning_artifacts`, `implementation_artifacts`, `project_knowledge` 경로를
설치 설정으로 받는다. ^[raw/official-docs/bmad-method-v6-5-0-bmm-module-yaml.md]

### Analysis workflow 6개

- `bmad-document-project`: 기존 프로젝트 문서화.
- `bmad-prfaq`: Working Backwards 방식의 product challenge.
- `bmad-product-brief`: 제품 아이디어를 brief로 정리.
- `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research`:
  domain, market, technical research를 각각 수행.

### Planning workflow 4개

- `bmad-create-prd`, `bmad-validate-prd`, `bmad-edit-prd`: PRD 생성·검증·수정.
- `bmad-create-ux-design`: UI가 중요한 제품의 UX 계획.

### Solutioning workflow 4개

- `bmad-create-architecture`: 기술 결정을 architecture로 기록.
- `bmad-create-epics-and-stories`: Architecture 이후 Epic과 Story 생성.
- `bmad-check-implementation-readiness`: PRD, UX, Architecture, Story 정렬 검사.
- `bmad-generate-project-context`: brownfield codebase에서
  `project-context.md` 생성.

### Implementation workflow 10개

- `bmad-sprint-planning`, `bmad-sprint-status`: sprint tracking 생성과 상태 안내.
- `bmad-create-story`, `bmad-dev-story`, `bmad-code-review`: story 준비, 구현,
  review cycle.
- `bmad-quick-dev`: clarify → plan → implement → review → present의 빠른 경로.
- `bmad-checkpoint-preview`: commit, branch 또는 PR의 사람 walkthrough.
- `bmad-qa-generate-e2e-tests`: 구현 후 API/E2E test 생성.
- `bmad-retrospective`: epic 완료 후 회고.
- `bmad-correct-course`: 큰 범위 변화 때 계획 재조정.

BMM help catalog는 Create PRD, Architecture, Epics/Stories, Readiness, Sprint
Planning과 story cycle을 required 또는 ordering metadata로 연결한다.
^[raw/official-docs/bmad-method-v6-5-0-bmm-module-help-csv.md]

## Core skill 기준선

| Skill | v6.5.0 책임 |
| --- | --- |
| `bmad-advanced-elicitation` | 고급 elicitation 방법 |
| `bmad-brainstorming` | 아이디어 생성과 facilitation |
| `bmad-customize` | agent/workflow override 생성과 merge 검증 |
| `bmad-distillator` | downstream LLM용 정보 보존형 압축 |
| `bmad-editorial-review-prose` | 문서 문장과 표현 review |
| `bmad-editorial-review-structure` | 문서 구조 review |
| `bmad-help` | 설치된 skill 탐색과 routing 도움 |
| `bmad-index-docs` | 전체 문서를 읽지 않는 문서 index 생성 |
| `bmad-party-mode` | 여러 agent 관점의 토론 orchestration |
| `bmad-review-adversarial-general` | 범용 adversarial review |
| `bmad-review-edge-case-hunter` | edge case 중심 review |
| `bmad-shard-doc` | 큰 문서를 작은 단위로 분할 |

Core 설정은 `user_name`, 대화 언어, 문서 출력 언어와 공통 output folder를
정의한다. BMM workflow가 사용하는 공통 사용자·출력 설정의 소유자는 Core다.
^[raw/official-docs/bmad-method-v6-5-0-core-module-yaml.md]

## Delta 수집 정책

Inventory의 module scope tree OID는 다음과 같다.

| Module | v6.5.0 scope tree OID |
| --- | --- |
| BMM | `bde383035df88f2e252e83dc76af7acfe39aeed1` |
| Core | `dc5d00bf44f96271fee315555838c884a56ac89f` |

후속 stable tag에서는 다음 순서만 수행한다.

1. BMM/Core module scope tree ID를 비교한다.
2. 동일하면 repository를 갱신하지 않고 불변으로 보고한다.
3. 다르면 exact-path skill tree ID를 비교한다.
4. 변경된 root만 Git diff하고 공식 `SKILL.md`, reference, script, template 또는
   registry 중 의사결정에 필요한 파일만 raw로 수집한다.
5. 입력·출력·상태·gate·의존성·설치 노출이 달라질 때만 canonical을 갱신한다.

Tree fingerprint는 formatting 변경도 탐지하므로 tree ID 차이만으로 canonical을
바꾸지 않는다. 반대로 `SKILL.md`가 같아도 reference나 script가 달라지면 root
tree ID가 달라져 검토 대상이 된다.
^[raw/experiments/bmad-method-v6-5-0-bmm-core-skill-inventory.md]

## 릴리스 해석 경계

v6.5.0 공식 release body의 중심 내용은 agent platform 18종 추가와
`.agents/skills/` 표준 경로 사용이다. 이 release 요약만으로 42개 skill의 세부
계약이 모두 변경되었다고 판단하지 않는다. Skill 계약은 pinned tree와 manifest를
기준으로 삼는다. ^[raw/releases/bmad-method-v6-5-0-release-api-2026-08-17.md]

후속 skill catalog 변화는
[[bmad-v6-5-0-to-v6-11-0-bmm-core-skill-delta]], workflow 변화는
[[bmad-v6-10-0-workflow-contracts]]와 [[bmad-v6-11-0-workflow-contracts]],
자동화 명칭 변화는 [[bmad-v6-11-0-automation-and-human-gates]]에서 비교한다.

## 알려진 공백

- 이번 기준선은 저장소 정적 inventory이며 설치 및 runtime 실행은 하지 않았다.
- v6.5.0에서 v6.10.0까지 어느 tag에서 각 변경이 처음 발생했는지는 후속
  tag-by-tag delta 조사 대상이다.
- 경로 삭제·추가가 rename인지 독립 제거·추가인지는 release와 Git similarity를
  함께 확인해야 한다.
