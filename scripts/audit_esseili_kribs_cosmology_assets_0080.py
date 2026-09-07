#!/usr/bin/env python3
import hashlib
import io
import json
import re
import tarfile
import urllib.request
from collections import Counter
from pathlib import PurePosixPath

SOURCE_URL = "https://export.arxiv.org/e-print/2308.07955v2"
GRAPHIC_EXTS = [".pdf", ".eps", ".svg", ".png", ".jpg", ".jpeg"]
VECTOR_EXTS = {".pdf", ".eps", ".svg"}
RASTER_EXTS = {".png", ".jpg", ".jpeg"}
NUMERIC_EXTS = {".csv", ".tsv", ".dat", ".txt", ".npy", ".npz", ".json", ".py"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-authority-audit/0080"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def open_archive(data: bytes):
    return tarfile.open(fileobj=io.BytesIO(data), mode="r:*")


def decode_text(data: bytes) -> str:
    for enc in ("utf-8", "latin-1"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="replace")


def resolve_graphic(ref: str, member_names):
    ref = ref.strip().replace("\\", "/")
    p = PurePosixPath(ref)
    candidates = [str(p)] if p.suffix.lower() in GRAPHIC_EXTS else [str(p) + ext for ext in GRAPHIC_EXTS]
    exact = [c for c in candidates if c in member_names]
    if exact:
        return exact
    base_candidates = {PurePosixPath(c).name for c in candidates}
    by_base = [n for n in member_names if PurePosixPath(n).name in base_candidates]
    return by_base if len(by_base) == 1 else []


def audit():
    raw = fetch(SOURCE_URL)
    source_hash = sha256(raw)
    with open_archive(raw) as tf:
        members = [m for m in tf.getmembers() if m.isfile()]
        names = [m.name.lstrip("./") for m in members]
        member_info = [{"name": n, "size": m.size, "ext": PurePosixPath(n).suffix.lower()} for m, n in zip(members, names)]
        tex_records = []
        graphics = []
        numeric_assets = []
        for m, n in zip(members, names):
            ext = PurePosixPath(n).suffix.lower()
            if ext in NUMERIC_EXTS:
                numeric_assets.append({"name": n, "size": m.size, "ext": ext})
            if ext not in {".tex", ".ltx"}:
                continue
            f = tf.extractfile(m)
            if not f:
                continue
            text = decode_text(f.read())
            tex_records.append({"name": n, "length": len(text)})
            for env_index, match in enumerate(re.finditer(r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", text, flags=re.S), start=1):
                block = match.group(1)
                refs = re.findall(r"\\includegraphics\*?(?:\[[^\]]*\])?\{([^}]+)\}", block)
                caption_m = re.search(r"\\caption\{(.*?)\}(?=\s*\\label|\s*$)", block, flags=re.S)
                label_m = re.search(r"\\label\{([^}]+)\}", block)
                caption = re.sub(r"\s+", " ", caption_m.group(1)).strip() if caption_m else None
                label = label_m.group(1).strip() if label_m else None
                resolved = []
                for ref in refs:
                    for hit in resolve_graphic(ref, names):
                        ext2 = PurePosixPath(hit).suffix.lower()
                        resolved.append({
                            "ref": ref,
                            "asset": hit,
                            "ext": ext2,
                            "kind": "vector" if ext2 in VECTOR_EXTS else "raster" if ext2 in RASTER_EXTS else "other",
                        })
                graphics.append({
                    "tex": n,
                    "source_figure_index_in_tex": env_index,
                    "caption": caption,
                    "label": label,
                    "refs": refs,
                    "resolved": resolved,
                })

        counts = Counter(g["tex"] for g in graphics)
        main_tex = counts.most_common(1)[0][0] if counts else None
        target = [
            g for g in graphics
            if g["tex"] == main_tex and g["source_figure_index_in_tex"] in {5, 6, 7, 8}
        ]
        resolved_assets = [x for g in target for x in g["resolved"]]
        vector_assets = sorted({x["asset"] for x in resolved_assets if x["kind"] == "vector"})
        raster_assets = sorted({x["asset"] for x in resolved_assets if x["kind"] == "raster"})
        unresolved_target_refs = [r for g in target for r in g["refs"] if not resolve_graphic(r, names)]
        target_each_resolved = len(target) == 4 and all(g["refs"] and g["resolved"] for g in target)
        target_semantics = []
        for g in target:
            s = ((g.get("caption") or "") + " " + (g.get("label") or "")).lower()
            target_semantics.append({
                "index": g["source_figure_index_in_tex"],
                "mentions_majorana": "majorana" in s,
                "mentions_dirac": "dirac" in s,
                "mentions_bbn_or_helium": any(k in s for k in ["bbn", "helium", "y_p", "y_{p}"]),
                "mentions_neff_or_cmb": any(k in s for k in ["n_{\\rm eff}", "n_{\rm eff}", "n_eff", "cmb", "planck"]),
            })
        # Source-order semantic guard: four exact figure environments must exist and be resolved;
        # pair identity must at minimum distinguish Majorana/Dirac in 5/6 or via 'same as' caption linkage.
        scenario_mentions = sum(x["mentions_majorana"] or x["mentions_dirac"] for x in target_semantics)
        semantic_guard = target_each_resolved and scenario_mentions >= 2

        numerical_candidates = [a for a in numeric_assets if not a["name"].lower().endswith(("references.txt", "readme.txt"))]

        all_target_vector = target_each_resolved and all(
            all(x["kind"] == "vector" for x in g["resolved"]) for g in target
        )
        all_target_raster = target_each_resolved and all(
            all(x["kind"] == "raster" for x in g["resolved"]) for g in target
        )
        if semantic_guard and all_target_vector:
            classification = "PASS_COSMOLOGY_B_L_VECTOR_ASSET_AUTHORITY"
        elif semantic_guard and all_target_raster and not numerical_candidates:
            classification = "PARTIAL_COSMOLOGY_B_L_RASTER_ONLY"
        else:
            classification = "BLOCKED_COSMOLOGY_B_L_SOURCE_SEMANTICS"

        return {
            "iteration": "0080",
            "source_url": SOURCE_URL,
            "source_sha256": source_hash,
            "source_bytes": len(raw),
            "member_count": len(member_info),
            "tex_files": tex_records,
            "main_tex_by_figure_count": main_tex,
            "all_members": member_info,
            "all_figure_blocks": graphics,
            "target_published_figures_5_8": target,
            "target_semantic_checks": target_semantics,
            "target_vector_assets": vector_assets,
            "target_raster_assets": raster_assets,
            "unresolved_target_refs": unresolved_target_refs,
            "numerical_asset_candidates_uninterpreted": numerical_candidates,
            "classification": classification,
            "guard": "Source-asset authority only; no contour values, axis calibration, raster digitization, observational-threshold choice, scenario combination, or envelope union performed.",
        }


def main():
    result = audit()
    with open("esseili_kribs_cosmology_assets_0080.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["classification"] == "BLOCKED_COSMOLOGY_B_L_SOURCE_SEMANTICS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
