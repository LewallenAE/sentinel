#!/usr/bin/env python3
"""
 Enter module docstring here
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------


# ---------- Third Party Imports ----------


# ---------- Project Level Imports ----------
from sentinel.ml.schemas import EvalCase, OracleResult

# ---------- Begin File ----------


def exact_match_score(case: EvalCase, output: str) -> OracleResult:
    expected = case.expected_output.strip()
    actual = output.strip()
    passed = actual == expected

    return OracleResult(
        passed = passed,
        reward=1.0 if passed else 0.0,
        oracle_type="exact_match",
        reason=(
            "output matched expected_output"
            if passed
            else f"expected {expected!r}, got {actual!r}"
        ),
    )