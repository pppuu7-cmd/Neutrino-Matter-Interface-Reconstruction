import pytest

from nmir.gravity_focusing import (
    M_SUN_KG,
    R_SUN_M,
    focal_distance_m,
    null_deflection_rad,
    point_lens_magnification,
    solar_limb_focal_distance_au,
)


def test_solar_limb_focal_distance():
    assert solar_limb_focal_distance_au() == pytest.approx(547.741, rel=2e-6)


def test_focal_distance_equals_b_over_alpha():
    alpha = null_deflection_rad(M_SUN_KG, R_SUN_M)
    assert focal_distance_m(M_SUN_KG, R_SUN_M) == pytest.approx(R_SUN_M / alpha)


def test_point_lens_magnification_reference():
    assert point_lens_magnification(1.0) == pytest.approx(3.0 / (5.0**0.5), rel=1e-12)


def test_point_lens_magnification_tends_to_one():
    assert point_lens_magnification(100.0) == pytest.approx(1.0, rel=1e-7)


def test_caustic_requires_finite_source_model():
    with pytest.raises(ValueError):
        point_lens_magnification(0.0)
