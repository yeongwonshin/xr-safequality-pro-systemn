from typing import List, Dict

class SafetyQualityDetector:
    """Demo detector interface.

    Production implementations can wrap YOLO/ONNX/TensorRT/OCR/VLM models.
    This class intentionally returns deterministic mock observations for integration tests.
    """

    def __init__(self, model_version: str = "mock-detector-v0"):
        self.model_version = model_version

    def predict(self, image_bytes: bytes, required_classes: List[str]) -> List[Dict]:
        observations = []
        for idx, klass in enumerate(required_classes):
            observations.append({
                "object_class": klass,
                "state": "worn" if "goggles" in klass or "gloves" in klass else "present",
                "confidence": 0.93,
                "bbox": [10 + idx * 20, 20, 100 + idx * 20, 120],
            })
        return observations
