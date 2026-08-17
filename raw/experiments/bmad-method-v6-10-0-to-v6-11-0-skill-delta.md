---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/compare/v6.10.0...v6.11.0"
source_type: synthetic-experiment
ingested: 2026-08-17
retrieved_at: "2026-08-17T15:11:24+09:00"
repository: bmad-code-org/BMAD-METHOD
version: 6.11.0
tag: v6.11.0
commit_sha: 9ce3c397c9b238de96f7365da8019f6f66b059da
license: MIT
sha256: 8c968dc2da7df3e2e24569bd0e1fe4ce77bea4ac729000fbb49819a96fdcc0b3
---
# BMAD v6.10.0 to v6.11.0 BMM/Core skill delta

## 목적

두 공식 stable tag의 BMM/Core skill root 전체를 재귀 Git tree ID로 비교한다.
동일 경로와 동일 tree ID는 불변으로 판정하고, 변경·추가·제거된 root만 후속 의미 검토 대상으로 삼는다.

## 재현 범위

- From: v6.10.0 / 081e64ee5aab2316b912883f7bee528ee143ce36
- To: v6.11.0 / 9ce3c397c9b238de96f7365da8019f6f66b059da
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
| From roots | 46 |
| To roots | 49 |
| Exact-path unchanged | 0 |
| Exact-path changed | 6 |
| Added paths | 43 |
| Removed paths | 40 |

| Scope | From tree OID | To tree OID |
| --- | --- | --- |
| BMM | 35d38ee00128d3de3a60b28786e7ba2b3937f8d2 | de6bfcdba0c38dfaefeaa5d2058e446d365c88a6 |
| Core | cc8d11e8293a51568f892808321294c4a6cddb7d | 072bf56654e611e799b409fec1645068cc45ef7e |

## Exact-path unchanged

| Module | Skill root | Tree OID | Files |
| --- | --- | --- | ---: |

## Exact-path changed

| Module | Skill root | From tree | To tree | Files |
| --- | --- | --- | --- | ---: |
| core | src/core-skills/bmad-advanced-elicitation | a4394f3e54e1fbd3add81115b8a8a45b67f17f20 | 235ccd1af2eafe1a92b7ee4663190c139f587b1e | 2 to 5 |
| core | src/core-skills/bmad-brainstorming | 6af260260b36c9e41a3d228a61aa136bd0ad4765 | 92de8d822ead8c63f8a9b64e2081518dac4a121d | 17 to 15 |
| core | src/core-skills/bmad-customize | 6387e0a0df6b38fa23b80d4e3ec159f48e4ae5fe | 474bd07ffc2bc031a0f3b7546486592f5e32664a | 3 to 3 |
| core | src/core-skills/bmad-forge-idea | b0319cd94977d4577b1e5d1e711962c10c6dd5de | 4058a868f0c648e5547633e29422e549888c435f | 4 to 4 |
| core | src/core-skills/bmad-help | 4da58d85244f9b952a0d7d43f19d80f3d1032675 | 216de2faddbea8cd7c30dc7ca2cdc18ed6f808c3 | 1 to 1 |
| core | src/core-skills/bmad-party-mode | 736b0149357d9ae6f4b69aa27a8450f23fd73e03 | d40571ffb25dbe00550f3b3479d0cca6d368cc9c | 9 to 9 |

## Added paths

| Module | Skill root | Tree OID | Files |
| --- | --- | --- | ---: |
| bmm | src/bmm-skills/agents/bmad-agent-analyst | d56469835d01aa686e4e7fd4ec0c76a1e3f0dcb3 | 2 |
| bmm | src/bmm-skills/agents/bmad-agent-architect | b672ef0d2b6d95b4118b87cb2aa40419d6641aa0 | 2 |
| bmm | src/bmm-skills/agents/bmad-agent-dev | 7f144ce1a11b7936133c9d01f984deb831613dfc | 2 |
| bmm | src/bmm-skills/agents/bmad-agent-pm | 2470130f0d359746e9d66a64f81743807b31d4d2 | 2 |
| bmm | src/bmm-skills/agents/bmad-agent-ux-designer | f5a70764e232f0474956dae9ecd72440bb461b34 | 2 |
| bmm | src/bmm-skills/plan/bmad-architecture | 82d89983ec7fa595b8a879345807925e094b97db | 7 |
| bmm | src/bmm-skills/plan/bmad-create-epics-and-stories | bbca622adc6185affd14307b58a54c2d4850051a | 7 |
| bmm | src/bmm-skills/plan/bmad-generate-project-context | ffa9993fdbfa56b167318b64283294a33dac6ad1 | 1 |
| bmm | src/bmm-skills/plan/bmad-prd | 1f309956004f6adaa19af9bcdc36511677cdef10 | 8 |
| bmm | src/bmm-skills/plan/bmad-prfaq | 67a13e56c211c1d38b9bc4404c2dab6807317f60 | 10 |
| bmm | src/bmm-skills/plan/bmad-product-brief | 597854ccbcceae5c9ed842f5e84398ac7e54e917 | 3 |
| bmm | src/bmm-skills/plan/bmad-project-context | 4924ae93e5918ad61d14028f18ea836aee43ca8c | 4 |
| bmm | src/bmm-skills/plan/bmad-spec | 94d9f1d87432d586a842900c78c5a5f65362f6bf | 5 |
| bmm | src/bmm-skills/plan/bmad-sprint-planning | 14f39a7d6fdfb8c11e6cf202d67f3ffedef652c0 | 10 |
| bmm | src/bmm-skills/plan/bmad-ux | a3a482c57883adcbfed74ab254e8c2784a7967b4 | 17 |
| bmm | src/bmm-skills/ship/bmad-build | 8b550869cfe5be9ef858479c9dc21cb7f2d5802c | 15 |
| bmm | src/bmm-skills/ship/bmad-build-auto | 4566a8d5dcceaa7477b7bd9bad5982549d45c22b | 12 |
| bmm | src/bmm-skills/ship/bmad-checkpoint-preview | e12f0ed1cc0f7b1badea37093cf38d192b519870 | 8 |
| bmm | src/bmm-skills/ship/bmad-code-review | ab59b59b8e734bc808e10898cd2ce050ee990384 | 9 |
| bmm | src/bmm-skills/ship/bmad-correct-course | f5e25906f744015ee1bd0f4c20a7107b529b8805 | 3 |
| bmm | src/bmm-skills/ship/bmad-qa-generate-e2e-tests | ab437aaa5ef1dbbf8255dca89a86dd485bab7b36 | 3 |
| bmm | src/bmm-skills/ship/bmad-retrospective | ced07c3bdad8ada76ebd6f7e0702cbbb019797dd | 12 |
| bmm | src/bmm-skills/v6-shims/bmad-create-architecture | e3785923162632297b016a53b7695a6f8c1c9dc8 | 2 |
| bmm | src/bmm-skills/v6-shims/bmad-create-prd | 9af7fe86e4964b857139e2d4a9be94c45c852440 | 2 |
| bmm | src/bmm-skills/v6-shims/bmad-create-story | 61162f7a8fb4b067881e48a71d1edfa9bc7f7ce9 | 5 |
| bmm | src/bmm-skills/v6-shims/bmad-dev-auto | 08d4c7f9fa21add71323dcebaeb2ab87b0b4cd35 | 1 |
| bmm | src/bmm-skills/v6-shims/bmad-dev-story | 7c1bfe92b252c3c69afd18176902b1afdde835aa | 3 |
| bmm | src/bmm-skills/v6-shims/bmad-document-project | 48008a21a1519723c8e371c09e7b892b9e9dfd8c | 1 |
| bmm | src/bmm-skills/v6-shims/bmad-domain-research | bdf7cc1878311af346418dc45a41f9a74a3df346 | 1 |
| bmm | src/bmm-skills/v6-shims/bmad-edit-prd | 4b7c71b829bc943dcf632a002db767476d6130e6 | 2 |
| bmm | src/bmm-skills/v6-shims/bmad-market-research | 30a78735687f0fb5832dae5e12b37c3a059e1681 | 1 |
| bmm | src/bmm-skills/v6-shims/bmad-quick-dev | 6342f100849b9839ce0fd4aafc14f982c2d93af1 | 1 |
| bmm | src/bmm-skills/v6-shims/bmad-sprint-status | c35a069a6a0c44c76709b3a9b06fa7b51d593b98 | 2 |
| bmm | src/bmm-skills/v6-shims/bmad-technical-research | ed3e7c97d52c8cf4810aa8889605a318882e989b | 1 |
| bmm | src/bmm-skills/v6-shims/bmad-validate-prd | fd649299c5bbae974a4606c7b68a6a3fcbd70a46 | 2 |
| core | src/core-skills/bmad-deep-recon | f3cd76f57f727c085f5fd0407487276f15c8cf2b | 20 |
| core | src/core-skills/bmad-review | 2174f40c5b62dc6e0fdbb668266ff4297f2351fe | 11 |
| core | src/core-skills/v6-shims/bmad-editorial-review | 7da5bf8804b032f389c6b176020c269fde98f4c2 | 2 |
| core | src/core-skills/v6-shims/bmad-editorial-review-prose | 7f0b301a3da7109c73227680211f7e0e5cc01610 | 1 |
| core | src/core-skills/v6-shims/bmad-editorial-review-structure | e3e1d2a0a1e0f8f53f6e5953434a5095c76e3967 | 1 |
| core | src/core-skills/v6-shims/bmad-review-adversarial-general | 80982194289cb325fb05a2be31abdece807fd6ef | 1 |
| core | src/core-skills/v6-shims/bmad-review-edge-case-hunter | 3d7735f935b0fb18ae747e666d97d0c398bdabbe | 1 |
| core | src/core-skills/v6-shims/bmad-review-verification-gap | 3cd0610eebeca5abac260b35d7c4edbab4d2fb1a | 1 |

## Removed paths

| Module | Skill root | Tree OID | Files |
| --- | --- | --- | ---: |
| bmm | src/bmm-skills/1-analysis/bmad-agent-analyst | 212ad5356ba50c0d704431255a65b17076d8f463 | 2 |
| bmm | src/bmm-skills/1-analysis/bmad-agent-tech-writer | 84827885245795fba974af166dcbdfd2de628ace | 6 |
| bmm | src/bmm-skills/1-analysis/bmad-document-project | 3ef40f197a272fd08d9f64d29ca3a668cbdaa8a7 | 14 |
| bmm | src/bmm-skills/1-analysis/bmad-prfaq | 07447e2d579c8a99ebeee27ab7c90288836e7c86 | 10 |
| bmm | src/bmm-skills/1-analysis/bmad-product-brief | 576ce3a8a87f54d46c0a626d91f5a61700381702 | 3 |
| bmm | src/bmm-skills/1-analysis/research/bmad-domain-research | bb0a561350e6c5fe315a86940a0ba7c9a131f9ce | 9 |
| bmm | src/bmm-skills/1-analysis/research/bmad-market-research | feea06514fdcf58890d8f5bcd11bf45f4bc1dfe8 | 9 |
| bmm | src/bmm-skills/1-analysis/research/bmad-technical-research | b37352301fc61ee912ddf768cf4e28b0ea045fba | 9 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-agent-pm | 25d42633d02f0abffde1c0d7f9316e2ec9b62244 | 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-agent-ux-designer | 1e13cc4815ef627f7631221d32db8d541ee35f9b | 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-create-prd | c60551add8a685464e29594d150559649e935861 | 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-edit-prd | 5bbc49252266b8ce6c4850ba0319849216a1e626 | 2 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-prd | f3dacf02d671cbea03104ab0cf27653811c42600 | 8 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-ux | 3f3abe65b5853c4d209f8d934fe3adddd7a566c1 | 17 |
| bmm | src/bmm-skills/2-plan-workflows/bmad-validate-prd | 5bc60bf988a8982b985277eb16e21f48f573dfe1 | 2 |
| bmm | src/bmm-skills/3-solutioning/bmad-agent-architect | 0f3bbc79c422d9dabddd23da260517aa4b41fdf2 | 2 |
| bmm | src/bmm-skills/3-solutioning/bmad-architecture | 402b1adbc4aee309b8fcfe14d56055c5d3990a78 | 7 |
| bmm | src/bmm-skills/3-solutioning/bmad-check-implementation-readiness | 644e59fe90e0817d9ccbcf7df6a605896cd8072f | 9 |
| bmm | src/bmm-skills/3-solutioning/bmad-create-architecture | 916a1a438610759d3d73851c40122762fbcb2e24 | 2 |
| bmm | src/bmm-skills/3-solutioning/bmad-create-epics-and-stories | 96b14cb6971ba3894db64e5d20cdb1c6b7b48d4f | 7 |
| bmm | src/bmm-skills/3-solutioning/bmad-generate-project-context | 42f512ada2620d34fed0abe29e373b0f54dec909 | 6 |
| bmm | src/bmm-skills/4-implementation/bmad-agent-dev | 07ba9c863f28a4b9933abb09bc27978169c1c0c5 | 2 |
| bmm | src/bmm-skills/4-implementation/bmad-checkpoint-preview | 5a9c703a12e38e32f8e97fc9930c3f4934ca1cd4 | 8 |
| bmm | src/bmm-skills/4-implementation/bmad-code-review | 2f7bd82aad5d85b5407b586f73fb90b086d6558e | 6 |
| bmm | src/bmm-skills/4-implementation/bmad-correct-course | 391ecad5cd563cd7c2e8f0ec41d1ab9603a4b2b6 | 3 |
| bmm | src/bmm-skills/4-implementation/bmad-create-story | cfcdedfe2a150d00c82428b8ad3ae90af914cf96 | 5 |
| bmm | src/bmm-skills/4-implementation/bmad-dev-auto | e514af61c3eacd7c99e6da3df581725457764757 | 8 |
| bmm | src/bmm-skills/4-implementation/bmad-dev-story | b920a0e57139949eacd8bbb1de97c2eeb0196fed | 3 |
| bmm | src/bmm-skills/4-implementation/bmad-qa-generate-e2e-tests | 7d2aeab849f07d3970cdf1a7956afab8f093c9a9 | 3 |
| bmm | src/bmm-skills/4-implementation/bmad-quick-dev | db0a08df6d10189e38a029caf0da63457cc8e042 | 11 |
| bmm | src/bmm-skills/4-implementation/bmad-retrospective | 6d27515bdaa79a7c003542c857859131503f7b17 | 2 |
| bmm | src/bmm-skills/4-implementation/bmad-sprint-planning | 2bf38d02553807f36149b876defa6b8feb11aaad | 4 |
| bmm | src/bmm-skills/4-implementation/bmad-sprint-status | e2367fd2203292ad3817d757b2d6c975ec490140 | 2 |
| core | src/core-skills/bmad-editorial-review-prose | 469701beb9f839fd05a162aa46c44359d85883e8 | 1 |
| core | src/core-skills/bmad-editorial-review-structure | fc1e08380fe47071e98b4803794d27dd667086d6 | 1 |
| core | src/core-skills/bmad-index-docs | d07c0e4ada9517bd0ef5f05cab831ebdbfaf688a | 1 |
| core | src/core-skills/bmad-review-adversarial-general | 2fc6d859f4fa69216dc72d6a295d0215011ba8be | 1 |
| core | src/core-skills/bmad-review-edge-case-hunter | 5b472e614eaac181e8bac5dd5a5c9eacaf01eaf8 | 2 |
| core | src/core-skills/bmad-shard-doc | cbfb01b74874522fa896a08ec90ffef4cf12a167 | 1 |
| core | src/core-skills/bmad-spec | ed1f7c24d848d493ac131064392e8ef7cc86615e | 4 |

## 판정 한계

- 경로 이동과 내용 변경이 동시에 일어나면 exact-path 비교에서는 remove와 add로 나타난다.
- 같은 basename이나 유사 content를 rename으로 확정하려면 manifest, release와 Git diff를 함께 확인해야 한다.
- 이 기록은 정적 source delta이며 실제 installer와 runtime을 실행하지 않았다.
