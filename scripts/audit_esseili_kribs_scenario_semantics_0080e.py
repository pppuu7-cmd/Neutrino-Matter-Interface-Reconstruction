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


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fetch_source() -> bytes:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "NMIR-scenario-semantics/0080e"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def norm(s: str) -> str:
    s = s.replace("~", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def context(text: str, needle: str, radius: int = 700):
    i = text.find(needle)
    if i < 0:
        return None
    return norm(text[max(0, i-radius):min(len(text), i + len(needle) + radius)])


def sentence_like_chunks(text: str):
    # Keep TeX source wording but make an auditable list of prose-sized chunks.
    flat = norm(text)
    return [c.strip() for c in re.split(r"(?<=[.!?])\s+", flat) if c.strip()]


def combination_candidate_contexts(text: str):
    """Return only source chunks that could prescribe composing Majorana/Dirac results.

    Nuclear/model-building phrases such as 'combined with the Dirac mass terms' do not
    qualify unless the same chunk also carries an explicit result-composition keyword.
    """
    result = []
    compose = re.compile(
        r"\b(combin(?:e|ed|ing|ation)|marginali[sz]|weight(?:ed|ing)?|"
        r"union|intersection|average|prefer(?:red|ence)?|supersed(?:e|es|ed)|"
        r"select(?:ed|ion)?|choose|choice)\b",
        re.I,
    )
    result_scope = re.compile(r"\b(constraint|bound|result|scenario|case|figure|fig\.|likelihood|posterior)\b", re.I)
    for chunk in sentence_like_chunks(text):
        low = chunk.lower()
        if "majorana" in low and "dirac" in low and compose.search(chunk) and result_scope.search(chunk):
            result.append(chunk)
    return result


def classify_text(text: str):
    # Frozen positive anchors from the primary source's scenario definition.
    two_scenarios = context(text, "two scenarios")
    dirac_case = context(text, "Dirac case")
    alternative_majorana = context(text, "The alternative")
    majorana_fig = context(text, "Majorana'' neutrino case") or context(text, 'Majorana" neutrino case')
    dirac_fig = context(text, "Dirac'' neutrino case") or context(text, 'Dirac" neutrino case')

    checks = {
        "two_scenarios_explicit": bool(two_scenarios and "two scenarios" in two_scenarios and "Dirac" in two_scenarios and "Majorana" in two_scenarios),
        "dirac_one_of_two_cases": bool(dirac_case and "one of the two cases" in dirac_case),
        "majorana_explicit_alternative": bool(alternative_majorana and "Majorana case" in alternative_majorana and "alternative" in alternative_majorana.lower()),
        "majorana_and_dirac_results_separate": bool(majorana_fig and dirac_fig),
    }

    composition_candidates = combination_candidate_contexts(text)
    explicit_common_rule = len(composition_candidates) > 0

    if all(checks.values()) and not explicit_common_rule:
        classification = "PASS_COSMOLOGY_B_L_SCENARIO_CONDITIONAL_AUTHORITY"
    elif explicit_common_rule:
        classification = "PASS_COSMOLOGY_B_L_COMMON_COMBINATION_AUTHORITY"
    else:
        classification = "BLOCKED_COSMOLOGY_B_L_SCENARIO_SEMANTICS"

    return {
        "classification": classification,
        "checks": checks,
        "contexts": {
            "two_scenarios": two_scenarios,
            "dirac_case": dirac_case,
            "alternative_majorana": alternative_majorana,
            "majorana_figure": majorana_fig,
            "dirac_figure": dirac_fig,
        },
        "explicit_common_combination_rule_detected": explicit_common_rule,
        "common_combination_candidate_contexts": composition_candidates,
        "ledger_semantics": {
            "majorana": "separate scenario-conditioned branch",
            "dirac": "separate scenario-conditioned branch",
            "scenario_independent_union_or_intersection_authorized": explicit_common_rule,
            "external_neutrino_nature_assumption_used": False,
        },
    }


def audit():
    raw = fetch_source()
    source_hash = sha256(raw)
    if source_hash != SOURCE_SHA256:
        raise RuntimeError(f"source SHA mismatch {source_hash}")
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
        raise RuntimeError(f"main TeX SHA mismatch {tex_hash}")
    text = data.decode("utf-8", errors="replace")
    result = classify_text(text)
    result.update({
        "iteration": "0080e",
        "source_url": SOURCE_URL,
        "source_sha256": SOURCE_SHA256,
        "main_tex": MAIN_TEX,
        "main_tex_sha256": MAIN_TEX_SHA256,
        "main_tex_bytes": len(data),
        "guard": "Primary TeX scenario semantics only; no geometry composition, external neutrino-nature assumption, BBN addition, global-envelope union, or BSM response scan.",
    })
    return result


def main():
    r = audit()
    with open("esseili_kribs_scenario_semantics_0080e.json", "w", encoding="utf-8") as f:
        json.dump(r, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(r, indent=2, sort_keys=True))
    if r["classification"].startswith("BLOCKED"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
