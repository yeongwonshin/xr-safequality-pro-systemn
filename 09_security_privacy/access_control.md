# Access Control

## Roles

| Role | Description |
|---|---|
| WORKER | 작업 수행자 |
| SUPERVISOR | 현장 리더, 예외 승인 |
| EHS_MANAGER | 안전 정책, 사고 관리 |
| QA_MANAGER | 품질 기준, 불량 관리 |
| ML_OPS | 모델 성능/배포 관리 |
| TENANT_ADMIN | 사용자/권한/SSO 관리 |
| AUDITOR | 읽기 전용 감사 조회 |

## Permission Matrix

| Resource | Worker | Supervisor | EHS | QA | ML Ops | Admin | Auditor |
|---|---|---|---|---|---|---|---|
| Own session | R/W | R | R | R | - | R | R |
| Team sessions | - | R | R | R | - | R | R |
| Evidence | R own | R team | R | R | limited | R | R |
| Procedure draft | - | C/R | C/R/A | C/R/A | - | R | R |
| Policy threshold | - | - | C/R/A | C/R/A | R | A | R |
| Model deploy | - | - | R | R | C/R/A | A | R |
| User management | - | - | - | - | - | C/R/U/D | R |

## Approval Rules

- 작업자는 본인 critical exception을 승인할 수 없다.
- Supervisor는 본인 팀 범위에서만 승인한다.
- 모델/정책/SOP production 변경은 2인 승인 옵션을 지원한다.
- 감사자는 데이터를 수정할 수 없다.
