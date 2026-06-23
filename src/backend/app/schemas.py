from pydantic import BaseModel
from typing import List, Optional

class EvidenceAsset(BaseModel):
    evidence_id: str
    media_type: str
    storage_uri: str
    sha256: str
    redaction_status: str

class StepEvaluation(BaseModel):
    session_id: str
    step_id: str
    result: str
    reasons: List[dict]
    sop_version: str
    model_version: str
    policy_version: str
    evidence_ids: List[str]

class OverrideRequest(BaseModel):
    session_id: str
    step_id: str
    worker_reason: str
    evidence_ids: List[str]
    requested_approver_role: str

class OverrideDecision(BaseModel):
    override_id: str
    approved: bool
    approver_id: str
    reason_code: str
    note: Optional[str] = None
