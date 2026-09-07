import math

import pytest

from nmir.contact_unitarity_ceiling import (
    FM2_TO_CM2,
    HBARC_MEV_FM,
    MEV_TO_J,
    nuclei_per_kg_class,
    odd_sum_through_l,
    partial_wave_lmax,
    sigma_unitarity_cm2,
    wave_number_fm_inv,
)


def test_odd_sum_identity():
    for lmax in range(12):
        assert odd_sum_through_l(lmax) == (lmax + 1) ** 2


def test_wave_number_units_and_s_wave_limit():
    e = 1.0
    k = wave_number_fm_inv(e)
    assert k == pytest.approx(e / HBARC_MEV_FM, rel=1e-15)
    # floor(kR) is zero for a 1-MeV neutrino on A=1 at nuclear radius scale.
    assert partial_wave_lmax(e, 1.0, 1.4, "floor") == 0
    expected = 4.0 * math.pi / (k * k) * FM2_TO_CM2
    assert sigma_unitarity_cm2(e, 1.0, 1.4, "floor") == pytest.approx(expected, rel=1e-15)


def test_ceil_is_never_smaller_than_floor():
    for a in (1.0, 4.0, 40.0, 208.0, 250.0):
        for e in (0.01, 0.1, 1.0, 5.0, 20.0):
            assert sigma_unitarity_cm2(e, a, 1.4, "ceil") >= sigma_unitarity_cm2(e, a, 1.4, "floor")


def test_target_count_uses_fixed_kg_and_Au():
    assert nuclei_per_kg_class(1.0) == pytest.approx(1000.0 / 1.66053906660e-24, rel=1e-15)
    assert nuclei_per_kg_class(100.0) == pytest.approx(nuclei_per_kg_class(1.0) / 100.0, rel=1e-15)


def test_mev_to_j_constant():
    assert MEV_TO_J == pytest.approx(1.602176634e-13, rel=0.0, abs=0.0)


def test_e_zero_is_fail_closed_for_nonzero_density():
    from nmir.contact_unitarity_ceiling import power_kernel_w_per_target

    assert power_kernel_w_per_target(0.0, 0.0, 1.0, 1.0) == 0.0
    with pytest.raises(ValueError):
        power_kernel_w_per_target(0.0, 1.0, 1.0, 1.0)
