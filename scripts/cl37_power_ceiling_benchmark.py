from __future__ import annotations

import json
from pathlib import Path

from nmir.cl37_power_ceiling import cl37_power_envelope


def main() -> None:
    out = {}
    for model in ("GS98", "AGSS09met"):
        out[model] = cl37_power_envelope(model, Path(".cache/cl37-power") / model)
    Path("results").mkdir(exist_ok=True)
    path = Path("results/cl37_neutrino_energy_ceiling.json")
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
