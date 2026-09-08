#!/usr/bin/env python3
"""Conformance wrapper for frozen NMIR 0085.

Scientific contract is unchanged. The only repair is removal of literal TeX
math-mode `$` delimiters during source-text normalization.
"""
import json
import audit_wagner_identity_free_envelope_0085 as base

_original_normalize_tex = base.normalize_tex


def normalize_tex_r1(s: str) -> str:
    return _original_normalize_tex(s).replace("$", " ")


# source_text_authority resolves normalize_tex from the base module's globals.
base.normalize_tex = normalize_tex_r1


def audit(fetcher=base.fetch):
    r = base.audit(fetcher=fetcher)
    r["iteration"] = "0085-r1"
    r["parent_gate"] = "0085"
    r["parser_conformance"] = "remove_literal_TeX_math_mode_dollar_delimiters_only"
    return r


def main():
    r = audit()
    fn = "wagner_identity_free_upper_envelope_0085_r1.json"
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(r, f, indent=2, sort_keys=True)
        f.write("\n")
    summary_keys = [
        "iteration", "parent_gate", "classification", "eps_sha256",
        "source_authority_ok", "topology", "component_count", "monotonic_ok",
        "roundtrip_max_abs_eps", "supported_mass_min_eV", "supported_mass_max_eV",
        "supported_grid_point_count", "active_component_sample_counts",
        "name_order_invariance_max_decade", "fine_shared_max_decade",
        "support_runs", "envelope_semantics"
    ]
    print(json.dumps({k: r.get(k) for k in summary_keys}, indent=2, sort_keys=True))
    if not r["classification"].startswith("PASS_"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
