---
title: "BMAD v6.11.0 workflow 및 artifact 계약"
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
  - human-gate
  - brownfield
  - versioning
  - provenance
sources:
  - raw/releases/bmad-method-v6-11-0-release-api-2026-08-17.md
  - raw/official-docs/bmad-method-v6-11-0-workflow-map.md
  - raw/official-docs/bmad-method-v6-11-0-build-workflow.md
  - raw/official-docs/bmad-method-v6-11-0-build-auto-reference.md
  - raw/official-docs/bmad-method-v6-11-0-sprint-planning-skill.md
  - raw/official-docs/bmad-method-v6-11-0-readiness-gate.md
  - raw/official-docs/bmad-method-v6-11-0-project-context-skill.md
confidence: high
contested: false
contradictions: []
---
# BMAD v6.11.0 workflow 및 artifact 계약

## 결론

BMAD v6.11.0의 공식 구현 경로는 `bmad-sprint-planning → bmad-build →
bmad-code-review`로 단순화되었다. 큰 작업은 PRD·UX·Architecture·Epics를 거쳐
sprint planning의 readiness gate로 들어가고, 작고 명확한 작업은 같은
`bmad-build`에 직접 넣는다. `bmad-create-story`와 `bmad-dev-story`는 더 이상
권장 Phase 4 경로가 아니며 v6 호환용으로만 남는다.
^[raw/releases/bmad-method-v6-11-0-release-api-2026-08-17.md]

## 버전과 freshness

- 대상: BMad Method/BMM
- 확인 버전/tag: `6.11.0` / `v6.11.0`
- commit: `9ce3c397c9b238de96f7365da8019f6f66b059da`
- 마지막 검증일: 2026-08-17
- 최신 버전 종속: 예
- 재검증 조건: 새 stable release가 Build 명칭, readiness 판정, spec 상태 또는
  v6 shim 제거 시점을 바꿀 때

## 전체 artifact 흐름

| 단계 | 주요 입력 | 출력 | 판단 지점 |
| --- | --- | --- | --- |
| Plan | direct intent 또는 Brief·PRD·UX | PRD, UX contract | 필요한 계획 깊이를 작업 위험과 불확실성으로 선택 |
| Solution | PRD/spec, UX, 기술 제약 | Architecture, Epics/Stories | 구현자가 기록되지 않은 결정을 발명해야 하는지 확인 |
| Sprint Planning | 실제 planning artifacts | PASS/CONCERNS/FAIL, `sprint-status.yaml` | CONCERNS는 진행 여부를 사람이 결정, FAIL은 중지 |
| Build | direct intent, issue, spec 또는 planned story | `spec-*.md`, code, verification | checkpoint에서 사람 입력을 기다림 |
| Build Auto | 같은 범주의 intent 또는 spec/story dispatch | terminal spec `done`/`blocked`, local commit | 안전하게 추론할 수 없으면 `blocked` |
| Review/Retro | diff·문서·완료 epic artifacts | findings/patches, retrospective | 변경 승인과 후속 action ownership은 외부 정책 |

공식 workflow map은 계획 artifact가 구현 context를 강화하지만 다른 구현
workflow를 선택하게 하지는 않는다고 명시한다. 모든 구현 진입은 `bmad-build`로
수렴하고, 무인 실행이 적합할 때만 `bmad-build-auto`를 사용한다.
^[raw/official-docs/bmad-method-v6-11-0-workflow-map.md]

## Sprint Planning과 readiness 계약

`bmad-check-implementation-readiness`는 독립 skill에서 제거되고
`bmad-sprint-planning`의 첫 gate로 통합되었다. readiness-only, full planning,
status, validate, fix의 다섯 intent를 가지며, headless 모드에서는 사람이
풀어야 할 중복·고아·미확정 repair를 추측하지 않고 `blocked`로 끝낸다.
^[raw/official-docs/bmad-method-v6-11-0-sprint-planning-skill.md]

Readiness는 파일명 존재 여부보다 “개발자가 기록되지 않은 결정을 발명하지 않고
구현할 수 있는가”를 판정한다. intent와 story의 양방향 trace, 독립 완료 가능한
story, 기록된 Architecture/UX 결정, artifact 충돌 표면화를 검사한다. UI story가
없다면 UX 문서 부재 자체는 finding이 아니다.
^[raw/official-docs/bmad-method-v6-11-0-readiness-gate.md]

| 판정 | 동작 |
| --- | --- |
| PASS | full planning이면 tracking 생성으로 계속 |
| CONCERNS | gap 위치를 제시하고 진행 또는 수정 여부를 사람에게 질문 |
| FAIL | 구현 불가능 근거와 수정 skill을 제시하고 중지 |

## Build 계약

`bmad-build`는 한 개의 사용자 목표를 clarify, plan, implement, review하는 공식
Phase 4 경로다. spec은 actionable, dependency-ordered, Given/When/Then testable,
placeholder-free, gap-free, coherent해야 ready-for-development다. 900–1600 token과
single-goal 범위는 제안값이며 사람이 override할 수 있다.
^[raw/official-docs/bmad-method-v6-11-0-build-workflow.md]

대화형 Build는 step file을 순차 실행하고 checkpoint마다 멈춰 사람 입력을
기다린다. 따라서 `bmad-build` 완료를 무인 orchestration 계약으로 해석하면 안
된다. 무인 반복은 별도 surface인 `bmad-build-auto`가 담당한다.

## Build Auto 계약

Build Auto는 하나의 intent, ticket/story, intent file, 기존 spec 또는 spec
folder+story id를 입력으로 받아 clarify → plan → implement → review를 한 번
수행한다. `draft`, `ready-for-dev`, `in-progress`, `in-review`, `done`, `blocked`
상태로 resume하며, subagent가 없으면 `no subagents`로 막힌다.
^[raw/official-docs/bmad-method-v6-11-0-build-auto-reference.md]

v6.11.0에서는 deferred finding이 별도 `deferred-work.md`가 아니라 spec
frontmatter의 `deferred:`에 들어간다. `final_revision`도 제거되어 commit 범위는
현재 story의 `baseline_revision`부터 다음 story의 `baseline_revision` 직전까지,
또는 종료 시 `..HEAD`로 계산한다.
성공 시 local commit을 만들지만 push하지 않는다.
^[raw/releases/bmad-method-v6-11-0-release-api-2026-08-17.md]

## Brownfield project context

`bmad-project-context`는 생성형 프로젝트 문서 묶음 대신 repository의
`AGENTS.md` 안에 작고 검증된 instruction block을 유지한다. setup, refresh,
record, audit intent를 제공하며 모든 write 전에 전체 block을 보여 주고 사용자의
승인을 받는다. repository에서 직접 읽을 수 있는 명령과 사실은 중복 저장하지
않고, 사람이 제공하는 governance·보안·동결 영역과 반복되는 실수만 보존한다.
^[raw/official-docs/bmad-method-v6-11-0-project-context-skill.md]

## 선택 기준

- 여러 stakeholder, architecture 또는 cross-service 의사결정이 크면 planning
  artifact와 sprint readiness를 먼저 통과한다.
- 범위가 작아도 사람이 checkpoint를 승인해야 하면 `bmad-build`를 사용한다.
- 닫힌 intent, 자동 검증, clean worktree, subagent가 모두 가능할 때만
  `bmad-build-auto`를 고려한다.
- 자동화와 migration gate는 [[bmad-v6-11-0-automation-and-human-gates]],
  cross-repository 경계는 [[bmad-msa-multi-repository-boundaries]]와 함께 본다.
- BMM/Core skill의 역사적 catalog와 변경 감지 기준은
  [[bmad-v6-5-0-bmm-core-skill-catalog]]에서 확인한다.
- workflow 변화가 실제 사용자 경험에 어떻게 드러났는지는
  [[bmad-v6-5-0-to-v6-11-0-community-opinions]]의 명시·추정 버전 표본과 함께 본다.

## 알려진 공백

- 이번 수집은 공식 tag의 정적 계약 검증이며 설치·실행 실험은 하지 않았다.
- `sprint_plan.py`의 실제 drift repair와 headless JSON은 synthetic experiment가
  필요하다.
- 여러 repository를 하나의 Build Auto run으로 변경하는 공식 계약은 확인하지
  않았다.
