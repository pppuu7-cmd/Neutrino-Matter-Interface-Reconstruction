#!/usr/bin/env python3
import argparse, hashlib, io, json, time, urllib.request
from pathlib import Path
from urllib.parse import urlparse
from pypdf import PdfReader

TARGETS = {
    "csi": {
        "arxiv": "1708.01294v1",
        "url": "https://arxiv.org/pdf/1708.01294v1",
        "title": "Observation of Coherent Elastic Neutrino-Nucleus Scattering",
        "doi": "10.1126/science.aao0990",
    },
    "ar": {
        "arxiv": "2003.10630v7",
        "url": "https://arxiv.org/pdf/2003.10630v7",
        "title": "First Measurement of Coherent Elastic Neutrino-Nucleus Scattering on Argon",
        "doi": "10.1103/PhysRevLett.126.012002",
    },
}


def fetch(url, tries=4, timeout=90):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0105a6b-authority-acquisition/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.geturl(), r.headers.get("Content-Type", "")
        except Exception as exc:
            last = repr(exc)
            if i + 1 < tries:
                time.sleep(2 ** i)
    raise RuntimeError(last)


def normalize(text):
    return " ".join(text.replace("\u00ad", "").replace("\n", " ").split())


def exact_versioned_arxiv_pdf_identity(resolved, arxiv_id):
    """Accept arXiv's exact versioned /pdf/<id> endpoint with optional .pdf suffix.

    arXiv currently resolves the frozen PDF URLs without appending '.pdf'.  The
    scientific identity predicate is therefore host + exact versioned path,
    while PDF identity itself is independently enforced by PDF magic, parsing,
    and frozen-title text checks.
    """
    parsed = urlparse(resolved)
    if parsed.scheme.lower() != "https" or parsed.netloc.lower() != "arxiv.org":
        return False
    path = parsed.path.rstrip("/")
    allowed = {f"/pdf/{arxiv_id}", f"/pdf/{arxiv_id}.pdf"}
    return path in allowed and not parsed.query and not parsed.fragment


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()

    result = {
        "benchmark": "NMIR-V2-0105A6B",
        "stage": "primary_collaboration_publication_byte_acquisition_only",
        "git_sha": args.git_sha,
        "sm_null_reproduction_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "targets": {},
    }
    ok = True

    for key, cfg in TARGETS.items():
        entry = dict(cfg)
        try:
            data, resolved, content_type = fetch(cfg["url"])
            reader = PdfReader(io.BytesIO(data))
            text = "\n".join((page.extract_text() or "") for page in reader.pages)
            norm = normalize(text).lower()
            title_ok = normalize(cfg["title"]).lower() in norm
            url_identity_ok = exact_versioned_arxiv_pdf_identity(resolved, cfg["arxiv"])
            pdf_magic_ok = data.startswith(b"%PDF")
            entry.update({
                "resolved_url": resolved,
                "content_type": content_type,
                "size_bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "pages": len(reader.pages),
                "text_chars": len(text),
                "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                "title_identity_ok": title_ok,
                "versioned_url_identity_ok": url_identity_ok,
                "pdf_magic_ok": pdf_magic_ok,
            })
            if not (title_ok and url_identity_ok and pdf_magic_ok and len(reader.pages) > 0):
                ok = False
                entry["error"] = "document_identity_validation_failed"
        except Exception as exc:
            ok = False
            entry["error"] = repr(exc)
        result["targets"][key] = entry

    result["status"] = (
        "PASS_0105A6B_PRIMARY_PUBLICATION_BYTE_ACQUISITION_NONDISCOVERY"
        if ok else "BLOCKED_0105A6B_PRIMARY_PUBLICATION_TRANSPORT_OR_IDENTITY"
    )
    result["semantic_completeness_classified"] = False
    result["sm_null_reproduction_allowed"] = False

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out.write_text(payload, encoding="utf-8")
    print(payload, end="")
    print("result_sha256=" + hashlib.sha256(payload.encode()).hexdigest())
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
