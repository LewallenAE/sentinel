#!/usr/bin/env python3
"""
 Enter module docstring here
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------
from typing import Literal

# ---------- Third Party Imports ----------
from pydantic import BaseModel, ConfigDict, Field, model_validator

# ---------- Project Level Imports ----------


# ---------- Begin File ----------

class EvalCase(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    
    case_id: str
    prompt: str
    expected_output: str
    

class OracleResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    
    passed: bool
    reward: float = Field(ge=0.0, le=1.0)
    oracle_type: Literal["exact_match"]
    reason: str


class EvalResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    
    run_id: str
    total_cases: int = Field(ge=0)
    passed_cases: int = Field(ge=0)
    failed_cases: int = Field(ge=0)
    mean_reward: float = Field(ge=0.0, le=1.0)
    
    @model_validator(mode="after")
    def validate_case_count(self) -> "EvalResult":
        if self.total_cases != self.passed_cases + self.failed_cases:
            raise ValueError("total_cases must equal passed_cases + failed_cases")
        return self 