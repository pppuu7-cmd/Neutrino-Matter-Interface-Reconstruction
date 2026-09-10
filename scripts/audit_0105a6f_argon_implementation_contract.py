#!/usr/bin/env python3
import argparse, hashlib, io, json, os, pathlib, re, tarfile, urllib.request

ARXIV_ID = "2003.10630v7"
ARXIV_SHA256 = "2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114"
MEMBER_SHA256 = {
    "main.tex": "9e7785c68173921361722af9b95d99c05ff2cdafbf7565fc6b8a057b626b2c86",
    "supplemental.tex": "183ec77ea668c91611fef8f8e117f3796e36eed36d27026608d1830b11a60a57",
}
ZENODO_RECORD = "3903810"
TERMS = ("likelihood","nll","roofit","profile","fit","constraint","correlation","systematic","uncertainty","normalization","background","cevns","brn","prompt","steady","f90","energy","time")
CONTEXT_RADIUS = 2
UA = "NMIR-v2-0105a6f-authority-audit/1.0"


def sha256(b): return hashlib.sha256(b).hexdigest()

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read(), r.geturl()

def decode_text(b):
    for enc in ("utf-8", "latin-1"):
        try: s=b.decode(enc); break
        except UnicodeDecodeError: continue
    else: return None
    sample=s[:10000]
    if sample and sum(ch.isprintable() or ch in "\r\n\t" for ch in sample)/len(sample) < .90: return None
    return s

def contexts(text):
    lines=text.splitlines()
    hits=[]
    for i,line in enumerate(lines):
        lo=line.lower()
        matched=sorted({t for t in TERMS if t in lo})
        if not matched: continue
        a=max(0,i-CONTEXT_RADIUS); b=min(len(lines),i+CONTEXT_RADIUS+1)
        hits.append({"line":i+1,"terms":matched,"context":[{"line":j+1,"text":lines[j][:1000]} for j in range(a,b)]})
    return hits

def fetch_arxiv():
    attempts=[]
    for url in (f"https://export.arxiv.org/e-print/{ARXIV_ID}", f"https://arxiv.org/e-print/{ARXIV_ID}", f"https://export.arxiv.org/src/{ARXIV_ID}", f"https://arxiv.org/src/{ARXIV_ID}"):
        try:
            b,res=get(url); h=sha256(b)
            attempts.append({"requested":url,"resolved":res,"size":len(b),"sha256":h})
            if h != ARXIV_SHA256: continue
            tf=tarfile.open(fileobj=io.BytesIO(b), mode="r:*")
            members={}
            for name,expected in MEMBER_SHA256.items():
                f=tf.extractfile(name)
                if f is None: raise RuntimeError("missing "+name)
                mb=f.read(); mh=sha256(mb)
                if mh != expected: raise RuntimeError("member hash mismatch "+name)
                text=decode_text(mb)
                members[name]={"sha256":mh,"size":len(mb),"contexts":contexts(text or "")}
            return {"status":"PASS_EXACT_BYTES","archive_sha256":h,"resolved":res,"attempts":attempts,"members":members}
        except Exception as e:
            attempts.append({"requested":url,"error":type(e).__name__+": "+str(e)[:300]})
    return {"status":"BLOCKED_EXACT_BYTES","attempts":attempts}

def fetch_zenodo():
    meta_b,meta_url=get(f"https://zenodo.org/api/records/{ZENODO_RECORD}")
    meta=json.loads(meta_b)
    files=[]
    for f in sorted(meta.get("files",[]), key=lambda x:x.get("key","")):
        key=f["key"]; url=f.get("links",{}).get("content") or f.get("links",{}).get("self")
        b,res=get(url); text=decode_text(b)
        files.append({"filename":key,"provider_checksum":f.get("checksum"),"provider_size":f.get("size"),"resolved":res,"size":len(b),"sha256":sha256(b),"text_decodable":text is not None,"contexts":contexts(text) if text is not None else []})
    return {"record":ZENODO_RECORD,"metadata_url":meta_url,"metadata_sha256":sha256(meta_b),"files":files}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); ap.add_argument("--git-sha",default=os.getenv("GITHUB_SHA","")); args=ap.parse_args()
    out={"benchmark":"NMIR-V2-0105A6F","git_sha":args.git_sha,"stage":"official_argon_semantic_inventory_only","sm_null_reproduction_permission_percent":0,"observed_bsm_residual_permission_percent":0,"scientific_pass_classified":False,"terms":list(TERMS)}
    out["arxiv"]=fetch_arxiv()
    if out["arxiv"]["status"] != "PASS_EXACT_BYTES":
        out["status"]="BLOCKED_0105A6F_ARGON_AUTHORITY_BYTE_OR_TRANSPORT"
    else:
        try:
            out["zenodo"]=fetch_zenodo(); out["status"]="EVIDENCE_ACQUIRED_REQUIRES_INDEPENDENT_SEMANTIC_CLASSIFICATION"
        except Exception as e:
            out["status"]="BLOCKED_0105A6F_ARGON_AUTHORITY_BYTE_OR_TRANSPORT"; out["zenodo_error"]=type(e).__name__+": "+str(e)[:500]
    raw=(json.dumps(out,indent=2,sort_keys=True)+"\n").encode(); pathlib.Path(args.output).write_bytes(raw); print(raw.decode(),end=""); print("result_sha256="+sha256(raw))
if __name__ == "__main__": main()
