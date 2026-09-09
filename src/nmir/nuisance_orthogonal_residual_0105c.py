"""NMIR v2 gate 0105c: nuisance-orthogonal residual geometry.

This module implements only pre-data linear-algebra controls frozen in
research/prereg/0105c_nuisance_orthogonal_residual_statistic.md.
It does not inspect observed residuals and does not calculate discovery
significances.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np


@dataclass(frozen=True)
class OrthonormalizedBasis:
    vectors: np.ndarray
    kept_indices: tuple[int, ...]
    dropped_nuisance_degenerate: tuple[int, ...]
    dropped_linear_dependent: tuple[int, ...]


def _as_2d(name: str, value: np.ndarray | Sequence[Sequence[float]]) -> np.ndarray:
    arr = np.asarray(value, dtype=float)
    if arr.ndim != 2:
        raise ValueError(f"{name} must be a 2D array")
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must contain only finite values")
    return arr


def _validated_metric(metric: np.ndarray | Sequence[Sequence[float]], n: int) -> np.ndarray:
    w = _as_2d("metric", metric)
    if w.shape != (n, n):
        raise ValueError("metric must be square with one row per bin")
    if not np.allclose(w, w.T, rtol=1e-12, atol=1e-14):
        raise ValueError("metric must be symmetric")
    evals = np.linalg.eigvalsh(w)
    scale = max(1.0, float(np.max(np.abs(evals))))
    if float(np.min(evals)) < -1e-12 * scale:
        raise ValueError("metric must be positive semidefinite")
    return w


def weighted_inner(a: np.ndarray, b: np.ndarray, metric: np.ndarray) -> float:
    av = np.asarray(a, dtype=float).reshape(-1)
    bv = np.asarray(b, dtype=float).reshape(-1)
    if av.shape != bv.shape:
        raise ValueError("vectors must have matching shape")
    w = _validated_metric(metric, av.size)
    return float(av @ w @ bv)


def weighted_norm(vector: np.ndarray, metric: np.ndarray) -> float:
    value = weighted_inner(vector, vector, metric)
    if value < 0.0 and abs(value) < 1e-12:
        value = 0.0
    if value < 0.0:
        raise ValueError("negative squared norm under supplied metric")
    return float(np.sqrt(value))


def nuisance_projector(
    nuisance_tangents: np.ndarray | Sequence[Sequence[float]],
    metric: np.ndarray | Sequence[Sequence[float]],
    *,
    rcond: float = 1e-12,
) -> np.ndarray:
    """Return P_perp = I - N (N^T W N)^+ N^T W."""
    nmat = _as_2d("nuisance_tangents", nuisance_tangents)
    n_bins, _ = nmat.shape
    w = _validated_metric(metric, n_bins)
    if rcond <= 0.0 or not np.isfinite(rcond):
        raise ValueError("rcond must be finite and > 0")
    if nmat.shape[1] == 0:
        return np.eye(n_bins, dtype=float)
    gram = nmat.T @ w @ nmat
    gram_pinv = np.linalg.pinv(gram, rcond=rcond, hermitian=True)
    return np.eye(n_bins, dtype=float) - nmat @ gram_pinv @ nmat.T @ w


def project_and_orthonormalize_basis(
    raw_basis: np.ndarray | Sequence[Sequence[float]],
    nuisance_tangents: np.ndarray | Sequence[Sequence[float]],
    metric: np.ndarray | Sequence[Sequence[float]],
    *,
    nuisance_degeneracy_ratio: float = 1e-8,
    linear_dependence_ratio: float = 1e-12,
    rcond: float = 1e-12,
) -> OrthonormalizedBasis:
    """Project basis columns away from nuisance tangents, preserving order."""
    basis = _as_2d("raw_basis", raw_basis)
    n_bins, n_modes = basis.shape
    nmat = _as_2d("nuisance_tangents", nuisance_tangents)
    if nmat.shape[0] != n_bins:
        raise ValueError("nuisance_tangents and raw_basis must share bin dimension")
    w = _validated_metric(metric, n_bins)
    if not (0.0 < nuisance_degeneracy_ratio < 1.0):
        raise ValueError("nuisance_degeneracy_ratio must lie in (0,1)")
    if not (0.0 < linear_dependence_ratio < 1.0):
        raise ValueError("linear_dependence_ratio must lie in (0,1)")

    projector = nuisance_projector(nmat, w, rcond=rcond)
    kept: list[int] = []
    nuisance_dropped: list[int] = []
    linear_dropped: list[int] = []
    q_vectors: list[np.ndarray] = []

    for k in range(n_modes):
        raw = basis[:, k]
        raw_norm = weighted_norm(raw, w)
        projected = projector @ raw
        projected_norm = weighted_norm(projected, w)

        if raw_norm == 0.0 or projected_norm < nuisance_degeneracy_ratio * raw_norm:
            nuisance_dropped.append(k)
            continue

        residual = projected.copy()
        # Modified weighted Gram-Schmidt in the prospectively fixed column order.
        for q in q_vectors:
            residual -= q * weighted_inner(q, residual, w)
        residual_norm = weighted_norm(residual, w)
        if residual_norm < linear_dependence_ratio * projected_norm:
            linear_dropped.append(k)
            continue

        q_vectors.append(residual / residual_norm)
        kept.append(k)

    vectors = np.column_stack(q_vectors) if q_vectors else np.zeros((n_bins, 0), dtype=float)
    return OrthonormalizedBasis(
        vectors=vectors,
        kept_indices=tuple(kept),
        dropped_nuisance_degenerate=tuple(nuisance_dropped),
        dropped_linear_dependent=tuple(linear_dropped),
    )


def clean_operator_response(
    response_jacobian: np.ndarray | Sequence[Sequence[float]],
    nuisance_tangents: np.ndarray | Sequence[Sequence[float]],
    metric: np.ndarray | Sequence[Sequence[float]],
    *,
    rcond: float = 1e-12,
) -> np.ndarray:
    response = _as_2d("response_jacobian", response_jacobian)
    nmat = _as_2d("nuisance_tangents", nuisance_tangents)
    if response.shape[0] != nmat.shape[0]:
        raise ValueError("response and nuisance tangents must share bin dimension")
    w = _validated_metric(metric, response.shape[0])
    return nuisance_projector(nmat, w, rcond=rcond) @ response


def matrix_rank_relative(matrix: np.ndarray | Sequence[Sequence[float]], *, rtol: float = 1e-10) -> int:
    arr = _as_2d("matrix", matrix)
    if not (0.0 < rtol < 1.0):
        raise ValueError("rtol must lie in (0,1)")
    if min(arr.shape) == 0:
        return 0
    singular = np.linalg.svd(arr, compute_uv=False)
    if singular.size == 0 or singular[0] == 0.0:
        return 0
    return int(np.count_nonzero(singular > rtol * singular[0]))


def stacked_identifiability_rank(
    cleaned_jacobians: Iterable[np.ndarray | Sequence[Sequence[float]]],
    *,
    rtol: float = 1e-10,
) -> int:
    blocks = [_as_2d("cleaned_jacobian", block) for block in cleaned_jacobians]
    if not blocks:
        raise ValueError("at least one cleaned Jacobian is required")
    n_parameters = blocks[0].shape[1]
    if any(block.shape[1] != n_parameters for block in blocks):
        raise ValueError("all cleaned Jacobians must share parameter dimension")
    stacked = np.vstack(blocks)
    return matrix_rank_relative(stacked, rtol=rtol)
