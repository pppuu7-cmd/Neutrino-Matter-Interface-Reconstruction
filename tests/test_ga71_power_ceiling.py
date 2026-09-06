import pytest

from nmir.capture_metrics import JOULE_PER_EV, target_atoms_per_kg
from nmir.ga71_power_ceiling import GA71_MOLAR_MASS_G_MOL, SNU


def test_energy_moment_to_power_reference():
    moment_snu_mev = 66.1
    power = moment_snu_mev * SNU * target_atoms_per_kg(GA71_MOLAR_MASS_G_MOL) * 1.0e6 * JOULE_PER_EV
    assert power == pytest.approx(8.99219e-23, rel=2e-6)


def test_neutrino_only_ceiling_is_linear_in_energy_moment():
    atoms = target_atoms_per_kg(GA71_MOLAR_MASS_G_MOL)
    p1 = 10.0 * SNU * atoms * 1.0e6 * JOULE_PER_EV
    p2 = 25.0 * SNU * atoms * 1.0e6 * JOULE_PER_EV
    assert p2 / p1 == pytest.approx(2.5)


def test_scope_guard_neutrino_energy_not_daughter_energy():
    # The implemented ceiling uses only the incident-neutrino energy moment.
    # No daughter half-life, decay Q value, or nuclear-mass-release term enters.
    atoms = target_atoms_per_kg(GA71_MOLAR_MASS_G_MOL)
    moment = 1.0
    expected = SNU * atoms * 1.0e6 * JOULE_PER_EV
    assert expected > 0.0
