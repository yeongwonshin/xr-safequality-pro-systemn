# Confidence & Decision Policy

## Decision Levels

| Level | 설명 | 처리 |
|---|---|---|
| Green | 조건 충족, confidence 충분 | 자동 통과 |
| Yellow | 조건 충족 가능성 있으나 불확실 | 재촬영 또는 보조 검증 |
| Red | 조건 미충족 또는 위험 상태 | 중지/수정 요청 |
| Blue | AI로 판단 불가 | 수동 승인 또는 관리자 확인 |

## 기본 정책

```yaml
class_policies:
  safety_goggles:
    criticality: critical
    pass_threshold: 0.92
    uncertain_min: 0.70
    on_uncertain: retake_or_supervisor_approval
    on_fail: block_step
  screw_present:
    criticality: quality
    pass_threshold: 0.88
    uncertain_min: 0.65
    on_uncertain: retake
    on_fail: rework_required
```

## Conflict Resolution

- OCR은 맞지만 객체가 불일치: Yellow → 재촬영
- 객체는 맞지만 라벨 텍스트가 불일치: Red → 차단
- PPE 검출 불가: Blue → 재촬영 또는 승인자 확인
- 금지구역 진입: Red → 즉시 경고, 지속 시 관리자 알림

## Human Override

Human override는 다음 필드를 반드시 포함한다.

- 승인자 ID
- 사유 코드
- 자유기술 사유
- 증적 이미지
- 관련 step/model/policy version
- 후속 조치 필요 여부
