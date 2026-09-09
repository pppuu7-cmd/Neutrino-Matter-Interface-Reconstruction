import math

import pytest

from nmir.range_information_kernel_0105e import (
    composition_information_amplitude_factor,
    range_information_kernel,
    range_information_kernel_from_f,
    range_information_kernel_mass_ratio,
)
from nmir.vector_mediator_bridge_0105b import finite_q_ratio


def test_direct_mass_q_and_f_forms_agree():
    for mass, q in ((1e-3, 0.04), (0.04, 0.04), (0.4, 0.04)):
        f = finite_q_ratio(mass, q)
        assert math.isclose(
            range_information_kernel(mass, q),
            range_information_kernel_from_f(f),
            rel_tol=2e-15,
            abs_tol=0.0,
        )


def test_kernel_nonnegative_with_endpoint_zeros():
    assert range_information_kernel_from_f(0.0) == 0.0
    assert range_information_kernel_from_f(1.0) == 0.0
    for i in range(101):
        assert range_information_kernel_from_f(i / 100.0) >= 0.0


def test_unique_grid_maximum_is_m_equals_q_and_one_quarter():
    assert range_information_kernel_mass_ratio(1.0) == 0.25
    xs = [10.0 ** (k / 20.0) for k in range(-80, 81)]
    values = [range_information_kernel_mass_ratio(x) for x in xs]
    imax = max(range(len(values)), key=values.__getitem__)
    assert xs[imax] == 1.0
    assert values[imax] == 0.25


def test_kernel_is_reciprocal_symmetric_in_mass_over_q():
    for x in (1e-4, 1e-2, 0.2, 0.7, 2.0, 50.0, 1e4):
        assert math.isclose(
            range_information_kernel_mass_ratio(x),
            range_information_kernel_mass_ratio(1.0 / x),
            rel_tol=5e-9,
            abs_tol=1e-30,
        )


def test_fourth_power_light_and_heavy_asymptotics():
    x = 1e-3
    light = range_information_kernel_mass_ratio(x)
    heavy = range_information_kernel_mass_ratio(1.0 / x)
    expected = 4.0 * x**4
    assert math.isclose(light, expected, rel_tol=5e-6)
    assert math.isclose(heavy, expected, rel_tol=5e-6)


def test_composition_amplitude_factor_has_expected_limits():
    q = 0.04
    x_light = 1e-3
    light = composition_information_amplitude_factor(x_light * q, q)
    assert math.isclose(light, x_light**4, rel_tol=5e-6)

    x_heavy = 1e3
    heavy = composition_information_amplitude_factor(x_heavy * q, q)
    assert math.isclose(heavy, 1.0, rel_tol=5e-6)


def test_invalid_domains_fail_closed():
    for mass, q in ((0.0, 1.0), (-1.0, 1.0), (1.0, 0.0), (1.0, -1.0)):
        with pytest.raises(ValueError):
            range_information_kernel(mass, q)
    for f in (-0.1, 1.1, math.inf, math.nan):
        with pytest.raises(ValueError):
            range_information_kernel_from_f(f)
