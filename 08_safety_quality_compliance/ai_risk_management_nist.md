# AI Risk Management Mapping

## 목적
AI가 안전·품질 판정에 관여할 때 발생하는 위험을 식별하고 통제하기 위한 운영 프레임워크입니다.

## Risk Categories

| 위험 | 설명 | 통제 |
|---|---|---|
| False Negative | 위험/불량을 놓침 | critical recall 목표, fail-safe, human review |
| False Positive | 정상 작업을 과도하게 막음 | 재촬영, 보조 검증, alert fatigue 관리 |
| Data Drift | 현장 조건 변화로 성능 저하 | drift monitoring, active learning |
| Prompt Injection | SOP 문서에 악성 지시 포함 | LLM output schema validation, allow-list |
| Privacy Leakage | 영상 속 얼굴/명찰/공정기밀 노출 | 마스킹, 최소 저장, 보존기간 |
| Automation Bias | 작업자가 AI 판단을 과신 | 설명, confidence 표시, 승인 절차 |
| Accountability Gap | 사고 시 판단 근거 불명확 | audit log, model/policy/SOP version tracking |

## Governance Functions

### Map
- 사용 환경, 고객, 위험 등급, 법규, 데이터 흐름 식별

### Measure
- 모델 성능, false negative/positive, drift, override rate 측정

### Manage
- threshold, 승인, 롤백, incident response, CAPA 연동

### Govern
- 책임자, 변경관리, 감사, 데이터 사용 동의, release gate 운영

## Release Checklist

- [ ] 모델 카드 작성
- [ ] 데이터셋 카드 작성
- [ ] 현장별 성능 검증
- [ ] critical class false negative 리뷰
- [ ] privacy impact review
- [ ] rollback plan
- [ ] 운영자 교육
- [ ] 고객 승인
