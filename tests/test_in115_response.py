import pytest

from nmir.in115_response import (
    IN115_THRESHOLD_MEV,
    in115_dominant_sigma_cm2,
    point_coulomb_fermi_factor,
)


def test_in115_threshold_is_fail_closed():
    assert in115_dominant_sigma_cm2(0.0) == 0.0
    assert in115_dominant_sigma_cm2(IN115_THRESHOLD_MEV) == 0.0


def test_in115_screening_cross_section_reference_points():
    assert in115_dominant_sigma_cm2(0.300) == pytest.approx(5.10390e-45, rel=3e-5)
    assert in115_dominant_sigma_cm2(0.862) == pytest.approx(1.75056e-44, rel=3e-5)
    assert in115_dominant_sigma_cm2(1.000) == pytest.approx(2.16422e-44, rel=3e-5)


def test_in115_cross_section_increases_over_solar_range():
    energies = [0.2, 0.3, 0.42, 0.862, 1.442, 5.0, 10.0]
    sigmas = [in115_dominant_sigma_cm2(e) for e in energies]
    assert all(b > a for a, b in zip(sigmas, sigmas[1:]))


def test_point_coulomb_attraction_enhances_electron_wavefunction():
    assert point_coulomb_fermi_factor(50, 1.0, 0.85) > 1.0
