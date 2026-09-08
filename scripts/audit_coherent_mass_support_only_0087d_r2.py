#!/usr/bin/env python3
"""NMIR 0087d-r2 exact B-L semantic parser-conformance wrapper.

Scientific contract is unchanged from prereg 0087d. This repair is limited to
literal B-minus-L lexical recognition required by amendment 0087d-r2. The
starred/unstarred includegraphics repair from r1 is retained.
"""
import json
import pathlib
import re

import audit_coherent_mass_support_only_0087d_r1 as r1

base = r1.base


_TEX_SPACING = re.compile(r"\\(?:!|,|:|;|>|quad|qquad|enspace|thinspace|medspace|thickspace)\s*")


def bl_context_r2(s: str) -> bool:
    """Accept only an explicit B-minus-L token after harmless TeX normalization."""
    q = _TEX_SPACING.sub("", s)
    q = q.replace("$", "")
    q = q.replace("{", "").replace("}", "")
    q = q.replace("−", "-").replace("–", "-").replace("—", "-")
    q = re.sub(r"\s+", " ", q)
    return bool(re.search(r"(?<![A-Za-z])B\s*-\s*L(?![A-Za-z])", q, re.I))


# r1.figure_candidates_r1 dereferences base.bl_context at call time, so this
# exact-semantic replacement automatically constrains the already-authorized
# starred/unstarred includegraphics parser without touching figure geometry.
base.bl_context = bl_context_r2
base.figure_candidates = r1.figure_candidates_r1


def audit(fetcher=base.fetch):
    r = base.audit(fetcher=fetcher)
    r["iteration"] = "0087d-r2"
    r["parent_gate"] = "0087d"
    r["parser_conformance"] = (
        "literal B-minus-L lexical-semantic recognition after harmless TeX "
        "spacing normalization; retains r1 starred/unstarred includegraphics"
    )
    return r


def main():
    fn = pathlib.Path("coherent_mass_support_only_0087d_r2.json")
    try:
        r = audit()
    except (OSError, RuntimeError, base.pymupdf.FileDataError, base.tarfile.TarError) as e:
        r = {
            "iteration": "0087d-r2",
            "parent_gate": "0087d",
            "classification": "INFRASTRUCTURE_FAIL_0087D_R2",
            "reason": repr(e),
        }
    fn.write_text(json.dumps(r, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(r, indent=2, sort_keys=True))
    if r["classification"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(3)
    if r["classification"] != "PASS_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
