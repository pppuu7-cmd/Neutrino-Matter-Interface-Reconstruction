#!/usr/bin/env python3
"""Iteration 0072: auditable Wagner et al. arXiv source-asset materialization.

Downloads the primary arXiv source archive for arXiv:1207.2442 and records
immutable transport/archive hashes plus candidate Figure-6 assets.  This script
DOES NOT digitize raster figures and DOES NOT classify any B-L contour.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import tarfile
import urllib.error
import urllib.request
from pathlib import PurePosixPath

URLS = (
    "https://arxiv.org/e-print/1207.2442",
    "https://export.arxiv.org/e-print/1207.2442",
)
VECTOR_EXT = {".eps", ".epsi", ".pdf", ".ps", ".svg"}
RASTER_EXT = {".png", ".jpg", ".jpeg", ".gif", ".tif", ".tiff"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download() -> tuple[bytes, dict]:
    errors = []
    for url in URLS:
        req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0072-source-audit/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                if not body:
                    raise RuntimeError("empty response")
                return body, {
                    "requested_url": url,
                    "final_url": r.geturl(),
                    "http_status": getattr(r, "status", None),
                    "content_type": r.headers.get("Content-Type"),
                    "etag": r.headers.get("ETag"),
                    "last_modified": r.headers.get("Last-Modified"),
                }
        except Exception as exc:  # preserve all route failures in artifact
            errors.append({"url": url, "error": repr(exc)})
    raise RuntimeError(json.dumps({"all_download_routes_failed": errors}, sort_keys=True))


def open_tar(body: bytes) -> tuple[tarfile.TarFile, str]:
    # arXiv e-print may be gzip-compressed tar or uncompressed tar.
    for mode, label in (("r:gz", "tar.gz"), ("r:", "tar")):
        try:
            return tarfile.open(fileobj=io.BytesIO(body), mode=mode), label
        except tarfile.TarError:
            pass
    # Occasionally a single gzipped TeX source is returned; classify explicitly.
    try:
        raw = gzip.decompress(body)
        if b"\\document" in raw or b"\\begin{" in raw:
            raise RuntimeError("primary source is a single gzipped TeX file; no archive assets to inspect")
    except (OSError, EOFError):
        pass
    raise RuntimeError("downloaded primary source is not a readable tar/tar.gz archive")


def classify_member(name: str) -> dict:
    p = PurePosixPath(name)
    low = p.name.lower()
    ext = p.suffix.lower()
    return {
        "name": name,
        "size": None,
        "extension": ext,
        "mentions_figure6": any(k in low for k in ("figure6", "fig6", "figure_6", "fig_6")),
        "mentions_wep": "wep" in low,
        "is_vector_candidate": ext in VECTOR_EXT,
        "is_raster": ext in RASTER_EXT,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    result = {
        "iteration": "0072",
        "source": "Wagner et al., arXiv:1207.2442v1",
        "purpose": "primary source-asset audit only; no raster digitization",
        "classification": "INFRASTRUCTURE_FAIL_UNSET",
    }
    try:
        body, transport = download()
        result["transport"] = transport
        result["download_bytes"] = len(body)
        result["download_sha256"] = sha256(body)
        tf, archive_format = open_tar(body)
        result["archive_format"] = archive_format
        members = []
        for m in tf.getmembers():
            if not m.isfile():
                continue
            entry = classify_member(m.name)
            entry["size"] = m.size
            try:
                f = tf.extractfile(m)
                if f is not None:
                    entry["sha256"] = sha256(f.read())
            except Exception as exc:
                entry["hash_error"] = repr(exc)
            members.append(entry)
        tf.close()
        result["file_count"] = len(members)
        result["members"] = members
        fig6 = [x for x in members if x["mentions_figure6"]]
        wep_assets = [x for x in members if x["mentions_wep"] and (x["is_vector_candidate"] or x["is_raster"])]
        result["figure6_named_assets"] = fig6
        result["wep_named_graphics"] = wep_assets
        vector = [x for x in fig6 if x["is_vector_candidate"]]
        raster = [x for x in fig6 if x["is_raster"]]
        result["vector_figure6_candidates"] = vector
        result["raster_figure6_candidates"] = raster
        if vector:
            result["classification"] = "PRIMARY_VECTOR_ASSET_FOUND_REQUIRES_CALIBRATION"
        elif raster:
            result["classification"] = "PRIMARY_FIGURE6_RASTER_ONLY_IN_SOURCE_ARCHIVE"
        else:
            result["classification"] = "PRIMARY_FIGURE6_ASSET_NOT_IDENTIFIED_BY_FILENAME"
    except Exception as exc:
        result["classification"] = "INFRASTRUCTURE_FAIL"
        result["error"] = repr(exc)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(result, sort_keys=True))
    return 2 if result["classification"] == "INFRASTRUCTURE_FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
