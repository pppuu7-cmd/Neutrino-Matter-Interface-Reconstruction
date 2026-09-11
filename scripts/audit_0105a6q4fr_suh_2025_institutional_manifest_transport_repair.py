#!/usr/bin/env python3
import argparse
import hashlib
import html
import json
import re
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

PREREG_COMMIT = "f47dda9bd5fda788c4497d58e4a2f58f2e042cb3"
CEEM_PLAQUE_URL = "https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html"
CEEM_EDUCATION_URL = "https://ceem.indiana.edu/education/index.html"
TITLE = "TOWARDS AN IMPROVED MEASUREMENT OF THE CEVNS PROCESS WITH THE CENNS-10 LAR DETECTOR"
AUTHORS = ("Benjamin D. Suh", "Benjamin Suh")
YEAR = "2025"
UA = "NMIR-0105a6q4fr-institutional-manifest-transport-repair/1.0"

PASS_CLASS = "PASS_0105A6Q4FR_INSTITUTIONAL_MANIFEST_TRANSPORT_REPAIRED_NONDISCOVERY"
BLOCKED_CLASS = "BLOCKED_0105A6Q4FR_INSTITUTIONAL_MANIFEST_TRANSPORT_OR_IDENTITY_INCOMPLETE"


class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def normalize_text(text):
    return " ".join(html.unescape(text).split()).casefold()


def payload_text(payload, content_type):
    charset = "utf-8"
    match = re.search(r"charset\s*=\s*([^\s;]+)", content_type or "", re.I)
    if match:
        charset = match.group(1).strip("\"'")
    decoded = payload.decode(charset, errors="replace")
    parser = _TextExtractor()
    parser.feed(decoded)
    parser.close()
    return normalize_text(" ".join(parser.parts))


def identity_flags(payload, content_type):
    text = payload_text(payload, content_type)
    title_ok = normalize_text(TITLE) in text
    author_matches = [name for name in AUTHORS if normalize_text(name) in text]
    year_ok = re.search(r"(?<!\d)2025(?!\d)", text) is not None
    return {
        "author": bool(author_matches),
        "year": year_ok,
        "title": title_ok,
        "complete": bool(author_matches) and year_ok and title_ok,
    }


def _record(url, final_url, status, payload, content_type, error):
    flags = identity_flags(payload, content_type) if payload else {
        "author": False, "year": False, "title": False, "complete": False
    }
    return {
        "requested_url": url,
        "final_url": final_url,
        "status": status,
        "content_type": content_type,
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest() if payload else hashlib.sha256(b"").hexdigest(),
        "identity": flags,
        "error": error,
    }


def probe(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            payload = response.read()
            return _record(
                url,
                response.geturl(),
                int(getattr(response, "status", response.getcode())),
                payload,
                response.headers.get("Content-Type"),
                None,
            )
    except urllib.error.HTTPError as exc:
        payload = exc.read()
        return _record(
            url,
            exc.geturl(),
            int(exc.code),
            payload,
            exc.headers.get("Content-Type"),
            type(exc).__name__,
        )
    except Exception as exc:
        return {
            "requested_url": url,
            "final_url": None,
            "status": None,
            "content_type": None,
            "bytes": 0,
            "sha256": None,
            "identity": {"author": False, "year": False, "title": False, "complete": False},
            "error": type(exc).__name__ + ": " + str(exc),
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--git-sha", required=True)
    args = parser.parse_args()

    probes = [probe(CEEM_PLAQUE_URL), probe(CEEM_EDUCATION_URL)]
    passed = all(item["status"] == 200 and item["identity"]["complete"] for item in probes)
    classification = PASS_CLASS if passed else BLOCKED_CLASS

    result = {
        "benchmark": "NMIR-V2-0105A6Q4FR",
        "preregistration_commit": PREREG_COMMIT,
        "git_sha": args.git_sha,
        "classification": classification,
        "probes": probes,
        "page_links_followed": False,
        "pdf_downloaded": False,
        "pdf_content_inspected": False,
        "pdftotext_executed": False,
        "ocr_executed": False,
        "likelihood_evaluated": False,
        "pseudo_data_generated": False,
        "observed_bsm_residual_inspected": False,
        "bsm_fit_executed": False,
        "systematic_monte_carlo_preregistration_permission_percent": 0,
        "systematic_monte_carlo_execution_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
