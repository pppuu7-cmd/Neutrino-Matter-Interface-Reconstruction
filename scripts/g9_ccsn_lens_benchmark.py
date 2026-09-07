#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import urllib.request

from nmir.g9_ccsn_lens import (
    all_flavour_totals,
    alignment_theta_upper_rad,
    finite_source_mu_bracket,
    isotropic_fluence,
    perfect_solar_aperture_mu_ceiling,
    source_angular_radius_rad,
    source_footprint_cm,
    stable_small_cap_probability,
)
from nmir.gravity_extended import focal_distance_au, parse_model_s_text

MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB_SHA = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = "https://raw.githubusercontent.com/ramses-organisation/ramses/" + MODEL_S_COMMIT + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
R_SUN_CM = 6.96e10
ROOT_B = 0.024
SOURCE_DATA = Path("data/g9_ccsn_nakazato_integ2002.data")
SOURCE_SHA256 = "3e422ceff392d2f70521b4bbda7ad8df4674a69ed1c55b693b88e46e27dfa03b"
D_KPC = 10.0
CCSN_RATE_PER_YEAR = 1.63 / 100.0
OB_SCALE_HEIGHT_PC = 76.0
ECLIPTIC_GALACTIC_INCLINATION_DEG = 60.2


def git_blob_sha1(payload: bytes) -> str:
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def thin_disk_ecliptic_density_ratio(distance_pc: float, scale_height_pc: float, inclination_deg: float, n: int = 200000) -> float:
    """Average smooth thin-disk sky density along the ecliptic / isotropic density.

    Fixed-distance control: p(Omega) proportional exp[-D |sin b_gal|/h].
    It is not a full Milky-Way population synthesis; the isotropic result is also
    retained independently and the larger duty result is used fail-closed.
    """
    k = distance_pc / scale_height_pc
    inc = math.radians(inclination_deg)
    total = 0.0
    for j in range(n):
        lam = 2.0 * math.pi * (j + 0.5) / n
        sin_b = math.sin(inc) * math.sin(lam)
        total += math.exp(-k * abs(sin_b))
    mean_exp = total / n
    return k * mean_exp / (1.0 - math.exp(-k))


def main() -> None:
    payload = SOURCE_DATA.read_bytes()
    source_sha = hashlib.sha256(payload).hexdigest()
    first = [float(x) for x in payload.decode().splitlines()[0].split()]
    if len(first) != 6:
        raise SystemExit("malformed Nakazato total row")
    n_total, e_total = all_flavour_totals(*first)
    fluence = isotropic_fluence(n_total, D_KPC)

    with urllib.request.urlopen(MODEL_S_URL, timeout=30) as response:
        model_payload = response.read()
    model_blob = git_blob_sha1(model_payload)
    profile = parse_model_s_text(model_payload.decode())
    focal = lambda b: focal_distance_au(profile, b, R_SUN_CM)
    observer_au = focal(ROOT_B)

    disk_ratio = thin_disk_ecliptic_density_ratio(10000.0, OB_SCALE_HEIGHT_PC, ECLIPTIC_GALACTIC_INCLINATION_DEG)
    receivers = []
    max_expected_ceiling = 0.0
    min_physical_mu_lower = float("inf")
    for receiver_m in (1.0, 10.0, 100.0):
        a_cm = receiver_m * 100.0
        footprint = source_footprint_cm(21.0, D_KPC, observer_au)
        z_au, mu_lower, mu_upper = finite_source_mu_bracket(ROOT_B, a_cm, footprint, R_SUN_CM, focal)
        theta = alignment_theta_upper_rad(a_cm, footprint, z_au)
        p_iso = stable_small_cap_probability(theta)
        p_disk = p_iso * disk_ratio
        p_used = max(p_iso, p_disk)
        mu_aperture = perfect_solar_aperture_mu_ceiling(a_cm, R_SUN_CM)
        expected_ceiling = 1.0 + p_used * (mu_aperture - 1.0)
        aligned_rate_per_year = CCSN_RATE_PER_YEAR * p_used
        receivers.append({
            "receiver_radius_m": receiver_m,
            "observer_au": z_au,
            "source_footprint_cm_21km": footprint,
            "finite_source_mu_lower_one_ring": mu_lower,
            "finite_source_mu_upper_one_ring": mu_upper,
            "finite_source_bracket_ratio": mu_upper / mu_lower,
            "alignment_theta_upper_rad": theta,
            "isotropic_alignment_probability": p_iso,
            "thin_disk_alignment_probability": p_disk,
            "duty_probability_used_ceiling": p_used,
            "perfect_full_solar_aperture_mu_ceiling": mu_aperture,
            "expected_multiplier_ceiling": expected_ceiling,
            "aligned_ccsn_rate_per_year_ceiling": aligned_rate_per_year,
            "mean_years_per_aligned_ccsn_ceiling": 1.0 / aligned_rate_per_year,
        })
        max_expected_ceiling = max(max_expected_ceiling, expected_ceiling)
        min_physical_mu_lower = min(min_physical_mu_lower, mu_lower)

    # Source-size sensitivity enters only the very generous duty ceiling.
    size_sensitivity = []
    for r_km in (21.0, 100.0):
        footprint = source_footprint_cm(r_km, D_KPC, observer_au)
        a_cm = 100.0
        theta = alignment_theta_upper_rad(a_cm, footprint, observer_au)
        p_iso = stable_small_cap_probability(theta)
        p_used = max(p_iso, p_iso * disk_ratio)
        mu_ap = perfect_solar_aperture_mu_ceiling(a_cm, R_SUN_CM)
        size_sensitivity.append({"source_radius_km": r_km, "source_angular_radius_rad": source_angular_radius_rad(r_km, D_KPC), "footprint_cm": footprint, "expected_multiplier_ceiling_1m_receiver": 1.0 + p_used * (mu_ap - 1.0)})

    passed = (
        source_sha == SOURCE_SHA256
        and model_blob == MODEL_S_BLOB_SHA
        and abs(fluence / 8.900146153964761e11 - 1.0) < 1e-10
        and 22.0 < observer_au < 26.0
        and min_physical_mu_lower > 1.0
        and all(row["finite_source_bracket_ratio"] < 1.01 for row in receivers)
        and max_expected_ceiling < 2.0
        and max(row["expected_multiplier_ceiling_1m_receiver"] for row in size_sensitivity) < 2.0
    )
    result = {
        "status": "PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY" if passed else "SCIENTIFIC_FAIL_MODEL",
        "source_payload_sha256": source_sha,
        "model_s_git_blob_sha1": model_blob,
        "nakazato_all_flavour_total_number": n_total,
        "nakazato_all_flavour_total_energy_erg": e_total,
        "unlensed_all_flavour_fluence_10kpc_cm_minus2": fluence,
        "burst_horizon_s": 20.0,
        "fiducial_source_radius_km": 21.0,
        "observer_ring_b_over_Rsun": ROOT_B,
        "observer_distance_au": observer_au,
        "thin_disk_ecliptic_density_ratio_to_isotropic": disk_ratio,
        "ccsn_rate_per_year": CCSN_RATE_PER_YEAR,
        "receivers": receivers,
        "source_size_sensitivity": size_sensitivity,
        "utility_logic": "physical one-ring finite-source receiver magnification is bounded directly; occurrence utility is fail-closed with an impossible full-solar-disk perfect-collection aperture ceiling and the larger of isotropic or smooth thin-disk alignment probabilities",
        "scope": "interaction/event fluence multiplier only; no detector, metastable, resonance, geometry-stack or neutrino-energy gain multiplication",
    }
    Path("g9_ccsn_lens_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
