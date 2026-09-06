"""Small convention-safe utilities for NMIR production/absorption studies.

These are not a nuclear-reaction calculator.  They encode generic thermodynamic
and spectral diagnostics used to gate candidate inverse-reaction mechanisms.
"""

from __future__ import annotations

import math

K_B_EV_PER_K = 8.617333262145e-5


def detailed_balance_ratio(energy_transfer_ev: float, temperature_k: float) -> float:
    """Return exp(-omega/kT) for positive energy transfer omega.

    In thermal equilibrium and under the standard Hermitian-response
    assumptions, this is the factor relating negative- and positive-frequency
    dynamic structure factors, S(-omega)/S(+omega).
    """
    if energy_transfer_ev < 0:
        raise ValueError("energy_transfer_ev must be non-negative")
    if temperature_k <= 0:
        raise ValueError("temperature_k must be positive")
    x = energy_transfer_ev / (K_B_EV_PER_K * temperature_k)
    if x > 745.0:
        return 0.0
    return math.exp(-x)


def deposited_fraction(excitation_energy_ev: float, neutrino_energy_ev: float) -> float:
    """Fraction of incident neutrino energy deposited in one excitation."""
    if excitation_energy_ev < 0:
        raise ValueError("excitation_energy_ev must be non-negative")
    if neutrino_energy_ev <= 0:
        raise ValueError("neutrino_energy_ev must be positive")
    return excitation_energy_ev / neutrino_energy_ev


def normalized_lorentzian(energy_ev: float, center_ev: float, fwhm_ev: float) -> float:
    """Unit-area Lorentzian spectral line in inverse-eV.

    The integral over (-inf,+inf) is one.  This is useful for demonstrating
    that narrowing a resonance increases the peak height while preserving
    integrated spectral strength in a fixed-strength toy model.
    """
    if fwhm_ev <= 0:
        raise ValueError("fwhm_ev must be positive")
    gamma = 0.5 * fwhm_ev
    return (gamma / math.pi) / ((energy_ev - center_ev) ** 2 + gamma**2)


def lorentzian_peak(fwhm_ev: float) -> float:
    """Peak height of the unit-area Lorentzian."""
    return normalized_lorentzian(0.0, 0.0, fwhm_ev)
