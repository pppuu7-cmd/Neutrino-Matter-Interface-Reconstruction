#!/usr/bin/env python3
import hashlib
import io
import json
import os
import re
import tarfile
import time
import urllib.request

SOURCES = {
    "hong_shin_yun_2021": {
        "arxiv": "2012.05427v3",
        "url": "https://export.arxiv.org/e-print/2012.05427v3",
        "sha256": "6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc",
    },
    "cerdeno_et_al_2021": {
        "arxiv": "2106.11660v3",
        "url": "https://export.arxiv.org/e-print/2106.11660v3",
        "sha256": "f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d",
    },
    "shin_yun_2022": {
        "arxiv": "2110.03362v2",
        "url": "https://export.arxiv.org/e-print/2110.03362v2",
        "sha256": "7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd",
    },
}

TEXT_EXTS = {".tex", ".sty", ".cls", ".txt"}
CONSTRAINT_WORDS = ("constraint", "bound", "exclud", "limit")
NONCONTROL_WORDS = ("diagram", "spectrum", "spectral", "cooling history", "hint")
REVISION_WORDS = ("revisit", "reconsider", "improv", "stronger", "previous", "earlier", "update")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str, attempts: int = 3) -> bytes:
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0082a-semantic-scope/1.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except Exception as exc:
            last = exc
            if i + 1 < attempts:
                time.sleep(2 ** i)
    raise RuntimeError(f"fetch failed: {url}: {last}")


def decode(b: bytes) -> str:
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("latin-1", errors="replace")


def normalize(s: str) -> str:
    s = s.lower().replace("−", "-").replace("–", "-")
    s = re.sub(r"%[^\n]*", " ", s)
    s = s.replace("\\!", "").replace("\\,", " ").replace("~", " ")
    s = re.sub(r"\\(?:mathrm|rm|text|operatorname|mathcal|mathbf)\s*\{([^{}]*)\}", r" \1 ", s)
    s = s.replace("{", "").replace("}", "").replace("$", " ")
    s = s.replace("\\prime", "'")
    s = re.sub(r"\\[a-zA-Z@]+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def has_bl(s: str) -> bool:
    n = normalize(s)
    return bool(
        re.search(r"u\s*\(?1\)?[^\n]{0,50}b\s*-\s*l", n)
        or re.search(r"\bb\s*-\s*l\b", n)
        or "b-l gauge" in n
    )


def balanced_arg(text: str, command: str, start: int = 0):
    m = re.search(r"\\" + re.escape(command) + r"\s*(?:\[[^\]]*\]\s*)?\{", text[start:], flags=re.S)
    if not m:
        return None
    open_pos = start + m.end() - 1
    depth = 0
    for i in range(open_pos, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[open_pos + 1:i]
    return None


def resolve_include(token: str, names):
    clean_tok = token.strip().lstrip("./")
    base = os.path.basename(clean_tok)
    stem, ext = os.path.splitext(base)
    out = []
    for name in names:
        n = name.lstrip("./")
        b = os.path.basename(n)
        s, e = os.path.splitext(b)
        if n == clean_tok or b == base or (not ext and s == stem):
            out.append(n)
    return sorted(set(out))


def nearest_paragraph_before(text, pos, max_chars=1600):
    lo = max(0, pos - max_chars)
    chunk = text[lo:pos]
    split = re.split(r"\n\s*\n", chunk)
    return split[-1] if split else chunk


def nearest_paragraph_after(text, pos, max_chars=1600):
    chunk = text[pos:pos + max_chars]
    split = re.split(r"\n\s*\n", chunk)
    return split[0] if split else chunk


def scope_tags(s: str):
    n = normalize(s)
    tags = []
    def add(cond, tag):
        if cond and tag not in tags:
            tags.append(tag)
    add("sn1987a" in n or "sn 1987a" in n, "SN1987A")
    add("ns1987a" in n or "ns 1987a" in n, "NS1987A")
    add("cas a" in n or "cassiopeia a" in n, "Cas_A")
    add("young neutron star" in n or "young ns" in n, "young_neutron_star_cooling")
    add("medium effect" in n, "medium_effects")
    add("transverse" in n, "transverse")
    add("longitudinal" in n, "longitudinal")
    if any(w in n for w in ("other constraint", "existing constraint", "combined constraint", "summary constraint", "constraints on")):
        add(True, "global_summary_other_constraints")
    return tags


def parse_figures(text: str, member_names):
    figures = []
    rx = re.compile(r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", re.S | re.I)
    for idx, m in enumerate(rx.finditer(text)):
        body = m.group(1)
        caption = balanced_arg(body, "caption") or ""
        label = balanced_arg(body, "label") or ""
        toks = re.findall(r"\\includegraphics(?:\s*\[[^\]]*\])?\s*\{([^{}]+)\}", body, flags=re.S | re.I)
        resolved = {t.strip(): resolve_include(t, member_names) for t in toks}
        before = nearest_paragraph_before(text, m.start())
        after = nearest_paragraph_after(text, m.end())
        associated = " ".join((caption, before, after))
        ncap = normalize(caption)
        nassoc = normalize(associated)
        bl_sem = has_bl(associated)
        constraint_sem = any(w in nassoc for w in CONSTRAINT_WORDS)
        caption_constraint = any(w in ncap for w in CONSTRAINT_WORDS)
        noncontrol_caption = any(w in ncap for w in NONCONTROL_WORDS) and not caption_constraint
        accepted = bool(toks and bl_sem and constraint_sem and not noncontrol_caption)
        scopes = scope_tags(associated) if accepted else []
        if accepted and not scopes:
            scopes = ["global_summary_other_constraints"]
        figures.append({
            "index": idx,
            "label": label,
            "caption_normalized": ncap[:1200],
            "include_tokens": [t.strip() for t in toks],
            "resolved_assets": resolved,
            "bl_semantics": bl_sem,
            "constraint_semantics": constraint_sem,
            "noncontrol_caption": noncontrol_caption,
            "accepted_bl_constraint_figure": accepted,
            "scope_tags": scopes,
        })
    return figures


def parameter_convention(text: str):
    raw = text
    n = normalize(text)
    coupling_patterns = [
        r"g_?\s*\{?\s*b\s*-\s*l\s*\}?",
        r"g\s*\^?\s*'?\s*[^\n]{0,30}b\s*-\s*l",
        r"b\s*-\s*l\s+gauge\s+coupling",
        r"gauge\s+coupling[^\n]{0,50}b\s*-\s*l",
    ]
    mass_patterns = [
        r"m_?\s*\{?\s*z[^\n]{0,12}'",
        r"m_?\s*\{?\s*x\s*\}?",
        r"mass\s+of\s+(?:the\s+)?(?:b\s*-\s*l|gauge|vector)[^\n]{0,80}",
        r"gauge\s+boson\s+mass",
        r"vector\s+boson\s+mass",
    ]
    coupling_matches = []
    mass_matches = []
    for p in coupling_patterns:
        for m in re.finditer(p, n, flags=re.I):
            coupling_matches.append(n[max(0, m.start()-100):m.end()+120])
    for p in mass_patterns:
        for m in re.finditer(p, n, flags=re.I):
            mass_matches.append(n[max(0, m.start()-100):m.end()+120])
    # Preserve a compact source-native symbol inventory independent of geometry.
    raw_symbol_candidates = sorted(set(re.findall(r"g\s*_\s*\{[^{}]{1,30}\}", raw)))[:30]
    raw_mass_candidates = sorted(set(re.findall(r"m\s*_\s*\{[^{}]{1,30}\}", raw)))[:30]
    unit_tokens = sorted(set(re.findall(r"\b(?:eV|keV|MeV|GeV)\b", raw)))
    passed = bool(coupling_matches and mass_matches)
    return {
        "passed": passed,
        "coupling_evidence": coupling_matches[:12],
        "mass_evidence": mass_matches[:12],
        "raw_coupling_symbol_candidates": raw_symbol_candidates,
        "raw_mass_symbol_candidates": raw_mass_candidates,
        "unit_tokens": unit_tokens,
    }


def strict_explicit_replacement(n: str, target_patterns):
    action = r"(?:revisit|reconsider|replace|revise|update|improv|stronger|correct|supersed)"
    for target in target_patterns:
        if re.search(action + r"[^.]{0,180}" + target, n, flags=re.I):
            return True
        if re.search(target + r"[^.]{0,180}" + action, n, flags=re.I):
            return True
    return False


def shin_revision(text: str):
    n = normalize(text)
    windows = []
    for word in REVISION_WORDS:
        for m in re.finditer(word, n):
            windows.append(n[max(0, m.start()-650):m.end()+900])
    joined = " ".join(windows)
    bl = has_bl(joined)
    sn = "sn1987a" in joined or "sn 1987a" in joined
    transverse = "transverse" in joined
    longitudinal = "longitudinal" in joined
    revised_sn_transverse = bool(bl and sn and transverse and any(w in joined for w in REVISION_WORDS))
    new_longitudinal = bool(bl and sn and longitudinal and ("new" in joined or "exclud" in joined or "bound" in joined or "constraint" in joined))
    return {
        "revision_windows": windows[:20],
        "revised_sn1987a_transverse": revised_sn_transverse,
        "new_sn1987a_longitudinal_region": new_longitudinal,
        "explicit_replace_ns1987a": strict_explicit_replacement(n, (r"ns1987a", r"ns 1987a")),
        "explicit_replace_cas_a": strict_explicit_replacement(n, (r"cas a", r"cassiopeia a")),
        "explicit_replace_young_ns": strict_explicit_replacement(n, (r"young neutron star", r"young ns")),
    }


def inspect_source(raw: bytes, key: str, cfg: dict):
    if sha256(raw) != cfg["sha256"]:
        raise RuntimeError(f"source SHA mismatch for {key}")
    texts = []
    names = []
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
        for m in tf.getmembers():
            if not m.isfile():
                continue
            name = m.name.lstrip("./")
            names.append(name)
            if os.path.splitext(name.lower())[1] in TEXT_EXTS:
                fh = tf.extractfile(m)
                if fh is not None:
                    texts.append((name, decode(fh.read())))
    # Parse figures in each TeX-like source file separately to preserve same-environment identity.
    figures = []
    for name, text in texts:
        if os.path.splitext(name.lower())[1] != ".tex":
            continue
        for f in parse_figures(text, names):
            f["source_member"] = name
            figures.append(f)
    accepted = [f for f in figures if f["accepted_bl_constraint_figure"]]
    whole = "\n".join(t for _, t in texts)
    param = parameter_convention(whole)
    revision = shin_revision(whole) if key == "shin_yun_2022" else None
    scopes = sorted({tag for f in accepted for tag in f["scope_tags"]})
    source_pass = bool(accepted and scopes and param["passed"])
    if key == "shin_yun_2022":
        source_pass = source_pass and revision["revised_sn1987a_transverse"] and revision["new_sn1987a_longitudinal_region"]
    return {
        "source_key": key,
        "arxiv": cfg["arxiv"],
        "archive_sha256": cfg["sha256"],
        "all_figures": figures,
        "accepted_constraint_figures": accepted,
        "accepted_scope_tags": scopes,
        "parameter_convention": param,
        "shin_yun_revision_scope": revision,
        "source_semantic_scope_pass": source_pass,
    }


def classify(results):
    if all(r["source_semantic_scope_pass"] for r in results.values()):
        return "PASS_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY"
    # Distinguish ambiguity from missing authority. Multiple accepted figures are not by themselves ambiguous
    # because prereg allows distinct scopes; PARTIAL is reserved for same-scope indistinguishability.
    for r in results.values():
        if not r["accepted_constraint_figures"] or not r["parameter_convention"]["passed"]:
            return "BLOCKED_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY"
    rev = results["shin_yun_2022"]["shin_yun_revision_scope"]
    if not (rev and rev["revised_sn1987a_transverse"] and rev["new_sn1987a_longitudinal_region"]):
        return "BLOCKED_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY"
    # Conservative same-scope duplicate test after all hard semantic checks.
    for r in results.values():
        scope_to_assets = {}
        for f in r["accepted_constraint_figures"]:
            key = tuple(f["scope_tags"])
            assets = tuple(a for vals in f["resolved_assets"].values() for a in vals)
            scope_to_assets.setdefault(key, set()).update(assets)
        if any(len(v) > 1 for v in scope_to_assets.values()):
            return "PASS_PARTIAL_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY"
    return "PASS_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY"


def audit(fetcher=fetch):
    results = {}
    for key, cfg in SOURCES.items():
        results[key] = inspect_source(fetcher(cfg["url"]), key, cfg)
    return {
        "iteration": "0082a",
        "classification": classify(results),
        "sources": results,
        "guard": "TeX semantic/scope and parameter-convention authority only; no PDF vector drawing/path/color inspection, axis calibration, numerical contour extraction, cross-paper union/intersection, broad supersession claim, global envelope, or response scan.",
    }


def main():
    r = audit()
    out = "bl_stellar_sn_semantic_scope_0082a.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(r, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(r, indent=2, sort_keys=True))
    if r["classification"].startswith("BLOCKED_"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
