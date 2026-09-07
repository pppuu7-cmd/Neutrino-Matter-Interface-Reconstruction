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


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fetch_source():
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "NMIR-CMB-semantics/0080c"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def norm(s: str) -> str:
    s = s.replace("~", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def context(text: str, needle: str, radius=700):
    i = text.find(needle)
    if i < 0:
        return None
    return norm(text[max(0, i-radius):min(len(text), i+len(needle)+radius)])


def contains_0p3_0p4(ctx: str | None) -> bool:
    # Primary TeX writes the interval as e.g. `0.3$-$0.4`; allow TeX
    # punctuation between the already-frozen numeric endpoints, but do not
    # change either endpoint or the scientific criterion.
    return bool(ctx and re.search(r"0\.3[^0-9]{0,12}0\.4", ctx))


def classify_text(text: str):
    planck_ctx = context(text, "Current constraints from Planck data exclude")
    conservative_ctx = context(text, "conservative analysis suggests")

    # The pinned v2 source uses the macro `\dneff` and lowercase `figure`,
    # whereas the initial parser fixture used expanded Delta-N_eff text and
    # `Fig.`. Anchor on the frozen caption prose instead of a macro spelling.
    fig5_ctx = context(text, "Calculations of")
    fig6_ctx = context(text, "Same as figure")
    if fig6_ctx is None:
        fig6_ctx = context(text, "Same as Fig.")

    checks = {
        "planck_phrase": planck_ctx is not None,
        "planck_range_0p3_0p4": contains_0p3_0p4(planck_ctx),
        "planck_dataset_dependence": bool(planck_ctx and "depending on the choice of dataset" in planck_ctx),
        "conservative_phrase": conservative_ctx is not None,
        "conservative_range_0p3_0p4": contains_0p3_0p4(conservative_ctx),
        "conservative_95cl": bool(conservative_ctx and ("95\\% C.L." in conservative_ctx or "95% C.L." in conservative_ctx)),
        "dark_light_blue_ruled_out": bool(conservative_ctx and "dark and light blue are ruled out" in conservative_ctx),
        "green_strongly_disfavored": bool(conservative_ctx and re.search(r"(?:the )?green region strongly disfavored", conservative_ctx)),
        "fig5_levels": bool(fig5_ctx and all(x in fig5_ctx for x in ["0.05", "0.1", "0.2", "0.3", "0.4", "0.5"])),
        "fig5_color_order": bool(fig5_ctx and all(x in fig5_ctx for x in ["(pink)", "(red)", "(orange)", "(green)", "(light blue)", "(dark blue)"])),
        "fig6_same_as_fig5": bool(fig6_ctx and ("Same as figure" in fig6_ctx or "Same as Fig." in fig6_ctx) and "Dirac" in fig6_ctx),
    }
    passed = all(checks.values())
    return {
        "classification": "PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_95CL_SEMANTICS" if passed else "BLOCKED_COSMOLOGY_B_L_CMB_OBSERVATIONAL_SEMANTICS",
        "checks": checks,
        "contexts": {"planck": planck_ctx, "conservative": conservative_ctx, "figure5": fig5_ctx, "figure6": fig6_ctx},
        "frozen_nmir_semantics": {
            "hard_exclusion_delta_neff_min": 0.4,
            "confidence": "95% C.L.",
            "hard_excluded_colors": ["light blue", "dark blue"],
            "not_hard_excluded_color": "green",
            "green_semantics": "strongly disfavored only",
            "reason": "prospectively use weaker/high endpoint of source-stated 0.3-0.4 current constraint range; no geometry inspected in this gate",
        },
    }


def audit():
    raw = fetch_source()
    h = sha256(raw)
    if h != SOURCE_SHA256:
        raise RuntimeError(f"source SHA mismatch {h}")
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
        members = {m.name.lstrip("./"): m for m in tf.getmembers() if m.isfile()}
        if MAIN_TEX not in members:
            raise RuntimeError("main TeX missing")
        fh = tf.extractfile(members[MAIN_TEX])
        if fh is None:
            raise RuntimeError("main TeX unreadable")
        data = fh.read()
    text = data.decode("utf-8", errors="replace")
    result = classify_text(text)
    result.update({
        "iteration": "0080c",
        "source_url": SOURCE_URL,
        "source_sha256": SOURCE_SHA256,
        "main_tex": MAIN_TEX,
        "main_tex_sha256": sha256(data),
        "main_tex_bytes": len(data),
        "guard": "Primary textual semantics only; no vector path extraction, no manual figure reading, no scenario/envelope union, no response scan.",
    })
    return result


def main():
    r = audit()
    with open("esseili_kribs_cmb_semantics_0080c.json", "w", encoding="utf-8") as f:
        json.dump(r, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(r, indent=2, sort_keys=True))
    if r["classification"].startswith("BLOCKED"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
