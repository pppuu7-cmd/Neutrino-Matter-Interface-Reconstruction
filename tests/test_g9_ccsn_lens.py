import math

import pytest

from nmir.g9_ccsn_lens import (
    all_flavour_totals,
    annular_point_source_receiver_mu,
    expected_multiplier_upper_isotropic,
    finite_source_mu_bracket,
    isotropic_fluence,
    source_angular_radius_rad,
    source_footprint_cm,
    stable_small_cap_probability,
)


def test_nakazato_all_flavour_total_and_10kpc_fluence():
    n, e = all_flavour_totals(2.211848e57, 1.590254e57, 1.711720e57, 3.302304e52, 2.823673e52, 3.267222e52)
    assert n == pytest.approx(1.0648982e58, rel=1e-12)
    assert e == pytest.approx(1.9194865e53, rel=1e-12)
    assert isotropic_fluence(n, 10.0) == pytest.approx(8.900146153964761e11, rel=1e-12)


def test_ccsn_source_is_sub_mm_at_24au():
    theta = source_angular_radius_rad(21.0, 10.0)
    assert theta == pytest.approx(6.805636507833167e-17, rel=1e-12)
    footprint = source_footprint_cm(21.0, 10.0, 24.0)
    assert footprint < 0.03  # cm, i.e. sub-mm


def test_small_cap_stable():
    theta = 1e-12
    assert stable_small_cap_probability(theta) == pytest.approx(theta * theta / 4.0, rel=1e-12)


def test_impossible_full_sun_ceiling_still_duty_negative():
    # One-metre radius receiver, source footprint generously set to 1 cm.
    mu, p, expected = expected_multiplier_upper_isotropic(100.0, 1.0, 24.0)
    assert mu > 1e17
    assert p < 1e-24
    assert expected < 1.000001


def test_toy_annular_receiver_and_finite_source_bracket():
    root = 0.2
    z = 24.0
    # Smooth toy focal curve with a resolved root and nonzero local derivative.
    def focal(b):
        return z * (1.0 + 5.0 * (b - root))

    z_out, blo, bhi, mu = annular_point_source_receiver_mu(root, 100.0, 1.0e8, focal)
    assert z_out == pytest.approx(z)
    assert blo < root < bhi
    assert mu > 1.0
    z2, mlo, mhi = finite_source_mu_bracket(root, 100.0, 0.1, 1.0e8, focal)
    assert z2 == pytest.approx(z)
    assert 0.0 < mlo <= mhi
    assert mlo / mhi > 0.99
