# Inference Pipeline

## Real-Time Inference Flow

1. 클라이언트가 프레임을 샘플링한다.
2. 개인정보 영역을 가능하면 로컬에서 마스킹한다.
3. Edge Gateway가 현재 SOP step에 필요한 모델만 로드한다.
4. CV runtime이 객체/상태/라벨 결과를 반환한다.
5. 결과는 procedure condition evaluator로 전달된다.
6. low confidence 또는 conflict가 있으면 재촬영/보조 모델/승인 절차를 호출한다.
7. 판단 결과와 증적은 audit event로 기록된다.

## Observation Schema

```json
{
  "session_id": "uuid",
  "step_id": "ppe-check",
  "timestamp": "2026-06-24T09:00:00+09:00",
  "model_version": "ppe-detector-v1.4.2",
  "observations": [
    {
      "object_class": "safety_goggles",
      "state": "worn",
      "confidence": 0.94,
      "bbox": [100, 80, 240, 190],
      "evidence_id": "uuid"
    }
  ]
}
```

## Optimization

- Step-aware model routing: 현재 단계에 필요한 클래스만 추론
- Frame skipping: 변화가 적으면 프레임 처리 빈도 감소
- Region-of-interest: 설비/부품 위치를 기준으로 ROI 제한
- Quantization: edge GPU/CPU 성능에 맞게 INT8/FP16 최적화
- Local cache: SOP, model, policy를 현장 캐시에 저장
