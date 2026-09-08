#!/usr/bin/env python3
import hashlib, io, json, os, re, tarfile, urllib.request

URL = "https://export.arxiv.org/e-print/2211.11905v2"
ARCHIVE_SHA256 = "783019f9bb927b69fcdf4fcb3f239729fa9c029e0e3b16ad69d6a777965a355a"
TEX_PATH = "COHERENT-Combined-v2.tex"
TEX_SHA256 = "33e92629a34c16411f1541b2fd2793228953baac48edf099fcbb72efcf44f6a4"
TERMS = [
    r"chi", r"likelihood", r"minimum", r"best\s*[- ]?fit", r"standard model", r"\bSM\b",
    r"CsI", r"LAr", r"combined", r"B\s*-?\s*L", r"vector mediator"
]
NUMERIC_REL = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:\s*[x×*]\s*10\s*\^?\s*\{?[-+]?\d+\}?)?(?![A-Za-z])")


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def get_tex(data):
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as tf:
        m = tf.getmember(TEX_PATH)
        f = tf.extractfile(m)
        if f is None:
            raise RuntimeError("tex_member_unreadable")
        return f.read()


def extract_contexts(text):
    lines = text.splitlines()
    regexes = [(t, re.compile(t, re.I)) for t in TERMS]
    hits = []
    seen = set()
    for i, line in enumerate(lines):
        matched = [label for label, rx in regexes if rx.search(line)]
        if not matched and not NUMERIC_REL.search(line):
            continue
        lo, hi = max(0, i-3), min(len(lines), i+4)
        key = (lo, hi)
        if key in seen:
            continue
        seen.add(key)
        block = "\n".join(lines[lo:hi])
        hits.append({
            "start_line": lo + 1,
            "end_line": hi,
            "matched_terms": matched,
            "has_numeric_relation": bool(NUMERIC_REL.search(block)),
            "raw_context": block,
        })
    return hits


def main():
    out_path = os.environ.get("NMIR_0086A_OUTPUT", "artifacts/deromeri_coherent_benchmark_authority_0086a.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    result = {"gate":"0086a", "classification":"INFRASTRUCTURE_FAIL", "source":"arXiv:2211.11905v2"}
    try:
        req = urllib.request.Request(URL, headers={"User-Agent":"NMIR-reproducibility-audit/1.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            archive = r.read()
        result["archive_sha256"] = sha256(archive)
        if result["archive_sha256"] != ARCHIVE_SHA256:
            raise RuntimeError("archive_hash_mismatch")
        tex = get_tex(archive)
        result["tex_sha256"] = sha256(tex)
        if result["tex_sha256"] != TEX_SHA256:
            raise RuntimeError("tex_hash_mismatch")
        text = tex.decode("utf-8", errors="strict")
        contexts = extract_contexts(text)
        result["context_count"] = len(contexts)
        result["contexts"] = contexts
        result["classification"] = "PASS_DEROMERI_COHERENT_BENCHMARK_EVIDENCE_EXTRACTION"
    except Exception as e:
        result["error"] = f"{type(e).__name__}:{e}"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    print(json.dumps({k:result.get(k) for k in ["classification","archive_sha256","tex_sha256","context_count","error"]}, sort_keys=True))
    return 0 if result["classification"] == "PASS_DEROMERI_COHERENT_BENCHMARK_EVIDENCE_EXTRACTION" else 2

if __name__ == "__main__":
    raise SystemExit(main())
