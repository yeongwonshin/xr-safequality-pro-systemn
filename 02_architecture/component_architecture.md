# Component Architecture

## Components

| 컴포넌트 | 역할 | 기술 후보 |
|---|---|---|
| XR/Mobile Client | 작업 안내, 카메라 스트림, XR 오버레이, 알림 | WebRTC, WebXR, Unity, native XR SDK |
| Edge Inference Gateway | 저지연 모델 추론, 현장 캐시, 영상 최소화 | Python, Triton, ONNX Runtime, TensorRT |
| CV Service | 객체/세그먼트/OCR/포즈/구역 인식 | YOLO 계열, SAM 계열, OCR, Pose Estimation |
| Procedure Engine | SOP 상태머신, 조건 판정, 예외 승인 | Python/FastAPI, rules engine, DSL parser |
| Evidence Service | 이미지/비디오 스냅샷, hash, 보존정책 | S3-compatible object storage |
| Audit Service | 불변 이벤트 로그, 감사 리포트 | PostgreSQL, Kafka, WORM storage option |
| Admin Dashboard | KPI, 리포트, SOP 관리, 승인 | Next.js/React, BI charts |
| Model Registry | 모델 버전, 성능, 배포 상태 | MLflow, custom registry |
| Integration Hub | MES/QMS/LIMS/EHS/SSO 연동 | REST, Webhook, MQTT, OPC-UA adapter |
| LLM SOP Structurer | SOP 문서 파싱, 절차 초안 생성, 설명 | RAG, JSON schema constrained generation |

## Data Domains

- Tenant/Organization
- Site/Zone/Asset
- User/Role/Approval
- SOP/Procedure/Step/Condition
- Inspection Session
- Detection Event
- Evidence Asset
- Incident/Near-miss
- Model/Policy Version
- Audit Log

## Runtime Flow

1. 작업자가 클라이언트에서 작업 세션을 시작한다.
2. Procedure Engine이 SOP 버전과 현재 단계 조건을 내려준다.
3. 클라이언트가 프레임 또는 스냅샷을 Edge Gateway에 전송한다.
4. CV Service가 객체/라벨/상태/구역 결과를 반환한다.
5. Procedure Engine이 결과와 정책을 비교해 단계 상태를 판정한다.
6. Client는 XR 오버레이와 경고를 표시한다.
7. Evidence/Audit Service는 증적과 판단 로그를 저장한다.
8. Dashboard는 실시간/배치 분석을 제공한다.

## Fail-Safe Behavior

| 상황 | 동작 |
|---|---|
| 모델 confidence 낮음 | 재촬영/수동 승인 요구 |
| 네트워크 장애 | 로컬 절차 캐시 사용, 이벤트 큐 저장 |
| Edge 장애 | 저위험 단계는 클라우드 추론 fallback, 고위험 단계는 중지 |
| SOP 버전 충돌 | 세션 시작 시점 버전 고정, 변경 시 다음 세션부터 반영 |
| 영상 저장 실패 | critical 단계 통과 차단 또는 증적 재수집 |
