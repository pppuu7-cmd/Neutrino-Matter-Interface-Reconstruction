import pytest

from nmir.solar_oscillation import load_oscillation_convention, numerical_solar_parameters


def test_frozen_parameter_values():
    s12, s13, dm21 = numerical_solar_parameters()
    assert s12 == pytest.approx(0.307)
    assert s13 == pytest.approx(0.0220)
    assert dm21 == pytest.approx(7.53e-5)


def test_baseline_scope_is_explicit():
    c = load_oscillation_convention()
    assert c["mass_ordering"] == "NO"
    assert c["propagation"] == "three_flavor_MSW_adiabatic"
    assert c["earth_regeneration"] == "off"
