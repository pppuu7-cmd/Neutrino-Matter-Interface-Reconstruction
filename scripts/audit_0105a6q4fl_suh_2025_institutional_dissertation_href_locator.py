#!/usr/bin/env python3
import argparse
import hashlib
import html
import json
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

PREREG_COMMIT = "deadbcefe38ef9fa4618a57fd65ce82cf7178f3b"
SOURCES = (
    {
        "url": "https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html",
        "bytes": 23370,
        "sha256": "f1c245e9675c1a533bc9ad03ca928820499381d576c5f6fefee59c33b91d7488",
    },
    {
        "url": "https://ceem.indiana.edu/education/index.html",
        "bytes": 67845,
        "sha256": "3de3e09e5ebdb4006c0d8b969c3f73a25b041b31534476b6bf6987bbf5591fe6",
    },
)
IDENTITY_TOKENS = ("suh", "benjamin", "cenns-10", "cenns10")
REPOSITORY_TOKENS = ("scholarworks", "dspace", "/handle/", "/etd", "dissertation")
UA = "NMIR-0105a6q4fl-institutional-dissertation-href-locator/1.0"

CLASS_SOURCE_DRIFT = "BLOCKED_0105A6Q4FL_FROZEN_SOURCE_IDENTITY_DRIFT"
CLASS_NO_CANDIDATES = "BLOCKED_0105A6Q4FL_INSTITUTIONAL_DISSERTATION_LOCATOR_NO_CANDIDATES"
CLASS_CANDIDATES = "PASS_0105A6Q4FL_INSTITUTIONAL_DISSERTATION_LOCATOR_CANDIDATES_FOUND_NONDISCOVERY"


def normalize_text(value):
    return " ".join(html.unescape(value or "").split()).casefold()


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = []
        self._href = None
        self._text = []

    def handle_starttag(self, tag, attrs):
        if tag.casefold() == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag.casefold() == "a" and self._href is not None:
            self.anchors.append((self._href, " ".join(self._text)))
            self._href = None
            self._text = []


def parse_anchors(payload, content_type):
    charset = "utf-8"
    for part in (content_type or "").split(";")[1:]:
        if "charset=" in part.casefold():
            charset = part.split("=", 1)[1].strip().strip("\"'")
            break
    parser = AnchorParser()
    parser.feed(payload.decode(charset, errors="replace"))
    parser.close()
    return parser.anchors


def candidate_for(source_url, href, anchor_text):
    raw = (href or "").strip()
    low_raw = raw.casefold()
    if not raw or raw.startswith("#") or low_raw.startswith(("mailto:", "tel:", "javascript:")):
        return None

    resolved = urllib.parse.urljoin(source_url, raw)
    low_url = resolved.casefold()
    norm_anchor = normalize_text(anchor_text)

    identity_matches = sorted({
        token for token in IDENTITY_TOKENS if token in low_url or token in norm_anchor
    })
    repository_matches = sorted({
        token for token in REPOSITORY_TOKENS if token in low_url
    })
    parsed = urllib.parse.urlparse(resolved)
    if parsed.path.casefold().endswith(".pdf"):
        repository_matches.append(".pdf")

    if not identity_matches and not repository_matches:
        return None

    return {
        "source_url": source_url,
        "resolved_url": resolved,
        "anchor_text": norm_anchor,
        "identity_tokens": identity_matches,
        "repository_payload_tokens": sorted(set(repository_matches)),
    }


def fetch_source(spec):
    url = spec["url"]
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            payload = response.read()
            status = int(getattr(response, "status", response.getcode()))
            content_type = response.headers.get("Content-Type")
            final_url = response.geturl()
            error = None
    except urllib.error.HTTPError as exc:
        payload = exc.read()
        status = int(exc.code)
        content_type = exc.headers.get("Content-Type")
        final_url = exc.geturl()
        error = type(exc).__name__
    except Exception as exc:
        return {
            "record": {
                "requested_url": url,
                "final_url": None,
                "status": None,
                "content_type": None,
                "bytes": 0,
                "sha256": None,
                "identity_match": False,
                "error": type(exc).__name__ + ": " + str(exc),
            },
            "payload": None,
            "content_type": None,
        }

    digest = hashlib.sha256(payload).hexdigest()
    identity_match = status == 200 and len(payload) == spec["bytes"] and digest == spec["sha256"]
    return {
        "record": {
            "requested_url": url,
            "final_url": final_url,
            "status": status,
            "content_type": content_type,
            "bytes": len(payload),
            "sha256": digest,
            "identity_match": identity_match,
            "error": error,
        },
        "payload": payload,
        "content_type": content_type,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()

    fetched = [fetch_source(spec) for spec in SOURCES]
    source_records = [item["record"] for item in fetched]
    exact_sources = all(record["identity_match"] for record in source_records)

    candidates_by_url = {}
    if exact_sources:
        for spec, item in zip(SOURCES, fetched):
            for href, anchor_text in parse_anchors(item["payload"], item["content_type"]):
                candidate = candidate_for(spec["url"], href, anchor_text)
                if candidate is None:
                    continue
                key = candidate["resolved_url"]
                if key not in candidates_by_url:
                    candidates_by_url[key] = candidate
                else:
                    prior = candidates_by_url[key]
                    prior["identity_tokens"] = sorted(set(prior["identity_tokens"]) | set(candidate["identity_tokens"]))
                    prior["repository_payload_tokens"] = sorted(set(prior["repository_payload_tokens"]) | set(candidate["repository_payload_tokens"]))
                    if not prior["anchor_text"] and candidate["anchor_text"]:
                        prior["anchor_text"] = candidate["anchor_text"]

    candidates = sorted(candidates_by_url.values(), key=lambda x: x["resolved_url"])
    if not exact_sources:
        classification = CLASS_SOURCE_DRIFT
    elif not candidates:
        classification = CLASS_NO_CANDIDATES
    else:
        classification = CLASS_CANDIDATES

    result = {
        "benchmark": "NMIR-V2-0105A6Q4FL",
        "preregistration_commit": PREREG_COMMIT,
        "git_sha": args.git_sha,
        "classification": classification,
        "sources": source_records,
        "candidate_count": len(candidates),
        "candidates": candidates,
        "candidate_urls_requested": False,
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

    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
