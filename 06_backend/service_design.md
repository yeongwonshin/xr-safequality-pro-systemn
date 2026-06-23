# Backend Service Design

## Service Boundaries

### API Service
- 인증/인가
- 테넌트 context 주입
- REST API 제공
- 이벤트 발행

### Procedure Service
- SOP DSL 파싱
- 단계 상태머신 관리
- condition evaluation
- blocking/approval decision

### Evidence Service
- signed upload URL 발급
- 증적 hash 검증
- 보존기간/마스킹 상태 관리

### Audit Service
- append-only event write
- event integrity check
- export for audit report

### Integration Service
- MES/QMS/LIMS/EHS/SSO adapter
- webhook retry와 dead-letter queue

### Model Service
- 모델 버전/배포 상태 조회
- 추론 결과 schema validation
- model health metrics 수집

## API Principles

- 모든 write API는 idempotency key를 지원한다.
- 모든 request는 tenant isolation을 강제한다.
- 외부 시스템 연동 실패는 session progression과 분리하되 critical integration check는 정책에 따라 차단 가능하다.
- audit event는 business transaction과 함께 기록한다.

## Step Evaluation Pseudocode

```python
def evaluate_step(step, observations, policy):
    missing = []
    uncertain = []

    for condition in step.conditions:
        result = evaluate_condition(condition, observations, policy)
        if result.status == "fail":
            missing.append(result.reason)
        elif result.status == "uncertain":
            uncertain.append(result.reason)

    if missing and step.blocking:
        return StepResult("blocked", reasons=missing)
    if uncertain:
        if step.criticality == "critical":
            return StepResult("uncertain", action="retake_or_approval", reasons=uncertain)
        return StepResult("warn", reasons=uncertain)
    return StepResult("pass")
```
