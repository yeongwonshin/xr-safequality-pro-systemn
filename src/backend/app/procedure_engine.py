from dataclasses import dataclass
from typing import List, Optional, Dict, Any

@dataclass
class StepCondition:
    object_class: str
    required_state: Optional[str]
    min_confidence: float

@dataclass
class ProcedureStep:
    id: str
    title: str
    blocking: bool
    critical: bool
    conditions: List[StepCondition]


def _find_best_observation(condition: StepCondition, observations: List[Dict[str, Any]]):
    candidates = [o for o in observations if o.get("object_class") == condition.object_class]
    if condition.required_state is not None:
        candidates = [o for o in candidates if o.get("state") == condition.required_state]
    if not candidates:
        return None
    return max(candidates, key=lambda o: float(o.get("confidence", 0)))


def evaluate_step(step: ProcedureStep, observations: List[Dict[str, Any]]):
    failures = []
    uncertain = []

    for condition in step.conditions:
        obs = _find_best_observation(condition, observations)
        if obs is None:
            failures.append({
                "object_class": condition.object_class,
                "reason": "required observation missing",
            })
            continue

        confidence = float(obs.get("confidence", 0))
        if confidence < condition.min_confidence:
            uncertain.append({
                "object_class": condition.object_class,
                "confidence": confidence,
                "required": condition.min_confidence,
                "reason": "confidence below threshold",
            })

    if failures:
        return {
            "status": "blocked" if step.blocking else "fail",
            "action": "correct_and_retake" if step.blocking else "warn",
            "reasons": failures,
        }

    if uncertain:
        return {
            "status": "uncertain",
            "action": "retake_or_supervisor_approval" if step.critical else "retake",
            "reasons": uncertain,
        }

    return {"status": "pass", "action": "advance"}
