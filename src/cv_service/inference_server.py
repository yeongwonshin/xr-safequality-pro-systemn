from fastapi import FastAPI, UploadFile, File, Form
from typing import List
from detector import SafetyQualityDetector

app = FastAPI(title="XR SafeQuality Edge Inference", version="1.0.0")
detector = SafetyQualityDetector(model_version="mock-detector-v0")

@app.get("/health")
def health():
    return {"status": "ok", "model_version": detector.model_version}

@app.post("/v1/infer")
async def infer(file: UploadFile = File(...), required_classes: str = Form("safety_goggles,nitrile_gloves")):
    image_bytes = await file.read()
    classes: List[str] = [c.strip() for c in required_classes.split(",") if c.strip()]
    observations = detector.predict(image_bytes, classes)
    return {"model_version": detector.model_version, "observations": observations}
