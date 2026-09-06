from __future__ import annotations

import math

from nmir.klocal_higher_body import (
    classify_growing_coordination,
    contiguous_supports,
    frozen_m1_bound,
    frozen_triplet_bound,
    max_incidence,
    measured_m1,
    nested_local_commutator_amplitude,
    overlapping_triple_count,
    random_model,
)


def test_support_enumeration_never_exceeds_frozen_bound():
    for periodic in (False, True):
        for n in (4, 5, 6, 8):
            for k in (1, 2, 3):
                for l in (1, 2, 3):
                    if k > n or l > n:
                        continue
                    os = contiguous_supports(n, k, periodic)
                    hs = contiguous_supports(n, l, periodic)
                    d_o = max_incidence(n, os)
                    d_h = max_incidence(n, hs)
                    exact = overlapping_triple_count(os, hs)
                    bound = frozen_triplet_bound(n, k, l, d_o, d_h)
                    assert exact <= bound


def test_random_pauli_models_obey_local_nested_bound_and_global_m1_bound():
    o0 = 0.7
    h0 = 0.9
    for periodic in (False, True):
        for seed in range(8):
            n, k, l = 4, 2, 2
            os, hs, ot, ht, state = random_model(n, k, l, periodic, seed, o0=o0, h0=h0)
            local_bound = 4.0 * o0 * o0 * h0
            for z in ot:
                for h in ht:
                    for x in ot:
                        amp = nested_local_commutator_amplitude(z, h, x)
                        assert amp <= local_bound + 1e-15
            d_o = max_incidence(n, os)
            d_h = max_incidence(n, hs)
            bound = frozen_m1_bound(n, k, l, d_o, d_h, o0, h0)
            assert measured_m1(ot, ht, state) <= bound + 1e-12


def test_frozen_bound_per_site_is_constant_at_fixed_locality():
    k, l = 2, 3
    vals = []
    for n in (6, 8, 10, 12, 16, 20):
        os = contiguous_supports(n, k, True)
        hs = contiguous_supports(n, l, True)
        d_o = max_incidence(n, os)
        d_h = max_incidence(n, hs)
        vals.append(frozen_m1_bound(n, k, l, d_o, d_h, 1.0, 1.0) / n)
    assert max(vals) - min(vals) < 1e-12


def test_growing_coordination_counterexample_is_outside_scope():
    rows = [classify_growing_coordination(n) for n in (4, 8, 16, 32)]
    assert all(row["classification"] == "OUTSIDE_SCOPE_GROWING_COORDINATION" for row in rows)
    assert [row["d_o"] for row in rows] == [3, 7, 15, 31]
    assert all(not row["fixed_coordination"] for row in rows)
