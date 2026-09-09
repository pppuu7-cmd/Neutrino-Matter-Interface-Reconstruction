#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

from g9_persistent_global_0090 import CONTROLS

PREREG_COMMIT = "53863048c2d5b5803c9e120794c21fe415f1b319"
AMENDMENT_COMMIT = "3f873eb3ab8d90b931eb41f5ba25484fde843ced"
PARENT_PASS = "PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS"
NOT_RUN = "NOT_RUN_V2_G9_0097_PARENT_NOT_PASSED"
ACTIVE_PASS = "PASS_V2_G9_BETELGEUSE_ACTIVE_LINE_TRACKING_KINEMATICS"
ACTIVE_FAIL = "SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_ACTIVE_ASTROMETRY_50MAS"
PASS_ACTIVE_PASSIVE_FAIL = "PASS_V2_G9_BETELGEUSE_ACTIVE_KINEMATICS_PASSIVE_FAIL"
PASS_BOTH = "PASS_V2_G9_BETELGEUSE_BOTH_ARCHITECTURES"
FAIL_BOTH = "SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_LINE_TRACKING_ACTIONABILITY"
PASSIVE_PASS = "PASS_V2_G9_BETELGEUSE_SINGLE_PASSIVE_CONTINUOUS_COVERAGE"
PASSIVE_FAIL = "SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_SINGLE_PASSIVE_CONTINUOUS_COVERAGE"
BLOCKED = "BLOCKED_V2_G9_BETELGEUSE_LINE_TRACKING_AUTHORITY"
INFRA = "INFRASTRUCTURE_FAIL_V2_G9_0097"

# Frozen source astrometry from Harper et al. 2017, arXiv:1706.06020.
MU_ALPHA_MASYR = 26.42
MU_ALPHA_SIGMA_MASYR = 0.25
MU_DELTA_MASYR = 9.60
MU_DELTA_SIGMA_MASYR = 0.12
COSMIC_NOISE_MAS = 2.4
HORIZON_JULIAN_YR = 10.0
BETA_SUPPORT_MAS = 50.0

# IAU exact astronomical unit (2012 Resolution B2) and IAU 2015 B3
# exact nominal solar mass parameter, used here as a traceable conversion constant.
AU_M = 149_597_870_700.0
GM_SUN_NOMINAL_M3_S2 = 1.3271244e20
JULIAN_YEAR_S = 365.25 * 86400.0


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def mas_to_rad(x: float) -> float:
    return (x / 1000.0) * math.pi / (180.0 * 3600.0)


def finite_positive(*xs: float) -> bool:
    return all(math.isfinite(x) and x > 0.0 for x in xs)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    parent_path = Path(args.parent)

    try:
        parent = json.loads(parent_path.read_text())
        parent_hash = sha256(parent_path)
        parent_status = str(parent.get("status", ""))
        parent_run_id = os.getenv("PARENT_RUN_ID")
        parent_artifact_id = os.getenv("PARENT_ARTIFACT_ID")

        base = {
            "prereg_commit": PREREG_COMMIT,
            "amendment_0097a_commit": AMENDMENT_COMMIT,
            "head_sha": os.getenv("GITHUB_SHA"),
            "parent_status": parent_status,
            "parent_result_sha256": parent_hash,
            "parent_run_id": parent_run_id,
            "parent_artifact_id": parent_artifact_id,
            "authority": {
                "betelgeuse_astrometry": "Harper et al. 2017, arXiv:1706.06020",
                "astronomical_unit": "IAU 2012 Resolution B2; 149597870700 m exact",
                "solar_mass_parameter": "IAU 2015 Resolution B3 nominal (GM)_sun; 1.3271244e20 m^3 s^-2 exact nominal conversion constant",
                "downstream_focal_halfline": "Eshleman 1979 NASA NTRS 19790065362; NASA NIAC SGL NTRS 20180006788; directional geometry only",
            },
        }

        if parent_status != PARENT_PASS:
            result = {
                **base,
                "status": NOT_RUN,
                "reason": f"0096 parent status is {parent_status!r}, not required PASS",
            }
            Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
            print(json.dumps(result, indent=2, sort_keys=True))
            return

        mu_masyr = math.hypot(MU_ALPHA_MASYR, MU_DELTA_MASYR)
        mu_rad_s = mas_to_rad(mu_masyr) / JULIAN_YEAR_S
        sigma_alpha = math.sqrt(COSMIC_NOISE_MAS**2 + (MU_ALPHA_SIGMA_MASYR * HORIZON_JULIAN_YR)**2)
        sigma_delta = math.sqrt(COSMIC_NOISE_MAS**2 + (MU_DELTA_SIGMA_MASYR * HORIZON_JULIAN_YR)**2)
        eps_3sigma = 3.0 * math.hypot(sigma_alpha, sigma_delta)
        astrometry_ok = eps_3sigma <= BETA_SUPPORT_MAS
        active_status = ACTIVE_PASS if astrometry_ok else ACTIVE_FAIL

        beta_rad = mas_to_rad(BETA_SUPPORT_MAS)
        H_s = HORIZON_JULIAN_YR * JULIAN_YEAR_S
        z_controls = [float(c[1]) for c in CONTROLS]
        if len(z_controls) != 3 or any(not finite_positive(z) for z in z_controls):
            raise RuntimeError("inherited observer-distance controls invalid")

        rows = []
        passive_all_continuous = True
        for z_au in z_controls:
            r = z_au * AU_M
            d_support = r * math.tan(beta_rad)
            a_hover = GM_SUN_NOMINAL_M3_S2 / (r * r)
            dv_hover = a_hover * H_s
            v_track = r * mu_rad_s
            a_track = r * mu_rad_s * mu_rad_s
            ratio = a_track / a_hover

            v_orb = math.sqrt(GM_SUN_NOMINAL_M3_S2 / r)
            T_orb = 2.0 * math.pi * math.sqrt(r**3 / GM_SUN_NOMINAL_M3_S2)
            omega = 2.0 * math.pi / T_orb
            t_cross_linear = 2.0 * d_support / v_orb
            t_cross_exact = 2.0 * math.asin(d_support / r) / omega
            cross_rel = abs(t_cross_linear - t_cross_exact) / max(abs(t_cross_exact), 1e-300)

            # 0097a: the infinite source-Sun line has two geometric intersections
            # with a circular orbit, but only the downstream source->Sun->observer
            # half-line is a usable solar-lens window for this frozen source.
            geometric_line_intersections = 2
            usable_downstream_crossings = 1
            f_duty = usable_downstream_crossings * t_cross_exact / T_orb
            n_continuous = math.ceil(1.0 / f_duty)
            continuous = f_duty >= 1.0
            passive_all_continuous = passive_all_continuous and continuous

            vals = (r, d_support, a_hover, dv_hover, v_track, a_track, v_orb, T_orb, t_cross_exact, f_duty)
            if not finite_positive(*vals):
                raise RuntimeError("non-finite/non-positive architecture value")
            rows.append({
                "z_au": z_au,
                "r_m": r,
                "d_support_m": d_support,
                "a_hover_m_s2": a_hover,
                "delta_v_hover_10yr_m_s": dv_hover,
                "v_track_m_s": v_track,
                "a_track_m_s2": a_track,
                "a_track_over_a_hover": ratio,
                "v_orb_m_s": v_orb,
                "T_orb_s": T_orb,
                "T_orb_julian_yr": T_orb / JULIAN_YEAR_S,
                "t_cross_linear_s": t_cross_linear,
                "t_cross_exact_s": t_cross_exact,
                "linear_exact_crossing_relative_difference": cross_rel,
                "geometric_line_intersections_per_orbit": geometric_line_intersections,
                "usable_downstream_lens_crossings_per_orbit": usable_downstream_crossings,
                "passive_duty_fraction": f_duty,
                "N_continuous_ideal_equal_phase": n_continuous,
                "single_passive_continuous": continuous,
            })

        passive_status = PASSIVE_PASS if passive_all_continuous else PASSIVE_FAIL
        if active_status == ACTIVE_PASS and passive_status == PASSIVE_FAIL:
            combined = PASS_ACTIVE_PASSIVE_FAIL
        elif active_status == ACTIVE_PASS and passive_status == PASSIVE_PASS:
            combined = PASS_BOTH
        elif active_status == ACTIVE_FAIL and passive_status == PASSIVE_FAIL:
            combined = FAIL_BOTH
        else:
            # This branch is logically possible but not an allowed frozen terminal combination;
            # preserve it as authority/infrastructure blocked rather than invent a new science label.
            combined = BLOCKED

        result = {
            **base,
            "status": combined,
            "engineering_feasibility": "UNASSESSED",
            "source_astrometry": {
                "mu_alpha_cos_delta_mas_yr": MU_ALPHA_MASYR,
                "mu_alpha_sigma_mas_yr": MU_ALPHA_SIGMA_MASYR,
                "mu_delta_mas_yr": MU_DELTA_MASYR,
                "mu_delta_sigma_mas_yr": MU_DELTA_SIGMA_MASYR,
                "mu_total_mas_yr": mu_masyr,
                "mu_total_rad_s": mu_rad_s,
                "cosmic_noise_per_coordinate_mas": COSMIC_NOISE_MAS,
                "horizon_julian_yr": HORIZON_JULIAN_YR,
                "sigma_alpha_10yr_mas": sigma_alpha,
                "sigma_delta_10yr_mas": sigma_delta,
                "epsilon_3sigma_10yr_mas": eps_3sigma,
                "support_radius_mas": BETA_SUPPORT_MAS,
                "astrometry_inside_support": astrometry_ok,
            },
            "constants": {
                "AU_m_exact": AU_M,
                "GM_sun_nominal_m3_s2_exact": GM_SUN_NOMINAL_M3_S2,
                "julian_year_s": JULIAN_YEAR_S,
            },
            "architecture_A_status": active_status,
            "architecture_B_status": passive_status,
            "observer_controls": rows,
            "interpretation_guards": [
                "finite active kinematics is not spacecraft engineering feasibility",
                "passive duty cycle is geometry only, not cost or mission design",
                "only the downstream source-Sun-observer half-line is a usable lens crossing for the frozen source",
                "optical SGL focal distance is not imported into the transparent-Sun neutrino focal-distance calculation",
                "no Betelgeuse explosion date or probability is inferred",
                "0096 support is capped at the preregistered 50 mas in this gate",
                "no detector event, material response, deposited-energy, or useful-power gain is inferred",
            ],
        }
    except Exception as exc:
        result = {
            "status": INFRA,
            "reason": repr(exc),
            "prereg_commit": PREREG_COMMIT,
            "amendment_0097a_commit": AMENDMENT_COMMIT,
            "head_sha": os.getenv("GITHUB_SHA"),
        }

    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] == INFRA:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
