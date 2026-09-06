"""Hosted prospective validation of frozen 71Ga response against Bahcall source averages."""

from __future__ import annotations

import json
from pathlib import Path

from nmir.ga71_response import ga71_sigma_cm2, normalized_spectral_average_sigma_cm2, parse_two_column_spectrum
from nmir.solar_spectra import materialize_all_spectra


PUBLISHED_1E46 = {
    "pp": 11.72,
    "pep": 204.0,
    "Be7": 71.7,
    "N13": 60.4,
    "O15": 113.7,
    "F17": 113.9,
}

# Frozen before inspecting benchmark output. B8/hep are intentionally excluded:
# NMIR pins Ortiz-2000 B8 and a later materialized hep shape, whereas Bahcall's
# 1997 source-average values were evaluated with his then-current spectra.
REL_TOL = {
    "pp": 0.015,
    "pep": 0.04,
    "Be7": 0.005,
    "N13": 0.025,
    "O15": 0.025,
    "F17": 0.025,
}


def average_file(path: Path) -> float:
    e, f = parse_two_column_spectrum(path.read_text(encoding="utf-8"))
    return normalized_spectral_average_sigma_cm2(e, f) / 1e-46


def main() -> None:
    out_dir = Path("artifacts/ga71_benchmark/spectra")
    paths = materialize_all_spectra(out_dir)
    computed = {
        "pp": average_file(paths["pp"]),
        "N13": average_file(paths["N13"]),
        "O15": average_file(paths["O15"]),
        "F17": average_file(paths["F17"]),
        "pep": ga71_sigma_cm2(1.442) / 1e-46,
        "Be7": (0.897 * ga71_sigma_cm2(0.862) + 0.103 * ga71_sigma_cm2(0.384)) / 1e-46,
    }
    result = {}
    failed = []
    for name, value in computed.items():
        target = PUBLISHED_1E46[name]
        rel = abs(value / target - 1.0)
        ok = rel <= REL_TOL[name]
        result[name] = {"computed_1e46_cm2": value, "published_1e46_cm2": target, "relative_error": rel, "tolerance": REL_TOL[name], "pass": ok}
        if not ok:
            failed.append(name)
    payload = {"reference": "J.N. Bahcall, Phys. Rev. C 56, 3391 (1997), Table VI / numerical response tables", "results": result, "all_pass": not failed}
    target = Path("artifacts/ga71_benchmark/result.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    if failed:
        raise SystemExit("prospective Ga-71 source-average gate failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
