#!/usr/bin/env python3
"""0105a6p: reconstruct exact official COHERENT Ar bytes from an untrusted carrier.

Transport only. Acceptance requires exact official size+MD5+SHA256 identities
previously established by 0105a3. Allowed transformations are prospectively
limited to identity, append LF, append CRLF.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path

BENCHMARK = "NMIR-V2-0105A6P"
PREREG_COMMIT = "2a48003cc83349820d40fc0c4076850a2a8efef3"
CARRIER_REPO = "Newtrinos-org/Newtrinos.jl"
CARRIER_COMMIT = "fa87689ddedae1929e33d66ad1f0efa1b7cce206"
BASE = "src/experiments/coherent/coherent_2020/lAr"

EXPECTED = {
    "datanobkgsub.txt": (15537, "4346ec521e91a7227b2e34ff8f3c269b", "dabf3d80f13959f4b94b77c9b56f7347a645105801e8cc177424e7ffcf7c7f66", "central"),
    "cevnspdf.txt": (18857, "5601234e03bc9bbd01066591629e72c0", "3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37", "central"),
    "brnpdf.txt": (17304, "7ccf0fdc0d0010d2c6570d620816e4df", "02664ce6a84eca8c6146b6502497bc5d8165df945da132193622334ff4ff826f", "central"),
    "delbrnpdf.txt": (16116, "5d57e91a773f03368d149dc5739b6a01", "ebccca6c1650b0ace71fdbaade7a80ea289a99ff3c120266ae6ecf0083df5c63", "central"),
    "bkgpdf.txt": (21190, "ccc2df245a004a644cd04317d07b35df", "36c89291dde3032a19ca7a8e64510d036d7b40c34b0805ce475a13ccfa739dd1", "central"),
    "LArParametersAnlA.yaml": (4906, "cc9f2c60ce0c17809453e0caad9c4a38", "a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e", "central"),
    "brnpdf+1sigBRNTimingMean.txt": (17304, "edf00a561d1f934d3e8bef2c401e8d91", "7f06099e1bba0d2e328555c61cb255bb290607a44202327d29eb3ae3e05c1cd5", "systematic"),
    "brnpdf-1sigBRNTimingMean.txt": (17295, "937c7c0f53aff94600ed7dfffb69de8b", "b5c1c8d0cb8b2319d093d38418da5ac2ccda59108755fb23e7f4a559cfe154f8", "systematic"),
    "brnpdf+1sigEnergy.txt": (17333, "2ad879a7302d8ca2e25ef1e192f88183", "fb6fdaf99c9941653d33e1a909d8000b81c1ee9bb8e8ad3bf31839561faf6661", "systematic"),
    "brnpdf-1sigEnergy.txt": (17302, "ea7dd87225a19fe75f28d3dec00e7441", "20bcad29e716f3fb0f1e9eeb8ffb049b4b3d8b3b3a150800b9c8711e2b177be6", "systematic"),
    "brnpdfBRNTimingWidthSyst.txt": (17375, "5050ef987d122fae43eeef27b86ec1b2", "304dba1553989d7c0cd3f745df9731a5306ec07ecc1044c20efbe2952707b270", "systematic"),
    "cevnspdf+1sigF90.txt": (18837, "0237a293b243b371459bcb19bc2fa116", "308f78e19b7fb3e54399dc29c207bd2a89b91825df5309d48068a3495e1c92e2", "systematic"),
    "cevnspdf-1sigF90.txt": (18870, "b9bd9500b0c84b851f0d38e4869cad0f", "b4e8071f87aa22a562e0c00654a0989915251acf2c7e569068b9b78c3ae5ac35", "systematic"),
    "cevnspdfCEvNSTimingMeanSyst.txt": (18877, "24455c1cd2acf4f359cf0942deb7b29b", "3170dafd4cf44df35bde0795e1245606d8144c05f3e50f015648c57bcdba97f5", "systematic"),
}

TRANSFORMS = (
    ("identity", lambda b: b),
    ("append_LF", lambda b: b + b"\n"),
    ("append_CRLF", lambda b: b + b"\r\n"),
)


def md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def matches(data: bytes, expected: tuple[int, str, str, str]) -> bool:
    size, m5, s256, _ = expected
    return len(data) == size and md5(data) == m5 and sha256(data) == s256


def reconstruct(raw: bytes, expected: tuple[int, str, str, str]):
    hits = []
    for name, fn in TRANSFORMS:
        candidate = fn(raw)
        if matches(candidate, expected):
            hits.append((name, candidate))
    if len(hits) == 1:
        return hits[0]
    return None


def raw_url(filename: str) -> str:
    path = "/".join(urllib.parse.quote(part, safe="") for part in f"{BASE}/{filename}".split("/"))
    return f"https://raw.githubusercontent.com/{CARRIER_REPO}/{CARRIER_COMMIT}/{path}"


def fetch(filename: str) -> bytes:
    req = urllib.request.Request(raw_url(filename), headers={"User-Agent": "NMIR-0105a6p-byte-transport"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def audit(output_dir: Path, git_sha: str) -> dict:
    recovered_dir = output_dir / "reconstructed_exact_official_bytes"
    recovered_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for filename, exp in EXPECTED.items():
        size, m5, s256, group = exp
        rec = {
            "filename": filename,
            "group": group,
            "official_expected": {"size_bytes": size, "md5": m5, "sha256": s256},
            "carrier_url": raw_url(filename),
        }
        try:
            raw = fetch(filename)
            rec["carrier_observed"] = {"size_bytes": len(raw), "md5": md5(raw), "sha256": sha256(raw)}
            hit = reconstruct(raw, exp)
            if hit is None:
                rec["status"] = "REJECTED_NO_UNIQUE_EXACT_OFFICIAL_MATCH"
                rec["selected_reconstruction"] = None
            else:
                transform, exact = hit
                rec["status"] = "ACCEPTED_AS_EXACT_OFFICIAL_BYTES"
                rec["selected_reconstruction"] = transform
                rec["reconstructed"] = {"size_bytes": len(exact), "md5": md5(exact), "sha256": sha256(exact)}
                (recovered_dir / filename).write_bytes(exact)
        except Exception as exc:
            rec["status"] = "REJECTED_CARRIER_TRANSPORT_ERROR"
            rec["error_type"] = type(exc).__name__
        records.append(rec)

    central = [r for r in records if r["group"] == "central"]
    syst = [r for r in records if r["group"] == "systematic"]
    central_ready = all(r["status"] == "ACCEPTED_AS_EXACT_OFFICIAL_BYTES" for r in central)
    systematics_ready = all(r["status"] == "ACCEPTED_AS_EXACT_OFFICIAL_BYTES" for r in syst)
    if central_ready and systematics_ready:
        classification = "PASS_0105A6P_ALL_REQUIRED_ARGON_BYTES_RECONSTRUCTED_NONDISCOVERY"
    elif central_ready:
        classification = "PASS_0105A6P_CENTRAL_BYTES_RECONSTRUCTED_SYSTEMATICS_INCOMPLETE_NONDISCOVERY"
    else:
        classification = "BLOCKED_0105A6P_CENTRAL_EXACT_BYTE_RECONSTRUCTION_INCOMPLETE"

    return {
        "benchmark": BENCHMARK,
        "classification": classification,
        "preregistration_commit": PREREG_COMMIT,
        "git_sha": git_sha,
        "carrier": {"repository": CARRIER_REPO, "commit": CARRIER_COMMIT, "scientific_authority": False},
        "allowed_reconstructions": [name for name, _ in TRANSFORMS],
        "files": records,
        "accepted_count": sum(r["status"] == "ACCEPTED_AS_EXACT_OFFICIAL_BYTES" for r in records),
        "required_count": len(records),
        "central_ready": central_ready,
        "systematics_ready": systematics_ready,
        "a6o_stage0_central_input_permission_percent": 100 if central_ready else 0,
        "observed_bsm_residual_permission_percent": 0,
        "likelihood_evaluation_performed": False,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--git-sha", required=True)
    ns = ap.parse_args()
    outdir = Path(ns.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    result = audit(outdir, ns.git_sha)
    result_path = outdir / "manifest.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "benchmark": BENCHMARK,
        "classification": result["classification"],
        "accepted_count": result["accepted_count"],
        "required_count": result["required_count"],
        "central_ready": result["central_ready"],
        "systematics_ready": result["systematics_ready"],
        "selected_reconstructions": {r["filename"]: r.get("selected_reconstruction") for r in result["files"]},
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
