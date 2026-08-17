---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/tree/69cbeb4d07f318180c3d610c511381b9f494e786"
source_type: synthetic-experiment
ingested: 2026-08-17
retrieved_at: "2026-08-17T15:03:08+09:00"
repository: bmad-code-org/BMAD-METHOD
version: 6.5.0
tag: v6.5.0
commit_sha: 69cbeb4d07f318180c3d610c511381b9f494e786
license: MIT
sha256: 020978f0a85ac5981d0411b86f92d17747948abb736bb1ba0a622f9bc2e87a9c
---
# BMAD v6.5.0 BMM/Core skill inventory baseline

## 목적

이 기록은 v6.5.0의 BMM/Core 설치 소스에서 모든 SKILL.md를 찾고,
각 skill 디렉터리 전체의 Git tree object ID를 기준선으로 고정한다. 이후 버전은
같은 경로와 tree ID가 모두 같으면 재수집하지 않고, 차이가 있는 skill만 조사한다.

## 재현 환경

- Repository: bmad-code-org/BMAD-METHOD
- Tag: v6.5.0
- Commit: 69cbeb4d07f318180c3d610c511381b9f494e786
- Git object database from the public official repository
- Inventory date: 2026-08-17

## 절차

1. git ls-tree -r --name-only 69cbeb4d07f318180c3d610c511381b9f494e786 -- src/bmm-skills src/core-skills 로 파일 목록을 얻는다.
2. 경로가 /SKILL.md로 끝나는 항목을 정렬하고 그 부모 디렉터리를 skill root로 정한다.
3. 각 root에 git rev-parse 69cbeb4d07f318180c3d610c511381b9f494e786:경로 를 실행해 재귀 tree ID를 기록한다.
4. git ls-tree -r --name-only 69cbeb4d07f318180c3d610c511381b9f494e786:경로 의 행 수를 파일 수로 기록한다.
5. 다음 버전에서는 module scope tree가 다를 때만 skill 경로별 tree ID를 비교한다. 동일 경로와 동일 tree ID는 내용 불변으로 판정해 raw와 canonical을 갱신하지 않는다.

## 범위 결과

| Module | Scope tree OID | Skill count |
| --- | --- | ---: |
| BMM | bde383035df88f2e252e83dc76af7acfe39aeed1 | 30 |
| Core | dc5d00bf44f96271fee315555838c884a56ac89f | 12 |

총 42개 skill root를 확인했다. Tree ID는 SKILL.md뿐 아니라 같은 root 아래의
reference, step, template, script와 configuration 파일까지 재귀적으로 반영한다.

## Skill fingerprints

| Module | Skill root | Git tree OID | Files |
| --- | --- | --- | ---: |
| bmm | src/bmm-skills/1-analysis/bmad-agent-analyst | 3791ce4105d59811ce2cd7448b6d825561049b31 | 2 |
| bmm | src/bmm-skills/1-analysis/bmad-agent-tech-writer | 93f02696232623cac6f16571562340773cd57884 | 6 |
| bmm | src/bmm-skills/1-analysis/bmad-document-project | a16e6cfe19c275f7993ccbe6e73f8a675c0dad31 | 14 |
| bmm | src/bmm-skills/1-analysis/bmad-prfaq | edf3f0e9296524ab9fd24c161bf986a1d5f592ff | 10 |
| bmm | src/bmm-skills/1-analysis/bmad-product-brief | cbcf2b7b010a0a1429d452960d6f202d977e13ac | 12 |
| bmm | src/bmm-skills/1-analysis/research/bmad-domain-research | d475d7cf5b392da25dc53bf235775cacd8d0b6a3 | 9 |
| bmm | src/bmm-skills/1-analysis/research/bmad-market-research | b74cc105585ac333793fe328741dc48a79912105 | 9 |
| bmm | src/bmm-skills/1-analysis/research/bmad-technical-research | 0da03a524a6ca0b64ac2ee295395106d0c29f505 | 9 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-agent-pm | 474b050b7675cb45ec958143f651e4f6e2a4bbeb | 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-agent-ux-designer | 526642b021827d72180b7ee50e431da876b6a2bd | 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-create-prd | e418ca9ec2161a105fbb9205846fcff778020f1d | 21 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-create-ux-design | 5a5841efe90bbc4bdb2fe343c159a01764ae1ecb | 18 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-edit-prd | 060afc8190aa807dc5db8f8bd95b9e76f891eaf9 | 8 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-validate-prd | c45605997c4f8e94e6fde8a9a7789506f2eec6a1 | 19 |
| bmm | src/bmm-skills/3-solutioning/bmad-agent-architect | 82f7d2e148bcb5188eea5ef44459ffa05ddd3827 | 2 |
| bmm | src/bmm-skills/3-solutioning/bmad-check-implementation-readiness | 93b9b1fba6ff3bddd2060b63fb0e470a7d402689 | 9 |
| bmm | src/bmm-skills/3-solutioning/bmad-create-architecture | 2034f020e1d18a3cd7aec29c5d1607f2957e8dc6 | 14 |
| bmm | src/bmm-skills/3-solutioning/bmad-create-epics-and-stories | d3bcf6e97655ab69e7b0e461d10d3f9df47e9be4 | 7 |
| bmm | src/bmm-skills/3-solutioning/bmad-generate-project-context | 7a2557187d1b3af1ef1e8b7bf0f810c7cf701f20 | 6 |
| bmm | src/bmm-skills/4-implementation/bmad-agent-dev | 3781208250fcc417ef7ca26a6675d4e8446043e6 | 2 |
| bmm | src/bmm-skills/4-implementation/bmad-checkpoint-preview | a59a59f4d72fc5fdbb44c0fbc25a2a5f524673b2 | 8 |
| bmm | src/bmm-skills/4-implementation/bmad-code-review | a53020160b6c3adef8a9960c8b067facc994b29f | 6 |
| bmm | src/bmm-skills/4-implementation/bmad-correct-course | 001f5ff85eafd40971237bde5e1f6bbcea493a85 | 3 |
| bmm | src/bmm-skills/4-implementation/bmad-create-story | 884aca08c37d0b459cfa4786a949d2b9644a452c | 5 |
| bmm | src/bmm-skills/4-implementation/bmad-dev-story | b52ec1084ab85f258f23f50d68c4fef479b63daa | 3 |
| bmm | src/bmm-skills/4-implementation/bmad-qa-generate-e2e-tests | d7166195ce8ea00a34e30f54c2c21042a56831d2 | 3 |
| bmm | src/bmm-skills/4-implementation/bmad-quick-dev | 20cff8cb8c1451e3a281d5dc96320731d9a625c3 | 11 |
| bmm | src/bmm-skills/4-implementation/bmad-retrospective | bfb3dbf6bb8217e3fd9627d4d4af88dda3ea4a51 | 2 |
| bmm | src/bmm-skills/4-implementation/bmad-sprint-planning | ca45016302528fca8adec622be229c9be4f507c2 | 4 |
| bmm | src/bmm-skills/4-implementation/bmad-sprint-status | cc1095b759fa5a489c565f10631f3d7a8d559bc2 | 2 |
| core | src/core-skills/bmad-advanced-elicitation | cef4498b4e354775b190d80c53dea01ce212c7b1 | 2 |
| core | src/core-skills/bmad-brainstorming | b1f3890c3c89268bf15ae96b9b041c1ac24f1d9e | 12 |
| core | src/core-skills/bmad-customize | a66c1812242c6a332732edce7d75865c8817dcb6 | 3 |
| core | src/core-skills/bmad-distillator | 24ba71c4befc3d4caf7f261ee5c0fdd44e7d0945 | 8 |
| core | src/core-skills/bmad-editorial-review-prose | 469701beb9f839fd05a162aa46c44359d85883e8 | 1 |
| core | src/core-skills/bmad-editorial-review-structure | fc1e08380fe47071e98b4803794d27dd667086d6 | 1 |
| core | src/core-skills/bmad-help | c5475eb36fde9da40e0c5e4920b4e1182d961922 | 1 |
| core | src/core-skills/bmad-index-docs | d07c0e4ada9517bd0ef5f05cab831ebdbfaf688a | 1 |
| core | src/core-skills/bmad-party-mode | 9da9eadc8c94c557a83c6a1890985ba345538709 | 1 |
| core | src/core-skills/bmad-review-adversarial-general | 983a7e5a971ba7e32d01b87621ab00a4ab3fbbbe | 1 |
| core | src/core-skills/bmad-review-edge-case-hunter | 0219757c68f49d62ed35e4c3f8a951071ec43d87 | 1 |
| core | src/core-skills/bmad-shard-doc | cbfb01b74874522fa896a08ec90ffef4cf12a167 | 1 |

## Delta 판정 규칙

- 동일 경로와 동일 tree ID: 불변. 새 raw record, canonical update, index/log update를 만들지 않는다.
- 동일 경로와 다른 tree ID: 변경. Git diff로 바뀐 파일과 실행 계약 영향을 확인한다.
- 경로 삭제 또는 추가: rename, consolidation, removal 또는 새 skill 후보로 조사한다.
- registry만 변경: 설치, 노출, 필수 여부가 달라질 수 있으므로 manifest delta를 별도로 수집한다.
- 번역과 사이트 문서만 바뀌고 설치 skill tree와 registry가 같으면 canonical을 갱신하지 않는다.

## 한계

- Tree ID 차이는 변경 존재를 증명하지만 의미 변화의 크기는 별도 diff 검토가 필요하다.
- Git rename similarity는 이 inventory가 직접 판정하지 않는다. 삭제와 추가 쌍을 발견한 뒤 공식 release와 diff로 확인한다.
- 이 기준선은 저장소 정적 내용이며 실제 installer 실행이나 agent runtime 동작을 검증하지 않았다.
