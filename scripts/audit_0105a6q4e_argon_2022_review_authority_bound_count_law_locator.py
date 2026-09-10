#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import urllib.request
from pathlib import Path

BENCHMARK = "NMIR-V2-0105A6Q4E"
PREREG_COMMIT = "29c6f13ff456fd753bad72eb29c9568f66172d08"
PARENT_Q4D_SHA256 = "fd36f42625747fd849a1aa44acca61804dac84844f172f1eb4c5d91bb131e848"
PARENT_Q4D_CLASS = "BLOCKED_0105A6Q4D_CROSS_PROVIDER_REDIRECT_REQUIRES_SEPARATE_AUTHORITY_BINDING"
Q4C_SCRIPT_GIT_BLOB_SHA1 = "cd24f33be2b17f643d13d2399719e9bf26fecc7b"
TARGET_URL = "https://indico.global/event/13069/contributions/114762/attachments/53315/102415/JCZBLV2022_CEvNSReviewTalk.pdf"
TARGET_SIZE = 18484736
TARGET_SHA256 = "af0fb243be7d8433fbc003de1d963bee3b3510467cfbbd6b1990f1e6626de817"


class TargetIdentityError(RuntimeError):
    pass


class LexicalContractIdentityError(RuntimeError):
    pass


def h256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def verify_parent(path: Path) -> dict:
    raw = path.read_bytes()
    if h256(raw) != PARENT_Q4D_SHA256:
        raise TargetIdentityError("parent q4d SHA256 mismatch")
    obj = json.loads(raw)
    expected = {
        "classification": PARENT_Q4D_CLASS,
        "final_url": TARGET_URL,
        "payload_size_bytes": TARGET_SIZE,
        "payload_sha256": TARGET_SHA256,
        "page_text_inspected": False,
        "pdftotext_executed": False,
    }
    for key, value in expected.items():
        if obj.get(key) != value:
            raise TargetIdentityError(f"parent q4d provenance mismatch: {key}")
    return obj


def load_q4c_contract(path: Path):
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != Q4C_SCRIPT_GIT_BLOB_SHA1:
        raise LexicalContractIdentityError(
            f"q4c lexical implementation blob mismatch: {actual}"
        )
    spec = importlib.util.spec_from_file_location("nmir_frozen_q4c_contract", path)
    if spec is None or spec.loader is None:
        raise LexicalContractIdentityError("cannot load frozen q4c lexical implementation")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name in ("norm", "flags", "pages", "h256"):
        if not hasattr(module, name):
            raise LexicalContractIdentityError(f"q4c lexical symbol missing: {name}")
    return module


def download_exact(path: Path) -> tuple[bytes, str, int]:
    req = urllib.request.Request(
        TARGET_URL,
        headers={"User-Agent": "NMIR-0105a6q4e-authority-bound-locator/1.0"},
    )
    with urllib.request.urlopen(req, timeout=120) as response:
        final_url = response.geturl()
        status = int(getattr(response, "status", response.getcode()))
        payload = response.read()

    if final_url != TARGET_URL:
        raise TargetIdentityError(f"final URL mismatch: {final_url}")
    if status != 200:
        raise TargetIdentityError(f"HTTP status mismatch: {status}")
    if not payload.startswith(b"%PDF-"):
        raise TargetIdentityError("target response is not PDF")
    if len(payload) != TARGET_SIZE:
        raise TargetIdentityError(f"target size mismatch: {len(payload)}")
    digest = h256(payload)
    if digest != TARGET_SHA256:
        raise TargetIdentityError(f"target SHA256 mismatch: {digest}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return payload, final_url, status


def run(parent_q4d: Path, q4c_script: Path, presentation: Path) -> dict:
    verify_parent(parent_q4d)
    q4c = load_q4c_contract(q4c_script)
    payload, final_url, status = download_exact(presentation)

    # Content inspection begins only here, after every frozen identity gate passes.
    normalized_pages = q4c.pages(presentation)
    candidates = []
    for page_no, text in enumerate(normalized_pages, 1):
        flags = q4c.flags(text)
        if flags["categories"]:
            candidates.append(
                {
                    "physical_page": page_no,
                    "normalized_text_sha256": q4c.h256(text.encode()),
                    **flags,
                }
            )

    classification = (
        "PASS_0105A6Q4E_2022_REVIEW_CANDIDATE_PAGES_LOCATED_NONDISCOVERY"
        if candidates
        else "BLOCKED_0105A6Q4E_2022_REVIEW_HAS_NO_COUNT_LAW_CANDIDATE_PAGES"
    )
    return {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "parent_q4d_result_sha256": PARENT_Q4D_SHA256,
        "q4c_lexical_implementation_git_blob_sha1": Q4C_SCRIPT_GIT_BLOB_SHA1,
        "source": {
            "provider": "CERN Indico migration target / indico.global",
            "speaker": "Jacob Zettlemoyer",
            "title": "Experimental efforts and physics capabilities of Coherent Elastic Neutrino-Nucleus Scattering (CEvNS)",
            "date": "2022-09-08",
            "resolved_url": final_url,
            "http_status": status,
            "size": len(payload),
            "sha256": h256(payload),
        },
        "physical_page_count": len(normalized_pages),
        "candidate_pages": [x["physical_page"] for x in candidates],
        "candidate_records": candidates,
        "page_text_inspected": True,
        "page_text_retained": False,
        "pdftotext_executed": True,
        "classification": classification,
        "pseudo_data_generated": False,
        "likelihood_evaluated": False,
        "systematic_monte_carlo_preregistration_permission_percent": 0,
        "systematic_monte_carlo_execution_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "observed_bsm_residual_inspected": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-q4d-result", required=True)
    parser.add_argument("--q4c-script", required=True)
    parser.add_argument("--presentation", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--git-sha", required=True)
    args = parser.parse_args()

    base = {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "git_sha": args.git_sha,
        "pseudo_data_generated": False,
        "likelihood_evaluated": False,
        "systematic_monte_carlo_preregistration_permission_percent": 0,
        "systematic_monte_carlo_execution_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "observed_bsm_residual_inspected": False,
        "page_text_retained": False,
    }
    try:
        result = run(
            Path(args.parent_q4d_result),
            Path(args.q4c_script),
            Path(args.presentation),
        )
        result["git_sha"] = args.git_sha
    except LexicalContractIdentityError as exc:
        result = {
            **base,
            "classification": "BLOCKED_0105A6Q4E_LEXICAL_CONTRACT_IDENTITY_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "page_text_inspected": False,
            "pdftotext_executed": False,
        }
    except Exception as exc:
        result = {
            **base,
            "classification": "BLOCKED_0105A6Q4E_TARGET_IDENTITY_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "page_text_inspected": False,
            "pdftotext_executed": False,
        }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
