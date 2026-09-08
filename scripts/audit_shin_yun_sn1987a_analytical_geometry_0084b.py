#!/usr/bin/env python3
import hashlib, io, json, math, pathlib, re, tarfile, time, urllib.request

URL = "https://export.arxiv.org/e-print/2110.03362v2"
ARCHIVE_SHA256 = "7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd"
LEDGER_PATH = pathlib.Path(__file__).resolve().parents[1] / "data" / "b_minus_l_primary_constraints_0071.json"
M_E_MEV = 0.51099895069
M_E_STD_UNC_MEV = 0.00000000016
M_MIN_EV = 1.0e-6
T_LOW = 1.0e-11
T_HIGH = 1.5e-8
L_LOW_PRODUCT_MEV = 7.4e-10
L_HIGH_PRODUCT_MEV = 1.2e-5
REL_TOL = 1.0e-8


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def fetch(url):
    last = None
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0084b/1.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except Exception as exc:
            last = exc
            time.sleep(2 ** i)
    raise RuntimeError(f"fetch failed: {last}")


def tex_members(blob):
    out = []
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:*") as tf:
        for m in tf.getmembers():
            name = m.name.lstrip("./")
            if not (m.isfile() and name.lower().endswith(".tex")):
                continue
            raw = tf.extractfile(m).read()
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                text = raw.decode("latin-1")
            out.append((name, text))
    return out


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def compact(s):
    s = strip_comments(s)
    s = s.replace("\n", " ")
    s = s.replace("\\,", "").replace("\\!", "").replace("~", " ")
    s = re.sub(r"\s+", "", s)
    return s


def source_authority(text):
    c = compact(text)
    # Eq. (1): e' A'_mu J'^mu; current definition; explicit B-L specialization.
    lagrangian = bool(re.search(
        r"e\^\{?\\prime\}?A\^\{?\\prime\}?_\{?\\mu\}?J\^\{?\\prime\\mu\}?",
        c, re.I))
    current = bool(re.search(
        r"J\^\{?\\prime\\mu\}?=.*q_\{?f\}?\^\{?\\prime\}?.*\\bar\{?f\}?\\gamma\^\{?\\mu\}?f",
        c, re.I))
    bl = bool(re.search(r"anomaly-?free.*B-?L.*current|B-?L.*baryon.*lepton", c, re.I))

    # Exact source-native analytical relations used by 0084/0084a.
    t_low = bool(re.search(r"e\^\{?\\prime\}?<10\^\{?-11\}?", c))
    t_high = bool(re.search(r"e\^\{?\\prime\}?>1\.5\\times10\^\{?-8\}?", c))
    l_low = bool(re.search(
        r"e\^\{?\\prime\}?m_\{?\\gamma\^\{?\\prime\}?\}?<7\.4\\times10\^\{?-10\}?", c))
    l_high = bool(re.search(
        r"e\^\{?\\prime\}?m_\{?\\gamma\^\{?\\prime\}?\}?>1\.2\\times10\^\{?-5\}?", c))
    mass20 = bool(re.search(r"m_\{?\\gamma\^\{?\\prime\}?\}?<20(?:\\mathrm\{MeV\}|\{\\rmMeV\}|MeV)", c, re.I))
    body_2me = bool(re.search(r"m_\{?\\gamma\^\{?\\prime\}?\}?<2m_\{?e\}?", c))
    summary_1mev = bool(re.search(r"m_\{?\\gamma\^\{?\\prime\}?\}?<1(?:\\mathrm\{MeV\}|\{\\rmMeV\}|MeV)", c, re.I))
    return {
        "lagrangian_eprime_Aprime_Jprime": lagrangian,
        "source_current_definition": current,
        "explicit_B_minus_L_current_specialization": bl,
        "T_low_relation": t_low,
        "T_high_relation": t_high,
        "L_low_product_relation": l_low,
        "L_high_product_relation": l_high,
        "low_branch_mass_lt_20_MeV": mass20,
        "body_high_branch_mass_lt_2me": body_2me,
        "conclusion_high_branch_mass_lt_1_MeV": summary_1mev,
    }


def ledger_authority():
    obj = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    model = obj["model"]
    ok_interaction = model.get("interaction") == "L_int = g_BL V_mu J_{B-L}^mu"
    charges = model.get("charges", {})
    ok_charges = charges.get("leptons") == -1 and charges.get("quarks") == "1/3"
    return {
        "interaction": model.get("interaction"),
        "charges": charges,
        "same_standard_B_minus_L_current": bool(ok_interaction and ok_charges),
    }


def polygon_area(poly):
    s = 0.0
    for i, (x0, y0) in enumerate(poly):
        x1, y1 = poly[(i + 1) % len(poly)]
        s += x0 * y1 - x1 * y0
    return abs(s) / 2.0


def sampled_area(width_fn, x0, x1, n=10001):
    if n < 2:
        raise ValueError("n must be >=2")
    h = (x1 - x0) / (n - 1)
    total = 0.0
    prev = width_fn(x0)
    for i in range(1, n):
        x = x0 + i * h
        cur = width_fn(x)
        total += 0.5 * (prev + cur) * h
        prev = cur
    return total


def region(variant, polarization, mmax_mev):
    mmax_ev = mmax_mev * 1.0e6
    x0 = math.log10(M_MIN_EV)
    x1 = math.log10(mmax_ev)
    if not x1 > x0:
        raise ValueError("non-positive mass interval")

    if polarization == "T":
        ylo0 = ylo1 = math.log10(T_LOW)
        yhi0 = yhi1 = math.log10(T_HIGH)
        width = math.log10(T_HIGH / T_LOW)
        analytic = (x1 - x0) * width
        numerical = sampled_area(lambda _x: width, x0, x1)
        low_formula = "g_BL = 1e-11"
        high_formula = "g_BL = 1.5e-8"
    elif polarization == "L":
        def low_y(x):
            m_mev = 10.0 ** (x - 6.0)
            return math.log10(L_LOW_PRODUCT_MEV / m_mev)
        def high_y(x):
            m_mev = 10.0 ** (x - 6.0)
            return math.log10(L_HIGH_PRODUCT_MEV / m_mev)
        ylo0, ylo1 = low_y(x0), low_y(x1)
        yhi0, yhi1 = high_y(x0), high_y(x1)
        width = math.log10(L_HIGH_PRODUCT_MEV / L_LOW_PRODUCT_MEV)
        analytic = (x1 - x0) * width
        numerical = sampled_area(lambda x: high_y(x) - low_y(x), x0, x1)
        low_formula = "g_BL = (7.4e-10 MeV)/m_V[MeV]"
        high_formula = "g_BL = (1.2e-5 MeV)/m_V[MeV]"
    else:
        raise ValueError(polarization)

    poly = [(x0, ylo0), (x1, ylo1), (x1, yhi1), (x0, yhi0)]
    parea = polygon_area(poly)
    rel = abs(numerical - analytic) / analytic
    ordering = yhi0 > ylo0 and yhi1 > ylo1
    valid = analytic > 0 and parea > 0 and ordering
    poly_rel = abs(parea - analytic) / analytic
    return {
        "variant": variant,
        "polarization": polarization,
        "mass_interval_eV": [M_MIN_EV, mmax_ev],
        "mass_interval_MeV": [M_MIN_EV / 1.0e6, mmax_mev],
        "mass_width_decades": x1 - x0,
        "source_coupling_symbol": "e'",
        "mapped_coupling_symbol": "g_BL",
        "conversion_factor_gBL_over_eprime": 1.0,
        "low_boundary": low_formula,
        "high_boundary": high_formula,
        "polygon_log10_m_eV_log10_g": poly,
        "analytic_area_decade2": analytic,
        "polygon_area_decade2": parea,
        "sampled_area_decade2": numerical,
        "sampled_relative_difference": rel,
        "polygon_relative_difference": poly_rel,
        "ordering_ok_at_both_endpoints": ordering,
        "polygon_valid_positive": valid,
        "agreement_within_1e-8": rel <= REL_TOL and poly_rel <= REL_TOL,
    }


def audit(fetcher=fetch):
    blob = fetcher(URL)
    if sha256(blob) != ARCHIVE_SHA256:
        raise RuntimeError("archive SHA mismatch")
    members = tex_members(blob)
    if not members:
        raise RuntimeError("no TeX source members")
    source_text = "\n".join(t for _, t in members)
    src = source_authority(source_text)
    led = ledger_authority()

    required_source = [
        "lagrangian_eprime_Aprime_Jprime",
        "source_current_definition",
        "explicit_B_minus_L_current_specialization",
        "T_low_relation",
        "T_high_relation",
        "L_low_product_relation",
        "L_high_product_relation",
        "low_branch_mass_lt_20_MeV",
        "body_high_branch_mass_lt_2me",
        "conclusion_high_branch_mass_lt_1_MeV",
    ]
    convention_ok = led["same_standard_B_minus_L_current"] and all(src[k] for k in required_source[:3])
    semantics_ok = all(src[k] for k in required_source[3:])

    body_mmax = 2.0 * M_E_MEV
    variants = {
        "BODY_NATIVE": body_mmax,
        "CONCLUSION_SUMMARY": 1.0,
    }
    regions = []
    if convention_ok and semantics_ok:
        for v, mmax in variants.items():
            regions.append(region(v, "T", mmax))
            regions.append(region(v, "L", mmax))

    geometry_ok = bool(regions) and all(
        r["polygon_valid_positive"] and r["agreement_within_1e-8"] for r in regions
    )
    if not convention_ok or not semantics_ok:
        cls = "BLOCKED_SHIN_YUN_SN1987A_ANALYTICAL_GEOMETRY_AUTHORITY"
    elif geometry_ok:
        cls = "PASS_SHIN_YUN_SN1987A_ANALYTICAL_GEOMETRY_AUTHORITY"
    else:
        cls = "SCIENTIFIC_FAIL_SHIN_YUN_SN1987A_ANALYTICAL_GEOMETRY_AUTHORITY"

    return {
        "iteration": "0084b",
        "classification": cls,
        "archive_sha256": sha256(blob),
        "tex_files": [n for n, _ in members],
        "source_authority": src,
        "nmir_ledger_authority": led,
        "coupling_mapping": {
            "source": "e' A'_mu J'^{mu}, specialized by source to anomaly-free B-L current",
            "nmir": "g_BL V_mu J_{B-L}^mu",
            "identity": "g_BL = e'",
            "factor": 1.0,
            "passed": convention_ok,
        },
        "electron_mass_authority": {
            "authority": "NIST/CODATA 2022",
            "quantity": "electron mass energy equivalent in MeV",
            "central_value_MeV": M_E_MEV,
            "standard_uncertainty_MeV": M_E_STD_UNC_MEV,
            "two_me_MeV": body_mmax,
            "two_me_eV": body_mmax * 1.0e6,
        },
        "variants": {
            "BODY_NATIVE_upper_mass_MeV": body_mmax,
            "CONCLUSION_SUMMARY_upper_mass_MeV": 1.0,
        },
        "regions": regions,
        "geometry_ok": geometry_ok,
        "guard": "T/L separate; BODY_NATIVE and CONCLUSION_SUMMARY separate; no raster/OCR/manual digitization; no 2me=1MeV identity; no high-mass extrapolation; no union with other B-L families; no global envelope; no BSM response scan.",
    }


def main():
    result = audit()
    fn = "shin_yun_sn1987a_analytical_geometry_0084b.json"
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    summary = {
        "classification": result["classification"],
        "archive_sha256": result["archive_sha256"],
        "coupling_mapping": result["coupling_mapping"],
        "electron_mass_authority": result["electron_mass_authority"],
        "regions": [{k: r[k] for k in ["variant", "polarization", "mass_interval_eV", "analytic_area_decade2", "sampled_area_decade2", "polygon_area_decade2", "agreement_within_1e-8"]} for r in result["regions"]],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    if not result["classification"].startswith("PASS_"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
