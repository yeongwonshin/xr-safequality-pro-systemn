# ModelOps Runbook

## Model Registration

1. 모델 artifact 업로드
2. signature/hash 생성
3. model card 작성
4. dataset version 연결
5. evaluation report 연결
6. safety review 승인
7. staging 배포
8. shadow/canary 배포
9. production promotion

## Model Card Fields

- model_name
- version
- task
- classes
- training_data_version
- evaluation_data_version
- metrics by class
- critical class FN analysis
- known limitations
- recommended thresholds
- deployment targets
- rollback version

## Drift Response

1. drift alert 확인
2. 현장/조명/작업자/설비 변경 여부 확인
3. low confidence 샘플 리뷰
4. false positive/negative 분류
5. threshold 임시 조정 또는 수동 승인 강화
6. 추가 라벨링/재학습
7. canary 재배포

## Incident: Confirmed False Negative

- 즉시 affected model route 중지 또는 threshold 강화
- 관련 고객/현장 영향 범위 확인
- incident ticket 생성
- 증적/로그 보존
- root cause analysis
- corrective action release
