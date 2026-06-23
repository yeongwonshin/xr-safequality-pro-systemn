# Secure Deployment Checklist

## Pre-Deployment

- [ ] 고객 데이터 분류 완료
- [ ] 네트워크 경계와 방화벽 정책 확정
- [ ] SSO/OIDC/SAML 설정
- [ ] 관리자 MFA 적용
- [ ] 암호화 키 관리 방식 확정
- [ ] 영상 보존 정책 승인
- [ ] DPIA/PIA 또는 내부 개인정보 검토 완료
- [ ] 현장 디바이스 등록/MDM 정책 확정

## Application Security

- [ ] OWASP Top 10 점검
- [ ] API authorization test
- [ ] Tenant isolation test
- [ ] Rate limiting
- [ ] Audit log tamper test
- [ ] Dependency scan
- [ ] Container image scan
- [ ] Secrets rotation

## AI Security

- [ ] 모델 artifact signing
- [ ] 모델 registry 승인 워크플로우
- [ ] prompt injection test for SOP documents
- [ ] adversarial/hard-case evaluation
- [ ] rollback rehearsal

## Operations

- [ ] backup/restore test
- [ ] incident contact list
- [ ] monitoring alert routes
- [ ] edge gateway health dashboard
- [ ] disaster recovery runbook
