import math

import pytest

from nmir.background_nuisance import (
    asimov_significance_with_background_uncertainty,
    max_background_for_significance_with_uncertainty,
)

SCENARIOS = (10.0, 11.84624201853375, 9.909735084)
DELTAS = (0.0, 0.10, 0.30, 0.50)
KNOWN_0050 = {
    (10.0, 3.0): 8.22524098773645,
    (10.0, 5.0): 1.7175266766193094,
    (11.84624201853375, 3.0): 12.098668408825569,
    (11.84624201853375, 5.0): 2.7565547482229014,
    (9.909735084, 3.0): 8.05522455930435,
    (9.909735084, 5.0): 1.6734179605645096,
}


def test_zero_uncertainty_reproduces_iteration_0050():
    for signal in SCENARIOS:
        for z in (3.0, 5.0):
            b = max_background_for_significance_with_uncertainty(signal, z, 0.0)
            assert math.isclose(b, KNOWN_0050[(signal, z)], rel_tol=1e-10)


def test_inversion_reproduces_target_z():
    for signal in SCENARIOS:
        for delta in DELTAS:
            for z in (3.0, 5.0):
                b = max_background_for_significance_with_uncertainty(signal, z, delta)
                z_back = asimov_significance_with_background_uncertainty(signal, b, delta)
                assert math.isclose(z_back, z, rel_tol=1e-10)


def test_background_ceiling_strictly_tightens_with_uncertainty():
    for signal in SCENARIOS:
        for z in (3.0, 5.0):
            vals = [
                max_background_for_significance_with_uncertainty(signal, z, delta)
                for delta in DELTAS
            ]
            assert all(a > b for a, b in zip(vals, vals[1:]))


def test_five_sigma_is_stricter_than_three_sigma():
    for signal in SCENARIOS:
        for delta in DELTAS:
            b3 = max_background_for_significance_with_uncertainty(signal, 3.0, delta)
            b5 = max_background_for_significance_with_uncertainty(signal, 5.0, delta)
            assert b5 < b3


def test_invalid_inputs_fail_closed():
    with pytest.raises(ValueError):
        asimov_significance_with_background_uncertainty(0.0, 1.0, 0.1)
    with pytest.raises(ValueError):
        asimov_significance_with_background_uncertainty(1.0, 0.0, 0.1)
    with pytest.raises(ValueError):
        asimov_significance_with_background_uncertainty(1.0, 1.0, -0.1)
    with pytest.raises(ValueError):
        max_background_for_significance_with_uncertainty(0.0, 3.0, 0.1)
    with pytest.raises(ValueError):
        max_background_for_significance_with_uncertainty(1.0, 0.0, 0.1)
    with pytest.raises(ValueError):
        max_background_for_significance_with_uncertainty(1.0, 3.0, -0.1)
