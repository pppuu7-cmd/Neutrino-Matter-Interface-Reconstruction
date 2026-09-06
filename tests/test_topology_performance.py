import math

from nmir.topology_performance import (
    ACCEPTANCES,
    BRANCHES,
    required_topology_envelope,
    solve_rejection,
)

FROZEN_0057 = {
    "authority_capped_900d": 17757030.4169906,
    "stress_3y": 14440370.654436817,
}


def test_full_acceptance_reproduces_0057():
    result = required_topology_envelope(n=4096)
    for branch in BRANCHES:
        row = result["branches"][branch]
        assert math.isclose(
            row["base_rejection_full_acceptance"], FROZEN_0057[branch], rel_tol=1e-8
        )
        eps1 = row["acceptance_budget"]["1.0"]
        assert math.isclose(
            eps1["fixed_exposure"], FROZEN_0057[branch], rel_tol=1e-8
        )
        assert math.isclose(
            eps1["signal_restored_exposure"], FROZEN_0057[branch], rel_tol=1e-8
        )


def test_acceptance_loss_never_improves_requirement():
    result = required_topology_envelope(n=4096)
    for branch in BRANCHES:
        rows = result["branches"][branch]["acceptance_budget"]
        fixed = [rows[str(eps)]["fixed_exposure"] for eps in ACCEPTANCES]
        restored = [rows[str(eps)]["signal_restored_exposure"] for eps in ACCEPTANCES]
        assert all(b >= a for a, b in zip(fixed, fixed[1:]))
        assert all(b >= a for a, b in zip(restored, restored[1:]))


def test_restored_exposure_exact_law_and_fixed_is_harder():
    result = required_topology_envelope(n=4096)
    for branch in BRANCHES:
        base = result["branches"][branch]["base_rejection_full_acceptance"]
        rows = result["branches"][branch]["acceptance_budget"]
        for eps in ACCEPTANCES:
            row = rows[str(eps)]
            assert math.isclose(
                row["signal_restored_exposure"], base / eps, rel_tol=2e-14
            )
            if eps < 1.0:
                assert row["fixed_exposure"] >= row["signal_restored_exposure"]


def test_all_frozen_requirements_remain_million_scale():
    result = required_topology_envelope(n=4096)
    for branch in BRANCHES:
        for row in result["branches"][branch]["acceptance_budget"].values():
            assert row["fixed_exposure"] > 1e6
            assert row["signal_restored_exposure"] > 1e6


def test_grid_refinement_converges():
    for branch in BRANCHES:
        for eps in (1.0, 0.5, 0.3):
            coarse = solve_rejection(branch, 30.0 * eps, n=4096)
            fine = solve_rejection(branch, 30.0 * eps, n=8192)
            assert math.isclose(coarse, fine, rel_tol=1e-8)


def test_outputs_finite_positive():
    result = required_topology_envelope(n=4096)
    for branch in BRANCHES:
        base = result["branches"][branch]["base_rejection_full_acceptance"]
        assert math.isfinite(base) and base > 0
        for row in result["branches"][branch]["acceptance_budget"].values():
            assert all(math.isfinite(v) and v > 0 for v in row.values())
