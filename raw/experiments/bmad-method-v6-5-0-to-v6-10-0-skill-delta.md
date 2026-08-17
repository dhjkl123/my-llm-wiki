---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/compare/v6.5.0...v6.10.0"
source_type: synthetic-experiment
ingested: 2026-08-17
retrieved_at: "2026-08-17T15:11:24+09:00"
repository: bmad-code-org/BMAD-METHOD
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
sha256: dcc0c299a1992e13bd2d84d7f38f82ee05ccb560d492d4638b4e3774b665c647
---
# BMAD v6.5.0 to v6.10.0 BMM/Core skill delta

## 목적

두 공식 stable tag의 BMM/Core skill root 전체를 재귀 Git tree ID로 비교한다.
동일 경로와 동일 tree ID는 불변으로 판정하고, 변경·추가·제거된 root만 후속 의미 검토 대상으로 삼는다.

## 재현 범위

- From: v6.5.0 / 69cbeb4d07f318180c3d610c511381b9f494e786
- To: v6.10.0 / 081e64ee5aab2316b912883f7bee528ee143ce36
- Repository: bmad-code-org/BMAD-METHOD
- Compared paths: src/bmm-skills and src/core-skills
- Comparison date: 2026-08-17

## 절차

1. 각 commit에서 git ls-tree -r --name-only 로 두 module의 모든 /SKILL.md 경로를 정렬한다.
2. 각 SKILL.md 부모 root에 git rev-parse commit:path 를 실행해 재귀 tree ID를 얻는다.
3. exact path를 기준으로 unchanged, changed, added, removed를 분리한다.
4. Tree ID는 root 아래 SKILL.md, reference, step, template, script와 configuration을 모두 반영한다.
5. Tree 차이는 의미 변경 후보일 뿐이다. 공식 manifest, release와 변경 파일을 읽어 canonical 영향 여부를 별도로 판정한다.

## 요약

| Metric | Count |
| --- | ---: |
| From roots | 42 |
| To roots | 46 |
| Exact-path unchanged | 4 |
| Exact-path changed | 36 |
| Added paths | 6 |
| Removed paths | 2 |

| Scope | From tree OID | To tree OID |
| --- | --- | --- |
| BMM | bde383035df88f2e252e83dc76af7acfe39aeed1 | 35d38ee00128d3de3a60b28786e7ba2b3937f8d2 |
| Core | dc5d00bf44f96271fee315555838c884a56ac89f | cc8d11e8293a51568f892808321294c4a6cddb7d |

## Exact-path unchanged

| Module | Skill root | Tree OID | Files |
| --- | --- | --- | ---: |
| core | src/core-skills/bmad-editorial-review-prose | 469701beb9f839fd05a162aa46c44359d85883e8 | 1 |
| core | src/core-skills/bmad-editorial-review-structure | fc1e08380fe47071e98b4803794d27dd667086d6 | 1 |
| core | src/core-skills/bmad-index-docs | d07c0e4ada9517bd0ef5f05cab831ebdbfaf688a | 1 |
| core | src/core-skills/bmad-shard-doc | cbfb01b74874522fa896a08ec90ffef4cf12a167 | 1 |

## Exact-path changed

| Module | Skill root | From tree | To tree | Files |
| --- | --- | --- | --- | ---: |
| bmm | src/bmm-skills/1-analysis/bmad-agent-analyst | 3791ce4105d59811ce2cd7448b6d825561049b31 | 212ad5356ba50c0d704431255a65b17076d8f463 | 2 to 2 |
| bmm | src/bmm-skills/1-analysis/bmad-agent-tech-writer | 93f02696232623cac6f16571562340773cd57884 | 84827885245795fba974af166dcbdfd2de628ace | 6 to 6 |
| bmm | src/bmm-skills/1-analysis/bmad-document-project | a16e6cfe19c275f7993ccbe6e73f8a675c0dad31 | 3ef40f197a272fd08d9f64d29ca3a668cbdaa8a7 | 14 to 14 |
| bmm | src/bmm-skills/1-analysis/bmad-prfaq | edf3f0e9296524ab9fd24c161bf986a1d5f592ff | 07447e2d579c8a99ebeee27ab7c90288836e7c86 | 10 to 10 |
| bmm | src/bmm-skills/1-analysis/bmad-product-brief | cbcf2b7b010a0a1429d452960d6f202d977e13ac | 576ce3a8a87f54d46c0a626d91f5a61700381702 | 12 to 3 |
| bmm | src/bmm-skills/1-analysis/research/bmad-domain-research | d475d7cf5b392da25dc53bf235775cacd8d0b6a3 | bb0a561350e6c5fe315a86940a0ba7c9a131f9ce | 9 to 9 |
| bmm | src/bmm-skills/1-analysis/research/bmad-market-research | b74cc105585ac333793fe328741dc48a79912105 | feea06514fdcf58890d8f5bcd11bf45f4bc1dfe8 | 9 to 9 |
| bmm | src/bmm-skills/1-analysis/research/bmad-technical-research | 0da03a524a6ca0b64ac2ee295395106d0c29f505 | b37352301fc61ee912ddf768cf4e28b0ea045fba | 9 to 9 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-agent-pm | 474b050b7675cb45ec958143f651e4f6e2a4bbeb | 25d42633d02f0abffde1c0d7f9316e2ec9b62244 | 2 to 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-agent-ux-designer | 526642b021827d72180b7ee50e431da876b6a2bd | 1e13cc4815ef627f7631221d32db8d541ee35f9b | 2 to 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-create-prd | e418ca9ec2161a105fbb9205846fcff778020f1d | c60551add8a685464e29594d150559649e935861 | 21 to 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-edit-prd | 060afc8190aa807dc5db8f8bd95b9e76f891eaf9 | 5bbc49252266b8ce6c4850ba0319849216a1e626 | 8 to 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-validate-prd | c45605997c4f8e94e6fde8a9a7789506f2eec6a1 | 5bc60bf988a8982b985277eb16e21f48f573dfe1 | 19 to 2 |
| bmm | src/bmm-skills/3-solutioning/bmad-agent-architect | 82f7d2e148bcb5188eea5ef44459ffa05ddd3827 | 0f3bbc79c422d9dabddd23da260517aa4b41fdf2 | 2 to 2 |
| bmm | src/bmm-skills/3-solutioning/bmad-check-implementation-readiness | 93b9b1fba6ff3bddd2060b63fb0e470a7d402689 | 644e59fe90e0817d9ccbcf7df6a605896cd8072f | 9 to 9 |
| bmm | src/bmm-skills/3-solutioning/bmad-create-architecture | 2034f020e1d18a3cd7aec29c5d1607f2957e8dc6 | 916a1a438610759d3d73851c40122762fbcb2e24 | 14 to 2 |
| bmm | src/bmm-skills/3-solutioning/bmad-create-epics-and-stories | d3bcf6e97655ab69e7b0e461d10d3f9df47e9be4 | 96b14cb6971ba3894db64e5d20cdb1c6b7b48d4f | 7 to 7 |
| bmm | src/bmm-skills/3-solutioning/bmad-generate-project-context | 7a2557187d1b3af1ef1e8b7bf0f810c7cf701f20 | 42f512ada2620d34fed0abe29e373b0f54dec909 | 6 to 6 |
| bmm | src/bmm-skills/4-implementation/bmad-agent-dev | 3781208250fcc417ef7ca26a6675d4e8446043e6 | 07ba9c863f28a4b9933abb09bc27978169c1c0c5 | 2 to 2 |
| bmm | src/bmm-skills/4-implementation/bmad-checkpoint-preview | a59a59f4d72fc5fdbb44c0fbc25a2a5f524673b2 | 5a9c703a12e38e32f8e97fc9930c3f4934ca1cd4 | 8 to 8 |
| bmm | src/bmm-skills/4-implementation/bmad-code-review | a53020160b6c3adef8a9960c8b067facc994b29f | 2f7bd82aad5d85b5407b586f73fb90b086d6558e | 6 to 6 |
| bmm | src/bmm-skills/4-implementation/bmad-correct-course | 001f5ff85eafd40971237bde5e1f6bbcea493a85 | 391ecad5cd563cd7c2e8f0ec41d1ab9603a4b2b6 | 3 to 3 |
| bmm | src/bmm-skills/4-implementation/bmad-create-story | 884aca08c37d0b459cfa4786a949d2b9644a452c | cfcdedfe2a150d00c82428b8ad3ae90af914cf96 | 5 to 5 |
| bmm | src/bmm-skills/4-implementation/bmad-dev-story | b52ec1084ab85f258f23f50d68c4fef479b63daa | b920a0e57139949eacd8bbb1de97c2eeb0196fed | 3 to 3 |
| bmm | src/bmm-skills/4-implementation/bmad-qa-generate-e2e-tests | d7166195ce8ea00a34e30f54c2c21042a56831d2 | 7d2aeab849f07d3970cdf1a7956afab8f093c9a9 | 3 to 3 |
| bmm | src/bmm-skills/4-implementation/bmad-quick-dev | 20cff8cb8c1451e3a281d5dc96320731d9a625c3 | db0a08df6d10189e38a029caf0da63457cc8e042 | 11 to 11 |
| bmm | src/bmm-skills/4-implementation/bmad-retrospective | bfb3dbf6bb8217e3fd9627d4d4af88dda3ea4a51 | 6d27515bdaa79a7c003542c857859131503f7b17 | 2 to 2 |
| bmm | src/bmm-skills/4-implementation/bmad-sprint-planning | ca45016302528fca8adec622be229c9be4f507c2 | 2bf38d02553807f36149b876defa6b8feb11aaad | 4 to 4 |
| bmm | src/bmm-skills/4-implementation/bmad-sprint-status | cc1095b759fa5a489c565f10631f3d7a8d559bc2 | e2367fd2203292ad3817d757b2d6c975ec490140 | 2 to 2 |
| core | src/core-skills/bmad-advanced-elicitation | cef4498b4e354775b190d80c53dea01ce212c7b1 | a4394f3e54e1fbd3add81115b8a8a45b67f17f20 | 2 to 2 |
| core | src/core-skills/bmad-brainstorming | b1f3890c3c89268bf15ae96b9b041c1ac24f1d9e | 6af260260b36c9e41a3d228a61aa136bd0ad4765 | 12 to 17 |
| core | src/core-skills/bmad-customize | a66c1812242c6a332732edce7d75865c8817dcb6 | 6387e0a0df6b38fa23b80d4e3ec159f48e4ae5fe | 3 to 3 |
| core | src/core-skills/bmad-help | c5475eb36fde9da40e0c5e4920b4e1182d961922 | 4da58d85244f9b952a0d7d43f19d80f3d1032675 | 1 to 1 |
| core | src/core-skills/bmad-party-mode | 9da9eadc8c94c557a83c6a1890985ba345538709 | 736b0149357d9ae6f4b69aa27a8450f23fd73e03 | 1 to 9 |
| core | src/core-skills/bmad-review-adversarial-general | 983a7e5a971ba7e32d01b87621ab00a4ab3fbbbe | 2fc6d859f4fa69216dc72d6a295d0215011ba8be | 1 to 1 |
| core | src/core-skills/bmad-review-edge-case-hunter | 0219757c68f49d62ed35e4c3f8a951071ec43d87 | 5b472e614eaac181e8bac5dd5a5c9eacaf01eaf8 | 1 to 2 |

## Added paths

| Module | Skill root | Tree OID | Files |
| --- | --- | --- | ---: |
| bmm | src/bmm-skills/2-plan-workflows/bmad-prd | f3dacf02d671cbea03104ab0cf27653811c42600 | 8 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-ux | 3f3abe65b5853c4d209f8d934fe3adddd7a566c1 | 17 |
| bmm | src/bmm-skills/3-solutioning/bmad-architecture | 402b1adbc4aee309b8fcfe14d56055c5d3990a78 | 7 |
| bmm | src/bmm-skills/4-implementation/bmad-dev-auto | e514af61c3eacd7c99e6da3df581725457764757 | 8 |
| core | src/core-skills/bmad-forge-idea | b0319cd94977d4577b1e5d1e711962c10c6dd5de | 4 |
| core | src/core-skills/bmad-spec | ed1f7c24d848d493ac131064392e8ef7cc86615e | 4 |

## Removed paths

| Module | Skill root | Tree OID | Files |
| --- | --- | --- | ---: |
| bmm | src/bmm-skills/2-plan-workflows/bmad-create-ux-design | 5a5841efe90bbc4bdb2fe343c159a01764ae1ecb | 18 |
| core | src/core-skills/bmad-distillator | 24ba71c4befc3d4caf7f261ee5c0fdd44e7d0945 | 8 |

## 판정 한계

- 경로 이동과 내용 변경이 동시에 일어나면 exact-path 비교에서는 remove와 add로 나타난다.
- 같은 basename이나 유사 content를 rename으로 확정하려면 manifest, release와 Git diff를 함께 확인해야 한다.
- 이 기록은 정적 source delta이며 실제 installer와 runtime을 실행하지 않았다.
