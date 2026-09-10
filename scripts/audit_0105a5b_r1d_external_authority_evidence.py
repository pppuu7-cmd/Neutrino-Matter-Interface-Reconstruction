#!/usr/bin/env python3
"""0105a5b R1d authority-evidence collector.

Collects only release/publication authority evidence for Barr×6 and DIS-CSMS.
No oscillated expectation, likelihood, nuisance fit, residual, BSM quantity or
significance is computed here.
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

B4RITM_NOTEBOOK_ID = 11674675
B4RITM_README_ID = 11674676
B4RITM_NOTEBOOK_MD5 = "fd9ac548e6a6f136efb6c61058cc822f"
B4RITM_README_SHA256 = "0f8e7bbc6059d18376843370e36e98a0cfa69fbc4bd767df694c6d65f861149f"
ARXIV_ID = "2304.12236"
DATA_API = "https://dataverse.harvard.edu/api/access/datafile"
ARXIV_SOURCE_URLS = [
    "https://export.arxiv.org/e-print/2304.12236",
    "https://arxiv.org/e-print/2304.12236",
]
TERMS = ["BarrWP", "BarrWM", "BarrYP", "BarrYM", "BarrZP", "BarrZM", "MCEq", "CSMS", "DIS"]


def fetch(url: str, timeout: int = 300) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-v2-0105a5b-r1d"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def contexts(text: str, term: str, radius: int = 2) -> list[str]:
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines):
        if term.lower() in line.lower():
            lo, hi = max(0, i-radius), min(len(lines), i+radius+1)
            out.append("\n".join(lines[lo:hi])[:5000])
    return out[:40]


def notebook_text(payload: bytes) -> str:
    nb = json.loads(payload.decode("utf-8-sig"))
    chunks = []
    for cell in nb.get("cells", []):
        src = cell.get("source", [])
        chunks.append("".join(src) if isinstance(src, list) else str(src))
    return "\n".join(chunks)


def unpack_arxiv_text(payload: bytes, raw_dir: Path) -> tuple[str, list[dict]]:
    entries = []
    texts = []
    bio = io.BytesIO(payload)
    opened = None
    for mode in ("r:gz", "r:"):
        try:
            bio.seek(0)
            opened = tarfile.open(fileobj=bio, mode=mode)
            break
        except tarfile.TarError:
            opened = None
    if opened is None:
        # Some arXiv endpoints may return a single gzipped TeX stream.
        try:
            text = gzip.decompress(payload).decode("utf-8", errors="replace")
            p = raw_dir / "arxiv_source_single.tex"
            p.write_text(text, encoding="utf-8")
            return text, [{"name": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}]
        except Exception as exc:
            raise RuntimeError(f"unable to decode arXiv source archive: {exc}")
    with opened:
        for member in opened.getmembers():
            if not member.isfile():
                continue
            suffix = Path(member.name).suffix.lower()
            if suffix not in {".tex", ".bib", ".txt", ".sty"}:
                continue
            f = opened.extractfile(member)
            if f is None:
                continue
            data = f.read()
            safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", member.name)
            p = raw_dir / f"arxiv_{safe}"
            p.write_bytes(data)
            entries.append({"name": member.name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
            texts.append(data.decode("utf-8", errors="replace"))
    return "\n".join(texts), entries


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--raw-dir", required=True)
    args = ap.parse_args()
    out = Path(args.output)
    raw = Path(args.raw_dir)
    raw.mkdir(parents=True, exist_ok=True)

    try:
        notebook = fetch(f"{DATA_API}/{B4RITM_NOTEBOOK_ID}?format=original")
        readme = fetch(f"{DATA_API}/{B4RITM_README_ID}?format=original")
        if hashlib.md5(notebook).hexdigest() != B4RITM_NOTEBOOK_MD5:
            raise RuntimeError("B4RITM example.ipynb provider MD5 mismatch")
        if hashlib.sha256(readme).hexdigest() != B4RITM_README_SHA256:
            raise RuntimeError("B4RITM readme SHA256 mismatch")
        (raw / "b4ritm_example.ipynb").write_bytes(notebook)
        (raw / "b4ritm_readme.md").write_bytes(readme)

        arxiv = None
        arxiv_url = None
        errors = []
        for url in ARXIV_SOURCE_URLS:
            try:
                arxiv = fetch(url)
                arxiv_url = url
                break
            except Exception as exc:
                errors.append(f"{url}: {exc}")
        if arxiv is None:
            raise RuntimeError("arXiv source transport failed: " + " | ".join(errors))
        (raw / "arxiv_2304.12236_source.bin").write_bytes(arxiv)
        arxiv_text, arxiv_entries = unpack_arxiv_text(arxiv, raw)
        nb_text = notebook_text(notebook)
        readme_text = readme.decode("utf-8-sig")
    except Exception as exc:
        result = {
            "benchmark": "NMIR-V2-0105A5B-R1D-EVIDENCE",
            "status": "INFRASTRUCTURE_FAIL_0105A5B_R1D",
            "reason": str(exc),
            "observed_bsm_residual_permission_percent": 0,
        }
        out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
        print(result["status"])
        return 2

    evidence = {}
    for term in TERMS:
        evidence[term] = {
            "b4ritm_notebook": contexts(nb_text, term),
            "b4ritm_readme": contexts(readme_text, term),
            "icecube_arxiv_source": contexts(arxiv_text, term),
        }

    result = {
        "benchmark": "NMIR-V2-0105A5B-R1D-EVIDENCE",
        "status": "EVIDENCE_BUNDLE_ONLY_0105A5B_R1D_UNCLASSIFIED",
        "b4ritm_doi": "10.7910/DVN/B4RITM",
        "b4ritm_release": "1.0",
        "forbidden_sterile_doi": "10.7910/DVN/QKL28Z",
        "publication_doi": "10.1103/PhysRevD.108.012014",
        "arxiv_id": ARXIV_ID,
        "arxiv_source_url_used": arxiv_url,
        "b4ritm_notebook_md5": hashlib.md5(notebook).hexdigest(),
        "b4ritm_notebook_sha256": hashlib.sha256(notebook).hexdigest(),
        "b4ritm_readme_sha256": hashlib.sha256(readme).hexdigest(),
        "arxiv_source_sha256": hashlib.sha256(arxiv).hexdigest(),
        "arxiv_text_entry_count": len(arxiv_entries),
        "arxiv_text_entries": arxiv_entries,
        "evidence": evidence,
        "oscillated_expectation_computed": False,
        "likelihood_computed": False,
        "nuisance_fit_executed": False,
        "observed_minus_null_residual_computed": False,
        "bsm_quantity_computed": False,
        "observed_bsm_residual_permission_percent": 0,
    }
    out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(result["status"])
    print(f"notebook_sha256={result['b4ritm_notebook_sha256']}")
    print(f"arxiv_source_sha256={result['arxiv_source_sha256']}")
    for term in TERMS:
        n = sum(len(v) for v in evidence[term].values())
        print(f"{term}_context_blocks={n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
