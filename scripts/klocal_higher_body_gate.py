from __future__ import annotations

import json

from nmir.klocal_higher_body import (
    classify_growing_coordination,
    contiguous_supports,
    frozen_m1_bound,
    frozen_triplet_bound,
    max_incidence,
    measured_m1,
    nested_local_commutator_amplitude,
    overlapping_triple_count,
    random_model,
)


def main() -> None:
    enumeration = []
    max_triplet_ratio = 0.0
    for periodic in (False, True):
        for n in (4, 5, 6, 8):
            for k in (1, 2, 3):
                for l in (1, 2, 3):
                    if k > n or l > n:
                        continue
                    os = contiguous_supports(n, k, periodic)
                    hs = contiguous_supports(n, l, periodic)
                    d_o = max_incidence(n, os)
                    d_h = max_incidence(n, hs)
                    exact = overlapping_triple_count(os, hs)
                    bound = frozen_triplet_bound(n, k, l, d_o, d_h)
                    ratio = exact / bound if bound else 0.0
                    max_triplet_ratio = max(max_triplet_ratio, ratio)
                    enumeration.append({
                        "n": n, "k": k, "l": l, "periodic": periodic,
                        "d_o": d_o, "d_h": d_h,
                        "triples": exact, "bound": bound, "ratio": ratio,
                        "pass": exact <= bound,
                    })

    random_rows = []
    max_local_ratio = 0.0
    max_m1_ratio = 0.0
    o0, h0 = 0.7, 0.9
    for periodic in (False, True):
        for seed in range(12):
            n, k, l = 4, 2, 2
            os, hs, ot, ht, state = random_model(n, k, l, periodic, seed, o0=o0, h0=h0)
            local_bound = 4.0 * o0 * o0 * h0
            local_max = max(
                nested_local_commutator_amplitude(z, h, x)
                for z in ot for h in ht for x in ot
            )
            d_o = max_incidence(n, os)
            d_h = max_incidence(n, hs)
            m1_bound = frozen_m1_bound(n, k, l, d_o, d_h, o0, h0)
            m1 = measured_m1(ot, ht, state)
            max_local_ratio = max(max_local_ratio, local_max / local_bound if local_bound else 0.0)
            max_m1_ratio = max(max_m1_ratio, m1 / m1_bound if m1_bound else 0.0)
            random_rows.append({
                "periodic": periodic, "seed": seed,
                "local_nested_max": local_max, "local_nested_bound": local_bound,
                "m1_abs": m1, "m1_bound": m1_bound,
                "pass": local_max <= local_bound + 1e-15 and m1 <= m1_bound + 1e-12,
            })

    scaling = []
    per_site_values = []
    k, l = 2, 3
    for n in (6, 8, 10, 12, 16, 20, 32, 64):
        os = contiguous_supports(n, k, True)
        hs = contiguous_supports(n, l, True)
        d_o = max_incidence(n, os)
        d_h = max_incidence(n, hs)
        bound = frozen_m1_bound(n, k, l, d_o, d_h, 1.0, 1.0)
        per_site = bound / n
        per_site_values.append(per_site)
        scaling.append({"n": n, "d_o": d_o, "d_h": d_h, "bound": bound, "bound_per_site": per_site})

    growing = [classify_growing_coordination(n) for n in (4, 8, 16, 32, 64)]

    passed = (
        all(r["pass"] for r in enumeration)
        and all(r["pass"] for r in random_rows)
        and max(per_site_values) - min(per_site_values) < 1e-12
        and all(r["classification"] == "OUTSIDE_SCOPE_GROWING_COORDINATION" for r in growing)
    )
    status = "PASS_KLOCAL_EXTENSIVITY" if passed else "SCIENTIFIC_FAIL"
    result = {
        "status": status,
        "scope": "bounded finite-range k-local current and Hamiltonian terms at fixed support size, norm and site incidence; arbitrary target state",
        "analytic_bound": "|m1| <= 2 N k(k+l) d_O^2 d_H o0^2 h0",
        "max_enumerated_triplet_to_bound_ratio": max_triplet_ratio,
        "max_random_local_nested_to_bound_ratio": max_local_ratio,
        "max_random_m1_to_bound_ratio": max_m1_ratio,
        "scaling_bound_per_site_values": per_site_values,
        "growing_coordination": growing,
        "enumeration_cases": len(enumeration),
        "random_matrix_cases": len(random_rows),
        "interpretation": (
            "PASS closes only the free superextensive collective-scaling loophole for bounded finite-range k-local SM current classes. "
            "Absolute higher-body coefficients, genuinely long-range/growing-coordination operators and active/driven systems remain outside scope."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if status != "PASS_KLOCAL_EXTENSIVITY":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
