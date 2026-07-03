#!/usr/bin/env python3
"""
 Enter module docstring here
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------


# ---------- Third Party Imports ----------


# ---------- Project Level Imports ----------
from sentinel.evals.scorers import exact_match_score
from sentinel.ml.schemas import EvalCase

# ---------- Begin File ----------


def test_exact_match_score_passes_matching_output() -> None:
    case = EvalCase(
        case_id="math-001",
        prompt="Return 2 + 2",
        expected_output="4"
    )
    
    result = exact_match_score(case, output="4")
    
    assert result.passed is True
    assert result.reward == 1
    assert result.oracle_type == "exact_match"
    

def test_exact_match_score_fails_non_matching_output() -> None:
    case = EvalCase(
        case_id="math-001",
        prompt="Return 2 + 2.",
        expected_output="4",
    )

    result = exact_match_score(case, output="5")

    assert result.passed is False
    assert result.reward == 0.0
    assert "expected '4', got '5'" in result.reason
    
def test_exact_match_whitespace_behavior() -> None:
    case = EvalCase(
        case_id="math-001",
        prompt="Return 2 + 2",
        expected_output="4",
    )
    
    result = exact_match_score(case, output=" 4 ")
    
    assert result.passed is True
    assert result.reward == 1.0
    assert result.reason == "output matched expected_output"
    
def test_exact_match_whitespace_does_not_hide_wrong_answer() -> None:
    case = EvalCase(
        case_id="math-001",
        prompt="Return 2 + 2",
        expected_output="4",
    )

    result = exact_match_score(case, output=" 5 ")

    assert result.passed is False
    assert result.reward == 0.0
    assert result.oracle_type == "exact_match"
    assert "expected '4', got '5'" in result.reason