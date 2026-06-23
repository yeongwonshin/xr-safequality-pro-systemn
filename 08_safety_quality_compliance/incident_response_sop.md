# Incident Response SOP

## Incident Types

- Critical safety violation
- Restricted zone entry
- PPE non-compliance
- Quality gate failure
- AI false negative confirmed
- Data/privacy incident
- System outage affecting critical work

## Response Flow

1. 이벤트 감지
2. 작업자 즉시 경고 및 진행 차단
3. 현장 리더/관리자 알림
4. 증적 snapshot 고정
5. 사건 등급 분류
6. 원인 조사
7. corrective/preventive action 등록
8. 재발 방지 조치 완료 확인
9. 리포트 발행

## Severity

| 등급 | 예시 | 대응 |
|---|---|---|
| Sev1 | 중대 안전 위험, 실제 사고, critical FN | 즉시 중단, 관리자/고객 책임자 통보 |
| Sev2 | 반복 critical block, 금지구역 진입 | 당일 조사, CAPA 생성 |
| Sev3 | non-critical 품질 실패 | 표준 재작업/리포트 |
| Sev4 | 단순 시스템 경고 | 모니터링/배치 처리 |

## Post-Incident Review

- SOP가 충분했는가?
- 모델이 놓쳤는가?
- threshold가 적절했는가?
- 작업자 UX가 혼동을 유발했는가?
- 교육/코칭/현장 표식 개선이 필요한가?
- 데이터 라벨링/모델 재학습이 필요한가?
