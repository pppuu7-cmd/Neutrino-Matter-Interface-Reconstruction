import hashlib
import json

import scripts.extract_0105a5b_deepcore_release_semantics as mod


def synthetic_docs():
    readme = b"# release\nenergy zenith pid systematic hypersurface weight\n"
    nb = json.dumps({
        "cells": [
            {"cell_type": "markdown", "source": ["theta23 dm2 PREM"]},
            {"cell_type": "code", "source": ["import scipy\n# numu nue nutau minimize chi"]},
        ]
    }).encode()
    return {"readme.md": readme, "example.ipynb": nb}


def patch_contract(monkeypatch, payloads):
    docs = {}
    ids = {"readme.md": 1, "example.ipynb": 2}
    for name, payload in payloads.items():
        docs[name] = {
            "file_id": ids[name],
            "size": len(payload),
            "md5": hashlib.md5(payload).hexdigest(),
            "sha256": hashlib.sha256(payload).hexdigest(),
        }
    monkeypatch.setattr(mod, "DOCS", docs)


def fetcher_for(payloads):
    def fetcher(url):
        file_id = int(url.rsplit("/", 1)[-1])
        return payloads["readme.md"] if file_id == 1 else payloads["example.ipynb"]
    return fetcher


def test_frozen_real_document_authority_matches_0105a4d():
    assert mod.DOCS["readme.md"]["file_id"] == 11674676
    assert mod.DOCS["readme.md"]["sha256"] == "0f8e7bbc6059d18376843370e36e98a0cfa69fbc4bd767df694c6d65f861149f"
    assert mod.DOCS["example.ipynb"]["file_id"] == 11674675
    assert mod.DOCS["example.ipynb"]["sha256"] == "900acac6e74cced45e0b894017340b7aa0a64ccb615365b865cc7b4ae87be1a3"


def test_matching_docs_pass_only_after_hash_verification(monkeypatch):
    payloads = synthetic_docs()
    patch_contract(monkeypatch, payloads)
    result, outputs = mod.build(fetcher=fetcher_for(payloads))
    assert result["status"] == "PASS_0105A5B_R1_VERIFIED_DOC_EXTRACTION_NONDISCOVERY"
    assert result["all_doc_bytes_match_0105a4d"] is True
    assert result["parsed"] is True
    assert result["event_csv_opened"] is False
    assert result["event_rows_parsed"] is False
    assert result["observed_residual_execution_allowed"] is False
    assert set(outputs) == {"verified_readme.md", "verified_example_code.py", "verified_example_markdown.md"}


def test_hash_mismatch_blocks_without_doc_parse_outputs(monkeypatch):
    payloads = synthetic_docs()
    patch_contract(monkeypatch, payloads)
    wrong = dict(payloads)
    wrong["readme.md"] = payloads["readme.md"] + b"tamper"
    result, outputs = mod.build(fetcher=fetcher_for(wrong))
    assert result["status"] == "BLOCKED_0105A5B_BYTE_AUTHORITY_MISMATCH"
    assert result["parsed"] is False
    assert outputs == {}
    assert result["event_csv_opened"] is False
    assert result["observed_residual_execution_allowed"] is False


def test_notebook_summary_is_structural_not_event_analysis():
    nb = {
        "cells": [
            {"cell_type": "markdown", "source": ["theta23 systematic"]},
            {"cell_type": "code", "source": ["import scipy\n# PREM numu minimize"]},
        ]
    }
    out = mod.notebook_summary(nb)
    assert out["cell_count"] == 2
    assert out["code_cell_count"] == 1
    assert out["markdown_cell_count"] == 1
    assert out["keyword_presence"]["theta23"] is True
    assert out["keyword_presence"]["systematic"] is True
    assert out["keyword_presence"]["prem"] is True
    assert out["keyword_presence"]["numu"] is True
