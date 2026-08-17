# 공개 AIDD 개발 워크플로 의사결정 위키

**AIDD Workflow Evidence Wiki**

[English](README.md) | **한국어**

> 공개 공식 근거와 재현 가능한 실험을 버전별로 보존해 AIDD workflow,
> artifact, 자동화 범위와 Human Approval Gate를 선택하는 Markdown 지식베이스입니다.

## 프로젝트 소개

이 저장소는 `ains-lab/2nd-brain-template`의 evidence-first 구조를 사용한다.
도구 백과사전이 아니라 **상황 → 입력·출력 contract → 자동화 범위 → 사람 승인
지점 → 적용·비적용 조건**을 근거와 version 범위로 연결한다. 현재 pilot은 BMAD
Method 공식 tag `v6.11.0`, commit
`9ce3c397c9b238de96f7365da8019f6f66b059da`에 고정되어 있다.

- 운영 계약: [SCHEMA.md](SCHEMA.md)
- 조사 backlog: [docs/initial-research-backlog.md](docs/initial-research-backlog.md)
- canonical catalog: [index.md](index.md)
- append-only 작업 이력: [log.md](log.md)

### 전체 아키텍처

[전체 아키텍처](docs/architecture/second-brain-pkm-architecture.md)는 **Evidence → Canonical Memory → Discovery → Human Decision**의 네 계층으로 구성됩니다. 원본과 메타데이터는 불변 evidence로 보존하고, 반복해서 사용할 지식만 출처와 함께 canonical Markdown으로 컴파일합니다. NotebookLM과 지식그래프에서 발견한 관계는 가설로 취급하며, 사람의 검증을 통과한 내용만 장기 기억으로 승격합니다.

![2nd-Brain 증거 기반 개인 지식관리 아키텍처](docs/architecture/second-brain-pkm-architecture.png)

### 운영 워크플로

[운영 워크플로](docs/architecture/second-brain-pkm-architecture.md#6-핵심-워크플로우)는 **Capture → Compile → Discovery → Human Decision** 순서로 진행됩니다. 각 단계의 무결성·frontmatter·구조 검증 관문을 통과해야 다음 단계로 이동하며, 승인된 변경은 canonical 문서·index·log를 함께 갱신한 뒤 지식그래프와 재사용 산출물로 환류됩니다.

![2nd-Brain Evidence to Reusable Knowledge 운영 워크플로](docs/workflow/second-brain-workflow.png)

### 기술 스택

[기술 스택](docs/architecture/second-brain-pkm-architecture.md#5-기술-스택)의 핵심 자산은 특정 제품이 아니라 **공개 형식의 원본, canonical Markdown, 출처 메타데이터와 Git 이력**입니다. Obsidian·Zotero·NotebookLM·Understand Anything은 수집, 편집, 탐색과 분석을 담당하는 교체 가능한 도구이며, 무결성 검사와 사람의 승인 관문이 전체 스택을 연결합니다.

![2nd-Brain Durable Knowledge 기술 스택](docs/tech-stack/second-brain-technology-stack.png)

## 현재 pilot 지식 세트

공식 BMAD repository의 tag·commit permalink와 raw body hash를 보존하고 다음
의사결정 문서를 제공한다.

| 주요 기능 | 설명 |
| --- | --- |
| **Workflow contract** | [BMAD v6.11.0 workflow 및 artifact 계약](queries/bmad-v6-11-0-workflow-contracts.md): sprint readiness, Build, Build Auto와 project context의 입력·출력 |
| **자동화와 승인** | [BMAD v6.11.0 자동화 범위와 Human Approval Gate](comparisons/bmad-v6-11-0-automation-and-human-gates.md): Build/Build Auto, v6 shim migration, review gate 비교 |
| **Skill 기준선** | [BMAD v6.5.0 BMM 및 Core 스킬 기준선](queries/bmad-v6-5-0-bmm-core-skill-catalog.md): BMM/Core inventory와 변경된 skill만 수집하는 tree fingerprint 정책 |
| **Skill 버전 비교** | [BMAD v6.5.0에서 v6.11.0까지 BMM/Core skill 변화](comparisons/bmad-v6-5-0-to-v6-11-0-bmm-core-skill-delta.md): v6.10 추가와 v6.11 Build·shim·Core 통합 변화 |
| **MSA 경계** | [BMAD MSA 및 multi-repository artifact 경계](concepts/bmad-msa-multi-repository-boundaries.md): 공식 범위와 위키의 저신뢰도 경계 모델을 분리 |
| **근거 보존** | `raw/official-docs/`, `raw/releases/`, `raw/experiments/`에 provenance와 post-frontmatter SHA-256을 기록 |

## 사전 설치

일반 Markdown 편집만 필요하다면 Obsidian만 설치해도 시작할 수 있습니다. 웹·논문 수집부터 AI 기반 지식 정리와 그래프 탐색까지 전체 워크플로를 사용하려면 아래 도구를 순서대로 준비하세요.

### 앱과 데이터 수집 도구

| 구분 | 도구 | 용도 및 설치 방법 |
| --- | --- | --- |
| 필수 | [Obsidian](https://obsidian.md/download) | 이 저장소를 로컬 vault로 열어 Markdown 노트를 탐색하고 편집합니다. |
| 논문 수집 | [Zotero 및 Zotero Connector](https://www.zotero.org/download/) | Zotero 데스크톱 앱으로 논문·PDF·서지 정보를 관리하고, 같은 다운로드 페이지에서 Chrome용 Connector를 설치해 웹의 논문 정보를 Zotero로 저장합니다. |
| 웹 수집 | [Obsidian Web Clipper](https://obsidian.md/clipper) | Chrome에서 웹 페이지와 메타데이터를 Markdown으로 변환해 Obsidian vault에 저장합니다. |

### AI 자동화 도구

다음 항목은 에이전트를 이용해 수집 자료를 가져오고, 지식 노트로 정리하거나 시각화할 때 사용합니다. Obsidian 플러그인이 아니라 MCP 서버, CLI 또는 에이전트 스킬입니다.

> [!IMPORTANT] 에이전트 환경에 맞게 설치하세요
> MCP 설정 파일, 프로젝트·로컬 스킬 경로, 플러그인 지원 방식과 재시작 절차는 에이전트마다 다릅니다. 아래 링크의 공식 설치 문서를 먼저 읽고 현재 사용하는 에이전트 또는 MCP 클라이언트에 맞는 방법을 선택하세요. 다른 에이전트용 설정과 명령을 그대로 복사하지 마세요.

| 도구 | 역할 | 설치 안내 |
| --- | --- | --- |
| [Zotero MCP](https://github.com/54yyyu/zotero-mcp) | Zotero의 서지 메타데이터, 첨부 파일, 노트 및 원문을 에이전트가 조회하도록 연결합니다. | 공식 저장소의 설치 및 MCP 클라이언트 설정 안내를 따라 현재 환경에 서버를 설치·등록하세요. Zotero 로컬 API 설정도 공식 안내에 맞게 확인합니다. |
| [`llm-wiki`](https://github.com/ains-lab/harness/tree/main/skills/llm-wiki) | 수집한 원문을 출처가 추적되는 상호 연결형 Markdown 지식 베이스로 컴파일하고 검사합니다. | 링크된 스킬 문서와 사용하는 에이전트의 스킬 설치 문서를 함께 확인해 지원되는 로컬 또는 프로젝트 스킬 위치에 설치하세요. |
| [notebooklm-py](https://github.com/teng-lin/notebooklm-py) | NotebookLM 노트북과 소스를 CLI로 관리하고, 출처 기반 질의와 결과물 생성을 자동화합니다. | 공식 저장소의 설치·인증 문서를 따라 현재 Python 및 브라우저 환경에 맞는 방법으로 설치하세요. 에이전트에서 호출할 경우 해당 환경의 CLI 연동 방식도 확인합니다. |
| [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) | 코드와 지식 베이스의 관계를 분석해 대화형 지식 그래프를 생성합니다. | 공식 저장소에서 현재 사용하는 에이전트 또는 개발 환경에 해당하는 설치·연동 방법을 선택하고, 제공되는 확인 절차로 스킬이나 플러그인 인식을 점검하세요. |

> [!NOTE]
> `notebooklm-py`는 Google의 비공식 API를 사용하므로 서비스 변경으로 동작이 달라질 수 있습니다. Google 로그인 세션, Zotero API 키 등 인증 정보는 이 저장소에 커밋하지 마세요.

### 권장 설치 순서

1. Obsidian을 설치하고 이 저장소 폴더를 vault로 엽니다.
2. Zotero 데스크톱 앱과 Zotero Connector, Obsidian Web Clipper를 설치합니다.
3. 위 표의 공식 링크에서 각 도구가 지원하는 환경과 선행 조건을 확인합니다.
4. Zotero MCP는 공식 문서에 따라 Zotero와 현재 사용하는 MCP 클라이언트를 연결합니다.
5. `llm-wiki`와 Understand Anything은 각 공식 문서와 에이전트의 스킬·플러그인 설치 규칙을 함께 따라 설치합니다.
6. 필요하면 `notebooklm-py`를 공식 문서에 따라 설치하고 인증을 완료합니다.

설치가 끝나면 사용하는 환경의 MCP 서버 목록, 스킬·플러그인 목록 또는 CLI 확인 절차를 이용해 각 도구가 인식되는지 점검하세요. 정확한 확인 명령과 재시작 여부는 해당 도구와 에이전트의 공식 문서를 따릅니다.

## 권장 폴더 구조

이 저장소의 루트가 곧 하나의 wiki이자 Obsidian vault입니다. 별도 데이터베이스 없이 모든 경로를 저장소 루트 기준으로 해석하며, 폴더와 데이터의 유효성은 [SCHEMA.md](SCHEMA.md)가 정의합니다.

```text
.
├── inbox/                    # 분류와 정식 수집을 기다리는 임시 입력
├── raw/                      # 수정하지 않는 원본 증거
│   ├── articles/             # 기사·웹 클리핑 원문
│   ├── notebooklm/           # NotebookLM에서 가져온 소스 레코드
│   ├── papers/files/         # 논문 첨부 파일(필요할 때 생성)
│   ├── transcripts/          # 음성·영상·회의 전사 원문
│   ├── web/                  # 가져온 경로를 보존하는 웹 캡처
│   ├── youtube/              # YouTube 메타데이터와 전사 원문
│   └── assets/               # 원본 문서가 참조하는 이미지·첨부 자산
├── entities/                 # 사람·조직·도구 등 개체 정식 지식
├── concepts/                 # 개념·원리·방법론 정식 지식
├── comparisons/              # 도구·방법을 나란히 분석한 정식 지식
├── queries/                  # 출처 기반 질의와 종합 결과
├── docs/                     # 아키텍처·워크플로·기술 스택 산출물
│   ├── architecture/
│   ├── tech-stack/
│   └── workflow/
├── templates/                # 검증된 노트 양식(필요할 때 생성)
├── _archive/                 # 완전히 대체된 정식 지식(필요할 때 생성)
├── .obsidian/                # 공유 가능한 Obsidian 설정
├── SCHEMA.md                 # 폴더·메타데이터·무결성의 기준 계약
├── index.md                  # 활성 정식 지식의 전체 목록
└── log.md                    # wiki 작업을 덧붙여 기록하는 변경 이력
```

`raw/papers/files/`, `templates/`, `_archive/`는 해당 워크플로가 실제로 필요할 때만 만듭니다. `.ua/` 같은 지식그래프 캐시와 기타 생성 결과는 다시 만들 수 있는 파생 데이터이므로 정식 지식이나 원본 증거로 취급하지 않습니다.

### 구조가 의미하는 것

| 구분 | 저장 위치 | 의미와 관리 방식 |
| --- | --- | --- |
| 임시 수집함 | `inbox/` | 아직 출처 형식과 분류가 확정되지 않은 입력을 잠시 둡니다. 이곳의 파일은 증거나 정식 지식이 아니므로 검토 후 `raw/`로 캡처하거나 삭제합니다. |
| Layer 1: 원본 증거 | `raw/` | 수집 당시의 본문과 출처 메타데이터를 보존합니다. 최초 캡처 뒤 본문은 원칙적으로 수정하지 않으며, 해석과 정정은 정식 지식에 기록합니다. |
| Layer 2: 정식 지식 | `entities/`, `concepts/`, `comparisons/`, `queries/` | 원본 증거를 인용해 반복 사용 가능한 지식으로 종합합니다. 폴더명과 frontmatter의 `type`이 반드시 일치해야 합니다. |
| Layer 3: 운영 메타데이터 | `SCHEMA.md`, `index.md`, `log.md` | 스키마 계약, 활성 지식 탐색, 변경 이력을 담당합니다. 정식 지식을 변경할 때 세 파일의 규칙을 하나의 트랜잭션처럼 적용합니다. |
| 보조·파생 산출물 | `docs/`, `.obsidian/`, `.ua/` | 문서화, 편집 환경, 그래프 탐색을 지원하지만 출처 증거는 아닙니다. 특히 그래프가 제안한 관계는 원문 검증 전까지 가설로 다룹니다. |

## 빠르게 시작하기

### 1. 저장소 복제

```bash
git clone git@github.com:ains-lab/2nd-brain-template.git
cd 2nd-brain-template
```

### 2. 원하는 Markdown 편집기에서 열기

- **Obsidian**: `Open folder as vault`를 선택한 뒤 저장소 폴더를 지정합니다.
- **VS Code**: 저장소에서 `code .`을 실행합니다.
- **기타 편집기**: Markdown 파일과 폴더를 편집할 수 있는 도구라면 무엇이든 사용할 수 있습니다.

저장소를 복제하면 기본 폴더가 함께 준비되므로 별도의 번호 기반 분류 폴더를 만들 필요가 없습니다.

### 3. 운영 기준 확인

지식을 추가하기 전에 [SCHEMA.md](SCHEMA.md)를 읽고, [index.md](index.md)에서 이미 다루는 주제가 있는지 확인한 다음 [log.md](log.md)의 최신 기록을 살펴보세요. 기존 주제가 있다면 유사한 새 페이지를 만들지 말고 해당 페이지에 증거를 보강합니다.

## 기본 사용 흐름

1. **임시 수집**: 분류가 끝나지 않은 메모와 링크는 `inbox/`에 둡니다.
2. **원본 캡처**: 자료 유형에 맞는 `raw/` 하위 폴더에 출처 메타데이터와 본문을 저장하고, 지원되는 레코드는 본문 바이트 기준 SHA-256으로 무결성을 고정합니다.
3. **검증**: 실제 원본 경로, 필수 메타데이터, 해시와 파일 형식을 확인합니다. 가져오기 도구가 보존한 파일명과 상대 경로는 임의로 바꾸지 않습니다.
4. **지식 컴파일**: 주제의 성격에 따라 `entities/`, `concepts/`, `comparisons/`, `queries/` 중 하나에 정식 지식을 만들거나 기존 페이지를 갱신합니다.
5. **출처와 연결 기록**: `sources`에 실제 `raw/*.md` 경로를 넣고 필요한 주장에는 `^[raw/...md]` 출처 표식을 붙입니다. 관련 정식 지식은 `[[wikilinks]]`로 연결합니다.
6. **동기화**: 정식 지식 변경과 같은 작업에서 `index.md`를 갱신하고 `log.md`에 작업 내역을 한 번 추가합니다.
7. **탐색과 사람 검증**: NotebookLM과 지식그래프 결과는 발견 후보로만 사용합니다. 원본을 확인해 승인한 내용만 정식 지식으로 환류합니다.
8. **보관**: 완전히 대체된 페이지만 `_archive/`로 옮기고, 활성 링크와 `index.md`를 정리한 뒤 `log.md`에 기록합니다.

## 데이터 관리 원칙

> [!IMPORTANT]
> `README.ko.md`는 사용 안내이며, 실제 데이터 계약은 [SCHEMA.md](SCHEMA.md)가 우선합니다. 규칙이 다르게 보이면 `SCHEMA.md`를 따르세요.

- **원본은 불변입니다.** `raw/` 본문은 최초 캡처 후 수정하지 않습니다. 예외는 스키마가 허용한 Zotero 메타데이터 복구와 NotebookLM frontmatter 매핑뿐이며, 각 작업의 바이트 보존 규칙을 지켜야 합니다.
- **출처 경로는 실재해야 합니다.** 정식 지식의 `sources`에는 등록된 `raw/` 소스 폴더 아래 실제 Markdown 파일만 기록합니다. PDF·이미지 같은 첨부 파일만으로는 출처가 될 수 없습니다.
- **정식 지식은 선별해서 만듭니다.** 하나의 원본에서 중심적으로 다루거나 둘 이상의 원본에서 반복되는 주제만 페이지로 승격합니다. 이미 존재하는 주제에는 새 증거를 합칩니다.
- **정식 지식은 서로 연결합니다.** 활성 정식 페이지가 있다면 각 페이지는 자신을 제외한 서로 다른 활성 페이지 두 개 이상에 `[[wikilinks]]`로 연결되어야 합니다.
- **변경은 함께 기록합니다.** 정식 지식의 생성·수정·질의 편입·보관·삭제는 `index.md`와 `log.md` 갱신까지 완료되어야 하나의 작업으로 끝납니다. 이전 로그는 고치거나 지우지 않습니다.
- **파생 데이터는 원본과 분리합니다.** `docs/`의 설명 자료와 `.ua/`의 그래프 데이터는 분석을 돕는 산출물입니다. 이를 `raw/` 증거처럼 인용하거나 자동으로 정식 지식에 승격하지 않습니다.

## 동기화와 백업

Markdown 파일은 Git으로 변경 이력을 관리할 수 있습니다.

```bash
git add .
git commit -m "docs: update second brain notes"
git push
```

민감한 개인정보, 비밀번호, API 키는 저장소에 기록하지 마세요. 여러 기기에서 사용할 경우 Git 외에도 사용하는 편집기의 공식 동기화 기능이나 신뢰할 수 있는 백업 방식을 함께 고려하세요.

## 스키마 확장하기

새 소스 유형, 태그 또는 자동화를 추가할 때는 먼저 [SCHEMA.md](SCHEMA.md)에 역할과 무결성 규칙을 등록하세요. 원본 폴더를 추가한다면 정식 `sources`로 인정할 파일 형식과 경로 보존 정책을 함께 정의하고, 새 태그는 분류표에 등록한 뒤 사용합니다.

템플릿, 대시보드, 캘린더와 자동화는 정식 지식을 덮어쓰지 않고 공개 Markdown과 출처 메타데이터를 유지하는 범위에서 확장합니다. 교체 가능한 도구보다 `raw/` 원본, 정식 Markdown, `index.md`, `log.md`와 Git 이력을 오래 보존하는 것이 우선입니다.

## 기여하기

개선 아이디어나 새로운 템플릿은 Issue로 제안하거나 Pull Request로 공유해 주세요. 변경 사항은 특정 도구에만 의존하지 않고 일반 Markdown 환경에서도 이해할 수 있도록 작성하는 것을 권장합니다.
