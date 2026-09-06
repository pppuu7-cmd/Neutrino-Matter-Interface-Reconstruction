import math

from nmir.spin_local_sum import (
    all_to_all_heisenberg_bound,
    bounded_coordination_heisenberg_bound,
    heisenberg_bond_operator_norm,
    local_spin_first_moment_bound,
    single_mode_unweighted_strength,
    spin_half_heisenberg_first_moment_bound,
)


def relerr(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-300)


def test_pairwise_spin_half_specialization():
    term_norms = [0.2, 0.3, 0.5]
    generic = local_spin_first_moment_bound(term_norms, [2, 2, 2])
    assert relerr(generic, 2.0 * sum(term_norms)) <= 1e-15


def test_heisenberg_bond_norm_and_envelope():
    assert heisenberg_bond_operator_norm(2.0) == 1.5
    js = [0.1, 0.2, 0.4]
    assert relerr(spin_half_heisenberg_first_moment_bound(js), 1.5 * sum(js)) <= 1e-15


def test_bounded_coordination_scaling_is_extensive():
    one = bounded_coordination_heisenberg_bound(1, 6.0, 1.0)
    big = bounded_coordination_heisenberg_bound(1_000_000, 6.0, 1.0)
    assert relerr(big / one, 1_000_000.0) <= 1e-15
    assert not math.isclose(big / one, 1.0e12, rel_tol=1e-12)


def test_soft_mode_raises_unweighted_strength_not_first_moment():
    m1 = 3.0
    high = single_mode_unweighted_strength(m1, 1.0)
    low = single_mode_unweighted_strength(m1, 1e-6)
    assert low / high >= 1e6
    assert relerr(high * 1.0, m1) <= 1e-15
    assert relerr(low * 1e-6, m1) <= 1e-15


def test_all_to_all_loophole_and_kac_scaling_are_explicit():
    n1 = 1000
    n2 = 1_000_000
    raw1 = all_to_all_heisenberg_bound(n1, 1.0, kac_scale=False)
    raw2 = all_to_all_heisenberg_bound(n2, 1.0, kac_scale=False)
    ratio_raw = raw2 / raw1
    assert ratio_raw > 9.9e5**2 / 1e3**2  # definitely superlinear
    kac1 = all_to_all_heisenberg_bound(n1, 1.0, kac_scale=True)
    kac2 = all_to_all_heisenberg_bound(n2, 1.0, kac_scale=True)
    assert relerr(kac2 / kac1, n2 / n1) <= 1e-12
