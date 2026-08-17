---
title: "BMAD v6.11.0 자동화 범위와 Human Approval Gate"
created: 2026-08-17
updated: 2026-08-17
type: comparison
tags:
  - aidd
  - workflow
  - story
  - implementation
  - review
  - testing
  - automation
  - human-gate
  - governance
  - versioning
  - comparison
  - provenance
sources:
  - raw/releases/bmad-method-v6-11-0-release-api-2026-08-17.md
  - raw/official-docs/bmad-method-v6-11-0-workflow-map.md
  - raw/official-docs/bmad-method-v6-11-0-build-workflow.md
  - raw/official-docs/bmad-method-v6-11-0-build-auto-reference.md
  - raw/official-docs/bmad-method-v6-11-0-review-skill.md
  - raw/official-docs/bmad-method-v6-11-0-v6-shims-readme.md
confidence: high
contested: false
contradictions: []
---
# BMAD v6.11.0 자동화 범위와 Human Approval Gate

## 결론

v6.11.0은 v6.10.0의 `bmad-quick-dev`와 `bmad-dev-auto`를 각각
`bmad-build`와 `bmad-build-auto`로 바꾸고, Build를 유일한 공식 구현 모델로
정리했다. 대화형 Build는 checkpoint마다 사람을 기다리며, Build Auto는 같은
모델을 한 번 무인 실행하고 안전하지 않은 판단을 `blocked`로 외부에 넘긴다.
^[raw/releases/bmad-method-v6-11-0-release-api-2026-08-17.md]

## 버전 범위

- 대상/tag/commit: BMAD Method `v6.11.0`,
  `9ce3c397c9b238de96f7365da8019f6f66b059da`
- 마지막 검증일: 2026-08-17
- 최신 버전 종속: 예
- 재검증 조건: v7 shim 제거, Build/Build Auto 상태 machine 또는 review layer
  계약 변경

## v6.10.0에서 바뀐 선택지

| v6.10.0 명칭 | v6.11.0 판정 | migration 의미 |
| --- | --- | --- |
| `bmad-quick-dev` | `bmad-build`로 변경 | 기존 customization 파일명도 변경 |
| `bmad-dev-auto` | `bmad-build-auto`로 변경 | legacy customization이 있으면 shim이 승인 없이 덮어쓰지 않음 |
| `bmad-create-story` | deprecated, full shim 유지 | 권장 Phase 4 chain에서 제외; v7 제거 예정 |
| `bmad-dev-story` | deprecated, full shim 유지 | 권장 Phase 4 chain에서 제외; v7 제거 예정 |
| `bmad-check-implementation-readiness` | sprint planning에 통합 | 별도 readiness skill 대신 planning intent 사용 |
| `bmad-sprint-status` | sprint planning status view로 forwarding | v6 ID는 shim으로 동작 |

공식 shim 표는 old ID가 v6 중에는 설치되지만 v7에서 제거된다고 명시한다.
새 automation은 old ID의 무기한 호환을 전제로 설계하면 안 된다.
^[raw/official-docs/bmad-method-v6-11-0-v6-shims-readme.md]

Legacy customization 파일이 있으면 rename shim은 명시적 승인을 요구하고,
승인이 없거나 불가능하면 forwarding하지 않고 중지한다. 따라서 무인 runner가
`bmad-dev-auto`라는 과거 이름을 계속 호출하면 migration 단계에서 멈출 수 있다.
^[raw/releases/bmad-method-v6-11-0-release-api-2026-08-17.md]

## 실행 모델 비교

| 항목 | `bmad-build` | `bmad-build-auto` |
| --- | --- | --- |
| 목적 | 사람과 함께 한 goal을 clarify·plan·implement·review | 같은 개발 모델의 단일 unattended iteration |
| 입력 | direct intent, issue, spec, planned story | intent/ticket/file/spec 또는 spec folder+story id |
| 사람 gate | 모든 workflow checkpoint에서 HALT | 내부 질문 대신 terminal `blocked` |
| spec 범위 | 900–1600 token, single goal은 제안이며 override 가능 | 한 coherent intent; 상태 기반 resume |
| review | interactive checkpoint와 적용 판단 | configurable parallel layers, repair loop |
| 종료 | 검토 가능한 spec과 code | `done` 또는 `blocked`, durable result artifact |
| VCS | 외부 운영과 checkpoint에 좌우 | VCS가 있으면 clean tree, local commit, no push |

Build의 공식 workflow는 step 순서를 건너뛰지 않고 모든 checkpoint에서 입력을
기다리라고 요구한다. 이는 Human Approval Gate가 실행 모델 자체에 들어 있음을
뜻한다. ^[raw/official-docs/bmad-method-v6-11-0-build-workflow.md]

Build Auto는 `status`, blocking condition, follow-up review flag, deferred findings를
artifact로 남긴다. orchestrator는 chat 문구가 아니라 이 machine-readable
상태를 읽고 다음 run, escalation 또는 backlog 반영을 결정해야 한다.
^[raw/official-docs/bmad-method-v6-11-0-build-auto-reference.md]

## Review 경계

일반 `bmad-review`는 diff, code, spec, story, 문서를 하나 이상의 lens로 검토한다.
기본 lens는 adversarial, edge-case, verification-gap, structure, prose이며 설정으로
추가·교체·비활성화할 수 있다. 결과는 finding을 보고하지만 severity나 최종 승인
순위를 제공하지 않는다.
^[raw/official-docs/bmad-method-v6-11-0-review-skill.md]

Phase 4의 `bmad-code-review`, Build, Build Auto는 자체 review prompt 계약을
가지므로 범용 `bmad-review`의 lens 결과를 구현 승인과 동일시하면 안 된다.
v6.11.0 release는 Build Auto에 invocation intent를 받는 Intent Alignment Auditor와
설정 가능한 review layer를 추가한다.
^[raw/releases/bmad-method-v6-11-0-release-api-2026-08-17.md]

## 공식적으로 강제되는 gate

- **Sprint readiness CONCERNS:** 진행 또는 수정 여부를 사람에게 질문한다.
- **Sprint readiness FAIL:** 구현 가능한 기록이 없으므로 중지한다.
- **Build checkpoint:** 순차 단계마다 사용자 입력을 기다린다.
- **Build Auto blocked:** unclear intent, intent gap, no subagents, verification
  failure, non-convergence, story dispatch 오류 등을 외부로 route한다.
- **Legacy customization migration:** old name shim은 사용자 승인 없이 파일을
  덮어쓰지 않는다.

## 이 위키가 권장하는 추가 gate

- **진입 승인:** 데이터 삭제, schema migration, 외부 API·보안·규제 결정은
  unattended intent에 넣기 전에 owner가 승인한다.
- **범위 승인:** 한 run이 여러 독립 deliverable 또는 repository를 묶지 않는지
  확인한다.
- **Blocked 분류:** intent 결정을 요구하면 spec을 임의 수정해 resume하지 말고
  사람이 intent를 보완해 새 run을 시작한다.
- **Merge/배포 승인:** `done`과 local commit은 merge, push, deploy 승인이 아니다.
- **Deferred ownership:** spec의 `deferred:`는 backlog가 아니므로 owner가
  ticket 생성, 중복 제거, 무시 정책을 명시한다.

## 적용하면 안 되는 조건

- subagent 실행이나 clean worktree를 보장할 수 없는 unattended 환경.
- acceptance criteria와 실제로 실행되는 test가 불명확한 작업.
- legacy customization migration을 사람이 승인할 수 없는 old-ID runner.
- 여러 repository owner의 승인 없이 한 run이 교차 변경하는 경우.

Artifact 흐름은 [[bmad-v6-11-0-workflow-contracts]], repository 경계는
[[bmad-msa-multi-repository-boundaries]]와 함께 판단한다.
