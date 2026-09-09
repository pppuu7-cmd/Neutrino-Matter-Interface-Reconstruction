#!/usr/bin/env python3
"""Pin all preregistered COHERENT CEvNS event-release bytes for NMIR 0105a3.

Downloaded files are treated as opaque bytes only: provider MD5 is verified and
SHA256/size are recorded. No event content is parsed or analyzed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import socket
import time
import urllib.error
import urllib.parse
import urllib.request

RELEASES = {
    "csi": {
        "record_id": "1228631",
        "doi": "10.5281/zenodo.1228631",
        "version": "1.0",
        "files": {
            "arrivalTimePDF_delayedNeutrinos.txt": "fd5d053696ba30164cd3711b38b8eaa5",
            "arrivalTimePDF_promptNeutrinos.txt": "d5009119454ec8ed3b5a31bf8d1e82e5",
            "arrivalTimePDF_promptNeutrons.txt": "400d86635b180b52e51b429ec5fe5965",
            "coherent_parameters.yaml": "66b907201dcd7cccfb9af0a1b35893a7",
            "coherentCollaboration_dataReleaseCompanion_april2018.pdf": "0cb94c4e8fa3c03a1d4bb0cd8599d318",
            "data_anticoincidence_beamOff.txt": "c6371164b444b9357e004299c591546a",
            "data_anticoincidence_beamOn.txt": "4067e588ff44d0a210655eacb987e2d7",
            "data_coincidence_beamOff.txt": "529e822eb3a144170cd03d9d9628b4fa",
            "data_coincidence_beamOn.txt": "23f399e605e94401a611c23c37090a31",
            "promptPDF.txt": "faf1a4b6b27cd9fa685e17ddd38a00cf",
            "qfData_chicago.txt": "b9dec892fb9d6c7502ed03446ddd0305",
            "qfData_tunl.txt": "93b016293c04c741c3088bced0a5c015",
            "README": "40cbf0bcdb370530526b7e293480ab9d",
        },
    },
    "ar": {
        "record_id": "3903810",
        "doi": "10.5281/zenodo.3903810",
        "version": "1.0",
        "files": {
            "bkgpdf.txt": "ccc2df245a004a644cd04317d07b35df",
            "brnpdf+1sigBRNTimingMean.txt": "edf00a561d1f934d3e8bef2c401e8d91",
            "brnpdf+1sigEnergy.txt": "2ad879a7302d8ca2e25ef1e192f88183",
            "brnpdf-1sigBRNTimingMean.txt": "937c7c0f53aff94600ed7dfffb69de8b",
            "brnpdf-1sigEnergy.txt": "ea7dd87225a19fe75f28d3dec00e7441",
            "brnpdf.txt": "7ccf0fdc0d0010d2c6570d620816e4df",
            "brnpdfBRNTimingWidthSyst.txt": "5050ef987d122fae43eeef27b86ec1b2",
            "CENNS10AnlAEfficiency.txt": "77139f1bb79dcf972a3a0ecc28a4a8f5",
            "CENNS10DataReleaseCompanion.pdf": "f0f67a11113f5d60c84421bb76e37728",
            "cevnspdf+1sigF90.txt": "0237a293b243b371459bcb19bc2fa116",
            "cevnspdf-1sigF90.txt": "b9bd9500b0c84b851f0d38e4869cad0f",
            "cevnspdf.txt": "5601234e03bc9bbd01066591629e72c0",
            "cevnspdfCEvNSTimingMeanSyst.txt": "24455c1cd2acf4f359cf0942deb7b29b",
            "datanobkgsub.txt": "4346ec521e91a7227b2e34ff8f3c269b",
            "delbrnpdf.txt": "5d57e91a773f03368d149dc5739b6a01",
            "energydata1d.txt": "fb4122f9309e16df39de4d3f3224af56",
            "f90data1d.txt": "4fa866380574a7d70f719ffcbab11806",
            "LArParametersAnlA.yaml": "cc9f2c60ce0c17809453e0caad9c4a38",
            "PlotExtractedData.C": "1161762465460efdda35d4494a0d8547",
            "readYAMLParameters.py": "708becd2d56cec1c2e672038581b8c7c",
            "systerrors1denergy.txt": "d933e52f2c0dd8987e3535640194065f",
            "systerrors1dpsd.txt": "2d0cb7ca23e3b0a3edfd2f0cb0e9d5dd",
            "systerrors1dtime.txt": "98c920d71497cfa8b35bbd18fc8975c3",
            "timingdata1d.txt": "a467365800489d105f7305a38751c9e5",
        },
    },
}

TRANSIENT_HTTP = {429, 500, 502, 503, 504}


def hash_bytes(data: bytes) -> tuple[str, str]:
    return hashlib.md5(data).hexdigest(), hashlib.sha256(data).hexdigest()


def file_url(record_id: str, filename: str) -> str:
    quoted = urllib.parse.quote(filename, safe="")
    return f"https://zenodo.org/records/{record_id}/files/{quoted}?download=1"


def fetch_opaque_bytes(url: str, attempts: int = 4) -> tuple[bytes, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 NMIR/0105a3 opaque-byte-pin",
            "Accept": "application/octet-stream,*/*;q=0.8",
        },
    )
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return response.read(), response.geturl()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in TRANSIENT_HTTP:
                raise RuntimeError(f"BLOCKED_0105A3_HTTP_{exc.code} url={url}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last = exc
        if attempt < attempts:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"BLOCKED_0105A3_TRANSPORT attempts={attempts} url={url}") from last


def frozen_inventory_valid() -> bool:
    counts = {name: len(rel["files"]) for name, rel in RELEASES.items()}
    if counts != {"csi": 13, "ar": 24}:
        return False
    for rel in RELEASES.values():
        for filename, md5 in rel["files"].items():
            if not filename or len(md5) != 32:
                return False
            try:
                int(md5, 16)
            except ValueError:
                return False
    return True


def build_manifest(fetcher=fetch_opaque_bytes, git_sha: str | None = None) -> dict:
    if not frozen_inventory_valid():
        raise RuntimeError("BLOCKED_0105A3_FROZEN_INVENTORY_INVALID")

    releases_out = {}
    all_md5_ok = True
    file_count = 0
    for label, rel in RELEASES.items():
        files_out = []
        for filename, expected_md5 in rel["files"].items():
            url = file_url(rel["record_id"], filename)
            data, resolved_url = fetcher(url)
            actual_md5, sha256 = hash_bytes(data)
            md5_ok = actual_md5 == expected_md5
            all_md5_ok &= md5_ok
            file_count += 1
            files_out.append(
                {
                    "filename": filename,
                    "request_url": url,
                    "resolved_url": resolved_url,
                    "size_bytes": len(data),
                    "provider_md5_expected": expected_md5,
                    "md5_actual": actual_md5,
                    "provider_md5_match": md5_ok,
                    "sha256": sha256,
                }
            )
        releases_out[label] = {
            "record_id": rel["record_id"],
            "doi": rel["doi"],
            "version": rel["version"],
            "file_count": len(files_out),
            "files": files_out,
        }

    gates = {
        "frozen_inventory_valid": True,
        "exact_total_file_count_37": file_count == 37,
        "all_provider_md5_match": all_md5_ok,
        "all_sha256_recorded": all(
            len(f["sha256"]) == 64 for r in releases_out.values() for f in r["files"]
        ),
        "observed_residual_execution_remains_locked": True,
    }
    return {
        "benchmark": "NMIR-V2-0105A3",
        "status": (
            "PASS_0105A3_COHERENT_ZENODO_DIRECT_BYTE_LOCK_NONTERMINAL"
            if all(gates.values())
            else "BLOCKED_0105A3_COHERENT_ZENODO_BYTE_LOCK_INCOMPLETE"
        ),
        "releases": releases_out,
        "gates": gates,
        "coherent_event_byte_lock_complete": all(gates.values()),
        "observed_residual_execution_allowed": False,
        "git_sha": git_sha,
    }


def normalized_manifest(result: dict) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a3"))
    parser.add_argument("--git-sha")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    result = build_manifest(git_sha=args.git_sha)
    normalized = normalized_manifest(result)
    (args.output_dir / "coherent_zenodo_direct_byte_manifest.json").write_text(normalized, encoding="utf-8")
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    (args.output_dir / "manifest_sha256.txt").write_text(digest + "\n", encoding="utf-8")
    print(normalized, end="")
    print(f"manifest_sha256={digest}")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
