# Offline Mode

## 목적

현장 네트워크 장애가 있어도 작업자가 안전 절차를 놓치지 않도록 최소 기능을 유지한다.

## Local Cache

- 사용자 세션 토큰의 제한된 오프라인 권한
- 승인된 SOP 최신 버전
- 모델/정책 버전
- 현장/설비 metadata
- 미동기화 이벤트 큐

## Offline Rules

| 상황 | 허용 |
|---|---|
| Low-risk 안내 단계 | 진행 가능 |
| 증적이 필요한 non-critical 단계 | 로컬 저장 후 진행 가능 |
| Critical 단계 | 로컬 모델 검증 성공 시 가능, 아니면 차단/승인 필요 |
| Supervisor approval | 사전 등록된 오프라인 승인자만 가능 |
| SOP 변경 | 불가, 온라인 필요 |

## Sync Conflict

- 세션 시작 시점의 SOP/정책/모델 버전으로 판정한다.
- 온라인 복귀 후 이벤트를 순서대로 전송한다.
- 서버는 중복 event id를 idempotent 처리한다.
- 정책 위반이 나중에 발견되면 post-review queue에 등록한다.
