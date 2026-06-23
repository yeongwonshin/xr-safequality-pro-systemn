# Dataset Specification

## Dataset Unit

```json
{
  "tenant_id": "acme-lab",
  "site_id": "lab-a",
  "procedure_id": "chem-prep-001",
  "step_id": "ppe-check",
  "image_id": "uuid",
  "timestamp": "2026-06-24T09:00:00+09:00",
  "camera_context": {
    "device_type": "mobile|xr|fixed",
    "lighting": "normal|low|backlight",
    "distance_m": 0.8,
    "angle": "front|side|top"
  },
  "annotations": [
    {
      "class": "safety_goggles",
      "bbox": [100, 50, 220, 180],
      "mask_ref": "optional",
      "state": "worn|not_worn|unknown",
      "criticality": "critical"
    }
  ],
  "privacy": {
    "face_blurred": true,
    "contains_personal_data": true,
    "retention_days": 90
  }
}
```

## Class Taxonomy

### PPE
- safety_goggles
- face_shield
- lab_coat
- nitrile_gloves
- respirator
- safety_helmet
- esd_wrist_strap

### Lab Objects
- reagent_bottle
- waste_container
- fume_hood
- pipette
- centrifuge_tube
- chemical_label
- ghs_pictogram

### Manufacturing Objects
- screw
- washer
- connector
- valve
- gauge
- panel_cover
- battery_cell
- semiconductor_wafer_carrier

### Zone/State
- restricted_zone
- safe_zone
- spill_area
- open_guard
- closed_guard
- power_off_indicator
- lockout_tag

## Split Policy

- Train/validation/test는 단순 이미지 랜덤 분할 금지
- 현장, 촬영자, 조명, 설비 ID 기준으로 holdout set 구성
- 테스트셋에는 반드시 hard negative 포함
- Critical 클래스는 false negative 사례를 별도 리뷰

## Data Quality Checks

- 클래스 불균형 리포트
- 라벨 누락/중복 검출
- 이미지 blur/occlusion 점수
- 개인정보 마스킹 여부
- 현장/시간대/장비별 편향 점검
