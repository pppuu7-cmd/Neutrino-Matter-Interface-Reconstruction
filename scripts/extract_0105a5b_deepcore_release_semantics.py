#!/usr/bin/env python3
"""NMIR v2 0105a5b R1: verify and extract B4RITM release documentation.

Only the byte-locked readme and example notebook are consumed. Both assets are
fully hashed before either is decoded/parsed. No event CSV is opened here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import socket
import time
import urllib.error
import urllib.request

DOCS = {
    "readme.md": {
        "file_id": 11674676,
        "size": 7141,
        "md5": "848778cd0b870da83a6b925b89ba3d3d",
        "sha256": "0f8e7bbc6059d18376843370e36e98a0cfa69fbc4bd767df694c6d65f861149f",
    },
    "example.ipynb": {
        "file_id": 11674675,
        "size": 231264,
        "md5": "fd9ac548e6a6f136efb6c61058cc822f",
        "sha256": "900acac6e74cced45e0b894017340b7aa0a64ccb615365b865cc7b4ae87be1a3",
    },
}
TRANSIENT_HTTP = {429, 500, 502, 503, 504}


def fetch(url: str, attempts: int = 4, timeout: int = 120) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 NMIR/0105a5b-r1"})
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in TRANSIENT_HTTP:
                raise RuntimeError(f"BLOCKED_0105A5B_R1_HTTP_{exc.code} url={url}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last = exc
        if attempt < attempts:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"BLOCKED_0105A5B_R1_TRANSPORT attempts={attempts} url={url}") from last


def verify_payload(name: str, payload: bytes) -> dict:
    exp = DOCS[name]
    actual_md5 = hashlib.md5(payload).hexdigest()
    actual_sha = hashlib.sha256(payload).hexdigest()
    return {
        "name": name,
        "file_id": exp["file_id"],
        "expected_size": exp["size"],
        "actual_size": len(payload),
        "size_match": len(payload) == exp["size"],
        "expected_md5": exp["md5"],
        "actual_md5": actual_md5,
        "md5_match": actual_md5 == exp["md5"],
        "expected_sha256": exp["sha256"],
        "actual_sha256": actual_sha,
        "sha256_match": actual_sha == exp["sha256"],
    }


def notebook_summary(nb: dict) -> dict:
    cells = nb.get("cells") or []
    code = []
    markdown = []
    for cell in cells:
        src = cell.get("source") or []
        text = "".join(src) if isinstance(src, list) else str(src)
        if cell.get("cell_type") == "code":
            code.append(text)
        elif cell.get("cell_type") == "markdown":
            markdown.append(text)
    joined_code = "\n\n# ---- notebook cell ----\n\n".join(code)
    joined_md = "\n\n---\n\n".join(markdown)
    keywords = [
        "theta23", "dm2", "osc", "prem", "chi", "systematic", "hypersurface",
        "weight", "nu_mu", "numu", "nue", "nutau", "atmospheric", "pid",
        "energy", "zenith", "minimize", "scipy", "nuSQuIDS", "prob3",
    ]
    lower = (joined_code + "\n" + joined_md).lower()
    return {
        "cell_count": len(cells),
        "code_cell_count": len(code),
        "markdown_cell_count": len(markdown),
        "code_characters": len(joined_code),
        "markdown_characters": len(joined_md),
        "keyword_presence": {k: (k.lower() in lower) for k in keywords},
        "code": joined_code,
        "markdown": joined_md,
    }


def build(fetcher=fetch) -> tuple[dict, dict[str, bytes]]:
    raw = {}
    checks = []
    # R0: retrieve and verify every documentation asset before parsing either.
    for name, exp in DOCS.items():
        url = f"https://dataverse.harvard.edu/api/access/datafile/{exp['file_id']}"
        payload = fetcher(url)
        raw[name] = payload
        checks.append(verify_payload(name, payload))

    byte_gate = all(c["size_match"] and c["md5_match"] and c["sha256_match"] for c in checks)
    common = {
        "benchmark": "NMIR-V2-0105A5B-R1-DOCS",
        "dataset_doi": "10.7910/DVN/B4RITM",
        "checks": checks,
        "all_doc_bytes_match_0105a4d": byte_gate,
        "event_csv_opened": False,
        "event_rows_parsed": False,
        "observed_residual_execution_allowed": False,
        "bsm_interpretation_allowed": False,
    }
    if not byte_gate:
        return ({**common, "status": "BLOCKED_0105A5B_BYTE_AUTHORITY_MISMATCH", "parsed": False}, {})

    readme = raw["readme.md"].decode("utf-8")
    nb = json.loads(raw["example.ipynb"].decode("utf-8"))
    nbs = notebook_summary(nb)
    result = {
        **common,
        "status": "PASS_0105A5B_R1_VERIFIED_DOC_EXTRACTION_NONDISCOVERY",
        "parsed": True,
        "readme_characters": len(readme),
        "notebook": {k: v for k, v in nbs.items() if k not in {"code", "markdown"}},
    }
    outputs = {
        "verified_readme.md": readme.encode("utf-8"),
        "verified_example_code.py": nbs["code"].encode("utf-8"),
        "verified_example_markdown.md": nbs["markdown"].encode("utf-8"),
    }
    return result, outputs


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a5b_r1"))
    args = p.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result, outputs = build()
    for name, payload in outputs.items():
        (args.output_dir / name).write_bytes(payload)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    (args.output_dir / "release_doc_extraction_manifest.json").write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode()).hexdigest()
    (args.output_dir / "manifest_sha256.txt").write_text(digest + "\n", encoding="utf-8")
    print(text, end="")
    print(f"manifest_sha256={digest}")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
