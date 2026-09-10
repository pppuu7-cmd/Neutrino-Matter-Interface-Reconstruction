#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse

BENCHMARK = "NMIR-V2-0105A6Q4D"
PREREG_COMMIT = "843c2cc29f161d2a1fabab97d5b74f7fdffab3c1"
PARENT_Q4C_SHA256 = "988fbbc0b5c2f0a74562fb33a829eaae8ff3ebedd1ded7e25376d967a43ef612"
PARENT_Q4C_CLASS = "BLOCKED_0105A6Q4C_2022_REVIEW_TRANSPORT_OR_IDENTITY_FAILURE"
URL = "https://indico.cern.ch/event/978288/contributions/5014436/attachments/2504944/4303826/JCZBLV2022_CEvNSReviewTalk.pdf"
EXPECTED_HOST = "indico.cern.ch"
EXPECTED_PATH = "/event/978288/contributions/5014436/attachments/2504944/4303826/JCZBLV2022_CEvNSReviewTalk.pdf"


def h256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_initial_url(url: str) -> None:
    p = urlparse(url)
    if (
        p.scheme != "https"
        or p.hostname != EXPECTED_HOST
        or p.path != EXPECTED_PATH
        or p.query
        or p.fragment
    ):
        raise RuntimeError("initial frozen URL identity mismatch")


def verify_parent(path: Path) -> None:
    raw = path.read_bytes()
    obj = json.loads(raw)
    if h256(raw) != PARENT_Q4C_SHA256:
        raise RuntimeError("parent q4c SHA256 mismatch")
    if obj.get("classification") != PARENT_Q4C_CLASS:
        raise RuntimeError("parent q4c classification mismatch")


class RecordingRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self) -> None:
        super().__init__()
        self.chain: list[dict[str, object]] = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raw_location = headers.get("Location")
        resolved = urljoin(req.full_url, raw_location or newurl)
        self.chain.append(
            {
                "source_url": req.full_url,
                "status": int(code),
                "location": raw_location,
                "resolved_destination_url": resolved,
            }
        )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def classify(final_url: str, chain: list[dict[str, object]], is_pdf: bool) -> str:
    if not is_pdf:
        return "BLOCKED_0105A6Q4D_TRANSPORT_DIAGNOSTIC_FAILURE"
    destinations = [str(hop["resolved_destination_url"]) for hop in chain]
    if any(urlparse(u).hostname != EXPECTED_HOST for u in destinations):
        return "BLOCKED_0105A6Q4D_CROSS_PROVIDER_REDIRECT_REQUIRES_SEPARATE_AUTHORITY_BINDING"
    if not chain and final_url == URL:
        return "PASS_0105A6Q4D_EXACT_URL_IDENTITY_CONFIRMED"
    if urlparse(final_url).hostname == EXPECTED_HOST:
        return "PASS_0105A6Q4D_INDICO_REDIRECT_CHAIN_RECORDED_NONDISCOVERY"
    return "BLOCKED_0105A6Q4D_CROSS_PROVIDER_REDIRECT_REQUIRES_SEPARATE_AUTHORITY_BINDING"


def run(parent_q4c: Path) -> dict[str, object]:
    verify_parent(parent_q4c)
    verify_initial_url(URL)

    redirect_handler = RecordingRedirectHandler()
    opener = urllib.request.build_opener(redirect_handler)
    req = urllib.request.Request(
        URL,
        headers={"User-Agent": "NMIR-0105a6q4d-transport-diagnostic/1.0"},
    )
    with opener.open(req, timeout=120) as response:
        final_url = response.geturl()
        final_status = int(getattr(response, "status", response.getcode()))
        selected_headers = {
            key: response.headers.get(key)
            for key in ("Content-Type", "Content-Length", "ETag", "Last-Modified", "Content-Disposition")
            if response.headers.get(key) is not None
        }
        payload = response.read()

    is_pdf = payload.startswith(b"%PDF-")
    result_class = classify(final_url, redirect_handler.chain, is_pdf)
    return {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "parent_q4c_result_sha256": PARENT_Q4C_SHA256,
        "initial_url": URL,
        "redirect_chain": redirect_handler.chain,
        "redirect_count": len(redirect_handler.chain),
        "final_url": final_url,
        "final_status": final_status,
        "selected_headers": selected_headers,
        "payload_size_bytes": len(payload),
        "payload_sha256": h256(payload),
        "pdf_magic": is_pdf,
        "page_text_inspected": False,
        "page_text_retained": False,
        "pdftotext_executed": False,
        "pseudo_data_generated": False,
        "likelihood_evaluated": False,
        "observed_bsm_residual_inspected": False,
        "systematic_monte_carlo_preregistration_permission_percent": 0,
        "systematic_monte_carlo_execution_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "classification": result_class,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-q4c-result", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--git-sha", required=True)
    args = parser.parse_args()

    try:
        result = run(Path(args.parent_q4c_result))
        result["git_sha"] = args.git_sha
    except Exception as exc:
        result = {
            "benchmark": BENCHMARK,
            "preregistration_commit": PREREG_COMMIT,
            "git_sha": args.git_sha,
            "classification": "BLOCKED_0105A6Q4D_TRANSPORT_DIAGNOSTIC_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "page_text_inspected": False,
            "page_text_retained": False,
            "pdftotext_executed": False,
            "pseudo_data_generated": False,
            "likelihood_evaluated": False,
            "observed_bsm_residual_inspected": False,
            "systematic_monte_carlo_preregistration_permission_percent": 0,
            "systematic_monte_carlo_execution_permission_percent": 0,
            "observed_bsm_residual_permission_percent": 0,
        }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
