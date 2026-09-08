from __future__ import annotations

import importlib.util
from pathlib import Path

import mpmath as mp

from nmir.g9_continuous_projection import continuous_projected_mass_derivative_g_per_x
from nmir.gravity_extended import RadialDensityProfile

SCRIPT = Path(__file__).parents[1] / "scripts" / "g9_0089b_high_x_derivative_diag.py"
spec = importlib.util.spec_from_file_location("g9_0089b_high_x_diag", SCRIPT)
assert spec is not None and spec.loader is not None
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_theta_and_t_references_agree_on_fixed_toy():
    profile = RadialDensityProfile(
        (0.0, 0.2, 0.55, 0.82, 1.0),
        (8.0, 6.1, 3.2, 1.1, 0.2),
    )
    a, b = mod.references(profile, x_float=0.83, radius_cm=11.0)
    assert mod.symrel_mp(a, b) <= mp.mpf("1e-20")


def test_two_reference_consensus_matches_production_on_fixed_toy():
    profile = RadialDensityProfile(
        (0.0, 0.2, 0.55, 0.82, 1.0),
        (8.0, 6.1, 3.2, 1.1, 0.2),
    )
    a, b = mod.references(profile, x_float=0.83, radius_cm=11.0)
    consensus = (a + b) / 2
    got = continuous_projected_mass_derivative_g_per_x(profile, 0.83, 11.0)
    rel = abs(mp.mpf(repr(got)) - consensus) / max(abs(consensus), abs(mp.mpf(repr(got))))
    assert rel <= mp.mpf("1e-10")
