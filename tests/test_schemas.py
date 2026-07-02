#!/usr/bin/env python3
"""
 Enter module docstring here
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------


# ---------- Third Party Imports ----------
import pytest
from pydantic import ValidationError

# ---------- Project Level Imports ----------
from sentinel.ml.schemas import EvalCase

# ---------- Begin File ----------





def test_eval_case_can_be_created() -> None:
    case = EvalCase(
        case_id="math-001",
        prompt="Return 2+2",
        expected_output="4",
    )
    
    assert case.case_id =="math-001"
    assert case.prompt == "Return 2+2"
    assert case.expected_output == "4"
    
def test_eval_case_stores_prompt() -> None:
    case = EvalCase(
        case_id = "tool-001",
        prompt = "Use the calculator tool to add 10 and 5",
        expected_output = "15",
    )
    
    assert case.prompt == "Use the calculator tool to add 10 and 5"
    
# Purposeful broken test to prove frozen = True works

def tests_eval_case_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        case = EvalCase(
            case_id = "test-01",
            prompt = "Is the prompt working",
            expected = "This will fail",
        )
    
        assert case.expected == "This will fail"