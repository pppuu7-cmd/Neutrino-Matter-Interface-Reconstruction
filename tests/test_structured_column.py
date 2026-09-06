import itertools
import math
import random

from nmir.structured_column import (
    absorption_from_optical_depth,
    layered_absorption,
    mass_specific_optical_depth_coefficient,
    stressed_atomic_layer_geometry,
    tilted_capture_factor,
)


def test_layer_order_is_exactly_invariant():
    taus = (1.0e-6, 2.0e-4, 0.03, 1.2)
    ref = layered_absorption(taus)
    for perm in itertools.permutations(taus):
        assert math.isclose(layered_absorption(perm), ref, rel_tol=0.0, abs_tol=1.0e-15)


def test_layered_absorption_equals_sum_tau_formula():
    taus = (0.2, 0.4, 0.7)
    assert math.isclose(layered_absorption(taus), absorption_from_optical_depth(sum(taus)), rel_tol=0, abs_tol=0)


def test_fixed_mass_mixture_never_beats_best_component():
    rng = random.Random(20260906)
    for _ in range(1000):
        raw = [rng.random() for _ in range(5)]
        total = sum(raw)
        weights = [x / total for x in raw]
        kappas = [10 ** rng.uniform(-6, 6) for _ in range(5)]
        mixed = mass_specific_optical_depth_coefficient(weights, kappas)
        assert mixed <= max(kappas) * (1.0 + 1.0e-14)
        assert mixed >= min(kappas) * (1.0 - 1.0e-14)


def test_tilt_never_increases_total_capture_factor():
    taus = [1.0e-12, 1.0e-8, 1.0e-4, 0.1, 1.0, 10.0, 100.0]
    cosines = [1.0e-4, 1.0e-3, 1.0e-2, 0.1, 0.25, 0.5, 0.9, 1.0]
    for tau in taus:
        face = tilted_capture_factor(tau, 1.0)
        for c in cosines:
            assert tilted_capture_factor(tau, c) <= face * (1.0 + 1.0e-12)


def test_thin_tilt_limit_is_nearly_angle_invariant_when_tau_over_c_is_small():
    tau = 1.0e-12
    face = tilted_capture_factor(tau, 1.0)
    tilted = tilted_capture_factor(tau, 0.1)
    assert math.isclose(tilted / face, 1.0, rel_tol=1.0e-10)


def test_atomic_stress_still_needs_enormous_layer_count():
    row = stressed_atomic_layer_geometry()
    assert row["tau_per_ideal_dense_layer"] < 1.0e-15
    assert row["layers_for_tau_one"] > 1.0e15
    assert row["thickness_for_tau_one_m"] > 1.0e6
    assert row["effective_interaction_radius_m"] < 1.0e-18
