import math

from nmir.density_fsum import (
    deposition_proxy,
    energy_weighted_strength,
    identical_constituent_fsum,
    response_from_shape,
    single_mode_response,
    unweighted_strength,
    weighted_density_fsum,
)


def relerr(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-300)


def test_weighted_density_fsum_matches_identical_closed_form():
    q = 0.02
    m = 0.51099895
    g = 0.73
    n = 17
    direct = weighted_density_fsum(q, [m] * n, [g] * n)
    closed = identical_constituent_fsum(q, m, g, n)
    assert relerr(direct, closed) <= 1e-15


def test_spectral_rearrangements_preserve_m1_and_unit_kernel_deposition():
    m1 = 2.3456789e-5
    responses = [
        single_mode_response(m1, 1e-3),
        single_mode_response(m1, 1e-9),
        response_from_shape(m1, [1e-6, 2e-4, 4e-3], [5.0, 2.0, 1.0]),
        response_from_shape(m1, [0.999999, 1.0, 1.000001], [1.0, 4.0, 1.0]),
    ]
    for response in responses:
        assert relerr(energy_weighted_strength(response), m1) <= 1e-12
        assert relerr(deposition_proxy(response, lambda _: 1.0), m1) <= 1e-12


def test_bounded_kernel_obeys_fsum_bound():
    m1 = 7.0e-4
    kmax = 3.25
    response = response_from_shape(m1, [1e-8, 1e-5, 1e-2, 0.5], [7.0, 2.0, 3.0, 1.0])
    kernel = lambda e: kmax * (0.2 + 0.8 * math.exp(-e))
    assert deposition_proxy(response, kernel) <= kmax * m1 * (1.0 + 1e-12)


def test_low_energy_collective_mode_can_raise_unweighted_strength_without_energy_gain():
    m1 = 1.0
    high = single_mode_response(m1, 1.0)
    low = single_mode_response(m1, 1e-6)
    gain = unweighted_strength(low) / unweighted_strength(high)
    assert gain >= 1e6
    assert relerr(deposition_proxy(low, lambda _: 1.0), deposition_proxy(high, lambda _: 1.0)) <= 1e-12


def test_fsum_scales_linearly_not_quadratically_with_constituent_count():
    q = 0.01
    mass = 938.0
    coupling = 1.0
    m1_one = identical_constituent_fsum(q, mass, coupling, 1)
    m1_big = identical_constituent_fsum(q, mass, coupling, 1_000_000)
    assert relerr(m1_big / m1_one, 1_000_000.0) <= 1e-15
    assert not math.isclose(m1_big / m1_one, 1_000_000.0**2, rel_tol=1e-12)
