#!/usr/bin/env python3
import hashlib
import io
import json
import re
import tarfile
import urllib.request
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
    # TeX commonly refers relative to the tex file or omits a leading ./; only basename matching is allowed if unique.
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
            # Capture each figure environment, preserving source order and caption/label semantics.
            for env_index, match in enumerate(re.finditer(r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", text, flags=re.S), start=1):
                block = match.group(1)
                refs = re.findall(r"\\includegraphics\*?(?:\[[^\]]*\])?\{([^}]+)\}", block)
                caption_m = re.search(r"\\caption\{(.*?)\}(?=\s*\\label|\s*$)", block, flags=re.S)
                label_m = re.search(r"\\label\{([^}]+)\}", block)
                caption = re.sub(r"\s+", " ", caption_m.group(1)).strip() if caption_m else None
                label = label_m.group(1).strip() if label_m else None
                resolved = []
                for ref in refs:
                    hits = resolve_graphic(ref, names)
                    for hit in hits:
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

        # Identify cosmology figures only by source caption text / explicit labels.
        target = []
        for g in graphics:
            s = ((g.get("caption") or "") + " " + (g.get("label") or "")).lower()
            if any(k in s for k in ["majorana", "dirac", "n_{\\rm eff}", "n_{\rm eff}", "helium", "y_p", "y_{p}"]):
                target.append(g)

        resolved_assets = [x for g in target for x in g["resolved"]]
        vector_assets = sorted({x["asset"] for x in resolved_assets if x["kind"] == "vector"})
        raster_assets = sorted({x["asset"] for x in resolved_assets if x["kind"] == "raster"})
        unresolved_target_refs = [r for g in target for r in g["refs"] if not resolve_graphic(r, names)]

        # Numerical candidates are only inventoried. No semantics inferred here.
        numerical_candidates = [a for a in numeric_assets if a["ext"] in NUMERIC_EXTS and not a["name"].lower().endswith(("references.txt", "readme.txt"))]

        if target and not unresolved_target_refs and vector_assets:
            classification = "PASS_COSMOLOGY_B_L_VECTOR_ASSET_AUTHORITY"
        elif target and not unresolved_target_refs and raster_assets and not vector_assets:
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
            "all_members": member_info,
            "all_figure_blocks": graphics,
            "target_cosmology_figure_blocks": target,
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
