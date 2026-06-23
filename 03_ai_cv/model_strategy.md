# AI/CV Model Strategy

## 모델 계층

| 계층 | 목적 | 기술 후보 |
|---|---|---|
| Object Detection | PPE, 도구, 부품, 나사, 용기, 밸브 검출 | YOLO 계열, RT-DETR, EfficientDet |
| Segmentation | 금지구역, 작업영역, spill, 폐기물 영역 | Segment Anything 계열, Mask2Former |
| OCR/Label Recognition | 시약명, 농도, Lot, 유효기간, 바코드 | OCR engine, barcode/QR reader, VLM 보조 |
| Pose/Action | 보호구 착용, 손 위치, 위험 자세, 순서 행동 | pose estimation, temporal action model |
| Template Matching | 나사 위치, 부품 방향, 설비 상태 | keypoint/template matching, CAD alignment |
| Anomaly Detection | 미등록 상태, 이물, 예외 패턴 | visual anomaly detection, embedding similarity |

## 산업별 우선 모델

### 연구실
- PPE detection
- 시약 라벨 OCR
- 폐기 용기/라벨 검출
- 후드 sash 위치/장비 상태 검출

### 배터리/반도체
- 나사/부품 검출
- 방향성 부품 상태 판정
- 장갑/ESD wrist strap 확인
- 설비 패널/밸브/게이지 상태 확인

### 화학/바이오
- PPE, 라벨, GHS pictogram
- 위험구역/출입구역 인식
- 폐기 절차 상태 확인

## Confidence Policy

- Critical class는 precision보다 recall을 우선한다.
- 단, 불필요한 작업 중단을 줄이기 위해 다단계 검증을 적용한다.
  1. 1차 검출
  2. 재프레임/재촬영 요청
  3. 보조 모델 또는 OCR/바코드 교차검증
  4. supervisor approval

## Model Lifecycle

1. 고객 현장 kickoff: 객체 목록, 위험 등급, 촬영 조건 정의
2. 데이터 수집: consent/policy에 따른 샘플 촬영
3. 라벨링: 클래스 정의, negative sample, hard case 포함
4. 학습: base model fine-tuning
5. 검증: 현장 조명/각도/장갑/가림 조건 포함
6. 배포: canary rollout
7. 모니터링: drift, false positive/negative, retry rate
8. active learning: 낮은 confidence, 승인자 override 이벤트 우선 라벨링
