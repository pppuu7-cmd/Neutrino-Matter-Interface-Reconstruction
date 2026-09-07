import math

import pytest

from nmir.g9_persistent_lens import (
    large_source_ring_excess_upper,
    one_ring_receiver_mu,
    perfect_whole_sun_mu_upper,
    point_receiver_azimuth_fraction,
    uniform_disk_offset_samples,
)


def test_point_receiver_fraction_limits_and_partial_overlap():
    assert point_receiver_azimuth_fraction(0.0, 0.5, 1.0) == 1.0
    assert point_receiver_azimuth_fraction(0.0, 2.0, 1.0) == 0.0
    assert point_receiver_azimuth_fraction(0.5, 0.0, 1.0) == 1.0
    assert point_receiver_azimuth_fraction(2.0, 0.0, 1.0) == 0.0
    p = point_receiver_azimuth_fraction(1.0, 1.0, 1.0)
    assert p == pytest.approx(1.0 / 3.0, rel=0, abs=1e-14)


def test_uniform_disk_samples_are_rotation_symmetric():
    samples = uniform_disk_offset_samples(3.0, 0.0, 8, 16)
    assert len(samples) == 128
    mean_r2 = sum(x * x for x in samples) / len(samples)
    assert mean_r2 == pytest.approx(4.5, rel=0, abs=1e-12)


def test_one_ring_linear_toy_trapezoid_is_symmetric_and_finite():
    # Toy y=k|b-b0|.  This regression checks the implemented nonuniform-b
    # trapezoid convention; physical accuracy is independently benchmarked against
    # the exact annular solver in scripts/g9_persistent_lens_benchmark.py.
    b0 = 0.2
    k = 1000.0
    a = 1.0
    db = a / k
    grid = (
        (b0 - 2 * db, 2.0),
        (b0 - db, 1.0),
        (b0, 0.0),
        (b0 + db, 1.0),
        (b0 + 2 * db, 2.0),
    )
    mu = one_ring_receiver_mu(grid, a, 0.0, 0.0, solar_radius_cm=1.0)
    # p=[0,1,1,1,0] gives integral 3*b0*db and ring term 2*integral.
    assert mu == pytest.approx(1.0 + 6.0 * b0 * db, rel=1e-12)


def test_upper_ceiling_and_large_source_asymptote_are_finite():
    assert perfect_whole_sun_mu_upper(100.0) > 1.0
    assert large_source_ring_excess_upper(1e12) < large_source_ring_excess_upper(1e11)
    assert math.isfinite(large_source_ring_excess_upper(1e15))


def test_bad_inputs_fail_closed():
    with pytest.raises(ValueError):
        point_receiver_azimuth_fraction(1.0, 1.0, 0.0)
    with pytest.raises(ValueError):
        uniform_disk_offset_samples(-1.0, 0.0)
    with pytest.raises(ValueError):
        perfect_whole_sun_mu_upper(0.0)
