"""Passive harmonic-mediator scaling controls for NMIR."""

from __future__ import annotations


def scaled_coupling(n: float, g0: float, gamma: float) -> float:
    if n <= 0.0:
        raise ValueError("n must be positive")
    if g0 < 0.0:
        raise ValueError("g0 must be non-negative")
    return g0 / (n**gamma)


def minimizing_displacement(n: float, o: float, g0: float, gamma: float, kappa: float) -> float:
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    g = scaled_coupling(n, g0, gamma)
    collective_o = o * n
    return g * collective_o / kappa


def field_energy_at_minimum(n: float, o: float, g0: float, gamma: float, kappa: float) -> float:
    x = minimizing_displacement(n, o, g0, gamma, kappa)
    return 0.5 * kappa * x * x


def induced_energy_magnitude(n: float, o: float, g0: float, gamma: float, kappa: float) -> float:
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    g = scaled_coupling(n, g0, gamma)
    collective_o = o * n
    return g * g * collective_o * collective_o / (2.0 * kappa)


def mediator_hamiltonian(n: float, o: float, x: float, g0: float, gamma: float, kappa: float) -> float:
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    g = scaled_coupling(n, g0, gamma)
    collective_o = o * n
    return 0.5 * kappa * x * x - g * x * collective_o


def completed_square_hamiltonian(n: float, o: float, x: float, g0: float, gamma: float, kappa: float) -> float:
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    g = scaled_coupling(n, g0, gamma)
    collective_o = o * n
    shift = g * collective_o / kappa
    return 0.5 * kappa * (x - shift) ** 2 - g * g * collective_o * collective_o / (2.0 * kappa)


def effective_pair_scale(n: float, g0: float, gamma: float, kappa: float) -> float:
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    g = scaled_coupling(n, g0, gamma)
    return g * g / kappa


def per_particle_energy_gain(n1: float, n2: float, gamma: float) -> float:
    if n1 <= 0.0 or n2 <= 0.0:
        raise ValueError("n1,n2 must be positive")
    return (n2 / n1) ** (1.0 - 2.0 * gamma)
