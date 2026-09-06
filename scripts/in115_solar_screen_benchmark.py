#!/usr/bin/env python3
import json
from pathlib import Path

from nmir.in115_solar_screen import in115_b16_screen

out = {}
for model in ("GS98", "AGSS09met"):
    out[model] = {
        "oscillated": in115_b16_screen(model, Path(".cache/in115") / model / "osc", oscillated=True),
        "no_oscillation_control": in115_b16_screen(model, Path(".cache/in115") / model / "noosc", oscillated=False),
    }
Path("artifacts/in115_screen").mkdir(parents=True, exist_ok=True)
Path("artifacts/in115_screen/results.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2, sort_keys=True))
