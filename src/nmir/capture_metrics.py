"""Rate and deposited-power metrics for neutrino capture targets."""

from __future__ import annotations

AVOGADRO = 6.02214076e23
JOULE_PER_EV = 1.602176634e-19
SNU_PER_ATOM_PER_S = 1.0e-36


def target_atoms_per_kg(molar_mass_g_mol: float, isotopic_fraction: float = 1.0) -> float:
    """Number of target isotope atoms per kg of material.

    `isotopic_fraction=1` corresponds to isotopically pure target material.
    """
    if molar_mass_g_mol <= 0:
        raise ValueError("molar_mass_g_mol must be positive")
    if not 0.0 <= isotopic_fraction <= 1.0:
        raise ValueError("isotopic_fraction must lie in [0,1]")
    return 1000.0 / molar_mass_g_mol * AVOGADRO * isotopic_fraction


def capture_rate_per_kg_s(
    rate_snu: float,
    molar_mass_g_mol: float,
    isotopic_fraction: float = 1.0,
) -> float:
    """Captures per second per kg for a rate stated in SNU."""
    if rate_snu < 0:
        raise ValueError("rate_snu must be non-negative")
    return (
        rate_snu
        * SNU_PER_ATOM_PER_S
        * target_atoms_per_kg(molar_mass_g_mol, isotopic_fraction)
    )


def deposited_power_w_per_kg(
    rate_snu: float,
    mean_deposited_energy_mev: float,
    molar_mass_g_mol: float,
    isotopic_fraction: float = 1.0,
) -> float:
    """Deposited power in W/kg from a radiochemical-style capture rate.

    This is a normalization metric only: the caller must provide a physically
    justified mean deposited energy per successful capture.
    """
    if mean_deposited_energy_mev < 0:
        raise ValueError("mean_deposited_energy_mev must be non-negative")
    rate = capture_rate_per_kg_s(rate_snu, molar_mass_g_mol, isotopic_fraction)
    energy_j = mean_deposited_energy_mev * 1.0e6 * JOULE_PER_EV
    return rate * energy_j


def enhancement_to_target_power(
    current_power_w_per_kg: float,
    target_power_w_per_kg: float,
) -> float:
    """Multiplicative enhancement required to reach a target W/kg."""
    if current_power_w_per_kg <= 0:
        raise ValueError("current_power_w_per_kg must be positive")
    if target_power_w_per_kg < 0:
        raise ValueError("target_power_w_per_kg must be non-negative")
    return target_power_w_per_kg / current_power_w_per_kg
