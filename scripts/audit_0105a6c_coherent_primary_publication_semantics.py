#!/usr/bin/env python3
import argparse, hashlib, io, json, re, time, urllib.request
from pathlib import Path

TARGETS = {
    "csi": {
        "arxiv": "1708.01294v1",
        "url": "https://arxiv.org/pdf/1708.01294v1",
        "sha256": "a47539271203e0d0ea71a45ede2535011bcd2b0cdb2a846beecb1f54302fe9fc",
    },
    "ar": {
        "arxiv": "2003.10630v7",
        "url": "https://arxiv.org/pdf/2003.10630v7",
        "sha256": "2f875bda728739a85a2568db44761d7f164e113e77613d8f884e6c4b071acef2",
    },
}

PHRASE_FAMILIES = {
    "maximum_likelihood": [
        "maximum likelihood",
        "maximum-likelihood",
    ],
    "extended_maximum_likelihood": [
        "extended maximum likelihood",
        "extended maximum-likelihood",
    ],
    "binned_fit": [
        "binned maximum likelihood",
        "binned maximum-likelihood",
        "binned in",
    ],
    "cevns_component": [
        "cevns component",
        "cevns signal",
        "cevns pdf",
    ],
    "prompt_or_beam_neutron": [
        "prompt neutron",
        "beam-related neutron",
        "beam related neutron",
        "brn",
    ],
    "steady_state_background": [
        "steady-state background",
        "steady state background",
        "steady-state (ss)",
        "steady state (ss)",
    ],
    "gaussian_constraint": [
        "gaussian constraint",
        "gaussian-constrained",
        "gaussian constrained",
    ],
    "profile_likelihood": [
        "profile likelihood",
        "profile log-likelihood",
        "profile log likelihood",
        "likelihood profile",
    ],
    "null_or_significance_benchmark": [
        "standard deviations",
        "sigma significance",
        "null hypothesis",
        "ncevns = 0",
        "ncevns=0",
    ],
    "pseudo_validation": [
        "pseudo-data",
        "pseudo data",
        "pseudo-experiment",
        "pseudoexperiment",
        "toy monte carlo",
        "toy mc",
    ],
}


def fetch(url, tries=4, timeout=90):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "NMIR-0105a6c-semantic-inventory/1.0"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.geturl()
        except Exception as exc:
            last = repr(exc)
            if i + 1 < tries:
                time.sleep(2 ** i)
    raise RuntimeError(last)


def parse_pages(data):
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    return [(page.extract_text() or "") for page in reader.pages]


def normalized(text):
    return " ".join(text.replace("\u00ad", "").replace("\n", " ").lower().split())


def pages_for_phrases(pages, phrases):
    hits = []
    for idx, text in enumerate(pages, start=1):
        n = normalized(text)
        if any(phrase in n for phrase in phrases):
            hits.append(idx)
    return hits


def pages_with_near_terms(pages, term_a, term_b, max_chars=240):
    hits = []
    a = re.escape(term_a)
    b = re.escape(term_b)
    patterns = [
        re.compile(a + r".{0," + str(max_chars) + r"}" + b),
        re.compile(b + r".{0," + str(max_chars) + r"}" + a),
    ]
    for idx, text in enumerate(pages, start=1):
        n = normalized(text)
        if any(pattern.search(n) for pattern in patterns):
            hits.append(idx)
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()

    result = {
        "benchmark": "NMIR-V2-0105A6C",
        "stage": "frozen_primary_publication_semantic_inventory_only",
        "git_sha": args.git_sha,
        "sm_null_reproduction_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "semantic_completeness_classified": False,
        "targets": {},
    }
    all_ok = True

    for key, cfg in TARGETS.items():
        entry = {"arxiv": cfg["arxiv"], "url": cfg["url"], "expected_sha256": cfg["sha256"]}
        try:
            data, resolved = fetch(cfg["url"])
            observed_sha = hashlib.sha256(data).hexdigest()
            if observed_sha != cfg["sha256"]:
                entry.update({
                    "resolved_url": resolved,
                    "observed_sha256": observed_sha,
                    "byte_identity_ok": False,
                    "error": "frozen_pdf_sha256_mismatch",
                })
                result["targets"][key] = entry
                all_ok = False
                continue

            pages = parse_pages(data)
            evidence = {
                family: pages_for_phrases(pages, phrases)
                for family, phrases in PHRASE_FAMILIES.items()
            }
            evidence["poisson_near_likelihood_candidate"] = pages_with_near_terms(
                pages, "poisson", "likelihood", max_chars=240
            )
            evidence["log_likelihood_equation_candidate"] = [
                idx
                for idx, text in enumerate(pages, start=1)
                if ("ln" in normalized(text) or "log-likelihood" in normalized(text))
                and "=" in text
                and "likelihood" in normalized(text)
            ]
            entry.update({
                "resolved_url": resolved,
                "observed_sha256": observed_sha,
                "byte_identity_ok": True,
                "page_count": len(pages),
                "extracted_text_sha256": hashlib.sha256(
                    "\n".join(pages).encode("utf-8")
                ).hexdigest(),
                "evidence_pages_1_based": evidence,
                "evidence_note": "Phrase/page hits are locators only; they do not imply semantic completeness.",
            })
        except Exception as exc:
            all_ok = False
            entry["error"] = repr(exc)
        result["targets"][key] = entry

    result["status"] = (
        "PASS_0105A6C_PRIMARY_PUBLICATION_SEMANTIC_INVENTORY_NONDISCOVERY"
        if all_ok
        else "BLOCKED_0105A6C_FROZEN_BYTE_MISMATCH_OR_TRANSPORT"
    )
    result["sm_null_reproduction_allowed"] = False

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out.write_text(payload, encoding="utf-8")
    print(payload, end="")
    print("result_sha256=" + hashlib.sha256(payload.encode()).hexdigest())
    return 0 if all_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
