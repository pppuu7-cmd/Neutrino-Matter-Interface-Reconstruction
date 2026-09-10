#!/usr/bin/env python3
import argparse, hashlib, io, json, re, time, urllib.parse, urllib.request
from pathlib import Path
from pypdf import PdfReader

FILES = {
    "csi": {
        "record": "1228631",
        "README": "978ab4a7e7b01a463dd7e9d4e8938573ad736b78447db79717b5d5b57922f097",
        "coherent_parameters.yaml": "daa4f3feaeb5499cb1d876f8ea39f3cfd571f998a6ab92e9cdf552afc78b67e8",
        "coherentCollaboration_dataReleaseCompanion_april2018.pdf": "dd0bc860c53712cd0ebc17ce0ffdb8b88f62f7b64dbdac6389d79782a18556c1",
    },
    "ar": {
        "record": "3903810",
        "LArParametersAnlA.yaml": "a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e",
        "CENNS10DataReleaseCompanion.pdf": "ecfef10e2cb768f0d781b22e712b205fe2d56e5f8702a6054de80afddb1bc3dd",
        "readYAMLParameters.py": "3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6",
        "PlotExtractedData.C": "c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f",
    },
}

CATEGORIES = {
    "observable_binning": [r"bin", r"energy", r"time", r"photoelectron", r"PE\b", r"F90"],
    "sm_signal": [r"CEvNS", r"CENNS", r"signal", r"neutrino"],
    "detector_response": [r"efficien", r"quench", r"response", r"acceptance", r"light yield"],
    "backgrounds": [r"background", r"steady", r"beam.?related", r"BRN", r"prompt neutron"],
    "nuisance": [r"systematic", r"nuisance", r"uncertaint", r"prior", r"sigma"],
    "normalization": [r"exposure", r"POT", r"flux", r"normalization", r"mass"],
    "statistic": [r"likelihood", r"chi.?square", r"chi2", r"test statistic", r"fit"],
    "benchmark": [r"best.?fit", r"expected", r"observed", r"events", r"significance"],
}

def fetch(url, tries=4, timeout=60):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0105a6-authority-audit/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.geturl()
        except Exception as e:
            last = repr(e)
            if i + 1 < tries:
                time.sleep(2 ** i)
    raise RuntimeError(last)

def extract_text(name, data):
    if name.lower().endswith(".pdf"):
        reader = PdfReader(io.BytesIO(data))
        return "\n".join((p.extract_text() or "") for p in reader.pages)
    return data.decode("utf-8", errors="strict")

def hits(text):
    lines = text.splitlines()
    out = {}
    for cat, pats in CATEGORIES.items():
        found = []
        for idx, line in enumerate(lines, 1):
            if any(re.search(p, line, flags=re.I) for p in pats):
                clean = " ".join(line.strip().split())
                if clean:
                    found.append({"line": idx, "text": clean[:500]})
            if len(found) >= 12:
                break
        out[cat] = found
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()
    result = {
        "benchmark": "NMIR-V2-0105A6-STAGE-A",
        "git_sha": args.git_sha,
        "stage": "authority_evidence_inventory_only",
        "observed_bsm_residual_permission_percent": 0,
        "sources": {},
    }
    ok = True
    for detector, cfg in FILES.items():
        record = cfg["record"]
        result["sources"][detector] = {}
        for name, expected in cfg.items():
            if name == "record":
                continue
            quoted = urllib.parse.quote(name, safe="")
            url = f"https://zenodo.org/records/{record}/files/{quoted}?download=1"
            entry = {"record": record, "filename": name, "url": url, "expected_sha256": expected}
            try:
                data, resolved = fetch(url)
                actual = hashlib.sha256(data).hexdigest()
                entry.update({"resolved_url": resolved, "size_bytes": len(data), "actual_sha256": actual, "sha256_match": actual == expected})
                if actual != expected:
                    ok = False
                    entry["error"] = "sha256_mismatch"
                else:
                    text = extract_text(name, data)
                    entry["text_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
                    entry["text_chars"] = len(text)
                    entry["evidence_hits"] = hits(text)
            except Exception as e:
                ok = False
                entry["error"] = repr(e)
            result["sources"][detector][name] = entry
    result["status"] = "PASS_0105A6_STAGE_A_AUTHORITY_INVENTORY_NONDISCOVERY" if ok else "BLOCKED_0105A6_STAGE_A_AUTHORITY_TRANSPORT_OR_PARSE"
    result["likelihood_authority_complete"] = None
    result["sm_null_reproduction_allowed"] = False
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out.write_text(payload)
    print(payload, end="")
    print("result_sha256=" + hashlib.sha256(payload.encode()).hexdigest())
    return 0 if ok else 2

if __name__ == "__main__":
    raise SystemExit(main())
