from typing import Any
from pydantic import BaseModel, Field

class HydraulicRequest(BaseModel):
    features: dict[str, float] = Field(description="Exactly 170 cycle-level features in notebook schema")

class IMSRequest(BaseModel):
    test: str = Field(pattern="^(1st_test|2nd_test|3rd_test)$")
    features: dict[str, float] = Field(description="10 IMS snapshot feature values from notebook")

class Result(BaseModel):
    type: str
    target: str
    predicted_class: int | None = None
    score: float | None = None
    alarm: bool | None = None
    threshold: float | None = None
    details: dict[str, Any] = Field(default_factory=dict)
