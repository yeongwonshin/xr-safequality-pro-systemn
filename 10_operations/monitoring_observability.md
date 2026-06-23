# Monitoring & Observability

## Golden Signals

- API latency p50/p95/p99
- API error rate
- inspection session start/completion rate
- evidence upload failure rate
- queue lag
- edge gateway offline count
- inference latency
- model confidence drift
- critical block count

## Logs

- Structured JSON logs
- tenant_id, site_id, session_id, step_id, request_id 포함
- 개인정보/영상 원문 로그 금지

## Traces

- session start → procedure load → inference → evaluation → evidence upload → audit write
- integration webhook tracing

## Alerts

| Alert | Threshold |
|---|---|
| API error rate | 5분간 2% 이상 |
| Evidence upload fail | 5분간 5건 이상 |
| Edge offline | 3분 이상 heartbeat 없음 |
| Critical FN confirmed | 즉시 Sev1 |
| Model confidence drift | 기준 대비 통계적 이상 |
| Audit write failure | 즉시 Sev1/Sev2 |

## SLO Examples

- API availability: 99.9%
- Audit write success: 99.99%
- Evidence upload success: 99.5%
- Edge inference p95 latency: customer-specific, 기본 2초 이하
