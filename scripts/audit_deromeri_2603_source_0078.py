#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import io
import json
import re
import tarfile
import tempfile
import urllib.request
from pathlib import Path

ARXIV_ID = "2603.00554"
SOURCE_URLS = (
    f"https://export.arxiv.org/e-print/{ARXIV_ID}",
    f"https://arxiv.org/e-print/{ARXIV_ID}",
    f"https://arxiv.org/src/{ARXIV_ID}",
)
VECTOR_EXTS = {".pdf", ".eps", ".svg", ".ps"}
RASTER_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download() -> tuple[str, bytes]:
    last = None
    for url in SOURCE_URLS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-reproducibility-audit/1.0"})
            with urllib.request.urlopen(req, timeout=45) as r:
                payload = r.read()
            if payload:
                return url, payload
        except Exception as exc:  # infrastructure alternatives only
            last = repr(exc)
    raise RuntimeError(f"all arXiv source endpoints failed: {last}")


def safe_extract(tf: tarfile.TarFile, root: Path) -> None:
    root_resolved = root.resolve()
    for member in tf.getmembers():
        target = (root / member.name).resolve()
        if root_resolved not in target.parents and target != root_resolved:
            raise RuntimeError("unsafe tar member")
    tf.extractall(root)


def resolve_graphic(base: Path, token: str, files: list[Path]) -> list[Path]:
    token = token.strip()
    stem = (base / token).as_posix()
    matches = []
    for p in files:
        posix = p.as_posix()
        if posix == stem or Path(posix).with_suffix("").as_posix() == Path(stem).with_suffix("").as_posix():
            matches.append(p)
    if matches:
        return matches
    name = Path(token).name
    return [p for p in files if p.name == name or p.stem == Path(name).stem]


def main() -> None:
    try:
        used_url, payload = download()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            try:
                with tarfile.open(fileobj=io.BytesIO(payload), mode="r:*") as tf:
                    safe_extract(tf, root)
            except tarfile.TarError as exc:
                raise RuntimeError(f"source payload is not a readable tar archive: {exc}")

            files = [p.relative_to(root) for p in root.rglob("*") if p.is_file()]
            inventory = []
            for rel in sorted(files, key=lambda p: p.as_posix()):
                data = (root / rel).read_bytes()
                inventory.append({"path": rel.as_posix(), "size": len(data), "sha256": sha256(data)})

            hits = []
            graphics = []
            include_re = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
            for rel in files:
                if rel.suffix.lower() not in {".tex", ".ltx"}:
                    continue
                text = (root / rel).read_text(errors="replace")
                for m in re.finditer(r"(?is).{0,1400}(?:B\s*[-−]\\?L|B\\!\\!\s*-\s*L|vector\s+B).{0,1400}", text):
                    context = m.group(0)
                    tokens = include_re.findall(context)
                    if tokens:
                        for token in tokens:
                            resolved = resolve_graphic(rel.parent, token, files)
                            graphics.append({
                                "tex": rel.as_posix(),
                                "token": token,
                                "resolved": [p.as_posix() for p in resolved],
                                "context_excerpt": re.sub(r"\s+", " ", context)[-1800:],
                            })
                    hits.append({"tex": rel.as_posix(), "context_excerpt": re.sub(r"\s+", " ", context)[-1800:]})

            resolved_paths = sorted({p for g in graphics for p in g["resolved"]})
            resolved_assets = []
            for posix in resolved_paths:
                rel = Path(posix)
                ext = rel.suffix.lower()
                data = (root / rel).read_bytes()
                resolved_assets.append({
                    "path": posix,
                    "extension": ext,
                    "size": len(data),
                    "sha256": sha256(data),
                    "asset_class": "VECTOR_CANDIDATE" if ext in VECTOR_EXTS else "RASTER" if ext in RASTER_EXTS else "OTHER",
                })

            if any(a["asset_class"] == "VECTOR_CANDIDATE" for a in resolved_assets):
                status = "PRIMARY_VECTOR_CANDIDATE_FOUND"
            elif resolved_assets and all(a["asset_class"] == "RASTER" for a in resolved_assets):
                status = "RASTER_ONLY_MATCHED_B_L_ASSET"
            elif hits:
                status = "B_L_SEMANTICS_FOUND_ASSET_UNRESOLVED"
            else:
                status = "B_L_SEMANTICS_NOT_FOUND"

            result = {
                "iteration": "0078-source-audit",
                "arxiv_id": ARXIV_ID,
                "source_url": used_url,
                "source_sha256": sha256(payload),
                "source_bytes": len(payload),
                "status": status,
                "matched_graphics": graphics,
                "resolved_assets": resolved_assets,
                "inventory": inventory,
                "guard": "Source/asset provenance audit only; no raster reading, curve digitization, semantic relabeling, likelihood substitution, or B-L scientific PASS is performed here.",
            }
    except Exception as exc:
        result = {
            "iteration": "0078-source-audit",
            "arxiv_id": ARXIV_ID,
            "status": "INFRASTRUCTURE_FAIL",
            "reason": repr(exc),
        }

    Path("deromeri_2603_source_audit_0078.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in result if k not in {"inventory", "matched_graphics"}}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
