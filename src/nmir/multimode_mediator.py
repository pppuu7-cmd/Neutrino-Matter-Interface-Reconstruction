"""Passive linear multi-mode mediator accounting for NMIR G2.

For H(x)=1/2 x^T K x - b^T x with positive-definite K, the passive
minimum x*=K^-1 b gives equal field-displacement and induced-interaction
energy scales: E_field=|E_induced|=1/2 b^T K^-1 b.

This module is deliberately small and dependency-free.  It is a numerical
regression implementation of the exact square-completion identity, not a
model of a particular material.
"""

from __future__ import annotations

import math
from typing import Sequence

Vector = list[float]
Matrix = list[list[float]]


def _check_square(a: Sequence[Sequence[float]]) -> int:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("matrix must be non-empty and square")
    return n


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    if len(a) != len(b):
        raise ValueError("vector lengths differ")
    return sum(x * y for x, y in zip(a, b))


def matvec(a: Sequence[Sequence[float]], x: Sequence[float]) -> Vector:
    n = _check_square(a)
    if len(x) != n:
        raise ValueError("dimension mismatch")
    return [sum(a[i][j] * x[j] for j in range(n)) for i in range(n)]


def solve(a: Sequence[Sequence[float]], b: Sequence[float], *, pivot_tol: float = 1e-15) -> Vector:
    """Solve A x=b by Gaussian elimination with partial pivoting."""
    n = _check_square(a)
    if len(b) != n:
        raise ValueError("dimension mismatch")
    aug = [list(map(float, a[i])) + [float(b[i])] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) <= pivot_tol:
            raise ValueError("singular or numerically singular stiffness matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        for j in range(col, n + 1):
            aug[col][j] /= p
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor == 0.0:
                continue
            for j in range(col, n + 1):
                aug[r][j] -= factor * aug[col][j]
    return [aug[i][n] for i in range(n)]


def equilibrium_energy_scales(k: Sequence[Sequence[float]], source: Sequence[float]) -> dict[str, float | Vector]:
    """Return passive-equilibrium displacement and exact energy scales.

    `source` is b=G O in H=1/2 x^T K x-b^T x.
    Positive definiteness is assumed by the theorem and checked separately
    in the preregistered test constructions.
    """
    x = solve(k, source)
    kx = matvec(k, x)
    field = 0.5 * dot(x, kx)
    coupling = -dot(source, x)
    total = field + coupling
    induced = -0.5 * dot(source, x)
    return {
        "x_star": x,
        "field_energy": field,
        "coupling_energy": coupling,
        "total_energy_at_minimum": total,
        "induced_effective_energy": induced,
        "square_completion_residual": total - induced,
    }


def diagonal_null_mode_classification(stiffness: Sequence[float], source: Sequence[float], *, tol: float = 1e-15) -> str:
    """Classify exact diagonal null modes for the preregistered guard."""
    if len(stiffness) != len(source) or not stiffness:
        raise ValueError("dimension mismatch or empty input")
    for lam, s in zip(stiffness, source):
        if lam < -tol:
            return "UNSTABLE_NEGATIVE_STIFFNESS"
        if abs(lam) <= tol and abs(s) > tol:
            return "UNSTABLE_NO_PASSIVE_EQUILIBRIUM"
    return "FINITE_POSITIVE_SUBSPACE"


def diagonal_energy_scale(stiffness: Sequence[float], source: Sequence[float], *, tol: float = 1e-15) -> float:
    """Return 1/2 sum b_i^2/lambda_i, ignoring decoupled exact null modes."""
    status = diagonal_null_mode_classification(stiffness, source, tol=tol)
    if status.startswith("UNSTABLE"):
        raise ValueError(status)
    q = 0.0
    for lam, s in zip(stiffness, source):
        if abs(lam) <= tol:
            continue
        q += 0.5 * s * s / lam
    return q


def rotate_2d_matrix(k: Sequence[Sequence[float]], theta: float) -> Matrix:
    """Return R^T K R for a 2x2 rotation R."""
    if _check_square(k) != 2:
        raise ValueError("2x2 matrix required")
    c, s = math.cos(theta), math.sin(theta)
    r = [[c, -s], [s, c]]
    # K R
    kr = [[sum(k[i][m] * r[m][j] for m in range(2)) for j in range(2)] for i in range(2)]
    # R^T K R
    return [[sum(r[m][i] * kr[m][j] for m in range(2)) for j in range(2)] for i in range(2)]


def rotate_2d_vector(v: Sequence[float], theta: float) -> Vector:
    """Return R^T v for the same rotation convention as rotate_2d_matrix."""
    if len(v) != 2:
        raise ValueError("2-vector required")
    c, s = math.cos(theta), math.sin(theta)
    return [c * v[0] + s * v[1], -s * v[0] + c * v[1]]
