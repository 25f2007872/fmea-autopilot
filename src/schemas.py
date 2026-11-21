from pydantic import BaseModel
from typing import Optional

class QualityEvent(BaseModel):
    event_id: str
    source_file: str
    file_hash: str            # for idempotency
    process_step: str
    failure_mode: str
    effect: str
    cause: Optional[str]
    current_controls: Optional[str]
    severity_hint: Optional[str]
    extraction_confidence: float

class FMEARow(BaseModel):
    failure_mode_id: str
    process_step: str
    failure_mode: str
    effects: list[str]
    causes: list[str]
    severity: int             # 1-10
    occurrence: int           # 1-10, derived from event count
    detection: int            # 1-10
    rpn: int
    reasoning: str
    source_event_ids: list[str]   # traceability
    needs_review: bool