from src.backend.app.procedure_engine import ProcedureStep, StepCondition, evaluate_step


def test_step_passes_when_required_ppe_detected():
    step = ProcedureStep(
        id="ppe-check",
        title="PPE Check",
        blocking=True,
        critical=True,
        conditions=[
            StepCondition("safety_goggles", "worn", 0.92),
            StepCondition("nitrile_gloves", "worn", 0.90),
        ],
    )
    observations = [
        {"object_class": "safety_goggles", "state": "worn", "confidence": 0.96},
        {"object_class": "nitrile_gloves", "state": "worn", "confidence": 0.95},
    ]
    assert evaluate_step(step, observations)["status"] == "pass"


def test_step_blocks_when_required_object_missing():
    step = ProcedureStep(
        id="ppe-check",
        title="PPE Check",
        blocking=True,
        critical=True,
        conditions=[StepCondition("nitrile_gloves", "worn", 0.90)],
    )
    assert evaluate_step(step, [])["status"] == "blocked"


def test_step_uncertain_when_confidence_low():
    step = ProcedureStep(
        id="ppe-check",
        title="PPE Check",
        blocking=True,
        critical=True,
        conditions=[StepCondition("nitrile_gloves", "worn", 0.90)],
    )
    observations = [{"object_class": "nitrile_gloves", "state": "worn", "confidence": 0.72}]
    result = evaluate_step(step, observations)
    assert result["status"] == "uncertain"
    assert result["action"] == "retake_or_supervisor_approval"
