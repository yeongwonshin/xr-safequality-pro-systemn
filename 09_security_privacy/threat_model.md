# Threat Model

## Assets

- 작업자 개인정보
- 현장 영상/이미지
- 공정/설비/제품 기밀
- SOP와 품질 기준
- 모델 파일과 학습 데이터
- 감사 로그
- API 인증정보

## Threats and Controls

| 위협 | 예시 | 통제 |
|---|---|---|
| Unauthorized Access | 외부자가 증적 열람 | RBAC, SSO, MFA, tenant isolation |
| Data Leakage | 영상/공정 정보 유출 | 암호화, 마스킹, 최소저장, DLP |
| Prompt Injection | SOP 문서 내 악성 지시 | 문서 sanitization, schema validation |
| Model Tampering | 검증 안 된 모델 배포 | model signing, registry approval |
| Audit Log Alteration | 사고 로그 삭제/수정 | append-only, hash chain, WORM option |
| API Abuse | 대량 다운로드, credential misuse | rate limit, anomaly detection |
| Edge Device Compromise | 현장 서버 탈취 | disk encryption, cert rotation, secure boot option |

## Security Requirements

- TLS 1.2+ for all network traffic
- Encryption at rest
- Per-tenant keys for enterprise customers where required
- Fine-grained RBAC
- Evidence access audit
- Secrets in managed secret store
- Signed model artifacts
- Vulnerability scanning for container images
- Regular access review
