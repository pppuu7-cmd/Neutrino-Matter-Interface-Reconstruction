#!/usr/bin/env python3
"""0105a6j source-provenance/byte-lock audit. No thesis semantic analysis."""
from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import re
import tarfile
import time
import urllib.request
from pathlib import Path

COHERENT_THESES = "https://coherent.ornl.gov/theses/"
IU_ITEM = "https://scholarworks.iu.edu/dspace/items/ae71e100-a414-4756-bf9e-be4808f675e5"
IU_PDF = "https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download"
MEASUREMENT = "https://export.arxiv.org/e-print/2003.10630v7"
TITLE = "First Detection of Coherent Elastic Neutrino-Nucleus Scattering on an Argon Target"
DOI = "10.5967/3wza-6w73"
PREREG_COMMIT = "b53dec91a3b43b31d64714a294aa939a793216b3"


def fetch(url: str, attempts: int = 4, timeout: int = 60) -> tuple[bytes, str, str]:
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-authority-audit/0105a6j"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.geturl(), r.headers.get("Content-Type", "")
        except Exception as exc:
            last = exc
            if i + 1 < attempts:
                time.sleep(2 ** i)
    raise RuntimeError(f"fetch failed: {type(last).__name__}: {last}")


def visible_text(raw: bytes) -> str:
    text = raw.decode("utf-8", errors="replace")
    text = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def normalized(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def source_text(raw: bytes) -> str:
    chunks: list[str] = []
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
            for m in tf.getmembers():
                if m.isfile() and m.name.lower().endswith((".tex", ".txt", ".bbl")):
                    f = tf.extractfile(m)
                    if f:
                        chunks.append(f.read().decode("utf-8", errors="replace"))
    except tarfile.TarError:
        chunks.append(raw.decode("utf-8", errors="replace"))
    return "\n".join(chunks)


def classify(coherent_text: str, iu_text: str, measurement_text: str, pdf: bytes, pdf_url: str, pdf_type: str) -> dict:
    c = normalized(coherent_text)
    i = normalized(iu_text)
    m = normalized(measurement_text)
    title_n = normalized(TITLE)
    gates = {
        "P1_coherent_index_identity": all(x in c for x in ["jacob c zettlemoyer", "10 5967 3wza 6w73"]) and title_n in c,
        "P2_institutional_custody": all(x in i for x in ["zettlemoyer jacob c", "2020", "indiana university", "10 5967 3wza 6w73"]) and title_n in i,
        "P3_collaboration_author_linkage": "j zettlemoyer" in m or "j zettlemoyer" in normalized(measurement_text.replace(".", " ")),
        "P4_pdf_byte_acquisition": pdf.startswith(b"%PDF") and len(pdf) > 30_000_000,
        "P5_custody_consistency": "scholarworks.iu.edu" in pdf_url and ("pdf" in pdf_type.lower() or pdf.startswith(b"%PDF")),
    }
    passed = all(gates.values())
    return {
        "benchmark": "NMIR-V2-0105A6J",
        "preregistration_commit": PREREG_COMMIT,
        "gates": gates,
        "all_provenance_gates_pass": passed,
        "classification": (
            "PASS_0105A6J_ZETTLEMOYER_THESIS_PROVENANCE_BYTE_LOCK_NONDISCOVERY"
            if passed else
            "BLOCKED_0105A6J_ZETTLEMOYER_THESIS_PROVENANCE_OR_BYTE_AUTHORITY_INCOMPLETE"
        ),
        "authority_ceiling": {
            "collaboration_release_authority": False,
            "secondary_collaboration_author_source": True if passed else False,
            "sm_null_reproduction_permission_percent": 0,
            "observed_bsm_residual_permission_percent": 0,
        },
        "pdf": {
            "resolved_url": pdf_url,
            "content_type": pdf_type,
            "bytes": len(pdf),
            "sha256": hashlib.sha256(pdf).hexdigest(),
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", default="unknown")
    ns = ap.parse_args()
    out = {
        "benchmark": "NMIR-V2-0105A6J",
        "git_sha": ns.git_sha,
        "authority_ceiling": {"collaboration_release_authority": False, "sm_null_reproduction_permission_percent": 0, "observed_bsm_residual_permission_percent": 0},
    }
    try:
        craw, curl, ctype = fetch(COHERENT_THESES)
        iraw, iurl, itype = fetch(IU_ITEM)
        mraw, murl, mtype = fetch(MEASUREMENT)
        praw, purl, ptype = fetch(IU_PDF, timeout=120)
        out.update(classify(visible_text(craw), visible_text(iraw), source_text(mraw), praw, purl, ptype))
        out["git_sha"] = ns.git_sha
        out["source_receipts"] = {
            "coherent_theses_page": {"requested_url": COHERENT_THESES, "resolved_url": curl, "content_type": ctype, "bytes": len(craw), "sha256": hashlib.sha256(craw).hexdigest()},
            "iu_item_page": {"requested_url": IU_ITEM, "resolved_url": iurl, "content_type": itype, "bytes": len(iraw), "sha256": hashlib.sha256(iraw).hexdigest()},
            "measurement_eprint": {"requested_url": MEASUREMENT, "resolved_url": murl, "content_type": mtype, "bytes": len(mraw), "sha256": hashlib.sha256(mraw).hexdigest()},
        }
    except Exception as exc:
        out.update({
            "classification": "BLOCKED_0105A6J_SOURCE_TRANSPORT_OR_FORMAT",
            "error": f"{type(exc).__name__}: {exc}",
            "all_provenance_gates_pass": False,
        })
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
