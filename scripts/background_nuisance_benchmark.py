from __future__ import annotations

import json

from nmir.background_nuisance import (
    asimov_significance_with_background_uncertainty,
    max_background_for_significance_with_uncertainty,
)

SCENARIOS = {
    "design_S10": {"signal_per_year": 10.0, "mass_kg": None},
    "Ar40_10eV_eta0p50": {"signal_per_year": 11.84624201853375, "mass_kg": 10.0},
    "Ar40_20eV_eta0p75": {"signal_per_year": 9.909735084, "mass_kg": 10.0},
}
DELTAS = (0.0, 0.10, 0.30, 0.50)
TARGET_Z = (3.0, 5.0)
KNOWN_0050 = {
    (10.0, 3.0): 8.22524098773645,
    (10.0, 5.0): 1.7175266766193094,
    (11.84624201853375, 3.0): 12.098668408825569,
    (11.84624201853375, 5.0): 2.7565547482229014,
    (9.909735084, 3.0): 8.05522455930435,
    (9.909735084, 5.0): 1.6734179605645096,
}


def main() -> None:
    rows = {}
    max_rel_residual = 0.0
    max_zero_rel_error = 0.0
    strict_uncertainty_tightening = True
    five_sigma_stricter = True

    for name, meta in SCENARIOS.items():
        s = meta["signal_per_year"]
        per_delta = {}
        b_by_delta_z = {}

        for delta in DELTAS:
            per_z = {}
            for z in TARGET_Z:
                b = max_background_for_significance_with_uncertainty(s, z, delta)
                z_back = asimov_significance_with_background_uncertainty(s, b, delta)
                rel = abs(z_back / z - 1.0)
                max_rel_residual = max(max_rel_residual, rel)
                b_by_delta_z[(delta, z)] = b
                b0 = KNOWN_0050[(s, z)]
                if delta == 0.0:
                    max_zero_rel_error = max(max_zero_rel_error, abs(b / b0 - 1.0))
                per_z[str(int(z))] = {
                    "bmax_events_per_year": b,
                    "bmax_over_signal": b / s,
                    "bmax_events_per_kg_year": None if meta["mass_kg"] is None else b / meta["mass_kg"],
                    "tightening_ratio_to_delta0": b / b0,
                    "reconstructed_z": z_back,
                }
            per_delta[f"{delta:.2f}"] = per_z

        for z in TARGET_Z:
            vals = [b_by_delta_z[(delta, z)] for delta in DELTAS]
            strict_uncertainty_tightening &= all(a > b for a, b in zip(vals, vals[1:]))
        for delta in DELTAS:
            five_sigma_stricter &= b_by_delta_z[(delta, 5.0)] < b_by_delta_z[(delta, 3.0)]

        rows[name] = {**meta, "by_fractional_background_uncertainty": per_delta}

    passed = (
        max_rel_residual <= 1e-10
        and max_zero_rel_error <= 1e-10
        and strict_uncertainty_tightening
        and five_sigma_stricter
    )
    status = "PASS_BACKGROUND_NUISANCE_REQUIREMENT_MAP" if passed else "FAIL_BACKGROUND_NUISANCE_REQUIREMENT_MAP"

    print(json.dumps({
        "status": status,
        "scope": "one-year one-bin profile-likelihood Asimov median discovery requirement with Gaussian accepted-background normalization nuisance",
        "fractional_background_uncertainties": DELTAS,
        "max_relative_inversion_residual": max_rel_residual,
        "max_delta0_relative_error_vs_0050": max_zero_rel_error,
        "strict_uncertainty_tightening": strict_uncertainty_tightening,
        "five_sigma_stricter_than_three_sigma": five_sigma_stricter,
        "scenarios": rows,
        "guards": [
            "accepted indistinguishable background, not raw trigger or environmental background",
            "fractional uncertainty is a Gaussian normalization nuisance in a one-bin Asimov model",
            "no detector-specific recoil-shape discrimination, threshold distribution, or calibration claim",
            "no claim that any current detector attains the assumed uncertainty",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
