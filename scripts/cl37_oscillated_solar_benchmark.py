from __future__ import annotations
import json
from pathlib import Path
from nmir.cl37_solar_fold import oscillated_cl37_snu

out = {}
for model in ("GS98", "AGSS09met"):
    out[model] = {}
    for mode in ("threshold_linear", "zero_to_1"):
        out[model][mode] = oscillated_cl37_snu(
            model,
            Path("artifacts/cl37_solar") / model / mode,
            low_energy_mode=mode,
        )
print(json.dumps(out, indent=2, sort_keys=True))
Path("artifacts/cl37_solar").mkdir(parents=True, exist_ok=True)
Path("artifacts/cl37_solar/results.json").write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
