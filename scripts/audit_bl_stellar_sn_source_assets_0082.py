#!/usr/bin/env python3
import hashlib
import io
import json
import os
import re
import tarfile
import time
import urllib.request

SOURCES = {
    "hong_shin_yun_2021": {
        "arxiv": "2012.05427v3",
        "url": "https://export.arxiv.org/e-print/2012.05427v3",
        "role": "young_neutron_star_cooling",
    },
    "cerdeno_et_al_2021": {
        "arxiv": "2106.11660v3",
        "url": "https://export.arxiv.org/e-print/2106.11660v3",
        "role": "sn1987a_diffusion_medium_effects",
    },
    "shin_yun_2022": {
        "arxiv": "2110.03362v2",
        "url": "https://export.arxiv.org/e-print/2110.03362v2",
        "role": "sn1987a_and_ns1987a_bremsstrahlung_update",
    },
}

TEXT_EXTS = {".tex", ".sty", ".cls", ".bib", ".txt"}
VECTOR_EXTS = {".pdf", ".eps", ".ps", ".svg"}
NUMERIC_EXTS = {".csv", ".dat", ".tsv", ".json", ".yaml", ".yml", ".py", ".m", ".nb", ".ipynb", ".root"}
RASTER_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".tif", ".tiff"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str, attempts: int = 3) -> bytes:
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0082-source-authority/1.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except Exception as exc:  # infrastructure only
            last = exc
            if i + 1 < attempts:
                time.sleep(2 ** i)
    raise RuntimeError(f"source fetch failed after {attempts} attempts: {url}: {last}")


def norm_tex(text: str) -> str:
    s = text.lower()
    s = s.replace("−", "-").replace("–", "-")
    s = re.sub(r"\\(?:mathrm|rm|text|operatorname)\s*\{([^{}]*)\}", r"\1", s)
    s = s.replace("\\!", "").replace("\\,", "").replace("~", " ")
    s = s.replace("{", "").replace("}", "").replace("$", "")
    s = re.sub(r"\s+", " ", s)
    return s


def explicit_bl(text: str) -> bool:
    n = norm_tex(text)
    patterns = [
        r"u\s*\(?1\)?[^\n]{0,50}b\s*-\s*l",
        r"b\s*-\s*l\s+gauge",
        r"b\s*-\s*l\s+model",
        r"b\s*-\s*l\s+boson",
        r"b\s*-\s*l\s+coupl",
    ]
    return any(re.search(p, n, flags=re.I) for p in patterns)


def include_tokens(text: str):
    toks = []
    rx = re.compile(r"\\includegraphics(?:\s*\[[^\]]*\])?\s*\{([^{}]+)\}", re.I)
    for m in rx.finditer(text):
        tok = m.group(1).strip()
        if tok not in toks:
            toks.append(tok)
    return toks


def resolve_include(token: str, member_names):
    token = token.lstrip("./")
    out = []
    token_base = os.path.basename(token)
    token_stem, token_ext = os.path.splitext(token_base)
    for name in member_names:
        clean = name.lstrip("./")
        base = os.path.basename(clean)
        stem, ext = os.path.splitext(base)
        exact = clean == token or base == token_base
        stem_match = (not token_ext and stem == token_stem)
        if exact or stem_match:
            out.append(clean)
    return sorted(set(out))


def text_flags(text: str):
    n = norm_tex(text)
    return {
        "explicit_b_l": explicit_bl(text),
        "sn1987a": "sn1987a" in n or "sn 1987a" in n,
        "ns1987a": "ns1987a" in n or "ns 1987a" in n,
        "cas_a": "cas a" in n or "cassiopeia a" in n,
        "young_neutron_star": "young neutron star" in n or "young ns" in n,
        "medium_effect": "medium effect" in n,
        "transverse": "transverse" in n,
        "longitudinal": "longitudinal" in n,
        "revisit": "revisit" in n,
        "constraint_or_bound": ("constraint" in n or "bound" in n or "exclud" in n),
    }


def inspect_archive(raw: bytes, source_key: str, cfg: dict):
    manifest = []
    texts = []
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
        for m in tf.getmembers():
            if not m.isfile():
                continue
            name = m.name.lstrip("./")
            ext = os.path.splitext(name.lower())[1]
            manifest.append({"name": name, "bytes": int(m.size), "ext": ext})
            if ext in TEXT_EXTS:
                fh = tf.extractfile(m)
                if fh is not None:
                    b = fh.read()
                    try:
                        texts.append((name, b.decode("utf-8")))
                    except UnicodeDecodeError:
                        texts.append((name, b.decode("latin-1", errors="replace")))
    manifest.sort(key=lambda x: x["name"])
    text = "\n".join(t for _, t in texts)
    flags = text_flags(text)
    includes = include_tokens(text)
    names = [m["name"] for m in manifest]
    include_resolved = {tok: resolve_include(tok, names) for tok in includes}

    vector = [m for m in manifest if m["ext"] in VECTOR_EXTS]
    numeric = [m for m in manifest if m["ext"] in NUMERIC_EXTS]
    raster = [m for m in manifest if m["ext"] in RASTER_EXTS]
    referenced_vector = sorted({name for vals in include_resolved.values() for name in vals if os.path.splitext(name.lower())[1] in VECTOR_EXTS})
    referenced_numeric = sorted({name for vals in include_resolved.values() for name in vals if os.path.splitext(name.lower())[1] in NUMERIC_EXTS})
    candidate_route = bool(referenced_vector or referenced_numeric or numeric)

    semantic_ok = bool(flags["explicit_b_l"] and flags["constraint_or_bound"])
    if not semantic_ok:
        status = "BLOCKED_SOURCE_AUTHORITY"
    elif candidate_route:
        status = "PASS_SOURCE_AUTHORITY"
    else:
        status = "PARTIAL_SOURCE_AUTHORITY"

    revisit_ok = None
    if source_key == "shin_yun_2022":
        revisit_ok = bool(flags["explicit_b_l"] and flags["sn1987a"] and flags["revisit"] and flags["transverse"] and flags["longitudinal"])

    return {
        "source_key": source_key,
        "arxiv": cfg["arxiv"],
        "source_url": cfg["url"],
        "role": cfg["role"],
        "archive_sha256": sha256(raw),
        "archive_bytes": len(raw),
        "member_count": len(manifest),
        "text_member_names": [n for n, _ in texts],
        "text_flags": flags,
        "includegraphics_tokens": includes,
        "includegraphics_resolved": include_resolved,
        "vector_document_assets": vector,
        "numeric_code_assets": numeric,
        "raster_assets": raster,
        "referenced_vector_assets": referenced_vector,
        "referenced_numeric_assets": referenced_numeric,
        "candidate_machine_native_route": candidate_route,
        "shin_yun_revisit_semantics_pass": revisit_ok,
        "status": status,
        "manifest": manifest,
    }


def classify(results):
    statuses = [r["status"] for r in results.values()]
    revisit = results["shin_yun_2022"]["shin_yun_revisit_semantics_pass"]
    if any(s == "BLOCKED_SOURCE_AUTHORITY" for s in statuses) or revisit is False:
        return "BLOCKED_B_L_STELLAR_SN_PRIMARY_SOURCE_ASSET_AUTHORITY"
    if all(s == "PASS_SOURCE_AUTHORITY" for s in statuses) and revisit is True:
        return "PASS_B_L_STELLAR_SN_PRIMARY_SOURCE_ASSET_AUTHORITY"
    return "PASS_PARTIAL_B_L_STELLAR_SN_PRIMARY_SOURCE_ASSET_AUTHORITY"


def audit(fetcher=fetch):
    results = {}
    for key, cfg in SOURCES.items():
        raw = fetcher(cfg["url"])
        results[key] = inspect_archive(raw, key, cfg)
    return {
        "iteration": "0082",
        "classification": classify(results),
        "sources": results,
        "guard": "Source/archive and candidate-asset authority only; no contour extraction, raster digitization, excluded-side assignment, cross-source union/intersection, supersession claim, global B-L envelope, or response scan.",
    }


def main():
    result = audit()
    out = "bl_stellar_sn_source_assets_0082.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["classification"].startswith("BLOCKED_"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
