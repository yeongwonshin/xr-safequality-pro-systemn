# Alert Policy

## Alert Types

| Alert | Trigger | Recipient | Channel |
|---|---|---|---|
| Critical Step Blocked | critical step fail | Supervisor/EHS/QA | App, Email, Webhook |
| Restricted Zone Entry | person within restricted zone | Supervisor/EHS | App, Siren optional |
| PPE Missing | required PPE not detected | Worker/Supervisor | XR/Mobile |
| Quality Gate Failed | part/screw/label mismatch | QA/Line lead | Dashboard, MES webhook |
| Edge Gateway Down | health check fail | Admin/IT | Email, Slack/Webhook |
| Model Drift | confidence distribution change | ML Ops | Dashboard, Ticket |

## Escalation

```text
0~1 min: 작업자 로컬 경고
1~3 min: 현장 리더 알림
3~10 min: EHS/QA 관리자 알림
10+ min 또는 반복: incident ticket 생성
```

## Alert Fatigue Control

- 같은 세션/단계/객체에 대한 반복 경고는 deduplication
- 낮은 위험 경고는 batch summary로 묶음
- critical 경고는 중복 억제하되 종료 전까지 상태 유지
- false positive feedback을 모델 개선 큐로 연결
