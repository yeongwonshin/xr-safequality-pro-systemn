from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from .procedure_engine import StepCondition, ProcedureStep, evaluate_step

app = FastAPI(title="XR SafeQuality Pro API", version="1.0.0")

class Observation(BaseModel):
    object_class: str
    state: Optional[str] = None
    confidence: float
    bbox: Optional[List[float]] = None
    evidence_id: Optional[str] = None

class ObservationRequest(BaseModel):
    session_id: str
    step_id: str
    model_version: str
    policy_version: str
    observations: List[Observation]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/inspection-sessions/{session_id}/observations")
def submit_observation(session_id: str, request: ObservationRequest):
    # Demo step. Production system loads this from approved Procedure DSL.
    step = ProcedureStep(
        id=request.step_id,
        title="PPE Check",
        blocking=True,
        critical=True,
        conditions=[
            StepCondition(object_class="safety_goggles", required_state="worn", min_confidence=0.92),
            StepCondition(object_class="nitrile_gloves", required_state="worn", min_confidence=0.90),
        ],
    )
    result = evaluate_step(step, [obs.model_dump() for obs in request.observations])
    return {
        "session_id": session_id,
        "step_id": request.step_id,
        "result": result["status"],
        "action": result.get("action"),
        "reasons": result.get("reasons", []),
        "model_version": request.model_version,
        "policy_version": request.policy_version,
    }
