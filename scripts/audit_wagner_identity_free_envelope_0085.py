#!/usr/bin/env python3
from __future__ import annotations
import hashlib, io, json, math, pathlib, re, tarfile, urllib.request
from collections import defaultdict

from summarize_wagner_eps_paths_0072 import parse_paths

URL = "https://arxiv.org/e-print/1207.2442"
TARGET = "WEP_figure6.eps"
EPS_SHA256 = "4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882"
CAL_PATH = pathlib.Path(__file__).resolve().parents[1] / "data" / "wagner_axis_calibration_0072b.json"
BOX = (1.681, 6.681, 0.844, 4.844)
WIDTH = 0.010
CHAIN_TOL = 1e-9
ROUNDTRIP_TOL = 1e-9
G_CONST = 2.70463357586823e-19
HBARC = 1.973269804e-7
MASS_CLIP_EV = 1e-6
COLORS = {
    "blue": (0.0, 0.0, 1.0),
    "red": (1.0, 0.0, 0.0),
    "orange": (1.0, 0.5, 0.0),
    "magenta": (1.0, 0.0, 1.0),
}
EXPECTED = {"blue": 4, "red": 1, "orange": 1, "magenta": 2}


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0085/1.1"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def inside(p):
    x0, x1, y0, y1 = BOX
    x, y = p
    return x0 - 1e-9 <= x <= x1 + 1e-9 and y0 - 1e-9 <= y <= y1 + 1e-9


def dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def chain_family(records):
    chains = []
    cur = None
    for r in records:
        a, b = tuple(r["first"]), tuple(r["last"])
        if cur is not None and dist(cur["points"][-1], a) <= CHAIN_TOL:
            cur["points"].append(b)
            cur["segment_indices"].append(r["index"])
        else:
            if cur is not None:
                chains.append(cur)
            cur = {"points": [a, b], "segment_indices": [r["index"]]}
    if cur is not None:
        chains.append(cur)
    return chains


def monotonic_x(points):
    ds = [points[i + 1][0] - points[i][0] for i in range(len(points) - 1)]
    return all(d >= -1e-12 for d in ds) or all(d <= 1e-12 for d in ds)


def normalize_tex(s: str) -> str:
    s = re.sub(r"(?<!\\)%.*", " ", s)
    s = s.replace("\n", " ")
    s = s.replace("\\", " ").replace("{", " ").replace("}", " ").replace("~", " ")
    s = re.sub(r"\s+", " ", s)
    return s.lower()


def source_text_authority(tf: tarfile.TarFile):
    texts = []
    for m in tf.getmembers():
        if not (m.isfile() and m.name.lower().endswith(".tex")):
            continue
        raw = tf.extractfile(m).read()
        try:
            t = raw.decode("utf-8")
        except UnicodeDecodeError:
            t = raw.decode("latin-1")
        texts.append((m.name, normalize_tex(t)))
    merged = " ".join(t for _, t in texts)
    upper = bool(re.search(r"\b95\s*%\s*cl\s+upper\s+bounds?\b", merged))
    bl = bool(re.search(r"b\s*-\s*l|bminusl|baryon.{0,80}lepton", merged))
    fig6 = "figure 6" in merged or "fig. 6" in merged or "fig 6" in merged or "wep_figure6" in merged
    vector = "vector yukawa" in merged
    evidence = []
    for pat in [r"95\s*%\s*cl\s+upper\s+bounds?", r"vector yukawa", r"b\s*-\s*l", r"figure 6|wep_figure6"]:
        m = re.search(pat, merged)
        if m:
            p = m.start()
            evidence.append(merged[max(0, p - 220): min(len(merged), p + 420)])
    return {"tex_files": [n for n, _ in texts], "upper_bounds_95cl": upper, "B_minus_L": bl,
            "figure6_context": fig6, "vector_yukawa": vector, "evidence": evidence[:8]}


def transform_eps(p, tr):
    xe, ye = p
    loglam = tr["a_x"] * xe + tr["b_x"]
    logalpha = tr["a_y"] * ye + tr["b_y"]
    lam = 10.0 ** loglam
    alpha = 10.0 ** logalpha
    mass = HBARC / lam
    g = G_CONST * math.sqrt(alpha)
    return {"eps": [xe, ye], "log10_lambda_m": loglam, "log10_alpha": logalpha,
            "lambda_m": lam, "alpha": alpha, "m_V_eV": mass, "g_BL": g,
            "x": math.log10(mass), "y": math.log10(g)}


def build_components(eps_text: str, tr):
    paths = parse_paths(eps_text)
    records = defaultdict(list)
    for i, p in enumerate(paths):
        c = tuple(p["color"])
        fam = next((name for name, rgb in COLORS.items() if c == rgb), None)
        if fam is None or p["n"] != 2 or p["linewidth"] is None or abs(p["linewidth"] - WIDTH) > 1e-12:
            continue
        if inside(tuple(p["first"])) and inside(tuple(p["last"])):
            records[fam].append({"index": i, "first": p["first"], "last": p["last"]})

    components = []
    topology = {}
    dropped = {}
    max_rt = 0.0
    for fam in COLORS:
        raw = chain_family(records[fam])
        keep, drop = [], []
        for ch in raw:
            ch["n_segments"] = len(ch["segment_indices"])
            (keep if ch["n_segments"] >= 3 else drop).append(ch)
        topology[fam] = {"retained": len(keep), "expected": EXPECTED[fam], "dropped_fragments": len(drop)}
        dropped[fam] = [{"n_segments": x["n_segments"], "segment_indices": x["segment_indices"]} for x in drop]
        for j, ch in enumerate(keep):
            mono = monotonic_x(ch["points"])
            pts = [transform_eps(p, tr) for p in ch["points"]]
            for p0, q in zip(ch["points"], pts):
                xr = (q["log10_lambda_m"] - tr["b_x"]) / tr["a_x"]
                yr = (q["log10_alpha"] - tr["b_y"]) / tr["a_y"]
                max_rt = max(max_rt, abs(xr - p0[0]), abs(yr - p0[1]))
            pts.sort(key=lambda q: q["x"])
            finite = all(math.isfinite(q[k]) and q[k] > 0 for q in pts for k in ["m_V_eV", "alpha", "g_BL"])
            components.append({"anonymous_id": f"{fam}_{j}", "family": fam, "chain_index": j,
                               "n_segments": ch["n_segments"], "x_monotonic": mono, "finite_positive": finite,
                               "x_min": min(q["x"] for q in pts), "x_max": max(q["x"] for q in pts), "points": pts})
    return components, topology, dropped, max_rt


def interp_component(comp, x):
    if x < comp["x_min"] - 1e-13 or x > comp["x_max"] + 1e-13:
        return None
    pts = comp["points"]
    if abs(x - pts[-1]["x"]) <= 1e-13:
        return pts[-1]["y"]
    for a, b in zip(pts[:-1], pts[1:]):
        if a["x"] - 1e-13 <= x <= b["x"] + 1e-13:
            if abs(b["x"] - a["x"]) <= 1e-15:
                return min(a["y"], b["y"])
            t = (x - a["x"]) / (b["x"] - a["x"])
            return a["y"] + t * (b["y"] - a["y"])
    return None


def envelope_at(components, x):
    vals = []
    for c in components:
        y = interp_component(c, x)
        if y is not None:
            vals.append((y, c["anonymous_id"]))
    if not vals:
        return None
    y, cid = min(vals, key=lambda z: (z[0], z[1]))
    return y, cid, len(vals)


def make_grid(components, n_uniform):
    xmin = max(math.log10(MASS_CLIP_EV), min(c["x_min"] for c in components))
    xmax = max(c["x_max"] for c in components)
    if xmax <= xmin:
        return []
    xs = {xmin, xmax}
    for c in components:
        for p in c["points"]:
            if xmin <= p["x"] <= xmax:
                xs.add(p["x"])
    for i in range(n_uniform):
        xs.add(xmin + (xmax - xmin) * i / (n_uniform - 1))
    return sorted(xs)


def support_runs(samples):
    runs = []
    cur = []
    for s in samples:
        if s["supported"]:
            cur.append(s)
        elif cur:
            runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return [{"x_min": r[0]["x"], "x_max": r[-1]["x"], "n_samples": len(r)} for r in runs]


def audit(fetcher=fetch):
    body = fetcher(URL)
    with tarfile.open(fileobj=io.BytesIO(body), mode="r:gz") as tf:
        eps = tf.extractfile(tf.getmember(TARGET)).read()
        src = source_text_authority(tf)
    if sha256(eps) != EPS_SHA256:
        raise RuntimeError("EPS SHA mismatch")

    cal = json.loads(CAL_PATH.read_text(encoding="utf-8"))
    if cal.get("classification") != "PASS_WAGNER_AXIS_CALIBRATION" or cal.get("eps_sha256") != EPS_SHA256:
        raise RuntimeError("0072b calibration authority mismatch")
    tr = cal["transform"]

    comps, topology, dropped, max_rt = build_components(eps.decode("latin-1", errors="replace"), tr)
    topology_ok = all(topology[f]["retained"] == EXPECTED[f] for f in EXPECTED) and len(comps) == 8
    monotonic_ok = all(c["x_monotonic"] for c in comps)
    finite_ok = all(c["finite_positive"] for c in comps)
    source_ok = src["upper_bounds_95cl"] and src["B_minus_L"] and src["vector_yukawa"] and src["figure6_context"]
    roundtrip_ok = max_rt <= ROUNDTRIP_TOL

    coarse_x = make_grid(comps, 20001) if topology_ok and monotonic_ok and finite_ok else []
    coarse = []
    for x in coarse_x:
        e = envelope_at(comps, x)
        coarse.append({"x": x, "m_V_eV": 10.0 ** x, "supported": e is not None,
                       "y": None if e is None else e[0], "g_BL": None if e is None else 10.0 ** e[0],
                       "active_component": None if e is None else e[1], "n_supported_components": 0 if e is None else e[2]})
    supported = [s for s in coarse if s["supported"]]

    renamed = []
    for k, c in enumerate(reversed(comps)):
        z = dict(c)
        z["anonymous_id"] = f"anon_perm_{k}"
        renamed.append(z)
    inv_max = 0.0
    for s in supported:
        e2 = envelope_at(renamed, s["x"])
        if e2 is None:
            inv_max = float("inf")
            break
        inv_max = max(inv_max, abs(e2[0] - s["y"]))
    invariance_ok = inv_max <= 1e-12

    fine_x = make_grid(comps, 40001) if coarse_x else []
    fine_support = sum(envelope_at(comps, x) is not None for x in fine_x)
    shared_x = []
    if coarse_x:
        xmin, xmax = coarse_x[0], coarse_x[-1]
        shared_x = [xmin + (xmax - xmin) * i / 10000.0 for i in range(10001)]
    fine_check_max = 0.0
    shared_supported = 0
    for x in shared_x:
        a = envelope_at(comps, x)
        b = envelope_at(list(reversed(comps)), x)
        if (a is None) != (b is None):
            fine_check_max = float("inf")
            break
        if a is not None:
            shared_supported += 1
            fine_check_max = max(fine_check_max, abs(a[0] - b[0]))
    fine_ok = fine_check_max <= 1e-10 and shared_supported > 0 and fine_support > 0
    support_ok = bool(supported) and min(s["m_V_eV"] for s in supported) >= MASS_CLIP_EV * (1 - 1e-12)

    diagnostics_ok = topology_ok and monotonic_ok and finite_ok and source_ok and roundtrip_ok and invariance_ok and fine_ok and support_ok
    if diagnostics_ok:
        cls = "PASS_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE"
    elif not (source_ok and topology_ok and monotonic_ok and support_ok):
        cls = "BLOCKED_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE"
    else:
        cls = "SCIENTIFIC_FAIL_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE"

    env_points = [{"m_V_eV": s["m_V_eV"], "g_BL": s["g_BL"], "active_component": s["active_component"],
                   "n_supported_components": s["n_supported_components"]} for s in supported]
    active_counts = defaultdict(int)
    for s in supported:
        active_counts[s["active_component"]] += 1

    return {
        "iteration": "0085", "classification": cls, "eps_sha256": sha256(eps),
        "source_text_authority": src, "source_authority_ok": source_ok,
        "axis_calibration_sha": cal.get("eps_sha256"),
        "topology": topology, "topology_ok": topology_ok, "component_count": len(comps),
        "components": comps, "dropped_fragments": dropped, "monotonic_ok": monotonic_ok,
        "finite_positive_ok": finite_ok, "roundtrip_max_abs_eps": max_rt, "roundtrip_ok": roundtrip_ok,
        "mass_clip_eV": MASS_CLIP_EV, "support_runs": support_runs(coarse),
        "supported_mass_min_eV": None if not supported else min(s["m_V_eV"] for s in supported),
        "supported_mass_max_eV": None if not supported else max(s["m_V_eV"] for s in supported),
        "supported_grid_point_count": len(supported), "coarse_grid_total": len(coarse),
        "active_component_sample_counts": dict(sorted(active_counts.items())),
        "name_order_invariance_max_decade": inv_max, "name_order_invariance_ok": invariance_ok,
        "fine_grid_total": len(fine_x), "fine_supported_count": fine_support,
        "shared_check_supported_count": shared_supported, "fine_shared_max_decade": fine_check_max,
        "fine_reproduction_ok": fine_ok, "envelope_points": env_points,
        "envelope_semantics": "POINTWISE_STRONGEST_PUBLISHED_WAGNER_95CL_UPPER_LIMIT; NOT a statistically combined 95% CL curve; y>envelope excluded by at least one individual published upper-bound curve.",
        "guard": "Identity-free Wagner family only; blue EW/EW94/EW99 names unresolved; no interpolation across disconnected components; no extrapolation; no global B-L family union; no BSM response scan."
    }


def main():
    r = audit()
    fn = "wagner_identity_free_upper_envelope_0085.json"
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(r, f, indent=2, sort_keys=True)
        f.write("\n")
    summary = {k: r[k] for k in ["iteration", "classification", "eps_sha256", "source_authority_ok", "topology", "component_count",
        "monotonic_ok", "roundtrip_max_abs_eps", "supported_mass_min_eV", "supported_mass_max_eV",
        "supported_grid_point_count", "active_component_sample_counts", "name_order_invariance_max_decade",
        "fine_shared_max_decade", "support_runs", "envelope_semantics"]}
    print(json.dumps(summary, indent=2, sort_keys=True))
    if not r["classification"].startswith("PASS_"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
