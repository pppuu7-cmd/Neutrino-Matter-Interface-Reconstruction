#!/usr/bin/env python3
"""NMIR 0105a q6: fail-closed authority audit of COHERENT CsI-2021 ancillary material.

Nondiscovery only. This script does not run an observed residual, systematic MC,
or any BSM scan. It consumes only the prospectively frozen q6 authority chain.
"""
from __future__ import annotations
import hashlib, json, pathlib, re, subprocess, tempfile, urllib.request

PREREG_COMMIT = "a98dfd80a4db5d4b291e0d049fd1f00da9794a48"
BASE = "https://arxiv.org/src/2110.07730v2/anc/"
FILES = [
    "Paper_CEvNSCsI_FullDataset_SupMaterials.pdf",
    "brnPE.txt", "brnTrec.txt", "dataBeamOnAC.txt", "dataBeamOnC.txt",
    "effCoefficients.txt", "ninPE.txt", "ninTrec.txt", "scintRespCoefficients.txt",
    "snsFlux2D.root",
]
F1_REQUIRED = [
    "selected, unbinned data events",
    "All events selected with PE < 250 and 0 ≤ trec < 12 µs are included",
    "Events with energy 60 ≤ PE < 250 or trec ≥ 6 µs are not used for measuring the CEvNS cross",
    "dataBeamOnAC.txt",
    "dataBeamOnC.txt",
    "These two files contain all data relevant for this measurement",
]


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\x0c", " ").replace("ﬁ", "fi")).strip()


def classify(pdf_text: str, text_payloads: dict[str, str]) -> dict:
    n = normalize(pdf_text)
    f1_hits = {p: (normalize(p) in n) for p in F1_REQUIRED}
    cross_rule = ("Events with energy 60 ≤ PE < 250 or trec ≥ 6 µs are not used for measuring the CEvNS cross" in n
                  and "section but used for a search for light dark matter" in n)
    f1_complete = all(v for p, v in f1_hits.items() if not p.startswith("Events with energy")) and cross_rule
    corpus = n + "\n" + "\n".join(text_payloads.values())
    has3152 = bool(re.search(r"(?<!\d)3152(?!\d)", corpus))
    has3154 = bool(re.search(r"(?<!\d)3154(?!\d)", corpus))
    f7_complete = False  # literals/row counts cannot satisfy the frozen semantic-precedence contract
    return {
        "f1": {
            "status": "PASS_0105A_Q6_F1_PRIMARY_COUNT_LAW_LOCATED_NONDISCOVERY" if f1_complete else "BLOCKED_0105A_Q6_F1_PRIMARY_SEMANTICS_INCOMPLETE",
            "required_phrase_hits": f1_hits,
            "cross_section_exclusion_rule_complete": cross_rule,
            "interpretation": "Primary supplement explicitly supplies selected unbinned events, C/AC observed-data files, the full selected envelope, and the CEvNS measurement exclusion region; no numerical reverse engineering is needed to define what rows are counted in the measurement region." if f1_complete else "Primary q6 material did not satisfy the frozen count-law criterion.",
        },
        "f7": {
            "status": "PASS_0105A_Q6_F7_PRIMARY_3152_3154_PRECEDENCE_LOCATED_NONDISCOVERY" if f7_complete else "BLOCKED_0105A_Q6_F7_PRIMARY_SEMANTICS_INCOMPLETE",
            "literal_3152_present": has3152,
            "literal_3154_present": has3154,
            "interpretation": "The frozen q6 corpus does not explicitly identify the semantic role/precedence of both 3152 and 3154; numerical row counts are deliberately not promoted to authority.",
        },
    }


def main(outdir: str = "results/0105a_q6") -> None:
    od = pathlib.Path(outdir); od.mkdir(parents=True, exist_ok=True)
    payloads: dict[str, bytes] = {}
    meta = {}
    for name in FILES:
        with urllib.request.urlopen(BASE + name, timeout=90) as r:
            b = r.read()
        payloads[name] = b
        meta[name] = {"bytes": len(b), "sha256": sha256(b)}
    with tempfile.TemporaryDirectory() as td:
        pdf = pathlib.Path(td) / "supp.pdf"; txt = pathlib.Path(td) / "supp.txt"
        pdf.write_bytes(payloads[FILES[0]])
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
        pdf_text = txt.read_text(encoding="utf-8", errors="replace")
    text_payloads = {n: payloads[n].decode("utf-8", errors="replace") for n in FILES if n.endswith(".txt")}
    result = {
        "gate": "0105a_q6_csi2021_ancillary_authority",
        "preregistration_commit": PREREG_COMMIT,
        "scope": "NONDISCOVERY authority audit only",
        "source": "arXiv:2110.07730v2 collaboration ancillary material",
        "files": meta,
        "adjudication": classify(pdf_text, text_payloads),
        "hard_prohibitions": {"observed_bsm_residual": True, "systematic_mc": True, "posthoc_numeric_selection": True},
    }
    (od / "supplement_pdftotext.txt").write_text(pdf_text, encoding="utf-8")
    (od / "result.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
