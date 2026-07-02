#!/usr/bin/env python3
"""
 Enter module docstring here
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------
from typing import Literal

# ---------- Third Party Imports ----------
from pydantic import BaseModel, ConfigDict, Field

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