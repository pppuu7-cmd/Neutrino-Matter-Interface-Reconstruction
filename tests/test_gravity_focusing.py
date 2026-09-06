import pytest

from nmir.gravity_focusing import (
    M_SUN_KG,
    R_SUN_M,
    focal_distance_m,
    null_deflection_rad,
    numerical_uniform_disk_magnification,
    on_axis_uniform_disk_magnification,
    point_lens_magnification,
    solar_limb_focal_distance_au,
    surface_brightness_flux_gain,
    transparent_sun_rounded_check_au,
)


def test_solar_limb_focal_distance():
    assert solar_limb_focal_distance_au() == pytest.approx(547.741, rel=2e-6)


def test_focal_distance_equals_b_over_alpha():
    alpha = null_deflection_rad(M_SUN_KG, R_SUN_M)
    assert focal_distance_m(M_SUN_KG, R_SUN_M) == pytest.approx(R_SUN_M / alpha)


def test_transparent_sun_rounded_check_matches_published_scale():
    assert transparent_sun_rounded_check_au() == pytest.approx(23.5, rel=0.03)


def test_point_lens_magnification_reference():
    assert point_lens_magnification(1.0) == pytest.approx(3.0 / (5.0**0.5), rel=1e-12)


def test_point_lens_magnification_tends_to_one():
    assert point_lens_magnification(100.0) == pytest.approx(1.0, rel=1e-7)


def test_caustic_requires_finite_source_model():
    with pytest.raises(ValueError):
        point_lens_magnification(0.0)


def test_uniform_disk_finite_source_matches_numerical_average():
    for rho in (1e-3, 0.1, 1.0, 10.0):
        analytic = on_axis_uniform_disk_magnification(rho)
        numeric = numerical_uniform_disk_magnification(rho)
        assert numeric == pytest.approx(analytic, rel=1e-5)


def test_finite_source_regularizes_caustic():
    assert on_axis_uniform_disk_magnification(1e-3) < 2001.0
    assert on_axis_uniform_disk_magnification(1.0) == pytest.approx(5.0**0.5)


def test_liouville_surface_brightness_control():
    mu = on_axis_uniform_disk_magnification(0.2)
    assert surface_brightness_flux_gain(mu * 3.0, 3.0) == pytest.approx(mu)
