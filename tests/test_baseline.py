import math

import pytest

from nmir.baseline import (
    cevns_sigma_lowq_cm2,
    field_for_first_magnetic_maximum_t,
    magnetic_phase,
    minimal_dirac_magnetic_moment_mu_b,
    weak_charge,
    xenon132_reference,
)


def test_weak_charge_xe132_reference():
    assert weak_charge(54, 78) == pytest.approx(75.53112, rel=1e-12)


def test_cevns_energy_squared_scaling():
    s1 = cevns_sigma_lowq_cm2(1.0, 54, 78)
    s2 = cevns_sigma_lowq_cm2(2.0, 54, 78)
    assert s2 / s1 == pytest.approx(4.0, rel=1e-12)


def test_xe132_one_mev_reference_order():
    ref = xenon132_reference(1.0)
    assert ref["sigma_cm2"] == pytest.approx(2.40488e-41, rel=2e-5)
    assert ref["mean_free_path_m"] == pytest.approx(3.08354e16, rel=2e-5)


def test_magnetic_first_maximum_phase():
    mu = 1.0e-11
    length = 1.0
    b = field_for_first_magnetic_maximum_t(mu, length)
    assert magnetic_phase(mu, b, length) == pytest.approx(math.pi / 2.0, rel=1e-12)


def test_minimal_dirac_benchmark():
    mu = minimal_dirac_magnetic_moment_mu_b(0.05)
    assert mu == pytest.approx(1.6e-20, rel=1e-12)
    b = field_for_first_magnetic_maximum_t(mu, 1.0)
    assert b == pytest.approx(3.3468e17, rel=2e-5)
