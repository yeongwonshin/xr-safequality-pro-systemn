# Procedure DSL

## 설계 목표

SOP 문서를 작업자가 실행 가능한 단계와 검증 조건으로 변환한다. LLM은 초안 생성에 활용하지만, 실제 현장 실행은 아래 DSL을 Procedure Engine이 해석한다.

## 기본 구조

```yaml
procedure:
  id: chem-lab-prep-001
  name: 유해화학물질 취급 전 준비 절차
  version: 1.0.0
  criticality: high
  owner_role: EHS_MANAGER
  steps:
    - id: ppe-check
      title: 필수 보호구 착용 확인
      type: visual_verification
      required_evidence: image
      blocking: true
      conditions:
        - object: safety_goggles
          state: worn
          min_confidence: 0.92
        - object: nitrile_gloves
          state: worn
          min_confidence: 0.90
      on_fail:
        action: block
        message: 보호구 착용이 확인되지 않았습니다.
```

## Step Types

| Type | 설명 |
|---|---|
| instruction | 안내만 표시 |
| visual_verification | 카메라 기반 상태 확인 |
| barcode_scan | QR/바코드 확인 |
| manual_confirm | 작업자 확인 |
| supervisor_approval | 승인자 확인 |
| measurement_input | 수치 입력/센서값 검증 |
| integration_check | MES/LIMS/QMS 등 외부 시스템 상태 확인 |

## Condition Operators

- `exists`: 객체 존재
- `not_exists`: 객체 부재
- `state_is`: 상태 일치
- `text_matches`: OCR/라벨 텍스트 매칭
- `within_zone`: 객체가 지정 영역 안에 있음
- `outside_zone`: 객체가 지정 영역 밖에 있음
- `sequence_after`: 선행 단계 완료 필요
- `measurement_between`: 수치 범위 확인

## Blocking Modes

| Mode | 설명 |
|---|---|
| block | 조건 미충족 시 진행 차단 |
| warn | 경고하되 진행 가능 |
| require_approval | 승인자 확인 필요 |
| record_only | 기록만 남김 |

## Versioning

- 모든 절차는 immutable version으로 저장한다.
- 세션 시작 시점의 procedure version을 고정한다.
- 개정 절차는 승인 워크플로우를 통과해야 production에 배포된다.
