import pytest

from nmir.capture_metrics import (
    capture_rate_per_kg_s,
    deposited_power_w_per_kg,
    enhancement_to_target_power,
    target_atoms_per_kg,
)


def test_pure_ga71_reference_atoms_per_kg():
    atoms = target_atoms_per_kg(70.9247)
    assert atoms == pytest.approx(8.49089e24, rel=2e-6)


def test_ga71_66p1_snu_capture_rate():
    rate = capture_rate_per_kg_s(66.1, 70.9247)
    assert rate == pytest.approx(5.61248e-10, rel=2e-6)


def test_ga71_one_mev_power_normalization():
    power = deposited_power_w_per_kg(66.1, 1.0, 70.9247)
    assert power == pytest.approx(8.99219e-23, rel=2e-6)
    assert enhancement_to_target_power(power, 1.0) == pytest.approx(1.11207673e22, rel=2e-6)


def test_isotopic_fraction_scales_linearly():
    full = capture_rate_per_kg_s(10.0, 70.0, 1.0)
    partial = capture_rate_per_kg_s(10.0, 70.0, 0.4)
    assert partial / full == pytest.approx(0.4)


def test_invalid_inputs():
    with pytest.raises(ValueError):
        target_atoms_per_kg(0.0)
    with pytest.raises(ValueError):
        target_atoms_per_kg(70.0, 1.1)
    with pytest.raises(ValueError):
        capture_rate_per_kg_s(-1.0, 70.0)
