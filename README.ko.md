<!-- source: README.md sha256: 249ef3cd3488abaf2e2fb7e6a01baf523abaf90eca3e76bd9a34927c8d809660 -->
# stable-agent-documentation-guidebook

에이전트는 작업하기 전에 저장소의 문서를 읽습니다. 대상은 README, ARCHITECTURE, AGENTS.md 같은 컨텍스트 파일, CONTRIBUTING입니다. 문서가 낡았거나 엉뚱한 독자를 위해 쓰였다면, 에이전트는 틀린 사실을 바탕으로 일하게 됩니다. 이 가이드북은 문서마다 독자를 정하고 그 독자를 위해 쓰는 방법을 안내합니다. 또한 코드가 바뀌어도 문서가 정확하게 유지되도록 관리하는 방법과, 해당 독자를 대상으로 문서를 시험하는 방법도 안내합니다. 이미 발표된 연구와 현재 운영되는 도구를 적용하며, 새로운 도구는 만들지 않습니다.

모든 조항에는 근거 등급과 반증 기준이 붙어 있습니다. 조항은 결정 기록이 채택하기 전까지 제안 상태이므로, 사용하기 전에 각 조항의 상태를 확인해야 합니다. 원본은 영어로 작성하며 Simplified Technical English(STE)를 따릅니다. 번역본은 해당 언어의 작성 지침을 따릅니다([DESIGN.md](DESIGN.md) 11절).

이 문서는 영어 원본인 [README.md](README.md)를 한국어로 옮긴 번역본입니다. 한국어 번역본은 [fluent-korean](https://github.com/snflkd/fluent-korean) 지침에 따라 작성합니다. 번역본과 원본의 내용이 서로 다르면 영어 원본을 따릅니다.

## 누가 무엇을 읽는가

아래 표는 이 저장소의 각 문서에 대해 독자와 독자 과제를 밝힙니다(R-004).

| 문서 | 독자 | 독자 과제 |
|---|---|---|
| 이 README | 가이드북을 처음 보는 사람이나 에이전트 | 가이드북의 용도를 파악하고 다음에 읽을 문서를 찾습니다 |
| [guides/new-project.md](guides/new-project.md), [guides/templates/](guides/templates/) | 저장소의 문서를 작성하는 사람이나 에이전트 | 문서와 검사를 만들고, 각 문서를 해당 독자를 대상으로 시험합니다 |
| [guides/case-swift-monorepo.md](guides/case-swift-monorepo.md) | 위와 같은 작성자 | 안내를 적용한 사례 하나를 확인합니다 |
| [principles/](principles/), [practices/](practices/) | 컨텍스트 파일에서 조항을 인용하는 사람 | 조항의 내용, 근거의 강도, 조항이 틀리게 되는 조건을 설명합니다 |
| [REFERENCES.md](REFERENCES.md) | 조항을 검증하는 사람 | 각 출처와 그 한계를 찾습니다 |
| [GLOSSARY.md](GLOSSARY.md) | 이 저장소의 모든 작성자와 독자 | 용어의 뜻과 출처를 찾습니다 |
| [DESIGN.md](DESIGN.md), [AGENTS.md](AGENTS.md) | 이 가이드북을 고치는 사람이나 에이전트 | 진입 조건을 충족하는 조항을 추가하거나 고칩니다 |
| [decisions/](decisions/) | 결정을 바꾸려는 사람이나 에이전트 | 그 결정을 내린 이유와 기각된 대안을 설명합니다 |
| [snapshots/](snapshots/) | 측정 결과를 확인하는 사람 | 측정 데이터와 측정 조건을 찾습니다 |
| [README.ko.md](README.ko.md) | 이 README의 한국어 독자 | 이 README와 같은 과제를 수행합니다 |

## 사용 방법

```mermaid
flowchart LR
  A["문서마다 독자와<br/>독자 과제를 정한다"] --> B["템플릿으로<br/>문서를 작성한다"]
  B --> C["검사를 추가한다:<br/>생성 목록, 해시,<br/>낡은 참조"]
  C --> D{"독자마다<br/>독자 시험을 한다"}
  D -->|실패한다| B
  D -->|통과한다| E["정해진 주기로<br/>다시 읽는다"]
  E --> A
```

## 각 단계를 뒷받침하는 것

```mermaid
flowchart TB
  G["안내 단계와 템플릿"] -->|인용한다| R["관행<br/>근거 등급이 붙은 처방"]
  G -->|인용한다| P["원칙<br/>관찰된 현상"]
  R -->|근거로 삼는다| P
  R -->|인용한다| REF["참고 문헌<br/>연구와 도구"]
  P -->|인용한다| REF
```

조항이 제안되고 채택되고 다시 평가되는 과정은 DESIGN.md에 있습니다.

## 라이선스

[MIT](LICENSE)
