---
title: "BMAD MSA 및 multi-repository artifact 경계"
created: 2026-08-03
updated: 2026-08-17
type: concept
tags:
  - aidd
  - workflow
  - requirements
  - architecture
  - story
  - human-gate
  - governance
  - brownfield
  - msa
  - multi-repository
  - versioning
sources:
  - raw/official-docs/bmad-method-v6-10-0-architecture-contract-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-multipart-detection-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-multipart-output-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-create-story-inputs-excerpt.md
confidence: low
contested: false
contradictions: []
---
# BMAD MSA 및 multi-repository artifact 경계

## 판정

BMAD v6.10.0은 monolith, monorepo, multi-part를 탐지하고 사람이 part 구성을
확인한 뒤 part별 architecture와 'integration-architecture.md'를 만드는 공식
경로를 제공한다. 그러나 서로 다른 Git repository의 planning, status,
release를 하나로 조정하는 명시적 multi-repository contract는 이번 공식 근거
세트에서 확인하지 못했다.
^[raw/official-docs/bmad-method-v6-10-0-multipart-detection-excerpt.md]
^[raw/official-docs/bmad-method-v6-10-0-multipart-output-excerpt.md]

따라서 아래 multi-repository 배치는 공식 기능이 아니라, v6.10.0의 계층형
architecture spine과 artifact handoff를 적용한 위키 추론이다. confidence는
'low'다.

## 버전 범위

- 대상/tag/commit: BMAD Method v6.10.0,
  081e64ee5aab2316b912883f7bee528ee143ce36
- 마지막 검증일: 2026-08-03
- 최신 버전 종속: 부분적. 공식 multi-part 동작은 버전 종속이고 경계 모델은
  위키 정책이다.
- 재검증 조건: 공식 multi-repository module이나 cross-repo status contract가
  출시되거나 architecture inheritance 규칙이 바뀔 때

## 공식적으로 확인된 경계

- scan이 여러 part를 찾으면 경로를 제시하고 별도 문서화 여부를 묻는다.
- integration scan은 REST, GraphQL, gRPC, event bus, shared DB, auth/data flow를
  찾고 'integration-architecture.md'를 쓴다.
- 각 part에는 기술 stack, data/API, source tree, deployment, test 전략을 담은
  architecture 문서를 만든다.
- 상위 'ARCHITECTURE-SPINE.md'의 결정은 하위 epic spine에서 binding,
  read-only constraint이며, 하위는 상위가 열어 둔 사항만 결정한다.
^[raw/official-docs/bmad-method-v6-10-0-architecture-contract-excerpt.md]

## 위키 권장 경계 모델

| 수준 | 소유 문서 | 포함할 내용 | 제외할 내용 |
| --- | --- | --- | --- |
| 제품/플랫폼 | 제품 PRD, parent Architecture Spine, integration Epic, readiness | 사용자 결과, 공통 NFR, 서비스 경계, API/event/schema contract, E2E SLO와 release 순서 | repository 내부 파일·세부 task |
| 서비스/저장소 | local spine, project context, repository story, test/rollback | 상속 constraint, local 기술 결정, 변경 파일, service AC | 제품 요구사항 전체 복제 |
| 교차 변경 | coordinating Epic과 repository별 story | contract version, provider/consumer 순서, compatibility window, owner | 한 story가 여러 repo 상태를 암묵적으로 완료 처리 |

상위 spine은 제품 수준 불변 조건을 두고, 서비스 spine은 그 결정을 재논의하지
않은 채 local open question만 해결한다. 이는 공식 hierarchy를 repository
ownership에 대응시킨 추론이다.

## 적용 순서

1. 각 repository를 독립 part로 inventory하고 owner·deploy 경계를 사람이
   확인한다.
2. 제품 spine에 공통 NFR, data ownership, interface와 compatibility policy를
   고정한다.
3. repository별 spine에 상속한 decision ID와 local divergence만 기록한다.
4. 제품 Epic 아래 repository별 story를 만들고 각 story는 자신이 바꾸는 코드,
   test, migration, rollback만 소유한다.
5. 모든 local gate와 cross-repo contract/E2E test가 끝난 뒤 제품 완료를
   승인한다.

Create Story는 Epic을 중심 context로 쓰고 PRD·Architecture·UX는 fallback으로
선택 로드한다. 따라서 서비스 story에는 제품 문서 전체를 복제하기보다 관련
parent decision과 local spine을 trace하는 편이 이 구조와 맞는다. 마지막
문장은 위키 추론이다.
^[raw/official-docs/bmad-method-v6-10-0-create-story-inputs-excerpt.md]

## Human Approval Gate

- **Part 확인:** 자동 탐지한 part가 실제 ownership·deploy 단위와 맞는지 승인.
- **Interface 승인:** provider와 consumer가 contract version과 migration
  window를 함께 승인.
- **Story 진입 승인:** parent decision, local constraint, rollback이 trace되는지
  확인.
- **통합 완료 승인:** 각 repository의 done을 제품 완료로 간주하지 않고
  contract 및 E2E evidence를 확인.

## 적용하기 좋은 조건

- 서비스와 repository ownership이 명확하고 interface를 versioning할 수 있다.
- repository별 CI와 통합 검증, rollback owner가 있다.
- 제품 Epic과 local story 사이 traceability를 유지할 수 있다.

## 적용하면 안 되는 조건

- 작은 단일 저장소에 문서 계층만 늘어나는 경우.
- shared database나 암묵적 coupling을 owner 없이 자동 분리하려는 경우.
- 하나의 무인 loop가 여러 repository에서 commit·merge하도록 위임하는 경우.

현재 Workflow 입력·출력은 [[bmad-v6-11-0-workflow-contracts]], 자동화 선택은
[[bmad-v6-11-0-automation-and-human-gates]]를 함께 본다. 이 경계 모델의 직접
근거는 여전히 v6.10.0에 고정되어 있으므로 v6.11.0 cross-repository 재검증은
후속 과제다.
