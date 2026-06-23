# Admin Dashboard Specification

## Dashboard Sections

### 1. Executive Overview
- 현장별 safety score
- 품질 gate pass rate
- near-miss 추세
- critical block 이벤트
- 감사 리포트 생성 상태

### 2. Live Operations
- 현재 진행 중인 작업 세션
- blocked/uncertain step
- 승인 요청 큐
- Edge gateway health

### 3. Procedure Analytics
- SOP별 실패율
- 단계별 평균 소요시간
- 재촬영/재시도 횟수
- 자주 발생하는 누락 항목

### 4. Quality Analytics
- 공정/제품/설비별 불량 유형
- 나사/부품 누락 heatmap
- 재작업 전후 비교
- 검사자/교대조별 편차

### 5. Safety Analytics
- PPE 미착용 빈도
- 금지구역 진입 추세
- 위험 작업 예외 승인
- near-miss 유형 분포

### 6. Model Operations
- 모델 버전별 성능
- class별 confidence 분포
- drift/unknown 이벤트
- human override와 모델 판단 불일치

### 7. Audit Center
- 세션별 증적 조회
- SOP/정책/모델 버전 이력
- 승인자 override 이력
- PDF/CSV export

## 권한별 화면

| 역할 | 주요 권한 |
|---|---|
| Worker | 본인 작업 세션 조회 |
| Supervisor | 승인 요청 처리, 팀 현황 조회 |
| EHS Manager | 안전 정책, incident, 리포트 |
| QA Manager | 품질 gate, 불량 분석, QMS 연동 |
| Admin | 사용자/권한/SSO/테넌트 설정 |
| Auditor | 읽기 전용 감사 export |
