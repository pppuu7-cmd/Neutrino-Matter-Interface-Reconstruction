#!/usr/bin/env python3
from __future__ import annotations

import colorsys
import hashlib
import io
import json
import math
import tarfile
import tempfile
import urllib.request
from pathlib import Path

import fitz
from shapely.geometry import Polygon, box, Point
from shapely.ops import unary_union

ARXIV_ID = "2603.00554"
SOURCE_URLS = (f"https://export.arxiv.org/e-print/{ARXIV_ID}", f"https://arxiv.org/e-print/{ARXIV_ID}")
SOURCE_SHA256 = "09ab22f753ac3f5fbde5be65ac50926de67b0638550366d158aadcfde8e92564"
ASSET = "vector_BL_PnX_XnT_LZ_combined.pdf"
ASSET_SHA256 = "ace761499623535907263e780a6e96a17474adf418d3f9363dae8e28bc5e7a39"
AX, BX = 0.013440860603931617, -6.171186200127133
AY, BY = -0.01803751809647103, -1.3913180812870007
DOMAIN = (-5.0, -8.0, 1.0, -2.0)
CONNECT_TOL_PT = 1e-6
CLOSE_TOL_PT = 1e-5
AREA_REPLICA_TOL = 1e-4
BOUNDARY_TOL_DECADE = 0.05


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download() -> tuple[str, bytes]:
    last = None
    for url in SOURCE_URLS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-excluded-region/1.0"})
            with urllib.request.urlopen(req, timeout=45) as r:
                payload = r.read()
            if payload:
                return url, payload
        except Exception as exc:
            last = repr(exc)
    raise RuntimeError(f"source download failed: {last}")


def safe_extract(tf: tarfile.TarFile, root: Path) -> None:
    rr = root.resolve()
    for member in tf.getmembers():
        target = (root / member.name).resolve()
        if rr not in target.parents and target != rr:
            raise RuntimeError("unsafe tar member")
    tf.extractall(root)


def magenta(rgb) -> bool:
    if rgb is None or len(rgb) < 3:
        return False
    r, g, b = [max(0.0, min(1.0, float(v))) for v in rgb[:3]]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return 285.0 <= 360.0 * h <= 345.0 and s >= 0.35 and v >= 0.35


def xy(p):
    return (float(p.x), float(p.y))


def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])


def bezier(p0, p1, p2, p3, subdivisions):
    a, b, c, d = map(xy, (p0, p1, p2, p3))
    pts = []
    for i in range(subdivisions + 1):
        t = i / subdivisions
        u = 1.0 - t
        pts.append((
            u**3*a[0] + 3*u*u*t*b[0] + 3*u*t*t*c[0] + t**3*d[0],
            u**3*a[1] + 3*u*u*t*b[1] + 3*u*t*t*c[1] + t**3*d[1],
        ))
    return pts


def item_polyline(item, subdivisions):
    kind = item[0]
    if kind == "l":
        return [xy(item[1]), xy(item[2])], False
    if kind == "c":
        return bezier(item[1], item[2], item[3], item[4], subdivisions), False
    if kind == "re":
        r = item[1]
        return [(r.x0,r.y0),(r.x1,r.y0),(r.x1,r.y1),(r.x0,r.y1),(r.x0,r.y0)], True
    if kind == "qu":
        q = item[1]
        pts = [xy(q.ul), xy(q.ur), xy(q.lr), xy(q.ll), xy(q.ul)]
        return pts, True
    return [], False


def drawing_subpaths(drawing, subdivisions):
    subpaths = []
    current = []
    explicit_closed = []
    for item in drawing.get("items", ()):
        pts, closed_item = item_polyline(item, subdivisions)
        if len(pts) < 2:
            continue
        if not current:
            current = pts[:]
            explicit_closed = [closed_item]
        elif dist(current[-1], pts[0]) <= CONNECT_TOL_PT:
            current.extend(pts[1:])
            explicit_closed.append(closed_item)
        else:
            subpaths.append((current, any(explicit_closed)))
            current = pts[:]
            explicit_closed = [closed_item]
    if current:
        subpaths.append((current, any(explicit_closed)))

    loops = []
    drawing_close = bool(drawing.get("closePath", False))
    for pts, item_closed in subpaths:
        if len(pts) < 3:
            continue
        gap = dist(pts[0], pts[-1])
        if gap <= CLOSE_TOL_PT:
            if gap > 0:
                pts = pts + [pts[0]]
        elif item_closed or drawing_close:
            pts = pts + [pts[0]]
        else:
            continue
        loops.append(pts)
    return loops


def phys(pt):
    return (AX * pt[0] + BX, AY * pt[1] + BY)


def scientific_span(drawing):
    pts = []
    for item in drawing.get("items", ()):
        pl, _ = item_polyline(item, 8)
        pts.extend(pl)
    inside = []
    for p in pts:
        q = phys(p)
        if DOMAIN[0]-0.05 <= q[0] <= DOMAIN[2]+0.05 and DOMAIN[1]-0.05 <= q[1] <= DOMAIN[3]+0.05:
            inside.append(q)
    if len(inside) < 2:
        return False
    xs = [p[0] for p in inside]; ys = [p[1] for p in inside]
    return max(xs)-min(xs) >= 2.0 or max(ys)-min(ys) >= 1.0


def polygonal_union_from_fill(drawing, subdivisions):
    loops_pdf = drawing_subpaths(drawing, subdivisions)
    if not loops_pdf:
        raise ValueError("eligible filled magenta drawing has no closed subpaths")
    polys = []
    loop_meta = []
    for loop in loops_pdf:
        coords = [phys(p) for p in loop]
        if not all(math.isfinite(x) and math.isfinite(y) for x,y in coords):
            raise ValueError("non-finite physical polygon coordinate")
        poly = Polygon(coords)
        if not poly.is_valid or poly.area <= 0.0:
            raise ValueError("invalid or zero-area primary fill loop; topology repair forbidden")
        polys.append(poly)
        loop_meta.append({"vertex_count": len(coords), "area_before_clip": poly.area})
    # Preserve PDF fill rule deterministically: even-odd uses XOR, nonzero uses union.
    if bool(drawing.get("even_odd", False)):
        geom = polys[0]
        for p in polys[1:]:
            geom = geom.symmetric_difference(p)
    else:
        geom = unary_union(polys)
    clipped = geom.intersection(box(*DOMAIN))
    if clipped.is_empty or clipped.area <= 0.0:
        raise ValueError("clipped excluded union is empty")
    if not clipped.is_valid:
        raise ValueError("clipped excluded union invalid; topology repair forbidden")
    return clipped, loop_meta


def polygons_json(geom):
    if geom.geom_type == "Polygon":
        geoms = [geom]
    elif geom.geom_type == "MultiPolygon":
        geoms = list(geom.geoms)
    elif geom.geom_type == "GeometryCollection":
        geoms = [g for g in geom.geoms if g.geom_type == "Polygon" and g.area > 0]
    else:
        geoms = []
    out = []
    for p in geoms:
        rp = p.representative_point()
        out.append({
            "area_log10_decade2": p.area,
            "exterior": [[float(x), float(y)] for x,y in p.exterior.coords],
            "holes": [[[float(x), float(y)] for x,y in ring.coords] for ring in p.interiors],
            "representative_interior_point": [float(rp.x), float(rp.y)],
            "distance_to_plot_boundary": float(rp.distance(box(*DOMAIN).boundary)),
        })
    if not out:
        raise ValueError("no positive polygon components after clipping")
    return out


def sampled_stroke_points(drawing):
    out = []
    for item in drawing.get("items", ()):
        pts, _ = item_polyline(item, 32)
        for p in pts:
            q = phys(p)
            if DOMAIN[0] <= q[0] <= DOMAIN[2] and DOMAIN[1] <= q[1] <= DOMAIN[3]:
                out.append(q)
    return out


def main():
    try:
        used_url, source = download()
        if sha256(source) != SOURCE_SHA256:
            raise ValueError("source SHA256 mismatch")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            with tarfile.open(fileobj=io.BytesIO(source), mode="r:*") as tf:
                safe_extract(tf, root)
            asset_bytes = (root / ASSET).read_bytes()
            if sha256(asset_bytes) != ASSET_SHA256:
                raise ValueError("asset SHA256 mismatch")
            doc = fitz.open(stream=asset_bytes, filetype="pdf")
            if doc.page_count != 1:
                raise ValueError("unexpected page count")
            drawings = doc[0].get_drawings()
            sci_magenta = [d for d in drawings if (magenta(d.get("color")) or magenta(d.get("fill"))) and scientific_span(d)]
            filled = [d for d in sci_magenta if magenta(d.get("fill"))]
            stroke_only = [d for d in sci_magenta if magenta(d.get("color")) and not magenta(d.get("fill"))]
            if len(filled) != 1:
                result = {
                    "iteration":"0078c", "status":"PARTIAL_EXCLUDED_REGION_TOPOLOGY",
                    "reason":f"eligible scientific magenta filled drawing count is {len(filled)}, expected exactly one",
                    "scientific_magenta_count":len(sci_magenta), "filled_count":len(filled), "stroke_only_count":len(stroke_only)
                }
            else:
                g32, meta32 = polygonal_union_from_fill(filled[0], 32)
                g64, meta64 = polygonal_union_from_fill(filled[0], 64)
                area_rel = abs(g32.area-g64.area)/max(g64.area, 1e-300)
                sym_rel = g32.symmetric_difference(g64).area/max(g64.area, 1e-300)
                polygon_data = polygons_json(g64)
                interior_ok = any(p["distance_to_plot_boundary"] > 0.0 for p in polygon_data)

                stroke_points = [q for d in stroke_only for q in sampled_stroke_points(d)]
                if stroke_points:
                    near = sum(Point(q).distance(g64.boundary) <= BOUNDARY_TOL_DECADE for q in stroke_points)
                    boundary_fraction = near / len(stroke_points)
                else:
                    boundary_fraction = 0.0
                subdivision_ok = area_rel <= AREA_REPLICA_TOL and sym_rel <= AREA_REPLICA_TOL
                boundary_ok = boundary_fraction >= 0.5
                if not subdivision_ok or not boundary_ok or not interior_ok:
                    status = "PARTIAL_EXCLUDED_REGION_TOPOLOGY"
                else:
                    status = "PASS_SOLAR_CEVNS_B_L_EXCLUDED_REGION"

                existing = {
                    "wagner_0072": {
                        "classification": json.loads(Path("data/wagner_named_curves_0072c.json").read_text())["classification"],
                        "combination_status": "NOT_PROMOTED_GLOBAL_SIDE_AUTHORITY_UNRESOLVED"
                    },
                    "coherent_0074c": {
                        "classification": json.loads(Path("data/coherent_combined_likelihood_authority_audit_0074c.json").read_text())["classification"],
                        "combination_status": "NOT_COMBINED_BLOCKED_LIKELIHOOD_AUTHORITY"
                    },
                    "global_0071": {
                        "classification": json.loads(Path("data/b_minus_l_primary_constraints_0071.json").read_text())["classification"],
                        "combination_status": "GLOBAL_ENVELOPE_REMAINS_INCOMPLETE"
                    }
                }
                partial_envelope = status == "PASS_SOLAR_CEVNS_B_L_EXCLUDED_REGION"
                result = {
                    "iteration":"0078c", "status":status,
                    "secondary_classification":"PASS_PARTIAL_B_L_EXTERNAL_ENVELOPE" if partial_envelope else None,
                    "source_url":used_url, "source_sha256":SOURCE_SHA256,
                    "asset":ASSET, "asset_sha256":ASSET_SHA256,
                    "calibration":{"log10_m_GeV":[AX,BX],"log10_gBL":[AY,BY],"domain":DOMAIN},
                    "scientific_magenta_count":len(sci_magenta), "filled_count":len(filled), "stroke_only_count":len(stroke_only),
                    "fill_even_odd":bool(filled[0].get("even_odd",False)),
                    "subdivision_replica":{"area32":g32.area,"area64":g64.area,"area_relative_difference":area_rel,"symmetric_difference_relative_area":sym_rel,"pass":subdivision_ok},
                    "stroke_boundary_control":{"sample_count":len(stroke_points),"fraction_within_0p05_decade":boundary_fraction,"pass":boundary_ok},
                    "excluded_region":{"area_log10_decade2":g64.area,"polygon_components":polygon_data},
                    "existing_family_combination_audit":existing,
                    "global_envelope_complete":False,
                    "guard":"Primary filled magenta 90% CL solar-CEvNS B-L exclusion only. No response/enhancement scan and no assumed excluded side for older line-only/blocked families."
                }
    except (OSError, urllib.error.URLError, RuntimeError) as exc:
        result = {"iteration":"0078c","status":"INFRASTRUCTURE_FAIL","reason":repr(exc)}
    except (ValueError, fitz.FileDataError) as exc:
        result = {"iteration":"0078c","status":"SCIENTIFIC_FAIL_EXCLUDED_REGION_TOPOLOGY","reason":repr(exc)}

    Path("deromeri_bl_excluded_region_0078c.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    compact = dict(result)
    if "excluded_region" in compact:
        compact["excluded_region"] = {
            "area_log10_decade2": compact["excluded_region"]["area_log10_decade2"],
            "polygon_component_count": len(compact["excluded_region"]["polygon_components"]),
            "component_summaries": [
                {k:v for k,v in p.items() if k not in {"exterior","holes"}}
                for p in compact["excluded_region"]["polygon_components"]
            ]
        }
    print(json.dumps(compact, indent=2, sort_keys=True))
    if result.get("status","").startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
