from __future__ import annotations

import json

from nmir.cevns_mass_optimum import benchmark_row

BENCHMARKS = [
    (0.86258, 40.0, "Be7-like / 40 eV"),
    (0.86258, 20.0, "Be7-like / 20 eV"),
    (0.86258, 10.0, "Be7-like / 10 eV"),
    (0.420, 10.0, "pp endpoint / 10 eV"),
    (1.44, 40.0, "pep / 40 eV"),
]


def main() -> None:
    rows = []
    for energy, threshold, label in BENCHMARKS:
        row = benchmark_row(energy, threshold)
        row["label"] = label
        rows.append(row)
    max_a_residual = max(abs(r["relative_a_star_residual"]) for r in rows)
    max_ratio_residual = max(abs(r["exact_tmax_over_threshold_at_numeric_optimum"] / 3.0 - 1.0) for r in rows)
    print(json.dumps({
        "status": "PASS_CEVNS_MASS_THRESHOLD_OPTIMUM" if max_a_residual < 0.01 and max_ratio_residual < 0.01 else "FAIL",
        "scope": "continuous-A fixed-Qw/A low-q CEvNS inverse-design envelope; not a real-isotope recommendation",
        "analytic_rule": "A_star = 2 E_nu^2 / (3 m_u T_thr); equivalently T_max(A_star) approximately 3 T_thr",
        "max_relative_a_star_residual": max_a_residual,
        "max_relative_tmax_over_3threshold_residual": max_ratio_residual,
        "rows": rows,
        "interpretation": "At fixed detector mass and approximately fixed weak charge per nucleon, coherence favors heavier nuclei while recoil threshold favors lighter nuclei. Their low-energy CEvNS balance has an interior optimum near T_max=3 T_thr. Full solar-spectrum real-isotope optimization is the required next gate.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
