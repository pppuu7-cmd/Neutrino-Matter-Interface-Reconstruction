"""Hosted benchmark for NMIR passive convex homogeneous nonlinear mediator gate."""

from __future__ import annotations

import json
import math

from nmir.nonlinear_homogeneous_mediator import (
    analytic_per_particle_gain,
    collective_scaling_energy,
    extensive_gamma,
    scalar_equilibrium,
)


def main() -> None:
    n1, n2 = 1.0e3, 1.0e6
    rows = {}
    max_identity_error = 0.0
    max_extensive_gain_error = 0.0
    max_unscaled_gain_rel_error = 0.0
    for p in (2.0, 3.0, 4.0, 6.0):
        eq = scalar_equilibrium(p=p, kappa=1.7, source=2.3)
        identity_error = max(
            abs(eq["induced_to_stored_ratio"] - (p - 1.0)),
            abs(eq["work_to_stored_ratio"] - p),
            abs(eq["stationarity_residual"]),
        )
        max_identity_error = max(max_identity_error, identity_error)

        gamma_ext = extensive_gamma(p)
        ext1 = collective_scaling_energy(n=n1, p=p, gamma=gamma_ext)
        ext2 = collective_scaling_energy(n=n2, p=p, gamma=gamma_ext)
        stored_ext_gain = ext2["stored_per_particle"] / ext1["stored_per_particle"]
        induced_ext_gain = ext2["induced_per_particle"] / ext1["induced_per_particle"]
        max_extensive_gain_error = max(
            max_extensive_gain_error,
            abs(stored_ext_gain - 1.0),
            abs(induced_ext_gain - 1.0),
        )

        raw1 = collective_scaling_energy(n=n1, p=p, gamma=0.0)
        raw2 = collective_scaling_energy(n=n2, p=p, gamma=0.0)
        raw_gain = raw2["induced_per_particle"] / raw1["induced_per_particle"]
        analytic_gain = analytic_per_particle_gain(n1=n1, n2=n2, p=p, gamma=0.0)
        rel = abs(raw_gain / analytic_gain - 1.0)
        max_unscaled_gain_rel_error = max(max_unscaled_gain_rel_error, rel)
        rows[str(int(p))] = {
            "p": p,
            "induced_to_stored_ratio": eq["induced_to_stored_ratio"],
            "extensive_gamma": gamma_ext,
            "extensive_stored_per_particle_gain": stored_ext_gain,
            "extensive_induced_per_particle_gain": induced_ext_gain,
            "unscaled_per_particle_gain": raw_gain,
            "unscaled_analytic_gain": analytic_gain,
        }

    status = "PASS_NONLINEAR_HOMOGENEOUS_BUDGET"
    if not (
        max_identity_error < 1e-12
        and max_extensive_gain_error < 1e-12
        and max_unscaled_gain_rel_error < 1e-12
        and math.isclose(rows["2"]["extensive_gamma"], 0.5, rel_tol=0, abs_tol=1e-15)
        and math.isclose(rows["4"]["extensive_gamma"], 0.25, rel_tol=0, abs_tol=1e-15)
        and math.isclose(rows["4"]["induced_to_stored_ratio"], 3.0, rel_tol=1e-12)
    ):
        status = "FAIL_NONLINEAR_HOMOGENEOUS_BUDGET"

    result = {
        "status": status,
        "N1": n1,
        "N2": n2,
        "rows": rows,
        "max_identity_absolute_error": max_identity_error,
        "max_extensive_per_particle_gain_abs_error_to_1": max_extensive_gain_error,
        "max_unscaled_gain_relative_error": max_unscaled_gain_rel_error,
        "interpretation": (
            "For a passive stable convex p-homogeneous medium, Euler homogeneity gives "
            "|E_induced|=(p-1)V at equilibrium. A collective unscaled source can look "
            "superextensive, but the medium/free-energy budget is superextensive by the same N exponent. "
            "Scaling g_N as N^(-1/p) restores extensivity and removes parametric per-particle gain."
        ),
        "scope": (
            "differentiable convex positive p-homogeneous passive media with fixed p>1; "
            "non-convex/multistable, mixed-degree crossover, driven/active, higher-body, BSM and gravity excluded"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if status != "PASS_NONLINEAR_HOMOGENEOUS_BUDGET":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
