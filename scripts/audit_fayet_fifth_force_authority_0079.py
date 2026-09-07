#!/usr/bin/env python3
"""NMIR 0079: hash-pin and inspect primary Fayet/MICROSCOPE source archives.

This script is an authority audit only. It does not convert a source limit to g_BL
and does not extrapolate a long-range result to finite mediator mass.
"""
from __future__ import annotations

import gzip
import hashlib
import io
import json
import re
import tarfile
import urllib.request
from pathlib import Path

SOURCES = [
    {
        "arxiv": "1809.04991v2",
        "url": "https://export.arxiv.org/e-print/1809.04991v2",
        "doi": "10.1103/PhysRevD.99.055043",
    },
    {
        "arxiv": "1712.00856v2",
        "url": "https://export.arxiv.org/e-print/1712.00856v2",
        "doi": "10.1103/PhysRevD.97.055039",
    },
]

KEY_PATTERNS = {
    "epsilon_bl": re.compile(r"epsilon.{0,35}(?:B.?-?.?L|B.?\\!-?L)", re.I | re.S),
    "alpha_g": re.compile(r"(?:bar\s*\\?alpha|\\?alpha).{0,20}_?g", re.I | re.S),
    "long_range": re.compile(r"long[ -]?range", re.I),
    "yukawa": re.compile(r"Yukawa|e\^\{-r|exp\s*\(-?r|lambda", re.I),
    "sigma": re.compile(r"2\s*\\?sigma|two\s+standard\s+deviation", re.I),
    "b_minus_l": re.compile(r"B\s*(?:\\!?-|-|\\minus)\s*L|B-L", re.I),
}

TEXT_SUFFIXES = {".tex", ".txt", ".sty", ".bbl", ".bib"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def decode_text(data: bytes) -> str:
    return data.decode("utf-8", errors="replace")


def extract_text_members(data: bytes) -> dict[str, str]:
    """Return text members from tar/tar.gz/gzip/plain arXiv source bytes."""
    out: dict[str, str] = {}
    bio = io.BytesIO(data)
    try:
        with tarfile.open(fileobj=bio, mode="r:*") as tf:
            for member in tf.getmembers():
                if not member.isfile():
                    continue
                suffix = Path(member.name).suffix.lower()
                if suffix not in TEXT_SUFFIXES:
                    continue
                f = tf.extractfile(member)
                if f is not None:
                    out[member.name] = decode_text(f.read())
            if out:
                return out
    except tarfile.ReadError:
        pass

    try:
        raw = gzip.decompress(data)
        return {"source.tex": decode_text(raw)}
    except (gzip.BadGzipFile, OSError):
        return {"source.tex": decode_text(data)}


def contexts(text: str, pattern: re.Pattern[str], radius: int = 320, limit: int = 8) -> list[str]:
    hits = []
    for m in pattern.finditer(text):
        lo = max(0, m.start() - radius)
        hi = min(len(text), m.end() + radius)
        snippet = re.sub(r"\s+", " ", text[lo:hi]).strip()
        hits.append(snippet)
        if len(hits) >= limit:
            break
    return hits


def audit_source(meta: dict[str, str]) -> dict:
    req = urllib.request.Request(meta["url"], headers={"User-Agent": "NMIR-0079/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    members = extract_text_members(data)
    combined = "\n\n".join(f"### {name}\n{text}" for name, text in sorted(members.items()))
    pattern_hits = {name: contexts(combined, pat) for name, pat in KEY_PATTERNS.items()}
    return {
        **meta,
        "byte_size": len(data),
        "sha256": sha256(data),
        "text_members": sorted(members),
        "text_member_count": len(members),
        "pattern_hit_counts": {k: len(v) for k, v in pattern_hits.items()},
        "contexts": pattern_hits,
    }


def main() -> None:
    results = [audit_source(meta) for meta in SOURCES]
    ledger = {
        "iteration": "0079",
        "scope": "primary authority audit only; no g_BL conversion or finite-mass extrapolation",
        "sources": results,
        "classification": "AWAITING_PRIMARY_TEXT_INSPECTION",
        "guards": [
            "no numerical g_BL conversion in 0079",
            "no long-range-to-finite-mass extrapolation",
            "no raster/manual contour reading",
        ],
    }
    out = Path("fayet_fifth_force_authority_0079.json")
    out.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "iteration": "0079",
        "sources": [
            {
                "arxiv": s["arxiv"],
                "byte_size": s["byte_size"],
                "sha256": s["sha256"],
                "pattern_hit_counts": s["pattern_hit_counts"],
            }
            for s in results
        ],
        "output_sha256": sha256(out.read_bytes()),
    }, indent=2))


if __name__ == "__main__":
    main()
