from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

from nmir.g9_continuous_projection import (
    continuous_focal_distance_au,
    continuous_projected_mass_derivative_g_per_x,
    continuous_projected_mass_g,
)
from nmir.gravity_extended import RadialDensityProfile

SCRIPT = Path(__file__).parents[1] / "scripts" / "g9_continuous_map_turning_roots_0089c.py"
spec = importlib.util.spec_from_file_location("g9_0089c", SCRIPT)
assert spec is not None and spec.loader is not None
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_bulk_port_matches_accepted_scalar_on_toy_profile():
    profile = RadialDensityProfile(
        (0.0, 0.12, 0.31, 0.57, 0.82, 1.0),
        (10.0, 8.2, 5.4, 2.7, 0.9, 0.15),
    )
    bulk = mod._bulk_eval_factory(profile)
    xs = np.asarray([1e-4, 0.03, 0.12, 0.29, 0.57, 0.77, 0.97, 0.999], dtype=float)
    bm, bd, bf = bulk(xs, need_derivative=True, chunk=3)
    for i, x in enumerate(xs):
        sm = continuous_projected_mass_g(profile, float(x), mod.R)
        sd = continuous_projected_mass_derivative_g_per_x(profile, float(x), mod.R)
        sf = continuous_focal_distance_au(profile, float(x), mod.R)
        assert mod.symrel(float(bm[i]), sm) <= 2e-12
        assert mod.symrel(float(bd[i]), sd) <= 2e-11
        assert mod.symrel(float(bf[i]), sf) <= 2e-12


def test_bracket_builder_finds_sign_change_and_near_zero_bridge():
    pts = np.asarray([0.0, 1.0, 2.0, 3.0, 4.0])
    signs = np.asarray([1, 1, 0, -1, -1], dtype=np.int8)
    assert mod.brackets_from_sequence(pts, signs) == [(1.0, 3.0)]


def test_bracket_builder_rejects_unresolved_near_zero():
    pts = np.asarray([0.0, 1.0, 2.0])
    signs = np.asarray([1, 0, 1], dtype=np.int8)
    try:
        mod.brackets_from_sequence(pts, signs)
    except mod.Blocked:
        pass
    else:
        raise AssertionError("unresolved near-zero must fail closed")
