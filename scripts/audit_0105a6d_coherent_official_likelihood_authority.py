#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.request

ZENODO_RECORDS = ("1228631", "3903810")
ARXIV_IDS = ("1708.01294v1", "2003.10630v7")
TERMS = (
    "likelihood", "loglikelihood", "log likelihood", "nll", "roofit", "roonllvar",
    "rooaddpdf", "roodatahist", "poisson", "chi2", "chi-square", "gaussian constraint",
    "constraint", "profile", "nuisance", "covariance", "correlation", "minuit", "fitto",
)
MAX_TEXT_BYTES = 25_000_000
UA = "NMIR-v2-0105a6d-authority-audit/1.0"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read(), r.geturl()


def sha256(b): return hashlib.sha256(b).hexdigest()


def term_hits(text):
    lo = text.lower()
    out = {}
    for t in TERMS:
        pat = re.escape(t.lower())
        hits = [m.start() for m in re.finditer(pat, lo)]
        if hits:
            out[t] = {"count": len(hits), "first_offsets": hits[:12]}
    return out


def decode_text(b):
    if len(b) > MAX_TEXT_BYTES or b"\x00" in b[:4096]: return None
    try:
        s = b.decode("utf-8")
    except UnicodeDecodeError:
        try: s = b.decode("latin-1")
        except Exception: return None
    printable = sum(ch.isprintable() or ch in "\r\n\t" for ch in s[:10000])
    if s and printable / min(len(s),10000) < 0.90: return None
    return s


def zenodo_record(record):
    meta_b, meta_url = get(f"https://zenodo.org/api/records/{record}")
    meta = json.loads(meta_b)
    files = []
    for f in meta.get("files", []):
        name = f.get("key") or f.get("filename")
        link = (f.get("links") or {}).get("self") or (f.get("links") or {}).get("content")
        entry = {"filename": name, "provider_checksum": f.get("checksum"), "provider_size": f.get("size"), "provider_url": link}
        if not link:
            entry["retrieval"] = "missing_provider_link"; files.append(entry); continue
        b, resolved = get(link)
        entry.update({"resolved_url": resolved, "size_bytes": len(b), "sha256": sha256(b)})
        text = decode_text(b)
        if text is not None:
            entry["text_sha256"] = sha256(text.encode("utf-8"))
            entry["term_hits"] = term_hits(text)
            entry["text_decodable"] = True
        else:
            entry["text_decodable"] = False
        files.append(entry)
    return {"record": record, "metadata_url": meta_url, "metadata_sha256": sha256(meta_b), "files": files}


def arxiv_source(arxiv_id):
    b, resolved = get(f"https://export.arxiv.org/e-print/{arxiv_id}")
    out = {"arxiv": arxiv_id, "resolved_url": resolved, "archive_size_bytes": len(b), "archive_sha256": sha256(b), "members": []}
    # arXiv e-print may be tar(.gz) or a single source file.
    try:
        tf = tarfile.open(fileobj=io.BytesIO(b), mode="r:*")
        for m in tf.getmembers():
            if not m.isfile() or m.size > MAX_TEXT_BYTES: continue
            fh = tf.extractfile(m)
            if fh is None: continue
            mb = fh.read()
            text = decode_text(mb)
            if text is None: continue
            out["members"].append({"path": m.name, "size_bytes": len(mb), "sha256": sha256(mb), "term_hits": term_hits(text)})
    except tarfile.TarError:
        text = decode_text(b)
        if text is not None:
            out["members"].append({"path": "single_source", "size_bytes": len(b), "sha256": sha256(b), "term_hits": term_hits(text)})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()
    result = {
        "benchmark": "NMIR-V2-0105A6D-STAGE-A",
        "git_sha": args.git_sha,
        "stage": "official_authority_inventory_only",
        "status": "PASS_0105A6D_STAGE_A_OFFICIAL_AUTHORITY_INVENTORY_NONDISCOVERY",
        "sm_null_reproduction_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "semantic_completeness_classified": False,
        "zenodo": {}, "arxiv_sources": {}, "terms": list(TERMS),
    }
    for rec in ZENODO_RECORDS:
        result["zenodo"][rec] = zenodo_record(rec)
    for aid in ARXIV_IDS:
        result["arxiv_sources"][aid] = arxiv_source(aid)
    raw = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    with open(args.output, "wb") as f: f.write(raw)
    print(raw.decode(), end="")
    print("result_sha256=" + sha256(raw))

if __name__ == "__main__": main()
