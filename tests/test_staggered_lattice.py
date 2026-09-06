import math

import pytest

from nmir.staggered_lattice import (
    elastic_structure_factor,
    geometric_nuclear_covering_per_layer,
    layers_for_geometric_covering,
    normalized_directional_gain,
    staggered_layer_positions,
)


def test_zero_momentum_directional_gain_reaches_n():
    positions = staggered_layer_positions(4, 3e-10, 1e-10)
    assert normalized_directional_gain(0.0, 0.0, positions) == pytest.approx(4.0)


def test_two_layer_destructive_interference():
    positions = [(0.0, 0.0), (0.5, 0.0)]
    f = elastic_structure_factor(2.0 * math.pi, 0.0, positions)
    assert abs(f) == pytest.approx(0.0, abs=1e-12)


def test_wrapped_staggering_repeats_unit_cell():
    positions = staggered_layer_positions(4, 1.0, 0.5, lattice_period_m=1.0)
    assert [p[0] for p in positions] == pytest.approx([0.0, 0.5, 0.0, 0.5])


def test_nuclear_geometric_covering_scale():
    f = geometric_nuclear_covering_per_layer(5e-15, 3e-10)
    assert f == pytest.approx(8.72664626e-10, rel=1e-8)
    n = layers_for_geometric_covering(5e-15, 3e-10)
    assert n == pytest.approx(1.14591559e9, rel=1e-8)
