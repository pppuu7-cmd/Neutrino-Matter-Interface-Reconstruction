"""Hosted exact-B16 solar-neutrino survival benchmark for NMIR."""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

from .solar_matter import (
    load_solar_matter_manifest,
    parse_solar_matter_bytes,
    raw_pinned_url,
)
from .solar_oscillation import production_averaged_day_pee

# Representative checkpoints only. Full spectral folding remains a later G3 step.
_COMPONENT_CHECKPOINTS_MEV: dict[str, tuple[float, ...]] = {
    "pp": (0.30,),
    "Be7": (0.384, 0.862),
    "pep": (1.442,),
    "B8": (5.0, 10.0),
    "N13": (0.70,),
    "O15": (1.00,),
    "F17": (1.00,),
    "hep": (10.0,),
}


def component_survival_benchmark() -> dict[str, dict[str, dict[str, float]]]:
    manifest = load_solar_matter_manifest()
    out: dict[str, dict[str, dict[str, float]]] = {}
    for model in sorted(manifest):
        with urllib.request.urlopen(raw_pinned_url(model, manifest), timeout=60) as response:
            data = response.read()
        table = parse_solar_matter_bytes(model, data, manifest, verify_blob=True)
        model_out: dict[str, dict[str, float]] = {}
        for component, energies in _COMPONENT_CHECKPOINTS_MEV.items():
            model_out[component] = {
                f"{energy:.3f}": production_averaged_day_pee(energy, table, component)
                for energy in energies
            }
        out[model] = model_out
    return out


def write_benchmark(path: str | Path) -> dict[str, dict[str, dict[str, float]]]:
    result = component_survival_benchmark()
    Path(path).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> None:
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("output", nargs="?", default="solar_survival_benchmark.json")
    args = p.parse_args()
    result = write_benchmark(args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
