#!/usr/bin/env python3
"""0092b-a1 infrastructure repair r1.

The original execution assumed the integer header was physical line 4.  The
official file has an optional blank record before it.  This repair locates the
first post-text record containing exactly four integers and otherwise reuses the
frozen 0092b implementation unchanged.
"""
from __future__ import annotations

import math

import g9_ccsn_mev_composition_0092b as base


def parse_fgong_r1(path):
    lines = path.read_text(encoding="ascii").splitlines()
    if len(lines) < 7:
        raise ValueError("FGONG file too short")

    header = None
    header_index = None
    # FGONG has three descriptive text records, followed by optional whitespace,
    # then the 4i10 integer record.  Do not search into the numerical body.
    for idx in range(3, min(len(lines), 12)):
        parts = lines[idx].split()
        if len(parts) != 4:
            continue
        try:
            candidate = tuple(int(v) for v in parts)
        except ValueError:
            continue
        header = candidate
        header_index = idx
        break
    if header is None:
        raise ValueError("cannot locate FGONG 4-integer header record")
    if header != base.EXPECTED_HEADER:
        raise ValueError(f"FGONG header {header} != frozen {base.EXPECTED_HEADER}")

    nn, iconst, ivar, ivers = header
    nums = [
        float(match.group(0))
        for match in base.FLOAT_RE.finditer("\n".join(lines[header_index + 1:]))
    ]
    expected = iconst + nn * ivar
    if len(nums) != expected:
        raise ValueError(f"FGONG real count {len(nums)} != expected {expected}")

    glob = nums[:iconst]
    values = nums[iconst:]
    radius_global = glob[1]
    if not (math.isfinite(radius_global) and radius_global > 0.0):
        raise ValueError("invalid glob(2) photospheric radius")

    rows = []
    max_closure = 0.0
    for n in range(nn):
        row = values[n * ivar:(n + 1) * ivar]
        r_cm = row[0]
        x_h = row[5]
        z_met = row[16]
        y_he = 1.0 - x_h - z_met
        vals = (r_cm, x_h, y_he, z_met)
        if not all(math.isfinite(v) for v in vals):
            raise ValueError(f"non-finite FGONG composition at mesh {n}")
        if r_cm < 0.0 or x_h < 0.0 or y_he < 0.0 or z_met < 0.0:
            raise ValueError(f"unphysical FGONG composition at mesh {n}: {vals}")
        closure = abs((x_h + y_he + z_met) - 1.0)
        max_closure = max(max_closure, closure)
        if closure > 5e-10:
            raise ValueError(f"FGONG fraction closure failed at mesh {n}: {closure}")
        rows.append((r_cm / radius_global, x_h, z_met))

    rows.sort(key=lambda t: t[0])
    dedup = []
    for r, x_h, z_met in rows:
        if dedup and r == dedup[-1][0]:
            if x_h != dedup[-1][1] or z_met != dedup[-1][2]:
                raise ValueError(f"FGONG duplicate normalized radius {r} inconsistent")
            continue
        dedup.append((r, x_h, z_met))
    if not dedup or dedup[0][0] > base.B_OVER_RSUN or dedup[-1][0] < 1.0:
        raise ValueError("FGONG composition does not cover frozen chord")

    return {
        "header": header,
        "header_record_zero_based": header_index,
        "global_radius_cm": radius_global,
        "r": [v[0] for v in dedup],
        "x": [v[1] for v in dedup],
        "z": [v[2] for v in dedup],
        "sha256": base.sha256(path),
        "rows": len(dedup),
        "max_fraction_closure": max_closure,
    }


base.parse_fgong = parse_fgong_r1

if __name__ == "__main__":
    raise SystemExit(base.main())
