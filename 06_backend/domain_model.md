# Domain Model

## Core Entities

### Tenant
- 고객 조직 단위
- 데이터 격리의 최상위 경계

### Site
- 공장, 연구실, 캠퍼스, 건물, 라인

### Zone
- 안전구역, 금지구역, 위험구역, 클린룸 등

### Asset
- 설비, 장비, 제품, fixture, 작업대

### Procedure
- SOP의 실행 가능한 구조화 버전
- 여러 version 보유

### Step
- procedure 내 하나의 작업 단위
- 조건, 증적, blocking policy 포함

### InspectionSession
- 작업자가 특정 procedure를 실행한 단위

### DetectionEvent
- CV 모델이 반환한 객체/상태/라벨 관찰값

### EvidenceAsset
- 이미지/비디오/센서값/문서/서명 등 증적

### AuditEvent
- 시스템/사용자/승인자/모델 판단의 불변 로그

### Incident
- fail, near-miss, override, 품질 불량, 안전 위반 이벤트

## Relationship Summary

```text
Tenant 1..n Site
Site 1..n Zone
Site 1..n Asset
Tenant 1..n Procedure
Procedure 1..n ProcedureVersion
ProcedureVersion 1..n Step
ProcedureVersion 1..n InspectionSession
InspectionSession 1..n DetectionEvent
InspectionSession 1..n EvidenceAsset
InspectionSession 1..n AuditEvent
DetectionEvent 0..1 Incident
```
