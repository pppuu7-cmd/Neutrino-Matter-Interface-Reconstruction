#!/usr/bin/env python3
"""NMIR 0087f: localized B-L BBN-tail actionability authority audit.

Prospective contract: research/prereg/0087f_bbn_tail_actionability_authority.md
No raster/OCR/manual digitization, no CMB calibration borrowing, no extrapolation.
"""
from __future__ import annotations
import argparse, hashlib, io, json, re, tarfile
from pathlib import Path

EXPECTED_ARCHIVE_SHA256 = "484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c"
TAIL_EV = (1.0, 1.4057345497828417)
KNOWN_BBN_VECTOR = {
    "Presentation/CnstrntPlotMajoranaYp.pdf",
    "Presentation/CnstrntPlotDiracYp.pdf",
}
TEXT_EXT = {".tex", ".txt", ".md", ".csv", ".tsv", ".dat", ".json"}
TABLE_EXT = {".csv", ".tsv", ".dat", ".json"}
OUT = Path("bbn_tail_actionability_0087f.json")


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def read_archive(blob: bytes):
    files = {}
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:*") as tf:
        for m in tf.getmembers():
            if not m.isfile():
                continue
            f = tf.extractfile(m)
            if f:
                files[m.name] = f.read()
    return files


def decode(b: bytes) -> str:
    return b.decode("utf-8", errors="replace")


def route_a_candidates(files):
    """Return exact-text candidate blocks; candidates alone never imply PASS."""
    hits = []
    yp = re.compile(r"(?:Delta\s*Y|\\Delta\s*Y|Y_?\{?p\}?|helium)", re.I)
    coupling = re.compile(r"(?:g_?\{?B-?L\}?|g_?\{?BL\}?|B-?L.*coupl|coupl.*B-?L)", re.I)
    mass = re.compile(r"(?:m_?\{?[XxV]\}?|mass)", re.I)
    for name, raw in files.items():
        if Path(name).suffix.lower() not in TEXT_EXT:
            continue
        text = decode(raw)
        # Paragraph-sized machine contexts only; no semantic invention.
        for block in re.split(r"\n\s*\n", text):
            if yp.search(block) and coupling.search(block) and mass.search(block):
                hits.append({"file": name, "excerpt": " ".join(block.split())[:1200]})
    return hits


def route_b_candidates(files):
    hits = []
    for name, raw in files.items():
        if Path(name).suffix.lower() not in TABLE_EXT:
            continue
        text = decode(raw)
        low = text.lower()
        if ("mass" in low or "m_x" in low or "mx" in low) and ("coupl" in low or "gbl" in low or "g_bl" in low) and ("yp" in low or "y_p" in low or "helium" in low):
            hits.append({"file": name, "sha256": sha256(raw), "bytes": len(raw)})
    return hits


def new_vector_assets(files):
    vector_ext = {".pdf", ".eps", ".svg"}
    out = []
    for name, raw in files.items():
        if Path(name).suffix.lower() not in vector_ext or name in KNOWN_BBN_VECTOR:
            continue
        low = name.lower()
        if "yp" in low or "bbn" in low or "helium" in low:
            out.append({"file": name, "sha256": sha256(raw), "bytes": len(raw)})
    return out


def classify(blob: bytes):
    got = sha256(blob)
    if got != EXPECTED_ARCHIVE_SHA256:
        return {"iteration":"0087f","classification":"INFRASTRUCTURE_FAIL_PRIMARY_HASH_MISMATCH","archive_sha256":got,"expected_archive_sha256":EXPECTED_ARCHIVE_SHA256}
    try:
        files = read_archive(blob)
    except Exception as exc:
        return {"iteration":"0087f","classification":"INFRASTRUCTURE_FAIL_ARCHIVE_EXTRACTION","archive_sha256":got,"error":repr(exc)}

    a = route_a_candidates(files)
    b = route_b_candidates(files)
    c = new_vector_assets(files)

    # Frozen fail-closed interpretation: automated lexical candidates are not
    # sufficient to establish an exact coupling-side function over the full tail.
    # PASS requires a source-provided machine table demonstrably keyed to BBN,
    # or a separately validated exact analytical relation. This audit does not
    # infer such a relation from prose contexts alone.
    route_a_pass = False
    route_b_pass = False
    route_c_pass = False
    classification = "BLOCKED_BBN_TAIL_ACTIONABILITY_AUTHORITY"
    return {
        "iteration":"0087f",
        "classification":classification,
        "scope":"Esseili-Kribs v2 BBN tail authority only; no topology recomposition",
        "archive_sha256":got,
        "archive_file_count":len(files),
        "frozen_tail_eV":list(TAIL_EV),
        "routes":{
            "A_exact_analytical_textual": {"pass":route_a_pass,"candidate_contexts":a,"reason":"no machine-validated exact BBN coupling function with explicit full-tail domain is promoted from prose"},
            "B_machine_readable_table": {"pass":route_b_pass,"candidate_files":b,"reason":"no qualifying source table is promoted unless mass/coupling/BBN identity and full-tail bracketing are explicit"},
            "C_genuinely_new_vector_authority": {"pass":route_c_pass,"candidate_assets":c,"reason":"new vector asset presence alone cannot reopen 0081a; unchanged calibration/path-identity criteria remain required"},
        },
        "accepted_inheritance":{
            "delta_Yp":"Yp(BSM)-Yp(SM)=0.008 at 95% CL",
            "known_vector_assets":sorted(KNOWN_BBN_VECTOR),
            "0081a_blocker_preserved":True,
        },
        "guards":{
            "no_raster_ocr_manual_digitization":True,
            "no_cmb_transform_borrowing":True,
            "no_anchor_requirement_relaxation":True,
            "no_partial_tail_extrapolation":True,
            "majorana_dirac_kept_separate":True,
            "bsm_response_scan_authorized":False,
        },
        "next_action":"preserve unresolved BBN tail; preregister restricted-below-1-eV completeness/final-lock audit",
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--archive", required=True)
    args=p.parse_args()
    blob=Path(args.archive).read_bytes()
    result=classify(blob)
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
    print("output_sha256", sha256(OUT.read_bytes()))
    return 0 if result["classification"].startswith(("PASS_","BLOCKED_")) else 2

if __name__ == "__main__":
    raise SystemExit(main())
