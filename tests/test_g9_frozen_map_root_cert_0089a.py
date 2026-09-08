import pytest

from nmir.g9_frozen_map_root_cert import (
    RootCertificationBlocked,
    base_fractions,
    stress_fractions,
    stress_mid_fractions,
    roots_from_probes,
    match_root_sets,
    sign_with_tau,
)


def sfn(fn):
    return lambda x: sign_with_tau(fn(x), max(1.0, abs(fn(x))))


def test_frozen_probe_meshes_are_deterministic_and_interior():
    b = base_fractions()
    s = stress_fractions()
    m = stress_mid_fractions()
    assert b == tuple(sorted(set(b)))
    assert s == tuple(sorted(set(s)))
    assert len(m) == 64
    assert all(0.0 < x < 1.0 for x in b + s + m)
    assert set(b).issubset(set(s))


def test_one_interior_turn_q32_q64_matches():
    fn = lambda x: x - 0.37123456789
    r32 = roots_from_probes(fn, sfn(fn), base_fractions())
    r64 = roots_from_probes(fn, sfn(fn), stress_fractions())
    match_root_sets(r32, r64)
    assert len(r64) == 1
    assert abs(r64[0].root - 0.37123456789) < 1e-11
    assert r64[0].orientation == (-1, 1)


def test_three_separated_turns_are_all_recovered():
    fn = lambda x: (x - 0.21) * (x - 0.53) * (x - 0.82)
    r32 = roots_from_probes(fn, sfn(fn), base_fractions())
    r64 = roots_from_probes(fn, sfn(fn), stress_fractions())
    match_root_sets(r32, r64)
    assert len(r64) == 3
    for got, want in zip(r64, (0.21, 0.53, 0.82)):
        assert abs(got.root - want) < 1e-10


def test_near_zero_probe_is_associated_only_with_sign_changing_root():
    fn = lambda x: x - 0.5
    roots = roots_from_probes(fn, sfn(fn), stress_fractions())
    assert len(roots) == 1
    assert roots[0].root == pytest.approx(0.5, abs=1e-12)


def test_unassociated_near_zero_probe_blocks_fail_closed():
    # Even-multiplicity zero at a frozen probe has no sign reversal and therefore
    # cannot be promoted to a certified turning root under 0089a.
    fn = lambda x: (x - 0.5) ** 2
    with pytest.raises(RootCertificationBlocked):
        roots_from_probes(fn, sfn(fn), stress_fractions())


def test_scale_aware_threshold_is_not_relaxed():
    assert sign_with_tau(1e-6, 1.0) == 1
    assert sign_with_tau(-1e-6, 1.0) == -1
    assert sign_with_tau(1e-12, 1.0) == 0
    with pytest.raises(RootCertificationBlocked):
        sign_with_tau(1.0, float("inf"))
