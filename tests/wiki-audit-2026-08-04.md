# 독립 Wiki 감사 결과

- 감사일: 2026-08-04
- 감사 범위: 현재 worktree의 BMAD v6.10.0 pilot 지식 세트
- 감사 방식: read-only 구조 검사, raw 본문 대조, 공식 BMAD tag/main 교차 검증
- 최종 판정: **REWORK_REQUIRED**

현재 canonical 구조와 해시는 대체로 잘 관리되어 있지만, raw 불변성 위반
이력 1건과 공식 Release 본문 fidelity 불일치 1건이 확인되었다. 또한
`bmad-build-auto`는 pinned `v6.10.0` tag에는 없지만 현재 공식 `main`에는
존재하므로 버전 범위를 더 명확히 분리해야 한다.

## 핵심 검증 결과

- 공식 `v6.10.0` annotated tag는 commit
  `081e64ee5aab2316b912883f7bee528ee143ce36`으로 정상 peel된다.
- v6.10 공식 excerpt 18개와 v6.1 excerpt 16개는 선언한 commit/line range와
  바이트 단위로 일치한다.
- 38개 raw 파일의 저장된 post-frontmatter SHA-256은 모두 현재 본문과
  일치한다.
- canonical 3개, index 3개, 비-self outbound link 6개, source 25개, claim
  marker 24개는 구조적으로 정상이다.
- validator 결과는 `PASS`, error 0, warning 4다.
- 기존 `log.md` 120줄은 수정되지 않았고 현재 변경은 append-only다.
- 민감정보·개인정보·credential은 발견하지 못했다.
- 공식 v6.10.0 Release는 `bmad-dev-auto`, `bmad-loop`, deprecated
  `bmad-automator`를 직접 확인한다.
- 현재 공식 `main`에는 `bmad-build-auto`가 존재하고, `bmad-dev-auto`는
  deprecated redirect shim이다.

## [P0] 허용되지 않은 raw record 변경 이력

- 관련 파일: `log.md`, `SCHEMA.md`,
  `raw/official-docs/bmad-method-v6-10-0-epics-prerequisites-excerpt.md`
- 관련 줄 또는 heading: `Epics excerpt trailing blank line 복원`,
  `Epics excerpt provenance boundary 정정`
- 문제 주장: 최초 capture 뒤 공식-doc raw의 body/frontmatter boundary와
  SHA-256을 같은 파일에서 수정했다.
- 실제 근거: log는 line 83 복원 시도 후 다시 `45–82`로 boundary와 SHA를
  변경했다고 기록한다. SCHEMA는 Zotero repair와 NotebookLM mapping 외 raw
  변경을 금지한다.
- 판정: **UNSUPPORTED**
- 영향: 현재 body는 공식 line 45–82와 일치하지만 immutable capture chain이
  깨져 최초 capture의 정확한 상태를 raw 자체만으로 재구성할 수 없다.
- 수정 방향: 최초 capture와 수정 capture를 별도 commit-qualified 또는
  datetime-qualified raw record로 보존하고 canonical에서 drift를 설명한다.
  과거 log는 수정하지 않는다.
- 확신도: 높음

## [P0] v6.10 Release raw가 공식 API 본문과 1바이트 불일치

- 관련 파일: `raw/releases/bmad-method-v6-10-0-release.md`, `log.md`
- 관련 줄 또는 heading: raw body byte 0, `Release fidelity`
- 문제 주장: log는 공식 GitHub API body와 LF normalization 후 일치한다고
  기록한다.
- 실제 근거: 공식 Release API body는 heading 앞에 LF 1개가 있지만 raw body는
  바로 `### ✨ Headline`으로 시작한다. 로컬 6,551자, API-normalized body
  6,552자다.
- 판정: **UNSUPPORTED**
- 영향: 의미상 내용 변화는 없으나 exact captured-body 계약과 lint 기록이
  사실과 다르다.
- 수정 방향: 기존 raw를 덮어쓰지 말고 정확한 API body를 새 record로 capture한
  뒤 drift를 기록한다.
- 확신도: 높음

## [P1] `bmad-build-auto` 판정이 현재 공식 main과 버전상 어긋남

- 관련 파일: `comparisons/bmad-v6-10-0-automation-and-human-gates.md`
- 관련 줄 또는 heading: `명칭별 판정`, lines 58, 65–67
- 문제 주장: `bmad-build-auto`는 확인되지 않았으며 다른 버전·fork·비공식
  alias일 수 있다.
- 실제 근거: pinned `v6.10.0` tag 검색에서는 실제로 없다. 그러나 현재 공식
  `main` commit `5247108ba3f45b2e9731fa41919029b3d2623023`에는 공식 skill과
  reference가 존재하고 `bmad-dev-auto`가 그 shim으로 바뀌었다. 현재
  `main/package.json`도 여전히 `6.10.0`이다.
- 판정: **VERSION_MISMATCH**
- 영향: “v6.10.0 tag snapshot”과 “현재 6.10 main”을 구분하지 않으면 사용자가
  새 설치에서 공식 명칭을 잘못 선택할 수 있다.
- 수정 방향: 명칭 표를 `v6.10.0 tag`와 `current main`으로 분리하고, 최신
  main에서는 `bmad-build-auto`가 확인됨을 명시한다.
- 확신도: 높음

## [P1] dirty worktree 요구사항이 권고로 약화됨

- 관련 파일: `comparisons/bmad-v6-10-0-automation-and-human-gates.md`,
  `raw/official-docs/bmad-method-v6-10-0-dev-auto-reference-excerpt.md`
- 관련 줄 또는 heading: 비교표 VCS line 77, 비적용 조건 lines 118–120
- 문제 주장: `clean worktree 권장`; dirty worktree도 변경 귀속을 분리할 수
  있으면 가능하다는 여지를 둔다.
- 실제 근거: 공식 v6.10 reference는 VCS가 있으면 “there must be no uncommitted
  changes”라고 강제한다.
- 판정: **PARTIALLY_SUPPORTED**
- 영향: 자동 commit과 revision range가 기존 사용자 변경을 포함할 수 있는 안전
  문제다.
- 수정 방향: pinned v6.10 기준으로 clean worktree를 필수 prerequisite로
  표시한다.
- 확신도: 높음

## [P1] Implementation contract 일부가 저장된 raw 범위를 넘음

- 관련 파일: `queries/bmad-v6-10-0-workflow-contracts.md`
- 관련 줄 또는 heading: lines 57, 93–96
- 문제 주장: PRD Coaching/final review, create-story의 story 선택,
  dev-story의 `ready-for-dev` input, code-review의 diff/story input이 저장 raw로
  검증된 계약처럼 제시된다.
- 실제 근거:
  - 저장된 PRD excerpt는 Fast path 시작까지만 capture한다.
  - create-story raw는 input path table과 final handoff만 capture하고
    story-selection 단계는 포함하지 않는다.
  - dev-story raw는 completion gates만 담고 초기 input discovery를 담지 않는다.
  - code-review raw는 human choice 단계만 담고 diff/context 수집 단계를 담지
    않는다.
  - pinned 공식 전체 파일에서는 대체로 확인되지만 저장소 raw provenance만으로는
    재검증할 수 없다.
- 판정: **PARTIALLY_SUPPORTED**
- 영향: offline evidence wiki의 핵심 입력 계약이 source marker만 따라가서는
  입증되지 않는다.
- 수정 방향: 해당 공식 line range를 별도 immutable excerpt로 capture하거나
  표의 주장을 현재 raw가 직접 지원하는 범위로 줄인다.
- 확신도: 높음

## [P2] `bmad-loop` setup을 Human Approval Gate로 분류

- 관련 파일: `comparisons/bmad-v6-10-0-automation-and-human-gates.md`
- 관련 줄 또는 heading: `공식적으로 강제되는 지점`, line 101
- 문제 주장: 별도 setup 필요성을 공식 Human Approval Gate 항목으로 분류한다.
- 실제 근거: 공식 registry/release는 setup을 설치·활성화 prerequisite로
  명시하지만 승인 decision이나 HALT 시 사람의 판단을 요구하는 gate라고 하지는
  않는다.
- 판정: **OVERSTATED**
- 영향: 운영 prerequisite와 governance approval이 혼동된다.
- 수정 방향: `Activation prerequisite`와 `Human decision/approval gate`를
  분리한다.
- 확신도: 높음

## [P2] Scenario A의 구체적 orchestration contract 부족

- 관련 파일: `comparisons/bmad-v6-10-0-automation-and-human-gates.md`,
  `queries/bmad-v6-10-0-workflow-contracts.md`
- 관련 줄 또는 heading: `두 실행 모델`, `Human Approval Gate`
- 문제 주장: create-story 이후 dev/review 자동화와 반복 실패 시 human stop을
  결정할 수 있다.
- 실제 근거: 위키는 일반 세 skill과 dev-auto 내부 loop를 구분하지만,
  `create-story → dev-story → code-review → dev-story` 외부 orchestration의 상태
  전이, 재시도 한도, re-entry input을 정의하지 않는다.
- 판정: **PARTIALLY_SUPPORTED**
- 영향: 일반 story artifact를 유지하려는 사용자가 `bmad-loop/dev-auto`와 잘못
  결합할 수 있다.
- 수정 방향: 공식 workflow 조합이 아니라 orchestrator 정책임을 명시하고
  terminal state, retry counter, human escalation, merge gate 계약을 별도로
  제시한다.
- 확신도: 높음

## [P2] Java Controller brownfield-to-story 경로 부재

- 관련 파일: `concepts/bmad-msa-multi-repository-boundaries.md`, `index.md`
- 관련 줄 또는 heading: 전체 canonical set
- 문제 주장: 문서가 부족한 Java brownfield를 Controller 단위로 분석해 story로
  전환하는 의사결정을 지원한다.
- 실제 근거: 저장 지식은 multi-part detection과 architecture 산출물을 다루지만
  Controller inventory, endpoint/dependency 분석, 분석 산출물에서 Epic/Story로
  이어지는 contract는 없다.
- 판정: **UNSUPPORTED**
- 영향: Scenario C는 추가 웹 조사 없이는 답할 수 없다.
- 수정 방향: `bmad-document-project`의 brownfield input/output과 Controller 단위
  deep-dive, architecture/project-context, epic/story handoff를 공식 근거로 별도
  조사한다.
- 확신도: 높음

## [P2] checker 존재와 최근 “0 issues” 설명이 현재 상태와 불일치

- 관련 파일: `AGENTS.md`, `scripts/validate_wiki.py`, `log.md`
- 관련 줄 또는 heading: `COMMANDS AND VALIDATION`, 최신 lint
- 문제 주장: repository-local executable checker가 없고 최신 lint는 0 issues다.
- 실제 근거: 현재 `scripts/validate_wiki.py`와 tests가 존재한다. 실제 실행은
  error 0이지만 warning 4다.
- 판정: **PARTIALLY_SUPPORTED**
- 영향: 후속 auditor가 validator 존재와 warning 정책을 잘못 이해할 수 있다.
- 수정 방향: “build/CI는 없지만 validator script는 있음”으로 설명하고
  `0 errors, 4 warnings, PASS`처럼 결과를 분리한다.
- 확신도: 높음

## Claim-level 사실 감사

| ID | 문서 | 주장 | 분류 | Source | Version/Commit | 근거 위치 | 판정 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q01 | workflow-contracts | 전체 planning/story 경로와 Quick Flow에 dev-auto가 존재 | DIRECT_FACT | workflow map | v6.10.0 / `081e64e` | raw workflow-map 38–61 | SUPPORTED |
| Q02 | workflow-contracts | PRD가 Create/Update/Validate와 세 산출물을 제공 | DIRECT_FACT | planning map, PRD excerpt | v6.10.0 | planning map 28–35; PRD 15–43 | SUPPORTED |
| Q03 | workflow-contracts | PRD Coaching 및 최종 검토 gate | DIRECT_FACT | PRD excerpt | v6.10.0 | 저장 excerpt 경계 밖 | PARTIALLY_SUPPORTED |
| Q04 | workflow-contracts | UX는 DESIGN/EXPERIENCE/memlog를 만들고 source 선택을 확인 | DIRECT_FACT | UX excerpt | v6.10.0 | raw 15–43 | SUPPORTED |
| Q05 | workflow-contracts | Architecture는 여러 형태의 입력과 parent-spine 상속을 지원 | DIRECT_FACT | architecture excerpt | v6.10.0 | raw 15–19 | SUPPORTED |
| Q06 | workflow-contracts | Epics에는 PRD·Architecture와 조건부 UX가 필요하며 epics.md 출력 | DIRECT_FACT | epics excerpt | v6.10.0 | raw 15–50 | SUPPORTED |
| Q07 | workflow-contracts | Readiness는 PRD/Architecture/Epics/UX와 중복 선택 gate를 사용 | DIRECT_FACT | readiness excerpt | v6.10.0 | raw 16–82 | SUPPORTED |
| Q08 | workflow-contracts | create-story는 story 선택/Epic을 입력으로 story ready-for-dev 출력 | DIRECT_FACT | create-story excerpts | v6.10.0 | raw input 15–32; handoff 15–49 | PARTIALLY_SUPPORTED |
| Q09 | workflow-contracts | dev-story는 ready-for-dev를 받아 DoD 후 review로 전환 | DIRECT_FACT | dev-story gates | v6.10.0 | raw 15–96 | PARTIALLY_SUPPORTED |
| Q10 | workflow-contracts | code-review는 diff/story를 받고 done 또는 in-progress로 전환 | DIRECT_FACT | review gates | v6.10.0 | raw 15–104 | PARTIALLY_SUPPORTED |
| Q11 | workflow-contracts | dev-auto는 intent/spec을 받아 상태 기반 resume와 local commit을 수행 | DIRECT_FACT | dev-auto reference | v6.10.0 | raw 19–170 | SUPPORTED |
| Q12 | workflow-contracts | 고위험·cross-repo 작업은 무인 workflow에 넘기지 말아야 함 | RECOMMENDATION | 종합 | v6.10.0 | canonical 115–123 | SUPPORTED |
| A01 | automation-gates | pinned tag에 bmad-dev-auto가 공식 존재 | DIRECT_FACT | Release, workflow map | v6.10.0 | Release 13–26 | SUPPORTED |
| A02 | automation-gates | bmad-loop는 opt-in deterministic orchestrator | DIRECT_FACT | Release, registry | v6.10.0 | registry 15–38 | SUPPORTED |
| A03 | automation-gates | bmad-automator는 deprecated | DIRECT_FACT | Release, registry | v6.10.0 | registry 62–73 | SUPPORTED |
| A04 | automation-gates | bmad-build-auto exact name은 pinned tag에서 없음 | REPRODUCED_FACT | name-search experiment | v6.10.0 | experiment 15–34 | SUPPORTED |
| A05 | automation-gates | bmad-build-auto가 다른 버전/fork일 수 있음 | INFERENCE | bounded search | tag vs current main | canonical 58–67 | VERSION_MISMATCH |
| A06 | automation-gates | dev-auto review는 patch 자동수정, bad-spec 재구현, 5회 초과 blocked | DIRECT_FACT | dev-auto review | v6.10.0 | raw 77–107 | SUPPORTED |
| A07 | automation-gates | dirty worktree는 조건에 따라 허용 가능 | RECOMMENDATION | dev-auto reference | v6.10.0 | raw 27–32 | PARTIALLY_SUPPORTED |
| A08 | automation-gates | merge/deploy와 반복 한도에 별도 사람 gate를 둬야 함 | RECOMMENDATION | 위키 정책 | v6.10.0 | canonical 107–114 | SUPPORTED |
| M01 | MSA-boundaries | BMAD가 monolith/monorepo/multi-part를 탐지하고 part 확인을 요청 | DIRECT_FACT | multipart detection | v6.10.0 | raw 18–35 | SUPPORTED |
| M02 | MSA-boundaries | integration architecture와 part별 architecture를 생성 | DIRECT_FACT | multipart output | v6.10.0 | raw 15–63 | SUPPORTED |
| M03 | MSA-boundaries | 공식 multi-repository coordination contract가 없다 | INFERENCE | bounded official source set | v6.10.0 | canonical 31–41 | NOT_VERIFIABLE |
| M04 | MSA-boundaries | parent spine의 decision은 child에서 read-only constraint | DIRECT_FACT | architecture excerpt | v6.10.0 | raw 17–19 | SUPPORTED |
| M05 | MSA-boundaries | 제품 문서와 repository-local 문서를 계층적으로 분리해야 함 | RECOMMENDATION | hierarchy 적용 추론 | v6.10.0 | canonical 64–86 | PARTIALLY_SUPPORTED |
| M06 | MSA-boundaries | cross-repo contract/E2E 및 owner 승인을 완료 gate로 둠 | RECOMMENDATION | 위키 정책 | v6.10.0 | canonical 94–114 | PARTIALLY_SUPPORTED |

## BMAD 핵심 판정

| 검증 항목 | 판정 |
| --- | --- |
| 실제 조사 버전 | `v6.10.0` tag/`081e64e…`로 정확히 고정됨 |
| create-story 명칭 | 해당 tag에서 확인됨 |
| create-story 고정/선택 입력 | 공식 전체 파일에서는 확인되나 저장 raw excerpt는 일부 부족 |
| create-story 출력 | story file, `ready-for-dev` 확인됨 |
| dev와 review 관계 | 공식적으로 별도 skill이며 권장 순서로 연결됨; 단일 일반 workflow는 아님 |
| review 실패 후 dev 재실행 | 일반 story chain의 공식 자동 동작으로 확인되지 않음; dev-auto의 `bad_spec` loopback만 공식 |
| `bmad-build-auto` | pinned tag에서는 미확인; 최신 공식 main에서 확인됨 |
| `bmad-loop` | v6.10.0 tag와 별도 공식 repo/module에서 확인됨 |
| 다른 fork/plugin 유래 가능성 | `bmad-loop`는 공식 별도 module; `bmad-build-auto`는 최신 공식 main, fork 가설 불필요 |
| MSA/multi-repository | multi-part는 공식; cross-repository ownership 모델은 작성자 권고 |
| Human Approval Gate | code-review HALT는 공식; merge/deploy/retry/owner gate는 작성자 추가 통제 |

## Confidence 감사

- `workflow-contracts: medium`: 적정하거나 보수적이다. 다수 공식 근거가 있으나
  실제 실행 실험이 없다.
- `automation-and-human-gates: medium`: 적정하다. 공식 기능은 강하지만 권고와
  bounded absence가 섞여 있다.
- `msa-multi-repository-boundaries: low`: 적정하다. 핵심 multi-repository
  모델이 명시적으로 추론이다.
- 과도한 page-level confidence는 발견하지 못했다.

## 의사결정 유용성 테스트

| Scenario | 위키만으로 가능한 답 | 빠진 핵심 | 판정 |
| --- | --- | --- | --- |
| A | 일반 경로는 create-story → dev-story → code-review이고, 별도 orchestrator가 retry limit와 human escalation을 관리해야 한다. dev-auto/loop는 별도 spec 기반 무인 모델이다. | 일반 chain의 공식 재실행 계약, retry 상태 machine, 구체적인 중단 횟수 | **FAIL** |
| B | 제품 PRD/parent spine/integration Epic은 공통 결과·NFR·interface를 소유하고, repository별 spine/story는 local 결정·code/test/rollback을 소유한다. owner와 E2E gate를 둔다. | 공식 multi-repository contract가 아니라 low-confidence 권고라는 한계 | **PASS** |
| C | multi-part inventory와 architecture 문서 생성 정도만 답할 수 있다. | Java/Controller input, endpoint/dependency 산출물, story 변환 순서 전부 | **FAIL** |

Scenario A는 output·version·근거·권장 Human Gate는 있으나 공식 orchestration과
필수/선택 input이 불완전하다. Scenario B는 모든 요소를 제공하지만 공식 기능과
추론을 구분해야 한다. Scenario C는 추가 공식 자료 검색이 필수이므로 의사결정
유용성 실패다.

## 최종 결과

| 검증 영역 | 결과 | P0 | P1 | P2 |
| --- | --- | ---: | ---: | ---: |
| 저장소 구조 | FAIL | 0 | 0 | 1 |
| Raw 무결성 | FAIL | 2 | 0 | 0 |
| Source 추적성 | FAIL | 0 | 1 | 0 |
| 사실 정확성 | FAIL | 0 | 1 | 1 |
| Version 일관성 | FAIL | 0 | 1 | 0 |
| Confidence 적정성 | PASS | 0 | 0 | 0 |
| 의사결정 유용성 | FAIL | 0 | 0 | 2 |
| 개인정보 안전성 | PASS | 0 | 0 | 0 |

**최종 판정: REWORK_REQUIRED**
