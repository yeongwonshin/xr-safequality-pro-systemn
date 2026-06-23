# Architecture Decision Records

## ADR-001: LLM은 절차 생성 보조로 제한한다

**Decision:** LLM은 SOP 문서에서 절차 초안을 생성하고 설명을 제공하되, 현장 실행 판정은 Procedure Engine의 DSL/상태머신과 CV 결과로 수행한다.

**Reason:** 안전·품질 현장에서는 재현 가능성, 감사 가능성, 책임소재가 중요하다. LLM 단독 판단은 비결정적이며 검증이 어렵다.

## ADR-002: Critical 단계는 fail-safe 정책 적용

**Decision:** Critical 단계는 confidence가 낮거나 증적 저장이 실패하면 통과할 수 없다.

**Reason:** PPE, 위험물, 전기/압력/고온/클린룸 관련 단계의 false negative는 사고로 이어질 수 있다.

## ADR-003: 영상 원본은 최소 저장

**Decision:** 기본 정책은 원본 영상 전체 저장이 아니라 이벤트 기반 스냅샷, 마스킹 이미지, 메타데이터 저장이다.

**Reason:** 개인정보·영업비밀·공정기밀 노출 위험을 줄인다.

## ADR-004: Edge-first inference

**Decision:** 저지연 및 데이터 주권 요구가 있는 고객은 Edge Inference Gateway를 기본 옵션으로 제공한다.

**Reason:** 공장/연구실은 네트워크 제약이 크고 영상 외부 전송을 꺼린다.

## ADR-005: 모델/정책/SOP 버전 삼중 추적

**Decision:** 모든 inspection event에는 `sop_version`, `model_version`, `policy_version`을 기록한다.

**Reason:** 감사와 사고 조사 시 어떤 기준으로 판단했는지 재현해야 한다.
