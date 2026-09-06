#!/usr/bin/env python3
import json
from pathlib import Path

from nmir.se82_solar_fold import se82_b16_fold

out = {}
for model in ("GS98", "AGSS09met"):
    out[model] = {
        "oscillated": se82_b16_fold(model, Path(".cache/se82_fold") / model / "osc", oscillated=True),
        "no_oscillation_control": se82_b16_fold(model, Path(".cache/se82_fold") / model / "noosc", oscillated=False),
    }
Path("artifacts/se82_solar_fold").mkdir(parents=True, exist_ok=True)
Path("artifacts/se82_solar_fold/results.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(out, indent=2, sort_keys=True))
