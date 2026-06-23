# Deployment Runbook

## SaaS Deployment

1. Terraform로 cloud infrastructure 생성
2. PostgreSQL, object storage, queue, secret store 구성
3. API/Dashboard container 배포
4. 기본 테넌트와 admin 생성
5. SSO 설정
6. 모델 registry 초기화
7. 샘플 SOP import
8. smoke test 실행
9. monitoring alert 연결

## Edge Gateway Deployment

1. 고객 현장 서버 사양 확인
2. OS hardening 및 disk encryption
3. GPU driver/runtime 설치
4. Edge agent 설치
5. tenant/site binding
6. 모델 다운로드 및 서명 검증
7. LAN client connectivity test
8. offline queue test
9. failover/degraded mode test

## Release Process

- 개발 → staging → pilot tenant → canary production → full rollout
- DB migration은 backward compatible 우선
- SOP/정책/모델 변경은 별도 release gate
- rollback plan 없이는 critical customer에 배포 금지

## Rollback

| 대상 | 방법 |
|---|---|
| API | 이전 container image 배포 |
| DB | migration rollback 또는 forward fix |
| Model | registry의 이전 approved model로 route 변경 |
| SOP | retired 전 approved version으로 재지정 |
| Policy | policy version rollback |
