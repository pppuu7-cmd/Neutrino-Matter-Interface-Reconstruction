import math

import pytest

from nmir.lee_mitigation_gap import (
    G0053_5SIGMA_DELTA30,
    classify_public_evidence,
    projected_residuals,
    residual_gap,
)


def test_projection_residuals_are_frozen_arithmetic():
    vals = projected_residuals()
    assert math.isclose(vals[10], G0053_5SIGMA_DELTA30 / 10.0, rel_tol=1e-15)
    assert math.isclose(vals[100], G0053_5SIGMA_DELTA30 / 100.0, rel_tol=1e-15)
    assert vals[10] > vals[100] > 1.0


def test_mechanism_without_public_factor_stays_quantitatively_open():
    assert classify_public_evidence(
        demonstrated_mechanism=True, comparable_measured_factor=False
    ) == "MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN"


def test_measured_factor_would_promote_gate():
    assert classify_public_evidence(
        demonstrated_mechanism=True, comparable_measured_factor=True
    ) == "PASS_MEASURED_LEE_MITIGATION_FACTOR"


def test_no_handle_fails():
    assert classify_public_evidence(
        demonstrated_mechanism=False, comparable_measured_factor=False
    ) == "FAIL_NO_LEE_MITIGATION_HANDLE"


def test_invalid_gap_inputs_fail_closed():
    with pytest.raises(ValueError):
        residual_gap(0.0, 10.0)
    with pytest.raises(ValueError):
        residual_gap(10.0, 0.0)
