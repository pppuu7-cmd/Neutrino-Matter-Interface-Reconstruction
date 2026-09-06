import math

import pytest

from nmir.resonance_overlap import (
    breit_wigner_area,
    breit_wigner_peak,
    dimensionless_numeric_area,
    entrance_width_area_bound,
    gaussian_profile,
    lorentzian_profile,
    profile_supremum_bound,
    validate_sampled_profile,
)


def _relative_overlap_numeric(*, profile, gamma_total, k_res=10.0, g=1.0, gamma_in=1e-20, branch=0.5, t_max=1e4, steps=200_000):
    gamma_out = branch * gamma_total
    h = 2.0 * t_max / steps
    prefactor = 2.0 * math.pi / (k_res * k_res) * g * gamma_in * gamma_out / gamma_total
    total = 0.0
    for i in range(steps + 1):
        t = -t_max + i * h
        delta_e = 0.5 * gamma_total * t
        weight = 0.5 if i in (0, steps) else 1.0
        total += weight * profile(delta_e) / (1.0 + t * t)
    return prefactor * h * total


def test_numeric_breit_wigner_area_over_twelve_width_decades():
    gamma_in = 1e-20
    for gamma_total in (1e-3, 1e-6, 1e-9, 1e-12, 1e-15):
        gamma_out = 0.5 * gamma_total
        analytic = breit_wigner_area(
            k_res=10.0,
            statistical_factor=1.0,
            gamma_in=gamma_in,
            gamma_out=gamma_out,
            gamma_total=gamma_total,
        )
        numeric = dimensionless_numeric_area(
            k_res=10.0,
            statistical_factor=1.0,
            gamma_in=gamma_in,
            gamma_out=gamma_out,
            gamma_total=gamma_total,
        )
        assert abs(numeric / analytic - 1.0) <= 1e-4


def test_narrowing_width_raises_peak_but_not_area_at_fixed_branching():
    gamma_in = 1e-20
    broad = 1e-6
    narrow = 1e-12
    branch = 0.5
    area_broad = breit_wigner_area(
        k_res=10.0,
        statistical_factor=1.0,
        gamma_in=gamma_in,
        gamma_out=branch * broad,
        gamma_total=broad,
    )
    area_narrow = breit_wigner_area(
        k_res=10.0,
        statistical_factor=1.0,
        gamma_in=gamma_in,
        gamma_out=branch * narrow,
        gamma_total=narrow,
    )
    peak_broad = breit_wigner_peak(
        k_res=10.0,
        statistical_factor=1.0,
        gamma_in=gamma_in,
        gamma_out=branch * broad,
        gamma_total=broad,
    )
    peak_narrow = breit_wigner_peak(
        k_res=10.0,
        statistical_factor=1.0,
        gamma_in=gamma_in,
        gamma_out=branch * narrow,
        gamma_total=narrow,
    )
    assert math.isclose(area_broad, area_narrow, rel_tol=1e-14)
    assert math.isclose(peak_narrow / peak_broad, broad / narrow, rel_tol=1e-14)


def test_area_never_exceeds_entrance_width_bound():
    bound = entrance_width_area_bound(k_res=10.0, statistical_factor=3.0, gamma_in=2e-18)
    for branch in (1e-6, 0.1, 0.5, 1.0):
        gamma_total = 1e-8
        area = breit_wigner_area(
            k_res=10.0,
            statistical_factor=3.0,
            gamma_in=2e-18,
            gamma_out=branch * gamma_total,
            gamma_total=gamma_total,
        )
        assert area <= bound * (1.0 + 1e-14)


@pytest.mark.parametrize("offset", [0.0, 0.5, 3.0, 8.0])
def test_gaussian_source_overlap_below_supremum_bound(offset):
    gamma_total = 1.0
    sigma_src = 3.0
    profile = lambda de: gaussian_profile(de, center=offset, sigma=sigma_src)
    overlap = _relative_overlap_numeric(profile=profile, gamma_total=gamma_total)
    area = breit_wigner_area(
        k_res=10.0,
        statistical_factor=1.0,
        gamma_in=1e-20,
        gamma_out=0.5 * gamma_total,
        gamma_total=gamma_total,
    )
    profile_max = gaussian_profile(offset, center=offset, sigma=sigma_src)
    assert overlap <= profile_supremum_bound(area, profile_max) * (1.0 + 1e-8)


@pytest.mark.parametrize("offset", [0.0, 1.0, 5.0])
def test_lorentzian_source_overlap_below_supremum_bound(offset):
    gamma_total = 1.0
    hwhm = 2.0
    profile = lambda de: lorentzian_profile(de, center=offset, half_width=hwhm)
    overlap = _relative_overlap_numeric(profile=profile, gamma_total=gamma_total)
    area = breit_wigner_area(
        k_res=10.0,
        statistical_factor=1.0,
        gamma_in=1e-20,
        gamma_out=0.5 * gamma_total,
        gamma_total=gamma_total,
    )
    profile_max = lorentzian_profile(offset, center=offset, half_width=hwhm)
    assert overlap <= profile_supremum_bound(area, profile_max) * (1.0 + 1e-8)


def test_profile_and_width_guards_fail_closed():
    with pytest.raises(ValueError):
        breit_wigner_area(k_res=1.0, statistical_factor=1.0, gamma_in=2.0, gamma_out=1.0, gamma_total=1.0)
    with pytest.raises(ValueError):
        breit_wigner_area(k_res=1.0, statistical_factor=1.0, gamma_in=0.1, gamma_out=2.0, gamma_total=1.0)
    with pytest.raises(ValueError):
        gaussian_profile(0.0, center=0.0, sigma=0.0)
    with pytest.raises(ValueError):
        lorentzian_profile(0.0, center=0.0, half_width=0.0)
    with pytest.raises(ValueError):
        validate_sampled_profile([0.0, 1.0], [1.0, -0.1])
    with pytest.raises(ValueError):
        validate_sampled_profile([0.0, 1.0], [0.0, 0.0])
