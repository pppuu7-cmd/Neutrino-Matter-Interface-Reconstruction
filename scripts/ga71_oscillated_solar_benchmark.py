from __future__ import annotations
import json
from pathlib import Path
from nmir.ga71_solar_fold import oscillated_ga71_snu

out = {}
for model in ("GS98", "AGSS09met"):
    out[model] = oscillated_ga71_snu(model, Path("artifacts/ga71_solar") / model)
print(json.dumps(out, indent=2, sort_keys=True))
Path("artifacts/ga71_solar").mkdir(parents=True, exist_ok=True)
Path("artifacts/ga71_solar/results.json").write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
