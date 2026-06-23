# Mobile First → XR Glasses Expansion

## Mobile First 이유

- 고객 PoC 진입 장벽이 낮다.
- 별도 하드웨어 구매 전 가치 검증 가능하다.
- 카메라 기반 CV와 절차 엔진의 핵심 위험을 먼저 검증할 수 있다.
- 관리자 대시보드와 감사 로그는 디바이스와 무관하게 재사용된다.

## XR 전환 시 추가 기능

- 핸즈프리 작업 안내
- 시야 중심의 오버레이
- 공간 앵커 기반 체크포인트
- 음성/제스처 명령
- 장시간 착용성 및 배터리 관리
- MDM 기반 기기 관리

## Device Abstraction Layer

```text
Client Core
├── Procedure Session Manager
├── Evidence Capture
├── Observation Sync
├── Alert Renderer
└── Device Adapter
    ├── Mobile Web Adapter
    ├── Android Native Adapter
    ├── iOS Native Adapter
    ├── Unity XR Adapter
    └── WebXR Adapter
```

## XR Readiness Checklist

- 현장 Wi-Fi/5G 품질
- 디바이스 착용 안전성
- 작업자 PPE와 글래스 간섭 여부
- 클린룸/방폭/화학물질 환경 적합성
- 배터리 운영 정책
- 기기 분실/파손/계정 관리
