#!/usr/bin/env python3
"""NMIR 0087 — authoritative partial B-L topology discovery.

Prospectively frozen by research/prereg/0087_authoritative_partial_b_minus_l_topology_discovery.md.
Only already-authoritative numerical B-L families are composed. Missing/blocked
families are never approximated.
"""
from __future__ import annotations

import hashlib
import io
import json
import math
import pathlib
import tarfile
from itertools import combinations

from shapely import wkt
from shapely.geometry import GeometryCollection, MultiPolygon, Polygon, box
from shapely.ops import unary_union

import extract_esseili_kribs_cmb_excluded_0080d as cmb
import audit_shin_yun_sn1987a_analytical_geometry_0084b as sn
import audit_wagner_identity_free_envelope_0085_r1 as wagner

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOLAR_PATH = ROOT / "data" / "deromeri_bl_excluded_region_0078c.json"
CMB_SUMMARY_PATH = ROOT / "data" / "esseili_kribs_cmb_excluded_0080d.json"
WINDOW = box(-6.0, -25.0, 10.0, -2.0)
WINDOW_AREA = WINDOW.area
MIN_COMPONENT_AREA = 0.01
BOUNDARY_TOL = 1e-9
AREA_CLOSURE_REL_TOL = 1e-10

EXPECTED_SOLAR_AREA = 12.51987545543835
EXPECTED_CMB_AREAS = {
    "Majorana": 48.332188584322665,
    "Dirac": 45.129364149717375,
}

BLOCKED_OR_OMITTED = {
    "NA64_0086c": "BLOCKED_NA64_B_L_VECTOR_AXIS_CALIBRATION",
    "BBN_0081a": "BLOCKED_COSMOLOGY_B_L_BBN_VECTOR_CALIBRATION_SEMANTIC_IDENTITY",
    "CERDENO_0082c": "BLOCKED_CERDENO_B_L_AXIS_CALIBRATION",
    "COHERENT_0074c": "BLOCKED_COMBINED_CEVNS_B_L_PRIMARY_BENCHMARK_AUTHORITY",
    "HONG_CAS_A": "NO_EXACT_FINITE_ENDPOINT_GEOMETRY",
    "FAYET_0079a_FINITE": "FINITE_MASS_CONTINUATION_FORBIDDEN",
}


def sha256_file(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def iter_polygons(g):
    if isinstance(g, Polygon):
        return [g]
    if isinstance(g, MultiPolygon):
        return list(g.geoms)
    if isinstance(g, GeometryCollection):
        return [x for x in g.geoms if isinstance(x, Polygon) and x.area > 0]
    return []


def require_valid_nonempty(name: str, g):
    if g.is_empty or g.area <= 0:
        raise ValueError(f"{name}: empty/nonpositive geometry")
    if not g.is_valid:
        raise ValueError(f"{name}: invalid geometry; topology repair forbidden")


def polygon_from_component(comp: dict, x_shift: float = 0.0) -> Polygon:
    ext = [(float(x) + x_shift, float(y)) for x, y in comp["exterior"]]
    holes = [[(float(x) + x_shift, float(y)) for x, y in ring] for ring in comp.get("holes", [])]
    p = Polygon(ext, holes)
    require_valid_nonempty("component", p)
    return p


def load_solar():
    obj = json.loads(SOLAR_PATH.read_text(encoding="utf-8"))
    if obj.get("status") != "PASS_SOLAR_CEVNS_B_L_EXCLUDED_REGION":
        raise RuntimeError(f"0078c authority mismatch: {obj.get('status')}")
    comps = obj["excluded_region"]["polygon_components"]
    native = unary_union([polygon_from_component(c, 0.0) for c in comps])
    if abs(native.area - EXPECTED_SOLAR_AREA) / EXPECTED_SOLAR_AREA > 1e-12:
        raise RuntimeError(f"0078c area mismatch {native.area}")
    # 0078c x = log10(m/GeV); 0087 x = log10(m/eV) = x_GeV + 9.
    shifted = unary_union([polygon_from_component(c, 9.0) for c in comps]).intersection(WINDOW)
    require_valid_nonempty("solar_0078c", shifted)
    return shifted, {
        "status": obj["status"],
        "data_sha256": sha256_file(SOLAR_PATH),
        "native_area_decade2": native.area,
        "window_clipped_area_decade2": shifted.area,
        "component_count": len(iter_polygons(shifted)),
        "x_conversion": "log10(m/eV)=log10(m/GeV)+9",
    }


def load_cmb():
    raw = cmb.fetch_source()
    h = cmb.sha256(raw)
    if h != cmb.SOURCE_SHA256:
        raise RuntimeError(f"0080d source SHA mismatch {h}")
    blobs = {}
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
        members = {m.name.lstrip("./"): m for m in tf.getmembers() if m.isfile()}
        for scenario, (path, expected_sha) in cmb.ASSETS.items():
            if path not in members:
                raise RuntimeError(f"0080d missing asset {path}")
            data = tf.extractfile(members[path]).read()
            if cmb.sha256(data) != expected_sha:
                raise RuntimeError(f"0080d asset SHA mismatch {path}")
            blobs[scenario] = data

    summary = json.loads(CMB_SUMMARY_PATH.read_text(encoding="utf-8"))
    if summary.get("classification") != "PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_EXCLUDED_GEOMETRY":
        raise RuntimeError("0080d persisted summary authority mismatch")

    geoms = {}
    meta = {}
    for scenario, data in blobs.items():
        r = cmb.inspect_scenario(data, scenario, 0.01)
        if r.get("classification", "").startswith("BLOCKED") or not r.get("valid"):
            raise RuntimeError(f"0080d {scenario} reconstruction blocked/invalid")
        expected = EXPECTED_CMB_AREAS[scenario]
        if abs(r["area_decade2"] - expected) / expected > 1e-12:
            raise RuntimeError(f"0080d {scenario} area mismatch {r['area_decade2']}")
        native = wkt.loads(r["geometry_wkt"])
        require_valid_nonempty(f"cmb_{scenario}", native)
        # 0080d physical x is log10(m/GeV); translate to log10(m/eV).
        from shapely.affinity import translate
        shifted = translate(native, xoff=9.0, yoff=0.0).intersection(WINDOW)
        require_valid_nonempty(f"cmb_{scenario}_window", shifted)
        geoms[scenario] = shifted
        meta[scenario] = {
            "source_sha256": h,
            "asset_sha256": cmb.ASSETS[scenario][1],
            "native_area_decade2": native.area,
            "window_clipped_area_decade2": shifted.area,
            "component_count": len(iter_polygons(shifted)),
            "selected_drawing_ids": [x["drawing_id"] for x in r.get("selected", [])],
            "x_conversion": "log10(m/eV)=log10(m/GeV)+9",
        }
    return geoms, meta


def load_sn():
    obj = sn.audit()
    if obj.get("classification") != "PASS_SHIN_YUN_SN1987A_ANALYTICAL_GEOMETRY_AUTHORITY":
        raise RuntimeError(f"0084b authority mismatch: {obj.get('classification')}")
    by_variant = {}
    meta = {}
    for variant in ("BODY_NATIVE", "CONCLUSION_SUMMARY"):
        regs = [r for r in obj["regions"] if r["variant"] == variant]
        if {r["polarization"] for r in regs} != {"T", "L"}:
            raise RuntimeError(f"0084b {variant}: missing T/L")
        polys = []
        regmeta = []
        for r in regs:
            p = Polygon([(float(x), float(y)) for x, y in r["polygon_log10_m_eV_log10_g"]])
            require_valid_nonempty(f"sn_{variant}_{r['polarization']}", p)
            if not r.get("agreement_within_1e-8"):
                raise RuntimeError(f"0084b {variant}/{r['polarization']} audit mismatch")
            polys.append(p)
            regmeta.append({
                "polarization": r["polarization"],
                "area_decade2": p.area,
                "mass_interval_eV": r["mass_interval_eV"],
            })
        g = unary_union(polys).intersection(WINDOW)
        require_valid_nonempty(f"sn_{variant}_union", g)
        by_variant[variant] = g
        meta[variant] = {
            "archive_sha256": obj["archive_sha256"],
            "T_L_regions": regmeta,
            "union_area_decade2": g.area,
            "component_count": len(iter_polygons(g)),
        }
    return by_variant, meta


def _interp_y(points, x):
    if x < points[0][0] - 1e-13 or x > points[-1][0] + 1e-13:
        return None
    for (xa, ya), (xb, yb) in zip(points[:-1], points[1:]):
        if xa - 1e-13 <= x <= xb + 1e-13:
            if abs(xb - xa) <= 1e-15:
                return min(ya, yb)
            t = (x - xa) / (xb - xa)
            return ya + t * (yb - ya)
    if abs(x - points[-1][0]) <= 1e-13:
        return points[-1][1]
    return None


def load_wagner():
    obj = wagner.audit()
    if obj.get("classification") != "PASS_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE":
        raise RuntimeError(f"0085-r1 authority mismatch: {obj.get('classification')}")
    counts = obj.get("active_component_sample_counts", {})
    active = [k for k, v in counts.items() if v > 0]
    if len(active) != 1:
        raise RuntimeError(f"0085 accepted envelope has non-unique active component set: {active}")
    active_id = active[0]
    comp = next(c for c in obj["components"] if c["anonymous_id"] == active_id)
    pts = sorted([(float(p["x"]), float(p["y"])) for p in comp["points"]], key=lambda q: q[0])
    xmin = max(-6.0, float(obj["support_runs"][0]["x_min"]))
    xmax = min(10.0, float(obj["support_runs"][0]["x_max"]))
    if xmax <= xmin:
        raise RuntimeError("0085 support empty after 0087 clip")
    y0 = _interp_y(pts, xmin)
    y1 = _interp_y(pts, xmax)
    if y0 is None or y1 is None:
        raise RuntimeError("0085 active component cannot reproduce support endpoints")
    chain = [(xmin, y0)] + [(x, y) for x, y in pts if xmin < x < xmax] + [(xmax, y1)]
    # Remove exact duplicate consecutive x/y vertices only.
    clean = []
    for q in chain:
        if not clean or abs(q[0]-clean[-1][0]) > 1e-14 or abs(q[1]-clean[-1][1]) > 1e-14:
            clean.append(q)
    # y > envelope is excluded, closed upward only within source x support.
    poly = Polygon(clean + [(xmax, -2.0), (xmin, -2.0)])
    require_valid_nonempty("wagner_0085", poly)
    clipped = poly.intersection(WINDOW)
    require_valid_nonempty("wagner_0085_window", clipped)
    return clipped, {
        "classification": obj["classification"],
        "eps_sha256": obj["eps_sha256"],
        "active_component": active_id,
        "support_x_log10_eV": [xmin, xmax],
        "source_vertex_count_after_clip": len(clean),
        "window_clipped_area_decade2": clipped.area,
        "semantics": obj["envelope_semantics"],
    }


def pairwise_overlap_areas(families: dict):
    return {
        f"{a}__{b}": families[a].intersection(families[b]).area
        for a, b in combinations(sorted(families), 2)
    }


def boundary_sources(component: Polygon, families: dict):
    labels = []
    details = {}
    for name, g in families.items():
        length = component.boundary.intersection(g.boundary).length
        details[name] = length
        if length > 1e-8:
            labels.append(name)
    return labels, details


def analyze_scenario(name: str, families: dict):
    for fname, g in families.items():
        require_valid_nonempty(fname, g)
    excluded = unary_union(list(families.values()))
    if not excluded.is_valid:
        raise ValueError(f"{name}: excluded union invalid")
    excluded = excluded.intersection(WINDOW)
    permitted = WINDOW.difference(excluded)
    if not permitted.is_valid:
        raise ValueError(f"{name}: permitted complement invalid")

    comps = sorted(iter_polygons(permitted), key=lambda p: (-p.area, p.bounds))
    comp_rows = []
    qualifying = []
    bounded_multi = []
    for i, p in enumerate(comps):
        touch_len = p.boundary.intersection(WINDOW.boundary).length
        touches_window = touch_len > BOUNDARY_TOL
        labels, lengths = boundary_sources(p, families)
        row = {
            "component": i,
            "area_decade2": p.area,
            "bounds": list(p.bounds),
            "touches_analysis_window": touches_window,
            "analysis_window_boundary_contact_length": touch_len,
            "source_boundary_labels": labels,
            "source_boundary_contact_lengths": lengths,
        }
        comp_rows.append(row)
        if p.area >= MIN_COMPONENT_AREA:
            qualifying.append(row)
            if not touches_window and len(labels) >= 2:
                bounded_multi.append(row)

    n1 = len(qualifying) >= 2
    n2 = bool(bounded_multi)
    # Under frozen semantics Wagner is the only included family that is globally
    # an upper-limit type object. Filled CMB/CEvNS and SN bands are not silently
    # reinterpreted as upper curves, so a cross-family N3 switch is impossible.
    n3 = False
    n3_detail = {
        "eligible_upper_limit_families": ["WAGNER_0085"],
        "base_samples_per_decade": 2001,
        "refined_samples_per_decade": 4001,
        "switch_count": 0,
        "reason": "only one included family has source-authorized upper-limit semantics; filled polygons/SN bands are not reinterpreted",
        "pass": False,
    }

    closure_rel = abs((excluded.area + permitted.area) - WINDOW_AREA) / WINDOW_AREA
    return {
        "scenario": name,
        "family_areas_decade2": {k: v.area for k, v in families.items()},
        "pairwise_overlap_areas_decade2": pairwise_overlap_areas(families),
        "excluded_union_area_decade2": excluded.area,
        "permitted_complement_area_decade2": permitted.area,
        "analysis_window_area_decade2": WINDOW_AREA,
        "area_closure_relative_error": closure_rel,
        "area_closure_pass": closure_rel <= AREA_CLOSURE_REL_TOL,
        "permitted_component_count": len(comps),
        "qualifying_component_count_ge_0p01": len(qualifying),
        "permitted_components": comp_rows,
        "N1_disconnected_permitted_topology": n1,
        "N2_bounded_multifamily_pocket_or_corridor": n2,
        "N2_components": bounded_multi,
        "N3_persistent_controlling_family_switch": n3,
        "N3_detail": n3_detail,
        "partial_topology_candidate": bool(n1 or n2 or n3),
    }


def audit():
    solar, solar_meta = load_solar()
    cmb_geoms, cmb_meta = load_cmb()
    sn_geoms, sn_meta = load_sn()
    wagner_geom, wagner_meta = load_wagner()

    scenarios = {}
    combos = [
        ("Majorana", "BODY_NATIVE"),
        ("Majorana", "CONCLUSION_SUMMARY"),
        ("Dirac", "BODY_NATIVE"),
        ("Dirac", "CONCLUSION_SUMMARY"),
    ]
    for csc, sv in combos:
        name = f"CMB_{csc.upper()}__SN_{sv}"
        families = {
            "SOLAR_CEVNS_0078c": solar,
            f"CMB_{csc.upper()}_0080d": cmb_geoms[csc],
            f"SN1987A_{sv}_0084b": sn_geoms[sv],
            "WAGNER_0085": wagner_geom,
        }
        scenarios[name] = analyze_scenario(name, families)

    closure_ok = all(s["area_closure_pass"] for s in scenarios.values())
    any_candidate = any(s["partial_topology_candidate"] for s in scenarios.values())
    if not closure_ok:
        classification = "SCIENTIFIC_FAIL_PARTIAL_B_L_TOPOLOGY_INTEGRITY"
    elif any_candidate:
        classification = "PASS_PARTIAL_B_L_TOPOLOGY_CANDIDATE"
    else:
        classification = "PASS_PARTIAL_B_L_NO_NONTRIVIAL_TOPOLOGY"

    return {
        "iteration": "0087",
        "classification": classification,
        "analysis_coordinates": {"x": "log10(m_V/eV)", "y": "log10(g_BL)"},
        "analysis_window": {"x": [-6.0, 10.0], "y": [-25.0, -2.0], "area_decade2": WINDOW_AREA,
                            "lower_y_is_analysis_boundary_not_physical_limit": True},
        "input_authority": {
            "solar_0078c": solar_meta,
            "cmb_0080d": cmb_meta,
            "sn1987a_0084b": sn_meta,
            "wagner_0085_r1": wagner_meta,
        },
        "blocked_or_omitted_families": BLOCKED_OR_OMITTED,
        "scenarios": scenarios,
        "candidate_scenarios": [k for k, v in scenarios.items() if v["partial_topology_candidate"]],
        "guard": "Authoritative partial topology only. Not a complete/global B-L allowed region; NA64/BBN/Cerdeno/COHERENT/finite fifth-force are not approximated; Majorana/Dirac and BODY_NATIVE/CONCLUSION_SUMMARY remain separate; no BSM response scan.",
    }


def main():
    out = pathlib.Path("partial_bl_topology_discovery_0087.json")
    try:
        result = audit()
    except (OSError, RuntimeError) as exc:
        result = {
            "iteration": "0087",
            "classification": "INFRASTRUCTURE_OR_AUTHORITY_REPRODUCTION_FAIL",
            "reason": repr(exc),
            "blocked_or_omitted_families": BLOCKED_OR_OMITTED,
        }
    except ValueError as exc:
        result = {
            "iteration": "0087",
            "classification": "SCIENTIFIC_FAIL_PARTIAL_B_L_TOPOLOGY_INTEGRITY",
            "reason": repr(exc),
            "blocked_or_omitted_families": BLOCKED_OR_OMITTED,
        }
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["classification"].startswith("INFRASTRUCTURE") or result["classification"].startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
