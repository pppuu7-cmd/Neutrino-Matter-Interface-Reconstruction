from __future__ import annotations

import csv
import json
from pathlib import Path

from nmir.lee_mitigation_gap import (
    G0053_5SIGMA_DELTA30,
    classify_public_evidence,
    projected_residuals,
)

LEDGER = Path("data/cresst_lee_mitigation_evidence.csv")


def main() -> None:
    rows = list(csv.DictReader(LEDGER.open()))
    demonstrated_mechanism = any(row["classification"] == "MECHANISM_ONLY" for row in rows)
    comparable_measured = any(
        row["public_comparable_prepost"].lower() == "true" and row["measured_numeric_factor"].strip()
        for row in rows
    )
    classification = classify_public_evidence(
        demonstrated_mechanism=demonstrated_mechanism,
        comparable_measured_factor=bool(comparable_measured),
    )
    residuals = projected_residuals()

    expected = "MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN"
    passed = (
        classification == expected
        and demonstrated_mechanism
        and not comparable_measured
        and residuals[10] > 1.0e8
        and residuals[100] > 1.0e7
    )
    status = "PASS_LEE_MITIGATION_EVIDENCE_AUDIT" if passed else "FAIL_LEE_MITIGATION_EVIDENCE_AUDIT"

    print(json.dumps({
        "status": status,
        "scientific_classification": classification,
        "frozen_0053_required_improvement_5sigma_delta30": G0053_5SIGMA_DELTA30,
        "projection_only_residual_gap": {
            "10x_projection": residuals[10],
            "100x_projection": residuals[100],
        },
        "evidence": {
            "rows": len(rows),
            "demonstrated_doubletes_mechanism": demonstrated_mechanism,
            "public_comparable_measured_suppression_factor_available": bool(comparable_measured),
            "doubletes_bulk_cut_fractional_difference": 0.35,
            "measured_absorber_band_decay_time_days": 10.2,
            "measured_absorber_band_decay_time_uncertainty_days": 1.1,
        },
        "guards": [
            "DoubleTES topology discrimination is experimentally demonstrated",
            "no public comparable pre/post rejection factor is promoted from qualitative figure text",
            "10x and 100x next-generation LEE reductions are projections/benchmarks, not measured global suppression factors",
            "projection-only factors cannot close the 0053 billion-scale stress gap by themselves",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
