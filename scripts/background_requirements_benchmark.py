from __future__ import annotations

import json

from nmir.background_requirements import asimov_significance, max_background_for_significance

SCENARIOS = {
    "design_S10": {"signal_per_year": 10.0, "mass_kg": None},
    "Ar40_10eV_eta0p50": {"signal_per_year": 11.84624201853375, "mass_kg": 10.0},
    "Ar40_20eV_eta0p75": {"signal_per_year": 9.909735084, "mass_kg": 10.0},
}


def main() -> None:
    rows = {}
    max_rel_residual = 0.0
    for name, meta in SCENARIOS.items():
        s = meta["signal_per_year"]
        per_z = {}
        for z in (3.0, 5.0):
            b = max_background_for_significance(s, z)
            z_back = asimov_significance(s, b)
            rel = abs(z_back / z - 1.0)
            max_rel_residual = max(max_rel_residual, rel)
            per_z[str(int(z))] = {
                "bmax_events_per_year": b,
                "bmax_over_signal": b / s,
                "reconstructed_z": z_back,
                "bmax_events_per_kg_year": None if meta["mass_kg"] is None else b / meta["mass_kg"],
            }
        rows[name] = {**meta, "requirements": per_z}

    status = "PASS_BACKGROUND_REQUIREMENT_MAP" if max_rel_residual <= 1e-10 else "FAIL_BACKGROUND_REQUIREMENT_MAP"
    print(json.dumps({
        "status": status,
        "scope": "one-year Poisson counting-only Asimov median discovery requirement with exactly known accepted background expectation",
        "max_relative_inversion_residual": max_rel_residual,
        "scenarios": rows,
        "guards": [
            "accepted indistinguishable background, not raw trigger rate",
            "background normalization uncertainty excluded and will tighten requirements",
            "no claim of current detector performance",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
