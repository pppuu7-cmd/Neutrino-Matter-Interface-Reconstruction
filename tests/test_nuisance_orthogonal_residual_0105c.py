import numpy as np

from nmir.nuisance_orthogonal_residual_0105c import (
    clean_operator_response,
    nuisance_projector,
    project_and_orthonormalize_basis,
    stacked_identifiability_rank,
    weighted_inner,
)


def test_projector_annihilates_nuisance_and_is_idempotent():
    w = np.diag([1.0, 2.0, 4.0, 3.0])
    n = np.array([[1.0], [1.0], [0.0], [0.0]])
    p = nuisance_projector(n, w)
    assert np.allclose(p @ n, 0.0, atol=1e-13)
    assert np.allclose(p @ p, p, atol=1e-13)
    assert np.allclose(n.T @ w @ p, 0.0, atol=1e-13)


def test_metric_orthogonal_signal_is_unchanged():
    w = np.diag([1.0, 2.0, 1.0])
    n = np.array([[1.0], [1.0], [0.0]])
    signal = np.array([2.0, -1.0, 3.0])
    assert abs(weighted_inner(n[:, 0], signal, w)) < 1e-14
    p = nuisance_projector(n, w)
    assert np.allclose(p @ signal, signal, atol=1e-13)


def test_nuisance_degenerate_mode_is_dropped_not_replaced():
    w = np.eye(4)
    n = np.array([[1.0], [1.0], [0.0], [0.0]])
    raw = np.column_stack(
        [
            n[:, 0],
            np.array([1.0, -1.0, 0.0, 0.0]),
            np.array([0.0, 0.0, 1.0, -1.0]),
        ]
    )
    result = project_and_orthonormalize_basis(raw, n, w)
    assert result.dropped_nuisance_degenerate == (0,)
    assert result.kept_indices == (1, 2)
    assert result.vectors.shape == (4, 2)
    assert np.allclose(result.vectors.T @ w @ result.vectors, np.eye(2), atol=1e-13)


def test_projection_can_create_linear_dependence_without_posthoc_replacement():
    w = np.eye(3)
    n = np.array([[1.0], [0.0], [0.0]])
    raw = np.column_stack(
        [
            np.array([0.0, 1.0, 0.0]),
            np.array([1.0, 2.0, 0.0]),
            np.array([0.0, 0.0, 1.0]),
        ]
    )
    result = project_and_orthonormalize_basis(raw, n, w)
    assert result.kept_indices == (0, 2)
    assert result.dropped_linear_dependent == (1,)


def test_cross_regime_stack_recovers_two_parameters_each_regime_cannot():
    w = np.eye(3)

    # Experiment A: nuisance absorbs parameter 2, but parameter 1 is visible.
    nuisance_a = np.array([[0.0], [1.0], [0.0]])
    response_a = np.column_stack(
        [
            np.array([1.0, 0.0, 0.0]),
            np.array([0.0, 1.0, 0.0]),
        ]
    )
    clean_a = clean_operator_response(response_a, nuisance_a, w)

    # Experiment B: nuisance absorbs parameter 1, but parameter 2 is visible.
    nuisance_b = np.array([[1.0], [0.0], [0.0]])
    response_b = np.column_stack(
        [
            np.array([1.0, 0.0, 0.0]),
            np.array([0.0, 0.0, 1.0]),
        ]
    )
    clean_b = clean_operator_response(response_b, nuisance_b, w)

    assert stacked_identifiability_rank([clean_a]) == 1
    assert stacked_identifiability_rank([clean_b]) == 1
    assert stacked_identifiability_rank([clean_a, clean_b]) == 2


def test_shared_direction_degenerate_in_every_regime_stays_unidentifiable():
    w = np.eye(3)
    nuisance_a = np.array([[1.0], [0.0], [0.0]])
    nuisance_b = np.array([[0.0], [1.0], [0.0]])
    response_a = np.array([[1.0], [0.0], [0.0]])
    response_b = np.array([[0.0], [2.0], [0.0]])
    clean_a = clean_operator_response(response_a, nuisance_a, w)
    clean_b = clean_operator_response(response_b, nuisance_b, w)
    assert stacked_identifiability_rank([clean_a, clean_b]) == 0
