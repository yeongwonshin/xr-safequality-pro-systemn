# Privacy by Design

## Data Minimization

- 전체 영상 저장 대신 이벤트 기반 스냅샷 저장
- 얼굴/명찰/개인 화면은 로컬 또는 엣지에서 마스킹
- 작업자 성과 분석은 안전·품질 목적에 한정
- 위치 데이터는 zone 수준으로 최소화

## Consent and Notice

- 고객 조직은 작업자에게 카메라 기반 점검의 목적, 수집 항목, 보존기간, 접근권한을 고지해야 한다.
- 개인별 평가/징계 활용 여부는 고객의 노사/법무 정책을 따라야 한다.

## Retention

- Low-risk evidence: 짧은 보존기간
- Critical incident evidence: 장기보관 가능
- 학습 데이터 사용: 별도 동의/계약/비식별화 필요

## Access Controls

| 데이터 | 기본 접근자 |
|---|---|
| 본인 작업 리포트 | 작업자, 리더 |
| 현장 통계 | Supervisor, EHS, QA |
| 증적 이미지 | 권한 있는 관리자/감사자 |
| 모델 학습 데이터 | ML Ops 제한 접근 |
| 개인정보 export/delete | Privacy/Admin 역할 |

## Privacy Risk Review

- 영상에 얼굴이 필요한가?
- 명찰/화이트보드/공정기밀이 노출되는가?
- 데이터가 고객 외부로 전송되는가?
- 고객 간 데이터가 섞일 가능성은 없는가?
- 보존기간 만료 후 삭제가 검증되는가?
