#!/usr/bin/env python3
import hashlib
import io
import json
import re
import tarfile
import urllib.request

SOURCE_URL = "https://export.arxiv.org/e-print/2308.07955v2"
SOURCE_SHA256 = "484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c"
MAIN_TEX = "neff_arXiv_v2.tex"
MAIN_TEX_SHA256 = "f77b577688b3609c574985b05fc9a213709c958ded60a511478357f1f881d678"
MAJORANA_ASSET = "Presentation/CnstrntPlotMajoranaYp.pdf"
DIRAC_ASSET = "Presentation/CnstrntPlotDiracYp.pdf"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm(s: str) -> str:
    s = s.replace("~", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def context(text: str, needle: str, radius: int = 900):
    i = text.find(needle)
    if i < 0:
        return None
    return norm(text[max(0, i-radius):min(len(text), i+len(needle)+radius)])


def fetch_source() -> bytes:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "NMIR-BBN-semantics/0081"})
    with urllib.request.urlopen(req, timeout=90) as response:
        return response.read()


def decimal_candidates(ctx: str | None):
    if not ctx:
        return []
    return [float(x) for x in re.findall(r"(?<![\d.])(0\.\d+)(?![\d.])", ctx)]


def extract_bound(ctx: str | None):
    if not ctx:
        return None
    patterns = [
        r"(?:lesssim|leq|<|upper bound)[^0-9]{0,80}(0\.\d+)",
        r"(0\.\d+)[^0-9]{0,80}95\\%[^A-Za-z]{0,20}C\.?L\. ?",
    ]
    for pattern in patterns:
        m = re.search(pattern, ctx, re.I)
        if m:
            return float(m.group(1))
    vals = sorted(set(x for x in decimal_candidates(ctx) if 0 < x < 0.1))
    return vals[0] if len(vals) == 1 else None


def extract_cl(ctx: str | None):
    if not ctx:
        return None
    for pattern in [r"(\d{2,3})\\%\s*C\.?\s*L\. ?", r"(\d{2,3})\s*%\s*C\.?\s*L\. ?"]:
        m = re.search(pattern, ctx, re.I)
        if m:
            return int(m.group(1))
    return None


def definition_semantics(ctx: str | None):
    if not ctx:
        return {"recovered": False, "kind": None, "uses_absolute": None}
    has_delta = "Delta Y_p" in ctx or "\\Delta Y_p" in ctx or "dYp" in ctx
    has_bsm = "BSM" in ctx
    has_sm = "SM" in ctx
    if not (has_delta and has_bsm and has_sm):
        return {"recovered": False, "kind": None, "uses_absolute": None}
    absolute = bool("\\left|" in ctx or "\\abs" in ctx or re.search(r"\|\s*Y", ctx))
    signed = bool(re.search(r"BSM[^=]{0,80}-[^=]{0,80}SM", ctx, re.S))
    if absolute:
        return {"recovered": True, "kind": "absolute_difference", "uses_absolute": True}
    if signed:
        return {"recovered": True, "kind": "signed_BSM_minus_SM", "uses_absolute": False}
    return {"recovered": False, "kind": None, "uses_absolute": None}


def classify_text(text: str):
    fig7 = context(text, MAJORANA_ASSET)
    fig8 = context(text, DIRAC_ASSET)
    bound_ctx = context(text, "a conservative upper bound") or context(text, "A conservative upper bound")
    definition_ctx = context(text, "BSM deviation of helium abundance")

    threshold = extract_bound(bound_ctx)
    confidence = extract_cl(bound_ctx)
    definition = definition_semantics(definition_ctx)

    checks = {
        "fig7_majorana_yp": bool(fig7 and "Majorana" in fig7 and ("Y_p" in fig7 or "Yp" in fig7 or "dYp" in fig7 or "Delta Y" in fig7)),
        "fig8_dirac_same_semantics": bool(fig8 and "Dirac" in fig8 and ("Same as" in fig8 or "same as" in fig8)),
        "conservative_numeric_threshold_recovered": threshold is not None,
        "confidence_level_recovered": confidence is not None,
        "delta_yp_sign_or_absolute_convention_recovered": definition["recovered"],
        "bbn_not_cmb_threshold_context": bool(bound_ctx and ("Y_p" in bound_ctx or "Yp" in bound_ctx or "dYp" in bound_ctx or "helium" in bound_ctx.lower())),
    }

    if all(checks.values()):
        classification = "PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS"
    elif threshold is not None and confidence is not None:
        classification = "PARTIAL_PASS_BBN_THRESHOLD_ONLY"
    else:
        classification = "BLOCKED_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS"

    return {
        "classification": classification,
        "checks": checks,
        "frozen_source_result": {
            "delta_Yp_upper_bound": threshold,
            "confidence_level_percent": confidence,
            "delta_Yp_definition_kind": definition["kind"],
            "delta_Yp_uses_absolute_deviation": definition["uses_absolute"],
            "majorana_asset": MAJORANA_ASSET,
            "dirac_asset": DIRAC_ASSET,
        },
        "contexts": {
            "fig7": fig7,
            "fig8": fig8,
            "bound": bound_ctx,
            "definition": definition_ctx,
        },
    }


def audit():
    raw = fetch_source()
    source_hash = sha256(raw)
    if source_hash != SOURCE_SHA256:
        raise RuntimeError(f"source SHA mismatch: {source_hash}")
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
        members = {m.name.lstrip("./"): m for m in tf.getmembers() if m.isfile()}
        if MAIN_TEX not in members:
            raise RuntimeError("main TeX missing")
        fh = tf.extractfile(members[MAIN_TEX])
        if fh is None:
            raise RuntimeError("main TeX unreadable")
        data = fh.read()
    tex_hash = sha256(data)
    if tex_hash != MAIN_TEX_SHA256:
        raise RuntimeError(f"main TeX SHA mismatch: {tex_hash}")
    text = data.decode("utf-8", errors="replace")
    result = classify_text(text)
    result.update({
        "iteration": "0081",
        "source_url": SOURCE_URL,
        "source_sha256": SOURCE_SHA256,
        "main_tex": MAIN_TEX,
        "main_tex_sha256": MAIN_TEX_SHA256,
        "guard": "Source semantics only; no BBN vector-path/color selection, no geometry composition, no CMB substitution, no Majorana/Dirac union, no response scan."
    })
    return result


def main():
    result = audit()
    with open("esseili_kribs_bbn_semantics_0081.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["classification"].startswith("BLOCKED"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
