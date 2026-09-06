"""Exact scoped f-sum utilities for passive density-coupled media.

Conventions
-----------
`q` is a momentum transfer in the same energy units as constituent masses
(c=1). `omega` is transferred energy. For a weighted density operator
rho_q = sum_i g_i exp(i q.r_i) and a coordinate-local nonrelativistic
Hamiltonian, the positive-frequency energy-weighted sum is

    m1(q) = q^2/2 * sum_i g_i^2/m_i.

The routines below deliberately separate unweighted spectral strength from
energy-weighted deposition so collective low-energy modes cannot be confused
with a new source of neutrino-supplied energy.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence


def weighted_density_fsum(
    q_mev: float,
    masses_mev: Sequence[float],
    couplings: Sequence[float],
) -> float:
    """Return m1(q) in MeV for a finite set of weighted constituents."""
    if q_mev < 0:
        raise ValueError("q_mev must be non-negative")
    if len(masses_mev) != len(couplings) or not masses_mev:
        raise ValueError("masses and couplings must have equal non-zero length")
    if any(m <= 0 for m in masses_mev):
        raise ValueError("all masses must be positive")
    return 0.5 * q_mev**2 * sum(g * g / m for m, g in zip(masses_mev, couplings))


def identical_constituent_fsum(q_mev: float, mass_mev: float, coupling: float, n: int) -> float:
    """Closed-form m1 for N identical constituents; scales exactly linearly in N."""
    if n <= 0:
        raise ValueError("n must be positive")
    if mass_mev <= 0:
        raise ValueError("mass_mev must be positive")
    if q_mev < 0:
        raise ValueError("q_mev must be non-negative")
    return 0.5 * q_mev**2 * n * coupling**2 / mass_mev


def single_mode_response(m1: float, mode_energy_mev: float) -> tuple[tuple[float, float], ...]:
    """A one-mode non-negative response that exactly saturates the requested m1."""
    if m1 < 0 or mode_energy_mev <= 0:
        raise ValueError("m1 must be non-negative and mode energy positive")
    return ((mode_energy_mev, m1 / mode_energy_mev),)


def response_from_shape(
    m1: float,
    energies_mev: Sequence[float],
    relative_weights: Sequence[float],
) -> tuple[tuple[float, float], ...]:
    """Scale any positive discrete spectral shape to a prescribed energy-weighted sum."""
    if m1 < 0:
        raise ValueError("m1 must be non-negative")
    if len(energies_mev) != len(relative_weights) or not energies_mev:
        raise ValueError("energies and weights must have equal non-zero length")
    if any(e <= 0 for e in energies_mev):
        raise ValueError("all spectral energies must be positive")
    if any(w < 0 for w in relative_weights) or not any(w > 0 for w in relative_weights):
        raise ValueError("relative weights must be non-negative with at least one positive")
    raw_m1 = sum(e * w for e, w in zip(energies_mev, relative_weights))
    scale = 0.0 if m1 == 0 else m1 / raw_m1
    return tuple((e, scale * w) for e, w in zip(energies_mev, relative_weights))


def unweighted_strength(response: Sequence[tuple[float, float]]) -> float:
    """Return integral S d omega for a discrete response."""
    return sum(weight for _, weight in response)


def energy_weighted_strength(response: Sequence[tuple[float, float]]) -> float:
    """Return integral omega S d omega for a discrete response."""
    return sum(energy * weight for energy, weight in response)


def deposition_proxy(
    response: Sequence[tuple[float, float]],
    kernel: Callable[[float], float],
) -> float:
    """Return integral omega K(omega) S d omega for a discrete response.

    The caller is responsible for supplying a physically relevant kernel.
    Negative kernels are rejected because the funnel bound uses non-negative
    rates/energy deposition.
    """
    total = 0.0
    for energy, weight in response:
        kval = kernel(energy)
        if kval < 0:
            raise ValueError("kernel must be non-negative")
        total += energy * kval * weight
    return total
