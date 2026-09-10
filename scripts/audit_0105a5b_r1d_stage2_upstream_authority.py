#!/usr/bin/env python3
"""0105a5b R1d stage-2 upstream authority collector.

Authority-only acquisition under the frozen R1d preregistration.  No
oscillated expectation, likelihood, nuisance fit, residual or BSM quantity is
computed.  Sources are restricted to the exact upstream papers explicitly
cited by the frozen IceCube analysis.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import re
import tarfile
import urllib.request
from pathlib import Path

SOURCES = {
    "barr_2006": "https://export.arxiv.org/e-print/astro-ph/0611266v1",
    "sibyll_mceq_2019": "https://export.arxiv.org/e-print/1806.04140v2",
    "csms_2011": "https://export.arxiv.org/e-print/1106.3723v1",
}
TOKENS = [
    "W", "X", "Y", "Z", "K+", "K-", "kaon", "meson", "antimeson",
    "MCEq", "Sibyll", "CSMS", "inelasticity", "GENIE", "GRV98",
    "BarrWP", "BarrWM", "BarrYP", "BarrYM", "BarrZP", "BarrZM",
]


def fetch(url: str, timeout: int = 300) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-v2-0105a5b-r1d-stage2"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def unpack_text(payload: bytes) -> str:
    bio = io.BytesIO(payload)
    for mode in ("r:gz", "r:"):
        try:
            bio.seek(0)
            with tarfile.open(fileobj=bio, mode=mode) as tf:
                chunks = []
                for member in tf.getmembers():
                    if not member.isfile() or Path(member.name).suffix.lower() not in {".tex", ".bib", ".txt"}:
                        continue
                    f = tf.extractfile(member)
                    if f:
                        chunks.append(f.read().decode("utf-8", errors="replace"))
                return "\n".join(chunks)
        except tarfile.TarError:
            pass
    try:
        return gzip.decompress(payload).decode("utf-8", errors="replace")
    except Exception:
        return payload.decode("utf-8", errors="replace")


def contexts(text: str, token: str, radius: int = 160) -> list[str]:
    out = []
    flags = re.IGNORECASE
    # Exact release-internal names are literal; generic scientific terms are word-ish.
    pat = re.escape(token)
    for m in re.finditer(pat, text, flags):
        lo, hi = max(0, m.start() - radius), min(len(text), m.end() + radius)
        out.append(text[lo:hi].replace("\x00", ""))
        if len(out) >= 12:
            break
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--raw-dir", required=True)
    args = ap.parse_args()
    raw_dir = Path(args.raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "benchmark": "NMIR-V2-0105A5B-R1D-STAGE2-UPSTREAM-AUTHORITY",
        "status": "EVIDENCE_BUNDLE_ONLY_0105A5B_R1D_STAGE2_UNCLASSIFIED",
        "authority_scope": "only exact upstream papers explicitly cited by IceCube 2304.12236",
        "observed_bsm_residual_permission_percent": 0,
        "oscillated_expectation_computed": False,
        "likelihood_computed": False,
        "nuisance_fit_executed": False,
        "observed_minus_null_residual_computed": False,
        "sources": {},
    }

    try:
        for name, url in SOURCES.items():
            payload = fetch(url)
            p = raw_dir / f"{name}.source"
            p.write_bytes(payload)
            text = unpack_text(payload)
            result["sources"][name] = {
                "url": url,
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
                "token_contexts": {tok: contexts(text, tok) for tok in TOKENS},
            }
    except Exception as exc:
        result["status"] = "INFRASTRUCTURE_FAIL_0105A5B_R1D"
        result["reason"] = str(exc)
        Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
        print(result["status"])
        return 2

    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(result["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
