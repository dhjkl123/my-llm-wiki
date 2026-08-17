# 초기 Research Backlog

## 프로젝트 목적

공개된 공식 문서, 공식 GitHub 저장소와 릴리스, 공식 예제, 공개 이슈,
재현 가능한 synthetic 실험을 근거로 개발자가 프로젝트 상황에 맞는 AIDD
산출물 구조, 코딩 에이전트 workflow, 자동화 범위와 사람 승인 지점을 선택할
수 있도록 반복 사용 가능한 판단 근거를 축적한다.

## 포함 범위

- 요구사항에서 구현·리뷰까지 이어지는 산출물 흐름
- workflow 또는 skill의 필수 입력, 선택 입력, 출력 계약
- 자동화 단위와 Human Approval Gate
- 개발, 리뷰, 테스트 품질 게이트와 실패 조건
- 버전별 변경과 공식 설명·재현 결과 사이의 차이
- MSA, multi-repository, brownfield 프로젝트의 문서 경계

## 제외 범위

- 일반 LLM 이론, 모델 성능 및 AI 업계 뉴스
- 프롬프트 수집이나 모든 코딩 에이전트 기능의 백과사전식 나열
- 출처 없는 추천, 검색 snippet, 비공개 자료와 내부 업무 기록
- 현재 AIDD workflow 의사결정에 직접 쓰이지 않는 도구 소개

## 초기 사용자

- 코딩 에이전트를 개발 프로세스에 도입하려는 개발자
- 백엔드 및 플랫폼 엔지니어
- PL, BA, Tech Lead
- AIDD 방법론 또는 개발 표준 설계 담당자

## 버전 해석

현재 확인 대상은 공식 tag `v6.11.0`과 commit
`9ce3c397c9b238de96f7365da8019f6f66b059da`이다. 이전 `v6.1.0`과
`v6.10.0` 수집물 및 canonical page는 버전 비교 이력으로 보존하며 현재 판단과
한정 없이 섞지 않는다.

## 우선 조사 항목

| 우선순위 | 질문 | 반복 사용 가치 | 필요한 근거 | 완료 조건 | 상태 | canonical 승격 후보 |
| --- | --- | --- | --- | --- | --- | --- |
| P0 | v6.11.0 Planning, Solutioning, Implementation의 artifact와 workflow 흐름은 무엇인가? | 새 프로젝트와 brownfield 프로젝트 모두에서 선행 문서와 handoff 누락을 줄인다. | tag 고정 workflow map, workflow/step 파일, template | 주요 workflow별 필수·선택 입력, 출력, 실패·정지 조건 표 작성 | 1차 완료 | workflow contract query |
| P0 | `create-story` 이후 dev와 review를 연속 자동화하는 공식 workflow/skill이 있는가? | unattended 실행 범위와 orchestration 추가 필요성을 결정한다. | tag 전체 manifest/path/본문 검색, 공식 release note | 공식 명칭·책임 범위 확인 또는 부재 범위와 검색식을 기록 | 1차 완료 | automation comparison |
| P0 | Story, Dev, Review 사이의 Human Approval Gate는 어디인가? | 품질 책임과 비가역 변경 승인 지점을 설계한다. | workflow의 ASK/HALT/menu/status 전이, checklist | 공식 강제 gate와 운영상 권장 gate를 분리 | 1차 완료 | gate decision guide |
| P1 | `bmad-build-auto`, `bmad-loop` 또는 유사 명칭은 어느 버전에 존재하는가? | 공식 명칭과 fork·과거 명칭을 혼동하지 않게 한다. | tag별 manifest, release, commit history | 존재 명칭의 책임 범위와 미확인 명칭의 검색 범위 기록 | v6.11.0 tag에서 build-auto 정식화, dev-auto는 v6 shim으로 확인 | version comparison |
| P1 | BMM/Core skill catalog와 실행 계약은 stable version 사이에서 어떻게 바뀌는가? | 전체 파일을 반복 수집하지 않고 실제 변경만 추적한다. | tag별 module manifest, help catalog, skill-root Git tree ID와 변경 파일 | v6.5.0 기준선 이후 동일 tree는 무변경, 다른 tree만 의미 검토 및 delta 수집 | v6.5.0→v6.10.0→v6.11.0 delta 완료 | skill catalog comparison |
| P1 | MSA 또는 multi-repository에서 제품 문서와 서비스 문서 경계를 어떻게 둘 것인가? | 중복 요구사항과 교차 저장소 변경의 책임 공백을 줄인다. | document-project, architecture, story input discovery, synthetic experiment | 공식 지원 범위와 wiki의 추론 모델을 분리하고 적용·비적용 조건 정의 | 1차 가설 | boundary decision guide |
| P1 | Brownfield에서 기존 시스템 문서를 어떤 입력으로 승격할 것인가? | 새 설계가 현재 동작을 덮어쓰거나 추측하는 위험을 줄인다. | document-project, PRD initialization, create-story discovery | 문서화→PRD→architecture/story 흐름과 재검증 조건 정의 | 조사 중 | brownfield workflow concept |

## 공통 완료 조건

- 모든 현재 사실은 `v6.11.0` tag 또는 full commit SHA에 고정한다.
- BMM/Core skill 버전 비교는 v6.5.0 inventory의 재귀 tree ID를 기준으로 하며,
  동일한 skill tree는 raw와 canonical을 중복 갱신하지 않는다.
- 검색 결과 snippet이 아니라 raw로 보존한 공식 본문 또는 재현 실험을 인용한다.
- 필수 입력, 선택 입력, 출력, 상태 전이, HALT 조건을 구분한다.
- 공식 강제 동작과 이 위키가 제안하는 운영 정책을 명시적으로 분리한다.
- 확인되지 않은 기능은 “확인되지 않음”, 가능한 다른 버전/fork, 추가 확인
  대상, `confidence: low`를 함께 기록한다.
- canonical 승격 시 적용 조건, 비적용 조건, 버전·freshness 정보를 포함한다.

## 개인정보 및 내부정보 금지

회사 내부 문서, 사내 방법론, 고객·프로젝트·조직 식별 정보, 비공개 코드,
개인정보, 인증 정보와 업무 기록을 수집하지 않는다. 업무와 유사한 검증이
필요하면 가상 제품과 synthetic 요구사항만 사용한다.
