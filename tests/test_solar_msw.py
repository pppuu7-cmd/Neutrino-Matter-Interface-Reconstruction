import pytest

from nmir.solar_matter import SolarMatterTable
from nmir.solar_oscillation import (
    adiabatic_day_pee_at_density,
    high_density_adiabatic_pee,
    numerical_solar_parameters,
    production_averaged_day_pee,
    vacuum_averaged_pee,
)


def test_zero_density_matches_vacuum_average():
    s12, s13, dm21 = numerical_solar_parameters()
    got = adiabatic_day_pee_at_density(1.0, 0.0, s12, s13, dm21)
    assert got == pytest.approx(vacuum_averaged_pee(s12, s13), rel=1e-12)


def test_high_density_limit():
    s12, s13, dm21 = numerical_solar_parameters()
    got = adiabatic_day_pee_at_density(10.0, 1.0e8, s12, s13, dm21)
    assert got == pytest.approx(high_density_adiabatic_pee(s12, s13), rel=1e-8)


def test_survival_decreases_between_vacuum_and_solar_core_like_density():
    low = adiabatic_day_pee_at_density(1.0, 0.0)
    high = adiabatic_day_pee_at_density(10.0, 100.0)
    assert 0.0 < high < low < 1.0


def test_production_average_constant_density_reproduces_point_value():
    table = SolarMatterTable(
        radius_rsun=(0.0, 0.5, 1.0),
        electron_density_mol_cm3=(50.0, 50.0, 50.0),
        production={"pp": (1.0, 2.0, 1.0)},
    )
    got = production_averaged_day_pee(0.5, table, "pp")
    expected = adiabatic_day_pee_at_density(0.5, 50.0)
    assert got == pytest.approx(expected, rel=1e-12)
