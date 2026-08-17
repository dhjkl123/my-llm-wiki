---
title: "BMAD v6.10.0 자동화 범위와 Human Approval Gate"
created: 2026-08-03
updated: 2026-08-04
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
  - experiment
sources:
  - raw/releases/bmad-method-v6-10-0-release-api-2026-08-04.md
  - raw/official-docs/bmad-method-v6-10-0-workflow-map-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-module-registry-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-dev-auto-reference-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-dev-auto-plan-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-dev-auto-implement-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-dev-auto-review-excerpt.md
  - raw/official-docs/bmad-method-v6-10-0-code-review-human-gates-excerpt.md
  - raw/experiments/bmad-method-v6-10-0-automation-name-search.md
  - raw/official-docs/bmad-method-main-5247108-package-version-excerpt.md
  - raw/official-docs/bmad-method-main-5247108-build-auto-skill.md
  - raw/official-docs/bmad-method-main-5247108-dev-auto-shim.md
confidence: medium
contested: false
contradictions: []
---
# BMAD v6.10.0 자동화 범위와 Human Approval Gate

## 결론

공식 tag `v6.10.0`에는 `create-story → dev → review`를 그대로 묶은 이름의
skill 대신,
작은 intent를 자체 spec으로 계획하고 구현·적대적 리뷰까지 한 번 무인 실행하는
공식 `bmad-dev-auto`가 존재한다. `bmad-loop`는 이를 반복 호출하고 정책·hook을
연결하는 별도 opt-in orchestrator module이다.
^[raw/releases/bmad-method-v6-10-0-release-api-2026-08-04.md]

반면 2026-08-04의 공식 `main` snapshot에서는 `bmad-build-auto`가 정식 명칭이고
`bmad-dev-auto`는 deprecated redirect shim이다. tag snapshot과 미출시 main을
같은 “v6.10.0 현재 사실”로 합치면 안 된다.
^[raw/official-docs/bmad-method-main-5247108-build-auto-skill.md]
^[raw/official-docs/bmad-method-main-5247108-dev-auto-shim.md]

## 버전 범위

- 대상/tag/commit: BMAD Method `v6.10.0`,
  `081e64ee5aab2316b912883f7bee528ee143ce36`
- 마지막 검증일: 2026-08-03
- 최신 버전 종속: 예
- 재검증 조건: module registry, dev-auto state machine 또는 release channel 변경

비교용 최신 snapshot은 공식 `main` commit
`5247108ba3f45b2e9731fa41919029b3d2623023`이며, 그 `package.json`은 여전히
`6.10.0`을 선언한다. 그러나 tag가 아닌 main이므로 출시된 `v6.10.0` 계약을
소급 변경하는 근거로 쓰지 않는다.
^[raw/official-docs/bmad-method-main-5247108-package-version-excerpt.md]

## 명칭별 판정

| 명칭 | `v6.10.0` tag 판정 | 책임 범위 | confidence |
| --- | --- | --- | --- |
| `bmad-dev-auto` | 공식 존재 | 단일 unattended iteration: clarify, spec, implement, review, finalize | high |
| `bmad-loop` | 공식 존재 | deterministic Python orchestrator, adversarial review 및 반복 실행 | high |
| `bmad-automator` | 공식 registry에 남아 있으나 deprecated | 과거 experimental predecessor; `bmad-loop`로 대체 | high |
| `bmad-build-auto` | bounded 검색에서 없음 | 이 tag에서는 정의되지 않음 | low |

공식 registry에서 `bmad-loop`는 기본 선택이 아니며 설치 뒤
`bmad-loop-setup`을 실행해야 automation과 project hook/policy가 활성화된다.
`bmad-automator`는 deprecated로 표시된다.
^[raw/official-docs/bmad-method-v6-10-0-module-registry-excerpt.md]

정확명 검색에서는 앞의 세 명칭을 확인했지만 `bmad-build-auto`는 찾지 못했다.
이 부재 판정은 pinned tag와 Markdown/YAML에 한정되므로 `low`다.
^[raw/experiments/bmad-method-v6-10-0-automation-name-search.md]

### 공식 main의 명칭 변경

| snapshot | 공식 주 명칭 | 호환 명칭 | 해석 |
| --- | --- | --- | --- |
| `main` @ `5247108…` | `bmad-build-auto` | `bmad-dev-auto` deprecated shim | 새 설치·main 사용자는 build-auto를 선택하고, dev-auto는 이전 이름 호환에만 사용 |

이 main snapshot은 `bmad-build-auto` skill을 직접 제공하고, `bmad-dev-auto`가
원래 입력을 그대로 전달하도록 명시한다. 따라서 이전의 “fork·비공식 alias
가능” 추정은 current main에는 적용하지 않는다.
^[raw/official-docs/bmad-method-main-5247108-build-auto-skill.md]
^[raw/official-docs/bmad-method-main-5247108-dev-auto-shim.md]

## 두 실행 모델

| 항목 | 일반 Story/Dev/Review | `bmad-dev-auto` + 선택적 `bmad-loop` |
| --- | --- | --- |
| 작업 단위 | Epic에서 준비한 story | 하나의 coherent intent와 `spec-*.md` |
| 상호작용 | 단계별 실행, review 선택에서 HALT | 내부 단계는 질문·승인 없이 진행 |
| review | 사람이 decision/patch 처리 선택 | Blind/Edge Case Hunter 병렬 실행, 자동 triage/repair |
| 실패 상태 | story `in-progress` 또는 workflow HALT | spec `blocked`와 blocking condition |
| VCS | workflow 외부 운영에 좌우 | VCS가 있으면 clean worktree 필수; local commit, push 안 함 |
| 적합성 | 고위험·모호한 판단, 명시적 승인 필요 | 작고 닫힌 intent, 자동 검증, 안전한 rollback |

일반 Code Review는 `decision_needed`와 patch 처리에서 사용자 선택을 기다리고,
그 뒤에도 다음 story/re-review/done 선택을 기다린다.
^[raw/official-docs/bmad-method-v6-10-0-code-review-human-gates-excerpt.md]

Dev Auto의 plan과 implement 단계는 사람에게 묻지 않는다. intent gap, spec gate
실패, implementation verification 실패는 추측하지 않고 `blocked`로 끝낸다.
^[raw/official-docs/bmad-method-v6-10-0-dev-auto-plan-excerpt.md]
^[raw/official-docs/bmad-method-v6-10-0-dev-auto-implement-excerpt.md]

Review도 무인으로 patch를 고치고 bad spec이면 재구현한다. intent gap이면
변경을 되돌리고, repair loop가 5회를 넘으면 `blocked`다. 성공 시 local commit
후 `done`이지만 push하지 않는다.
^[raw/official-docs/bmad-method-v6-10-0-dev-auto-review-excerpt.md]

## 일반 Story chain의 orchestration 경계

`bmad-create-story`, `bmad-dev-story`, `bmad-code-review`는 각각의 공식 skill이다.
현재 근거는 이 셋을 자동 반복하는 하나의 공식 workflow나 review 실패 뒤 dev를
자동 재실행하는 계약을 제공하지 않는다. 아래는 공식 기능이 아니라 일반 story
artifact를 보존하려는 외부 orchestrator의 최소 정책이다.

| 상태 | 진입 근거 | 허용 전이 | 사람에게 넘길 조건 |
| --- | --- | --- | --- |
| `prepared` | story가 `ready-for-dev` | 명시적 story path로 dev 실행 | story/input discovery 실패 |
| `review` | dev가 DoD를 통과해 `review`로 전이 | 명시적 diff와 story로 code-review 실행 | diff/spec 선택 또는 review checkpoint |
| `remediation` | review가 `in-progress` 또는 action item을 남김 | owner가 dev 재실행 여부와 입력을 지정 | 재진입 입력 불명확, 정책 retry 한도 도달 |
| `approved` | review가 `done`이고 merge gate 통과 | merge/deploy 절차 | repository owner, CI, security 승인 실패 |

Retry counter, re-entry input, terminal state, merge gate는 orchestrator가 별도
artifact에 기록한다. 이를 `bmad-dev-auto`의 내부 `bad_spec` loopback이나
`bmad-loop` 상태 machine과 혼합하지 않는다.

## Human Approval Gate

### 공식적으로 강제되는 지점

- 일반 `bmad-code-review`: decision과 patch 처리 선택.
- `bmad-dev-auto`: 내부 사람 gate가 아니라 안전하지 않은 상태를 `blocked`로
  외부 orchestrator 또는 사람에게 route하는 경계.

### Activation prerequisite

- `bmad-loop`: 설치만으로 실행되지 않으며 별도 setup이 필요하다. 이는 설치·활성화
  조건이지 사람의 승인 판단을 요구하는 Human Approval Gate는 아니다.

Dev Auto의 terminal 상태, blocking condition, revision range를 chat 문구가 아닌
artifact에서 읽는 것은 공식 orchestrator 책임이다.
^[raw/official-docs/bmad-method-v6-10-0-dev-auto-reference-excerpt.md]

### 이 위키가 권장하는 추가 gate

- **진입 승인:** 데이터 삭제, schema migration, 외부 API·보안·규제 결정은
  무인 intent로 넘기기 전 owner가 승인한다.
- **Blocked 분류:** intent 결정을 요구하면 사람이 보완하고 새 run을 시작한다.
- **Merge/배포 승인:** `status: done`과 local commit은 merge·push·배포 승인이
  아니다. CI, security, repository owner gate를 별도로 둔다.
- **반복 한도:** loop의 시간·비용·파일 범위·재시도 한도를 policy로 고정한다.

## 적용하면 안 되는 조건

- synchronous subagent 실행이 불가능한 환경.
- VCS가 있는데 uncommitted change가 남아 있는 경우.
- acceptance criteria와 자동 verification이 불명확한 경우.
- 여러 repository의 owner 승인 없이 한 intent가 동시에 변경하는 경우.

Artifact 계약은 [[bmad-v6-10-0-workflow-contracts]], MSA 경계는
[[bmad-msa-multi-repository-boundaries]]를 함께 적용한다.
