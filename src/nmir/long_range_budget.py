"""Long-range interaction-budget envelopes for NMIR many-body response.

The core quantity is the absolute pair-interaction norm budget
W_N = sum_{i<j} ||h_ij||.  For an additive observable O=sum_i o_i with
||o_i||<=o0, the first energy-weighted moment is bounded by
m1 <= 8 o0^2 W_N.
"""

from __future__ import annotations

import math


def pair_count(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >=1")
    return n * (n - 1) // 2


def all_to_all_pair_budget(n: int, j0: float, kappa: float) -> float:
    """Absolute pair-norm budget for ||h_ij|| = j0 / n**kappa."""
    if n < 1:
        raise ValueError("n must be >=1")
    if j0 < 0.0:
        raise ValueError("j0 must be non-negative")
    return pair_count(n) * j0 / (float(n) ** kappa)


def first_moment_pair_bound(pair_budget: float, o0: float) -> float:
    if pair_budget < 0.0:
        raise ValueError("pair_budget must be non-negative")
    if o0 < 0.0:
        raise ValueError("o0 must be non-negative")
    return 8.0 * o0 * o0 * pair_budget


def per_particle(value: float, n: int) -> float:
    if n < 1:
        raise ValueError("n must be >=1")
    return value / n


def finite_n_per_particle_gain(n1: int, n2: int, kappa: float) -> float:
    """Exact gain of W_N/N for the all-to-all scaling family."""
    if n1 < 2 or n2 < 2:
        raise ValueError("n1,n2 must be >=2")
    return ((n2 - 1) / (n1 - 1)) * ((n1 / n2) ** kappa)


def power_law_budget_factor(n: float, alpha: float, dimension: float) -> float:
    """Frozen asymptotic per-particle absolute-budget factor.

    This is a scaling diagnostic, not a lattice sum.  It uses the standard
    continuum asymptotics for J(r)~r^-alpha at fixed density:
      alpha<d: N^(1-alpha/d)
      alpha=d: log N
      alpha>d: O(1), represented by 1.
    """
    if n <= 1.0:
        raise ValueError("n must be >1")
    if alpha < 0.0:
        raise ValueError("alpha must be non-negative")
    if dimension <= 0.0:
        raise ValueError("dimension must be positive")
    if alpha < dimension:
        return n ** (1.0 - alpha / dimension)
    if math.isclose(alpha, dimension, rel_tol=0.0, abs_tol=1e-14):
        return math.log(n)
    return 1.0


def kac_normalized_factor(n: float, alpha: float, dimension: float) -> float:
    raw = power_law_budget_factor(n, alpha, dimension)
    return raw / raw
