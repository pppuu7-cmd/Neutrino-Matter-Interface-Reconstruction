#!/usr/bin/env python3
"""Contract-conformance runner for NMIR 0089d.

The initial benchmark implementation contained one extra, non-preregistered
zero-tolerance comparison between the total kernel K and a separately computed
one-ring diagnostic. The frozen 0089d V3 contract requires only (a) structural
containment of the inherited one-ring interval and (b) reproduction of its
accepted-area value within 0.5%. This runner removes only that extra assertion;
all frozen 0089d criteria and tolerances are unchanged.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

from nmir.g9_ccsn_lens import annular_point_source_receiver_mu


def load_benchmark():
    path = Path(__file__).with_name("g9_continuous_map_monotone_kernel_0089d.py")
    spec = importlib.util.spec_from_file_location("g9_0089d_benchmark", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load 0089d benchmark")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    mod = load_benchmark()

    def frozen_one_ring_checks(profile, rows, x0: float, z: float):
        focal = lambda x: mod.continuous_focal_distance_au(profile, x, mod.R)
        out = []
        by_r = {row["radius_cm"]: row for row in rows}
        for r in (100.0, 1000.0, 10000.0):
            row = by_r[r]
            containing = [
                iv for iv in row["accepted_intervals"]
                if iv["lo"] <= x0 <= iv["hi"]
            ]
            if len(containing) != 1:
                raise mod.KernelScientificFail(
                    "global interval set lacks unique inherited one-ring interval"
                )
            iv = containing[0]
            local_mu = mod.R**2 * (iv["hi"]**2 - iv["lo"]**2) / r**2
            exact_mu = annular_point_source_receiver_mu(x0, r, mod.R, focal)[3]
            re = abs(local_mu - exact_mu) / max(
                abs(local_mu), abs(exact_mu), 1e-300
            )
            if re > mod.REL_TOL:
                raise mod.KernelScientificFail(
                    "inherited one-ring reproduction exceeds 0.5%"
                )
            out.append({
                "radius_cm": r,
                "exact_one_ring_mu": exact_mu,
                "containing_interval_mu": local_mu,
                "relative_error": re,
            })
        return out

    mod.one_ring_checks = frozen_one_ring_checks
    mod.main()


if __name__ == "__main__":
    main()
