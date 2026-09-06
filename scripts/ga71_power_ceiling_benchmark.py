#!/usr/bin/env python3
import json
from pathlib import Path

from nmir.ga71_power_ceiling import oscillated_ga71_neutrino_energy_ceiling

out = {}
for model in ("GS98", "AGSS09met"):
    out[model] = oscillated_ga71_neutrino_energy_ceiling(model, Path(".cache/ga71-power") / model)
Path("results").mkdir(exist_ok=True)
Path("results/ga71_neutrino_energy_ceiling.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2, sort_keys=True))
