# PPE & Zone Policy

## Zone Types

| Zone | 설명 | 기본 정책 |
|---|---|---|
| Safe Zone | 일반 구역 | 기록만 |
| PPE Required Zone | PPE 필요 구역 | PPE 미착용 경고/차단 |
| Restricted Zone | 허가자만 진입 | 진입 감지 시 즉시 경고 |
| Critical Hazard Zone | 고위험 구역 | 2인 승인 또는 작업허가 필요 |
| Cleanroom Zone | 청정도/ESD 등 요구 | 복장/장비 조건 검증 |

## PPE Rule Example

```yaml
zone_policy:
  id: wet-lab-zone-a
  required_ppe:
    - safety_goggles
    - lab_coat
    - nitrile_gloves
  entry_condition:
    min_confidence: 0.90
    on_missing: block_entry
  violation_escalation:
    local_warning_seconds: 0
    supervisor_alert_seconds: 10
    incident_ticket_seconds: 60
```

## Zone Detection Options

- QR/Beacon 기반 위치 확인
- 카메라 기반 바닥 라인/표식 세그먼테이션
- 고정 카메라와 작업자 디바이스 조합
- UWB/BLE/RTLS 연동
- 수동 zone check-in + 카메라 검증
