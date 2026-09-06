from __future__ import annotations

import json
from pathlib import Path

from nmir.cl37_benchmark import source_average_sigma_from_spectrum
from nmir.cl37_source_average import load_cl37_source_averages
from nmir.solar_spectra import materialize_all_spectra

workdir = Path("artifacts/cl37_source_average")
paths = materialize_all_spectra(workdir / "spectra")
authority = load_cl37_source_averages()

out = {
    "B8": {
        "threshold_linear_cm2": source_average_sigma_from_spectrum(paths["B8"], low_energy_mode="threshold_linear"),
        "zero_to_1_cm2": source_average_sigma_from_spectrum(paths["B8"], low_energy_mode="zero_to_1"),
        "authority_cm2": authority["B8"],
    }
}
for mode in ("threshold_linear_cm2", "zero_to_1_cm2"):
    out["B8"][mode.replace("_cm2", "_relative_error")] = abs(out["B8"][mode] / authority["B8"] - 1.0)

workdir.mkdir(parents=True, exist_ok=True)
(workdir / "results.json").write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2, sort_keys=True))
