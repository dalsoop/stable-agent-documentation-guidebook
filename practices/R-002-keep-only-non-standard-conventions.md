---
id: R-002
layer: practice
status: proposed
certainty: low
downgraded-for: [indirectness, imprecision]
falsified-if: "Python 밖의 저장소에서 개요를 넣은 에이전트 지시 파일이 작업 성공률을 유의하게 높인다"
review-by: 2027-03-24
references: [3, 5]
superseded-by: null
---

# 에이전트 지시에는 그 저장소만의 관례만 둔다

## 조항

에이전트 지시 파일에는 README나 코드에서 알 수 없는, 그 저장소만의 관례와 명령만 둔다. 저장소 개요와 구조 설명은 README와 ARCHITECTURE에 두고 경로만 가리킨다.

## 이유

개요는 에이전트가 파일을 찾는 데 도움이 되지 않았고, 에이전트는 파일에 적힌 구체적인 지시를 따랐다 [3]. 개요를 빼면 파일이 짧아져 원칙 P-001이 말하는 증가의 대상도 줄어든다.

## 반대 근거와 판단

- **반대 근거**: [3]은 Python 저장소만 다뤘고, 문서가 적은 저장소에서는 결과가 다를 수 있다고 저자가 밝혔다.
  **판단**: 문서가 적은 저장소에서는 개요를 README에 먼저 쓰고 에이전트 지시에서 가리키는 방식으로 적용한다. 개요를 없애는 것이 아니라 위치를 옮기는 처방이다.

## 적용

```markdown
구조와 경계는 ARCHITECTURE.md를 먼저 읽는다.

- 새 앱은 `./repo new <app>`으로만 만든다. (이유: 스캐폴더가 필수 파일을 함께 만든다)
```
