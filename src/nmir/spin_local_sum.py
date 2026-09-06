"""Scoped local-Hamiltonian first-moment bounds for spin/axial response.

For H=sum_X h_X and O=sum_i g_i S_i^a, the standard first-moment
double-commutator identity plus ||[A,B]||<=2||A||||B|| gives

    |m1| <= 2 sum_X ||h_X|| ||O_X||^2
         <= 2 s^2 gmax^2 sum_X ||h_X|| |X|^2.

This module exposes that norm envelope and useful spin-1/2 Heisenberg
specializations. It is a scaling/no-free-lunch tool, not a precision material
cross-section calculator.
"""

from __future__ import annotations

from collections.abc import Sequence


def local_spin_first_moment_bound(
    term_norms: Sequence[float],
    support_sizes: Sequence[int],
    *,
    spin_component_norm: float = 0.5,
    coupling_abs_max: float = 1.0,
) -> float:
    """Return 2 s^2 gmax^2 sum_X ||h_X|| |X|^2."""
    if len(term_norms) != len(support_sizes):
        raise ValueError("term_norms and support_sizes must have equal length")
    if spin_component_norm < 0 or coupling_abs_max < 0:
        raise ValueError("norm bounds must be non-negative")
    if any(h < 0 for h in term_norms):
        raise ValueError("Hamiltonian term norms must be non-negative")
    if any(k <= 0 for k in support_sizes):
        raise ValueError("support sizes must be positive")
    pref = 2.0 * spin_component_norm**2 * coupling_abs_max**2
    return pref * sum(h * k * k for h, k in zip(term_norms, support_sizes))


def heisenberg_bond_operator_norm(j_abs: float) -> float:
    """Operator norm of J S_i·S_j for two spin-1/2 sites: 3|J|/4."""
    if j_abs < 0:
        raise ValueError("j_abs must be non-negative")
    return 0.75 * j_abs


def spin_half_heisenberg_first_moment_bound(j_abs_values: Sequence[float]) -> float:
    """Return (3/2) sum_bonds |J_ij| for one spin component, |g_i|<=1."""
    if any(j < 0 for j in j_abs_values):
        raise ValueError("exchange magnitudes must be non-negative")
    norms = [heisenberg_bond_operator_norm(j) for j in j_abs_values]
    return local_spin_first_moment_bound(norms, [2] * len(norms))


def bounded_coordination_heisenberg_bound(n_sites: int, coordination: float, jmax: float) -> float:
    """Return (3/4) N z Jmax, counting Nz/2 bonds."""
    if n_sites <= 0:
        raise ValueError("n_sites must be positive")
    if coordination < 0 or jmax < 0:
        raise ValueError("coordination and jmax must be non-negative")
    return 0.75 * n_sites * coordination * jmax


def all_to_all_heisenberg_bound(n_sites: int, j_abs: float, *, kac_scale: bool = False) -> float:
    """Pair-count diagnostic for a complete graph of spin-1/2 Heisenberg bonds.

    Without Kac scaling, there are N(N-1)/2 bonds with fixed |J| and the norm
    envelope is superextensive. With Kac scaling J->J/(N-1), the bound becomes
    extensive. This is an explicit loophole diagnostic, not a proposed material.
    """
    if n_sites <= 0:
        raise ValueError("n_sites must be positive")
    if j_abs < 0:
        raise ValueError("j_abs must be non-negative")
    if n_sites == 1:
        return 0.0
    effective_j = j_abs / (n_sites - 1) if kac_scale else j_abs
    bonds = n_sites * (n_sites - 1) / 2.0
    return 1.5 * bonds * effective_j


def single_mode_unweighted_strength(first_moment: float, mode_energy: float) -> float:
    """Unweighted spectral strength of a single mode saturating fixed m1."""
    if first_moment < 0 or mode_energy <= 0:
        raise ValueError("first_moment must be non-negative and mode_energy positive")
    return first_moment / mode_energy
