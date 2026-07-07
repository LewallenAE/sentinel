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
from sentinel.ml.schemas import EvalCase, OracleResult, EvalResult, ToolSpec, ToolCall, Observation

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
    

def test_eval_case_requires_expected_output() -> None:
    with pytest.raises(ValidationError) as exc_info:
        EvalCase(
            case_id = "test-01",
            prompt ="Prompt here"
        )
    assert "expected_output" in str(exc_info.value)
        

def test_oracle_result_can_be_created() -> None:
    OracleResult(
        passed = True,
        reward = 0.5,
        oracle_type = "exact_match",
        reason = "output matched expected_output",        
    )

def test_oracle_result_rejects_invalid_reward() -> None:
    with pytest.raises(ValidationError):
        OracleResult(
            passed = True,
            reward = -0.5,
            oracle_type = "exact_match",
            reason = "output matched expected_output",        
    )

def test_oracle_result_requires_oracle_type() -> None:
    with pytest.raises(ValidationError) as exc_info:
        OracleResult(
            passed = True,
            reward = 0.5,
            reason = "output matched expected_output", 
        )
        
    assert "oracle_type" in str(exc_info.value)


def test_oracle_result_rejects_unknown_oracle_type() -> None:
    with pytest.raises(ValidationError):
        OracleResult(
            passed = True,
            reward = 0.5,
            oracle_type = "judge_model",
            reason = "Not supported yet",
        )

def test_oracle_result_requires_passed() -> None:
    with pytest.raises(ValidationError) as exc_info:
        OracleResult(
            reward = 0.5,
            oracle_type = "exact_match",
            reason = "Not supported yet",
        )
    assert "passed" in str(exc_info.value)
    
def test_eval_result_can_be_created() -> None:
    eval_result = EvalResult(
        run_id = "test-01",
        total_cases = 20,
        passed_cases = 17,
        failed_cases = 3,
        mean_reward = 0.43,
    )
    
    assert eval_result.run_id == "test-01"
    assert eval_result.total_cases == 20
    assert eval_result.passed_cases == 17
    assert eval_result.failed_cases == 3
    assert eval_result.mean_reward == 0.43
    
def test_eval_result_error_mentions_case_count_invariant() -> None:
    with pytest.raises(ValidationError) as exc_info:
        EvalResult(
            run_id = "run-bad",
            total_cases = 100,
            passed_cases = 90,
            failed_cases = 90,
            mean_reward = 0.5,
        )
    assert "total_cases must equal passed_cases + failed_cases" in str(exc_info.value)
    
def test_tool_spec_can_be_created() -> None:
    tool = ToolSpec(
        name="calculator",
        description="Evaluates a simple arithmetic expression.",
        input_schema={"expression":"str"},
        timeout_seconds=5,
    )
    
    assert tool.name == "calculator"
    assert tool.description == "Evaluates a simple arithmetic expression."
    assert tool.input_schema == {"expression":"str"}
    assert tool.timeout_seconds == 5
    

def test_tool_call_can_be_created() -> None:
    call = ToolCall(
        call_id="call-001",
        tool_name="calculator",
        arguments = {"expression": "10+5"},
    )
    
    assert call.call_id == "call-001"
    assert call.tool_name == "calculator"
    assert call.arguments == {"expression": "10+5"} 
    

def test_observation_can_be_created() -> None:
    
    observation = Observation(
        call_id = "call-001",
        tool_name = "calculator",
        stdout = "15",
        stderr = "none",
        exit_code = 0,
        latency_ms = 10
    )
    
    assert observation.call_id == "call-001"
    assert observation.tool_name == "calculator"
    assert observation.stdout == "15"
    assert observation.stderr == "none"
    assert observation.exit_code == 0
    assert observation.latency_ms == 10