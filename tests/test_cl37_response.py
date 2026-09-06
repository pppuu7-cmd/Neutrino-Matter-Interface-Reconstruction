import pytest
from nmir.cl37_response import CL37_THRESHOLD_MEV, cl37_sigma_cm2, load_cl37_response


def test_cl37_frozen_table_identity():
    pts = load_cl37_response()
    assert len(pts) == 19
    assert pts[0].energy_mev == pytest.approx(1.0)
    assert pts[0].improved_cm2 == pytest.approx(5.21e-46)
    assert pts[-1].energy_mev == pytest.approx(30.0)
    assert pts[-1].improved_cm2 == pytest.approx(8.20e-41)


def test_cl37_threshold_and_anchor():
    assert cl37_sigma_cm2(0.0) == 0.0
    assert cl37_sigma_cm2(CL37_THRESHOLD_MEV) == 0.0
    assert 0.0 < cl37_sigma_cm2(0.9) < cl37_sigma_cm2(1.0)


def test_cl37_improved_reference_points():
    assert cl37_sigma_cm2(5.0) == pytest.approx(5.38e-44)
    assert cl37_sigma_cm2(10.0) == pytest.approx(3.00e-42)
    assert cl37_sigma_cm2(15.0) == pytest.approx(1.33e-41)


def test_cl37_fails_closed_above_table():
    with pytest.raises(ValueError):
        cl37_sigma_cm2(30.1)
    with pytest.raises(ValueError):
        cl37_sigma_cm2(5.0, branch="invalid")
