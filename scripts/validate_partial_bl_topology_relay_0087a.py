#!/usr/bin/env python3
"""NMIR 0087a — falsification-oriented validation of the 0087 B-L topology candidate."""
from __future__ import annotations

import json
import math
import pathlib
from itertools import combinations

from shapely.geometry import GeometryCollection, MultiPolygon, Polygon, box
from shapely.ops import unary_union

import audit_partial_bl_topology_discovery_0087 as parent

MIN_AREA = 0.01
AREA_TOL = 1e-10
Y_CEILINGS = (-2.0, -3.0, -4.0, -5.0)
XMIN, XMAX, YMIN = -6.0, 10.0, -25.0


def iter_polygons(g):
    if isinstance(g, Polygon): return [g]
    if isinstance(g, MultiPolygon): return list(g.geoms)
    if isinstance(g, GeometryCollection): return [x for x in g.geoms if isinstance(x, Polygon) and x.area > 0]
    return []


def clip_family(g, win):
    h = g.intersection(win)
    if h.is_empty or h.area <= 0:
        return GeometryCollection()
    if not h.is_valid:
        raise ValueError("invalid clipped family geometry; topology repair forbidden")
    return h


def qualifying_components(permitted):
    return [p for p in iter_polygons(permitted) if p.area >= MIN_AREA]


def analyze_window(families: dict, ymax: float):
    win = box(XMIN, YMIN, XMAX, ymax)
    clipped = {k: clip_family(v, win) for k, v in families.items()}
    active = [g for g in clipped.values() if not g.is_empty and g.area > 0]
    excluded = unary_union(active) if active else GeometryCollection()
    if not excluded.is_empty and not excluded.is_valid:
        raise ValueError("invalid excluded union")
    permitted = win.difference(excluded)
    if not permitted.is_valid:
        raise ValueError("invalid permitted complement")
    qual = qualifying_components(permitted)
    closure = abs((excluded.area + permitted.area) - win.area) / win.area
    overlaps = {}
    for a, b in combinations(sorted(clipped), 2):
        ga, gb = clipped[a], clipped[b]
        area = 0.0 if ga.is_empty or gb.is_empty else ga.intersection(gb).area
        if not math.isfinite(area) or area < -1e-15:
            raise ValueError("nonfinite/negative overlap")
        overlaps[f"{a}__{b}"] = max(0.0, area)
    return {
        "y_max": ymax,
        "window_area_decade2": win.area,
        "active_family_areas_decade2": {k: v.area for k, v in clipped.items()},
        "excluded_area_decade2": excluded.area,
        "permitted_area_decade2": permitted.area,
        "permitted_component_count": len(iter_polygons(permitted)),
        "qualifying_component_count_ge_0p01": len(qual),
        "qualifying_component_areas_decade2": sorted([p.area for p in qual], reverse=True),
        "N1": len(qual) >= 2,
        "area_closure_relative_error": closure,
        "area_closure_pass": closure <= AREA_TOL,
        "pairwise_overlap_areas_decade2": overlaps,
        "clipped_families": clipped,
    }


def graph_from_overlaps(nodes, overlaps):
    adj = {n: set() for n in nodes}
    edges = []
    for a, b in combinations(sorted(nodes), 2):
        area = overlaps.get(f"{a}__{b}", overlaps.get(f"{b}__{a}", 0.0))
        if area >= MIN_AREA:
            adj[a].add(b); adj[b].add(a)
            edges.append({"a": a, "b": b, "overlap_area_decade2": area})
    return adj, edges


def reachable(adj, start, removed=None):
    removed = set() if removed is None else set(removed)
    if start in removed: return set()
    seen = {start}; stack = [start]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in removed and v not in seen:
                seen.add(v); stack.append(v)
    return seen


def relay_test(nodes, overlaps, sn_name, cmb_name):
    w = "WAGNER_0085"; s = "SOLAR_CEVNS_0078c"
    adj, edges = graph_from_overlaps(nodes, overlaps)
    full_reach = reachable(adj, w)
    full_connected = len(full_reach) == len(nodes)
    w_sn_edge = sn_name in adj[w]
    path_cmb_before = cmb_name in full_reach
    path_solar_before = s in full_reach
    after = reachable(adj, w, removed={sn_name})
    separated_after = cmb_name not in after and s not in after
    passed = full_connected and w_sn_edge and path_cmb_before and path_solar_before and separated_after
    return {
        "nodes": sorted(nodes),
        "edges": edges,
        "full_connected": full_connected,
        "wagner_sn_edge": w_sn_edge,
        "wagner_path_to_cmb_before_sn_removal": path_cmb_before,
        "wagner_path_to_solar_before_sn_removal": path_solar_before,
        "reachable_from_wagner_after_sn_removal": sorted(after),
        "sn_removal_separates_wagner_from_cmb_and_solar": separated_after,
        "pass": passed,
    }


def leave_one_out(families: dict):
    out = {}
    for drop in sorted(families):
        keep = {k: v for k, v in families.items() if k != drop}
        r = analyze_window(keep, -2.0)
        out[drop] = {
            "qualifying_component_count_ge_0p01": r["qualifying_component_count_ge_0p01"],
            "permitted_component_count": r["permitted_component_count"],
            "N1": r["N1"],
            "excluded_area_decade2": r["excluded_area_decade2"],
            "permitted_area_decade2": r["permitted_area_decade2"],
            "area_closure_pass": r["area_closure_pass"],
        }
    return out


def build_authoritative_families():
    solar, solar_meta = parent.load_solar()
    cmb_geoms, cmb_meta = parent.load_cmb()
    sn_geoms, sn_meta = parent.load_sn()
    wagner, wagner_meta = parent.load_wagner()
    meta = {
        "solar_0078c": solar_meta,
        "cmb_0080d": cmb_meta,
        "sn1987a_0084b": sn_meta,
        "wagner_0085_r1": wagner_meta,
    }
    return solar, cmb_geoms, sn_geoms, wagner, meta


def audit():
    solar, cmb_geoms, sn_geoms, wagner, input_meta = build_authoritative_families()
    combos = [
        ("Majorana", "BODY_NATIVE"),
        ("Majorana", "CONCLUSION_SUMMARY"),
        ("Dirac", "BODY_NATIVE"),
        ("Dirac", "CONCLUSION_SUMMARY"),
    ]
    scenarios = {}
    all_window_stable = True
    all_relay_stable = True
    all_integrity = True
    for csc, sv in combos:
        cname = f"CMB_{csc.upper()}_0080d"
        snname = f"SN1987A_{sv}_0084b"
        sname = f"CMB_{csc.upper()}__SN_{sv}"
        families = {
            "SOLAR_CEVNS_0078c": solar,
            cname: cmb_geoms[csc],
            snname: sn_geoms[sv],
            "WAGNER_0085": wagner,
        }
        stress = {}
        n1s = []
        relays = []
        for ymax in Y_CEILINGS:
            r = analyze_window(families, ymax)
            relay = relay_test(set(families), r["pairwise_overlap_areas_decade2"], snname, cname)
            stress[str(ymax)] = {
                k: v for k, v in r.items() if k != "clipped_families"
            }
            stress[str(ymax)]["relay"] = relay
            n1s.append(r["N1"])
            relays.append(relay["pass"])
            all_integrity &= r["area_closure_pass"]
        window_stable = all(n1s)
        relay_stable = all(relays)
        all_window_stable &= window_stable
        all_relay_stable &= relay_stable
        lofo = leave_one_out(families)
        all_integrity &= all(x["area_closure_pass"] for x in lofo.values())
        scenarios[sname] = {
            "window_stable_N1": window_stable,
            "relay_stable": relay_stable,
            "stress_windows": stress,
            "leave_one_family_out_ymax_minus2": lofo,
        }

    if not all_integrity:
        cls = "SCIENTIFIC_FAIL_0087A_GEOMETRY_INTEGRITY"
    elif all_window_stable and all_relay_stable:
        cls = "PASS_PARTIAL_B_L_TOPOLOGY_AND_RELAY_ROBUST"
    elif all_relay_stable:
        cls = "PASS_B_L_CONSTRAINT_RELAY_ONLY_TOPOLOGY_EDGE_SENSITIVE"
    elif all_window_stable:
        cls = "PASS_PARTIAL_B_L_TOPOLOGY_STABLE_RELAY_NOT_VALIDATED"
    else:
        cls = "PASS_0087A_NO_ROBUST_STRUCTURE"

    return {
        "iteration": "0087a",
        "classification": cls,
        "frozen_y_ceilings": list(Y_CEILINGS),
        "minimum_component_or_overlap_area_decade2": MIN_AREA,
        "input_authority": input_meta,
        "all_four_scenarios_window_stable_N1": all_window_stable,
        "all_four_scenarios_relay_stable": all_relay_stable,
        "all_area_closure_checks_pass": all_integrity,
        "scenarios": scenarios,
        "guard": "Post-discovery validation only; inward clipping, no outward extrapolation; relay is a cross-family structural synthesis, not a complete B-L allowed region or new-particle claim; blocked families remain omitted; BSM response locked.",
    }


def main():
    out = pathlib.Path("partial_bl_topology_relay_validation_0087a.json")
    try:
        result = audit()
    except (OSError, RuntimeError) as exc:
        result = {"iteration":"0087a","classification":"BLOCKED_0087A_INPUT_AUTHORITY","reason":repr(exc)}
    except ValueError as exc:
        result = {"iteration":"0087a","classification":"SCIENTIFIC_FAIL_0087A_GEOMETRY_INTEGRITY","reason":repr(exc)}
    out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["classification"].startswith("BLOCKED") or result["classification"].startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(2)

if __name__ == "__main__":
    main()
