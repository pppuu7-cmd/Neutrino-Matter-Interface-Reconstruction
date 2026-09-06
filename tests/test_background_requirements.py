import math

import pytest

from nmir.background_requirements import asimov_significance, max_background_for_significance


def test_inversion_reproduces_target_z():
    for signal in (5.0, 10.0, 11.84624201853375, 23.0):
        for z in (3.0, 5.0):
            b = max_background_for_significance(signal, z)
            assert math.isclose(asimov_significance(signal, b), z, rel_tol=1e-10)


def test_five_sigma_requires_less_background_than_three_sigma():
    for signal in (9.909735084, 10.0, 11.84624201853375):
        assert max_background_for_significance(signal, 5.0) < max_background_for_significance(signal, 3.0)


def test_background_allowance_increases_with_signal():
    for z in (3.0, 5.0):
        vals = [max_background_for_significance(s, z) for s in (5.0, 10.0, 20.0)]
        assert vals[0] < vals[1] < vals[2]


def test_invalid_inputs_fail_closed():
    with pytest.raises(ValueError):
        asimov_significance(0.0, 1.0)
    with pytest.raises(ValueError):
        asimov_significance(1.0, 0.0)
    with pytest.raises(ValueError):
        max_background_for_significance(0.0, 3.0)
    with pytest.raises(ValueError):
        max_background_for_significance(1.0, 0.0)
