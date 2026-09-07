#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.request

ARXIV_URL = "https://export.arxiv.org/e-print/2110.03362v2"
EXPECTED_SHA256 = "7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd"

BL_RE = re.compile(r"B\s*[-–]?\s*L|U\s*\(\s*1\s*\)\s*_?\{?B\s*[-–]?\s*L\}?|B\\!-?L", re.I)
OBS_RE = re.compile(r"SN\s*1987A|NS\s*1987A|Cas\s*A|neutron\s+star|supernova", re.I)
REV_RE = re.compile(r"revis\w*|supersed\w*|replac\w*|weaken\w*|strengthen\w*|improv\w*|update\w*|previous\w*|earlier\w*|compared?\s+to", re.I)
NUM_RE = re.compile(r"(?:<|>|\\lesssim|\\gtrsim|\\sim|=)?\s*(?:\d+(?:\.\d*)?|\.\d+)\s*(?:\\times\s*)?10\s*\^\s*\{?[-+]?\d+\}?|(?:<|>|=|\\lesssim|\\gtrsim|\\sim)\s*\d+(?:\.\d*)?(?:e|E)[-+]?\d+")
# Source-native coupling relations. This intentionally excludes unrelated nearby
# density/luminosity/temperature numbers that happen to occur in a B-L paragraph.
COUPLING_REL_RE = re.compile(
    r"e\s*\^\s*\\prime(?:\s*m_\{?[^<>=,;]{0,80})?\s*"
    r"(?:<|>|\\lesssim|\\gtrsim|\\sim|=)\s*"
    r"(?:\d+(?:\.\d*)?|\.\d+)\s*(?:\\times\s*)?10\s*\^\s*\{?[-+]?\d+\}?",
    re.I,
)
MASS_RE = re.compile(r"(?:m_[^\s,;]{0,50}|mass[^,;.]{0,100})(?:MeV|keV|eV|GeV|O\s*\([^)]*\)|\\mathcal\{O\}[^,;.]*)", re.I)
CONF_RE = re.compile(r"\b(?:90|95|99)\s*\\?%|confidence|C\.L\.", re.I)


def normalize_tex(s):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = s.replace("~", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def source_members(blob):
    out = []
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:*") as tf:
        for m in tf.getmembers():
            if not m.isfile() or m.size > 5_000_000:
                continue
            if not re.search(r"\.(tex|txt|md)$", m.name, re.I):
                continue
            f = tf.extractfile(m)
            if f is None:
                continue
            raw = f.read()
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                text = raw.decode("latin-1", errors="replace")
            out.append((m.name, text))
    return out


def contexts(text, window=650):
    clean = normalize_tex(text)
    spans = []
    for m in BL_RE.finditer(clean):
        a, b = max(0, m.start()-window), min(len(clean), m.end()+window)
        spans.append(clean[a:b])
    seen, uniq = set(), []
    for x in spans:
        key = hashlib.sha256(x.encode()).hexdigest()
        if key not in seen:
            seen.add(key); uniq.append(x)
    return uniq


def classify_record(ctx, filename):
    nums = [m.group(0).strip() for m in NUM_RE.finditer(ctx)]
    coupling_relations = [m.group(0).strip() for m in COUPLING_REL_RE.finditer(ctx)]
    obs = sorted(set(m.group(0) for m in OBS_RE.finditer(ctx)), key=str.lower)
    rev = sorted(set(m.group(0) for m in REV_RE.finditer(ctx)), key=str.lower)
    masses = [m.group(0).strip() for m in MASS_RE.finditer(ctx)]
    conf = [m.group(0).strip() for m in CONF_RE.finditer(ctx)]
    return {
        "file": filename,
        "numbers": nums,
        "coupling_relations": coupling_relations,
        "observations": obs,
        "revision_terms": rev,
        "mass_phrases": masses,
        "confidence_terms": conf,
        "context": ctx,
    }


def audit(blob):
    sha = hashlib.sha256(blob).hexdigest()
    result = {"source_url": ARXIV_URL, "expected_sha256": EXPECTED_SHA256, "archive_sha256": sha}
    if sha != EXPECTED_SHA256:
        result.update({"classification":"INFRASTRUCTURE_FAIL_ARCHIVE_HASH", "records":[]})
        return result
    members = source_members(blob)
    records = []
    for name, text in members:
        for ctx in contexts(text):
            records.append(classify_record(ctx, name))
    coupling = [r for r in records if r["coupling_relations"]]
    bound = [r for r in coupling if r["observations"]]
    revision = [r for r in records if r["revision_terms"]]
    unresolved = [r for r in coupling if not r["observations"]]
    if bound and not unresolved:
        classification = "PASS_SHIN_YUN_B_L_REVISION_SCOPE_AUTHORITY" if revision else "PASS_SHIN_YUN_B_L_ANALYTICAL_ANCHOR_ONLY"
    else:
        classification = "BLOCKED_SHIN_YUN_B_L_SOURCE_TEXT_AUTHORITY"
    result.update({
        "classification": classification,
        "tex_files": [n for n,_ in members],
        "record_count": len(records),
        "coupling_record_count": len(coupling),
        "bound_record_count": len(bound),
        "revision_record_count": len(revision),
        "unresolved_coupling_record_count": len(unresolved),
        "records": records,
    })
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="optional local source archive")
    ap.add_argument("--output", default="data/shin_yun_bl_0084.json")
    args = ap.parse_args()
    if args.source:
        blob = open(args.source, "rb").read()
    else:
        req = urllib.request.Request(ARXIV_URL, headers={"User-Agent":"NMIR-reproducibility-audit/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            blob = r.read()
    res = audit(blob)
    import os
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    keys=["classification","archive_sha256","record_count","coupling_record_count","bound_record_count","revision_record_count","unresolved_coupling_record_count"]
    print(json.dumps({k:res[k] for k in keys if k in res}, indent=2))
    if res["classification"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(2)

if __name__ == "__main__":
    main()
