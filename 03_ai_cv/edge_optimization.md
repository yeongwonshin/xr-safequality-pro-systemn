# Edge Optimization

## 왜 Edge가 필요한가

- 실시간 경고 지연 최소화
- 민감한 영상의 외부 전송 감소
- 네트워크 불안정 환경 대응
- 공장/연구실 데이터 주권 요구 충족

## Optimization Checklist

- 모델 ONNX 변환
- TensorRT 또는 OpenVINO 최적화
- FP16/INT8 quantization 테스트
- 클래스별 step-aware routing
- ROI crop inference
- FPS와 정확도 trade-off 정책
- 모델 warmup과 memory pinning
- batch inference와 low-latency mode 분리

## Edge Health Metrics

| Metric | 의미 |
|---|---|
| inference_latency_p95 | 추론 지연 |
| dropped_frames | 처리하지 못한 프레임 수 |
| model_load_time | 모델 로드 시간 |
| gpu_memory_usage | GPU 메모리 사용률 |
| sync_queue_depth | 클라우드 동기화 대기 이벤트 |
| offline_duration | 네트워크 단절 시간 |

## Degraded Mode

- 모델 일부 불가: 해당 step만 수동 승인 모드
- 네트워크 불가: 로컬 캐시에 이벤트 저장
- 스토리지 부족: 증적 압축/저위험 스냅샷 삭제 정책 적용
- Edge 장애: critical 작업 시작 차단, non-critical 작업은 모바일/클라우드 fallback
