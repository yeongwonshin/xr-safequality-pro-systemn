# LLM Prompt Policy

## 사용 가능 영역

- SOP/PDF/문서에서 단계 후보 추출
- 위험 단어와 PPE 요구사항 후보 추출
- 작업자에게 쉬운 설명 생성
- 관리자 리포트 초안 생성
- 유사 절차 검색/RAG 질의응답

## 사용 금지 영역

- Critical step 통과/실패 최종 판정
- 법적 책임 판단
- 안전 예외 자동 승인
- 모델 confidence 무시 지시
- 현장 정책 우회 방법 제안

## Structured Output

LLM 출력은 반드시 JSON Schema 또는 Procedure DSL schema로 검증한다.

```json
{
  "procedure_id": "string",
  "steps": [
    {
      "id": "string",
      "title": "string",
      "hazards": ["string"],
      "required_ppe": ["string"],
      "verification_candidates": [
        {
          "type": "visual_verification",
          "object": "string",
          "state": "string"
        }
      ]
    }
  ]
}
```

## Reviewer Workflow

1. LLM이 SOP 초안을 생성한다.
2. 도메인 담당자가 단계, 위험, PPE, 차단 조건을 검토한다.
3. EHS/QA 승인자가 production 배포를 승인한다.
4. Procedure Engine은 승인된 DSL만 실행한다.

## Guardrails

- 근거 문단 없는 step 생성 금지
- 불확실한 항목은 `needs_human_review=true`
- 위험물/전기/고온/압력 관련 항목은 자동으로 critical 후보 표시
- SOP 변경 시 diff와 impact report 생성
