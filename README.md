# XR SafeQuality Pro System

**주제:** XR 안전 점검·품질검사 전문 시스템  
**목표:** 작업자가 부품 조립, 설비 점검, 실험 준비, 폐기 절차를 수행할 때 XR/모바일 카메라와 AI 절차 엔진이 실시간으로 상태를 확인하고, 누락·오류·위험행동을 차단하며, 감사 가능한 기록을 남기는 B2B SaaS/온프레미스 혼합 시스템.

이 디렉토리는 단순 MVP가 아니라 **상용 제품 기획 + 시스템 아키텍처 + AI/CV 파이프라인 + LLM 절차 엔진 + 관리자 대시보드 + 보안/컴플라이언스 + 운영 Runbook + 샘플 코드**까지 포함한 전문 시스템 패키지입니다.

## 핵심 제품 정의

- **현장 클라이언트:** 스마트폰 웹앱, 태블릿, XR 글래스 앱
- **실시간 감지:** PPE, 라벨, 부품, 나사, 밸브, 금지구역, 위험 자세, 순서 오류
- **절차 강제:** SOP를 DSL/YAML로 등록하고 LLM이 문서에서 절차 후보를 구조화하되, 실행 시에는 규칙 엔진과 검증 가능한 상태머신으로 통제
- **관리자 대시보드:** 작업별 합격/불합격, near-miss, 반복 오류, 현장별 리스크, 모델 신뢰도, 증적 이미지
- **수익모델:** 안전관리 SaaS, 공장/연구실/교육기관 라이선스, 산업별 절차팩, 온프레미스 프리미엄, API 과금

## 추천 시작 순서

1. `00_product/PRD.md`와 `01_requirements/system_requirements.md`로 제품 범위를 이해합니다.
2. `02_architecture/component_architecture.md`와 `02_architecture/sequence_realtime_inspection.mmd`로 시스템 흐름을 봅니다.
3. `04_llm_procedure_engine/procedure_dsl.md`와 샘플 YAML로 절차 엔진 구조를 확인합니다.
4. `06_backend/api_openapi.yaml`, `06_backend/database_schema.sql`, `src/backend/app/main.py`로 구현 골격을 확인합니다.
5. `08_safety_quality_compliance/`와 `09_security_privacy/`로 기업 납품에 필요한 통제 항목을 확인합니다.

## 디렉토리 맵

```text
XR SafeQuality Pro System
├── 00_product/                  # 사업화·시장·가격·로드맵
├── 01_requirements/             # 제품 요구사항·수용기준·유스케이스
├── 02_architecture/             # 전체 아키텍처·데이터 흐름·시퀀스
├── 03_ai_cv/                    # 객체/세그먼트/행동 인식 파이프라인
├── 04_llm_procedure_engine/     # SOP 구조화·절차 DSL·가드레일
├── 05_xr_client/                # XR/모바일 UX 및 오프라인 동작
├── 06_backend/                  # API, DB, 이벤트 스키마
├── 07_admin_dashboard/          # 관리자/감사/분석 대시보드
├── 08_safety_quality_compliance/# ISO/OSHA/NIST 매핑과 SOP
├── 09_security_privacy/         # 보안·개인정보·영상 거버넌스
├── 10_operations/               # 배포·모니터링·MLOps·고객 온보딩
├── 11_pilot_kpi/                # 파일럿 설계·ROI·KPI
├── src/                         # 샘플 구현 코드 골격
├── infra/                       # Docker/Kubernetes 배포 예시
├── samples/                     # 샘플 데이터·리포트
└── tests/                       # 절차 엔진 테스트
```

## 제품 포지셔닝 문장

> “XR SafeQuality는 현장 작업의 안전·품질 절차를 카메라 기반 AI와 검증 가능한 절차 엔진으로 실시간 강제하고, 모든 예외와 증적을 감사 가능한 형태로 남기는 산업용 Safety & Quality Assurance Platform입니다.”

## 주의

이 패키지는 상용 시스템 설계와 구현 골격입니다. 실제 도입 시에는 고객 현장별 위험성 평가, 법무 검토, 개인정보 영향평가, 네트워크 보안 심사, 모델 성능 검증, 현장 파일럿을 반드시 수행해야 합니다.
