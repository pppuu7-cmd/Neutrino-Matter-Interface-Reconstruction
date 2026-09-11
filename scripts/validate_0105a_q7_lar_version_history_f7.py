#!/usr/bin/env python3
"""Hosted reproducibility validator for prospectively frozen NMIR 0105a q7 F7."""
from __future__ import annotations
import hashlib, json, pathlib, re, subprocess, tempfile, urllib.request

PREREG = "ca909d318365dfb05b7b52c8abeacfbdd1f8bb7d"
AMENDMENT = "e97d5157dd586160b0e9feb476eb4975d88fe513"
URLS = {
    "v3.pdf": "https://arxiv.org/pdf/2003.10630v3",
    "v4.pdf": "https://arxiv.org/pdf/2003.10630v4",
    "v7.pdf": "https://arxiv.org/pdf/2003.10630v7",
    "history.html": "https://arxiv.org/abs/2003.10630",
    "release.pdf": "https://arxiv.org/pdf/2006.12659",
}

def h(b: bytes) -> str: return hashlib.sha256(b).hexdigest()
def norm(s: str) -> str: return re.sub(r"\s+", " ", s.replace("−", "-").replace("±", "+/-")).strip().lower()

def has_value(text: str, value: str) -> bool:
    n = norm(text)
    return bool(re.search(rf"(?:ss|nss).{{0,80}}{value}\s*(?:\+/-|\\pm)\s*25|{value}\s*(?:\+/-|\\pm)\s*25.{{0,80}}(?:ss|nss)", n))

def classify(v3: str, v4: str, v7: str, history: str, release: str) -> dict:
    c1 = has_value(v3, "3154")
    c2 = has_value(v4, "3152")
    c3 = "v4: fix typo in table 1" in norm(history)
    c4 = has_value(v7, "3152") or has_value(release, "3152")
    passed = all([c1,c2,c3,c4])
    return {
        "conditions": {"v3_3154": c1, "v4_3152": c2, "v4_history_typo_fix": c3, "3152_persists": c4},
        "status": "PASS_0105A_Q7_F7_PRIMARY_VERSIONED_PRECEDENCE_LOCATED_NONDISCOVERY" if passed else "BLOCKED_0105A_Q7_F7_PRIMARY_VERSIONED_PRECEDENCE_INCOMPLETE",
        "scientific_claim_machine_validated": passed,
    }

def main(outdir="results/0105a_q7_validation"):
    od=pathlib.Path(outdir); od.mkdir(parents=True, exist_ok=True)
    raw={}; meta={}; texts={}
    for name,url in URLS.items():
        req=urllib.request.Request(url, headers={"User-Agent":"NMIR-authority-audit/1.0"})
        with urllib.request.urlopen(req, timeout=120) as r: b=r.read()
        raw[name]=b; meta[name]={"url":url,"bytes":len(b),"sha256":h(b)}
    with tempfile.TemporaryDirectory() as td:
        for name in ["v3.pdf","v4.pdf","v7.pdf","release.pdf"]:
            p=pathlib.Path(td)/name; t=pathlib.Path(td)/(name+".txt"); p.write_bytes(raw[name])
            subprocess.run(["pdftotext","-layout",str(p),str(t)],check=True)
            texts[name]=t.read_text(encoding="utf-8",errors="replace")
    texts["history.html"]=raw["history.html"].decode("utf-8",errors="replace")
    adj=classify(texts["v3.pdf"],texts["v4.pdf"],texts["v7.pdf"],texts["history.html"],texts["release.pdf"])
    result={"gate":"0105a_q7_hosted_validation","preregistration":PREREG,"validation_amendment":AMENDMENT,"inputs":meta,"adjudication":adj,"hard_prohibitions":{"observed_bsm_residual":True,"systematic_mc":True,"fit_improvement_selection":True}}
    (od/"result.json").write_text(json.dumps(result,indent=2)+"\n")
    for n,t in texts.items(): (od/(n.replace('/','_')+".txt")).write_text(t,encoding="utf-8")
    print(json.dumps(result,indent=2))
    if not adj["scientific_claim_machine_validated"]: raise SystemExit(2)

if __name__=="__main__": main()
