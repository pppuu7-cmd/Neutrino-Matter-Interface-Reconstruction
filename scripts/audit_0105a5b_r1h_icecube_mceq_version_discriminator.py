#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.error, urllib.request
from pathlib import Path

URL = "https://export.arxiv.org/e-print/2304.12236"
CANDIDATES = {
    "mceq108": "1.0.8",
    "mceq_1_1_1": "1.1.1",
    "release_1_1_2": "1.1.2",
    "release_1_1_3": "1.1.3",
    "release_1_2_0": "1.2.0",
    "release_1_2_1": "1.2.1",
    "release_1_2_2": "1.2.2",
    "release_1_2_3": "1.2.3",
    "release_1_2_4": "1.2.4",
    "release_1_2_5": "1.2.5",
    "release_1_2_6": "1.2.6",
}
TEXT_SUFFIXES = (".tex", ".txt", ".bib", ".sty", ".cls")


def contexts(text, needle, radius=160):
    out=[]
    low=text.lower(); n=needle.lower(); start=0
    while True:
        i=low.find(n,start)
        if i<0: break
        out.append(text[max(0,i-radius):min(len(text),i+len(needle)+radius)])
        start=i+max(1,len(needle))
    return out


def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',required=True); p.add_argument('--git-sha',required=True); a=p.parse_args()
    out={"gate":"0105a5b-R1h","git_sha":a.git_sha,"classification":None,"authority_url":URL,"authority_bytes":None,"authority_sha256":None,"text_members":[],"matches":[],"matched_candidates":[],"mceq_implementation_inspected":False,"standard_3nu_executed":False,"systematic_monte_carlo_executed":False,"observed_bsm_residual_inspected":False,"observed_bsm_residual_permission_percent":0,"systematic_monte_carlo_execution_permission_percent":0}
    try:
        req=urllib.request.Request(URL,headers={"User-Agent":"NMIR-v2-R1h-authority-only"})
        with urllib.request.urlopen(req,timeout=60) as r:
            raw=r.read(); status=int(r.status)
        if status != 200: raise RuntimeError(f"HTTP {status}")
        out["authority_bytes"]=len(raw); out["authority_sha256"]=hashlib.sha256(raw).hexdigest()
        tf=tarfile.open(fileobj=io.BytesIO(raw),mode='r:*')
        texts=[]
        for m in tf.getmembers():
            if not m.isfile() or not m.name.lower().endswith(TEXT_SUFFIXES): continue
            f=tf.extractfile(m)
            if f is None: continue
            b=f.read(); text=b.decode('utf-8','replace')
            texts.append((m.name,text)); out['text_members'].append({"name":m.name,"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()})
        for tag,ver in CANDIDATES.items():
            literal_forms=[tag, f"MCEq {ver}", f"MCEq v{ver}", f"MCEq version {ver}"]
            for name,text in texts:
                for form in literal_forms:
                    for c in contexts(text,form): out['matches'].append({"candidate":tag,"member":name,"form":form,"context":c})
                # Generic 'version X.Y.Z' is accepted only when MCEq is within 160 chars.
                for c in contexts(text,f"version {ver}"):
                    if 'mceq' in c.lower(): out['matches'].append({"candidate":tag,"member":name,"form":f"version {ver} near MCEq","context":c})
        matched=sorted({x['candidate'] for x in out['matches']}); out['matched_candidates']=matched
        out['classification']=("PASS_0105A5B_R1H_ICECUBE_MCEQ_VERSION_UNIQUELY_DISCRIMINATED_NONDISCOVERY" if len(matched)==1 else "BLOCKED_0105A5B_R1H_ICECUBE_MCEQ_VERSION_NOT_UNIQUELY_DISCRIMINATED")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, tarfile.TarError, OSError, RuntimeError) as e:
        out['classification']="INFRASTRUCTURE_FAIL_0105A5B_R1H"; out['error']=f"{type(e).__name__}: {e}"
    canon=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(canon).hexdigest()
    path=Path(a.output); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

if __name__=='__main__': main()
