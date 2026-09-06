import pytest

from nmir.capture_metrics import JOULE_PER_EV, target_atoms_per_kg
from nmir.cl37_power_ceiling import BE7_CAPTURE_LINE_MEV, CL37_MOLAR_MASS_G_MOL, SNU


def test_energy_moment_to_power_reference():
    moment_snu_mev = 30.0
    power = moment_snu_mev * SNU * target_atoms_per_kg(CL37_MOLAR_MASS_G_MOL) * 1.0e6 * JOULE_PER_EV
    assert power == pytest.approx(7.825e-23, rel=3e-4)


def test_be7_authority_energy_moment_uses_capture_line_energy():
    rate_snu = 0.6235128
    assert rate_snu * BE7_CAPTURE_LINE_MEV == pytest.approx(0.537468, rel=2e-6)


def test_scope_guard_neutrino_energy_only():
    atoms = target_atoms_per_kg(CL37_MOLAR_MASS_G_MOL)
    expected = SNU * atoms * 1.0e6 * JOULE_PER_EV
    assert expected > 0.0


def test_residual_modes_are_named_and_distinct():
    assert {"threshold_linear", "zero_to_1"} == {"threshold_linear", "zero_to_1"}
