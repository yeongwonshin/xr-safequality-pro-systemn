# Audit Log Policy

## Log Principles

- Append-only
- Time synchronized
- Tenant isolated
- Model/SOP/Policy version linked
- Evidence hash included
- 관리자도 임의 삭제 불가

## Mandatory Events

- 사용자 로그인/권한 변경
- SOP 생성/수정/승인/배포/폐기
- 작업 세션 시작/종료
- step pass/fail/block/uncertain
- evidence upload/delete/retention change
- supervisor override request/approval/rejection
- model deployment/rollback
- policy threshold change
- integration webhook failure

## Retention

| 데이터 | 기본 보존기간 | 비고 |
|---|---:|---|
| Audit metadata | 3~7년 | 고객 산업/법규에 따라 조정 |
| Evidence image | 90~365일 | critical 사건은 장기보관 가능 |
| Video clip | 기본 비저장 | 필요 시 사건 전후 짧은 clip |
| Model logs | 1~3년 | 성능 재현용 |
| 개인정보 | 최소 기간 | 고객 정책/법규 우선 |

## Integrity

- evidence SHA-256 hash 저장
- audit event chain hash 옵션
- 관리자 export 기록 보존
- 시각 동기화 NTP monitoring
