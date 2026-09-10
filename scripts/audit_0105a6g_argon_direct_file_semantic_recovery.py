#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, re, urllib.request

PARENT_MANIFEST_SHA256 = "5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091"
AR_RECORD = "3903810"
AR_DOI = "10.5281/zenodo.3903810"
EXPECTED_AR_FILES = 24
TERMS = (
    "likelihood","nll","roofit","profile","fit","constraint","correlation","covariance",
    "systematic","uncertainty","normalization","background","cevns","brn","prompt","steady",
    "f90","energy","time","pdf","parameter","efficiency","acceptance","yaml"
)
SMALL_FULLTEXT = {"LArParametersAnlA.yaml","readYAMLParameters.py","PlotExtractedData.C","CENNS10AnlAEfficiency.txt"}
UA = "NMIR-v2-0105a6g-direct-provider-recovery/1.0"


def sha256(b): return hashlib.sha256(b).hexdigest()
def md5(b): return hashlib.md5(b).hexdigest()

def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":UA})
    with urllib.request.urlopen(req,timeout=120) as r:
        return r.read(),r.geturl()

def decode_text(b):
    for enc in ("utf-8","latin-1"):
        try: s=b.decode(enc); break
        except UnicodeDecodeError: continue
    else: return None
    sample=s[:10000]
    if sample and sum(ch.isprintable() or ch in "\r\n\t" for ch in sample)/len(sample)<.90: return None
    return s

def contexts(text,radius=1):
    lines=text.splitlines(); out=[]
    for i,line in enumerate(lines):
        lo=line.lower(); hits=sorted({t for t in TERMS if t in lo})
        if hits:
            a=max(0,i-radius); b=min(len(lines),i+radius+1)
            out.append({"line":i+1,"terms":hits,"context":[{"line":j+1,"text":lines[j][:1000]} for j in range(a,b)]})
    return out

def verify_parent(path):
    raw=pathlib.Path(path).read_bytes(); h=sha256(raw)
    if h!=PARENT_MANIFEST_SHA256: raise RuntimeError(f"parent manifest SHA256 mismatch: {h}")
    m=json.loads(raw)
    if m.get("benchmark")!="NMIR-V2-0105A3" or not m.get("coherent_event_byte_lock_complete"):
        raise RuntimeError("parent manifest is not a completed 0105a3 lock")
    if m.get("observed_residual_execution_allowed") is not False:
        raise RuntimeError("parent discovery guard invalid")
    ar=m.get("releases",{}).get("ar",{})
    if ar.get("doi")!=AR_DOI or ar.get("file_count")!=EXPECTED_AR_FILES or len(ar.get("files",[]))!=EXPECTED_AR_FILES:
        raise RuntimeError("parent Ar identity/count mismatch")
    names=[x.get("filename") for x in ar["files"]]
    if len(names)!=len(set(names)): raise RuntimeError("duplicate filename in parent manifest")
    return m,ar

def audit_file(e):
    url=e["request_url"]
    prefix=f"https://zenodo.org/records/{AR_RECORD}/files/"
    if not url.startswith(prefix): raise RuntimeError("non-frozen provider URL: "+url)
    b,res=get(url)
    observed={"filename":e["filename"],"request_url":url,"resolved_url":res,"size_bytes":len(b),"md5":md5(b),"sha256":sha256(b)}
    observed["gates"]={
        "size_match":len(b)==e["size_bytes"],
        "provider_md5_match":md5(b)==e["provider_md5_expected"],
        "sha256_match":sha256(b)==e["sha256"],
    }
    observed["exact_byte_match"]=all(observed["gates"].values())
    if observed["exact_byte_match"]:
        text=decode_text(b)
        observed["text_decodable"]=text is not None
        if text is not None:
            observed["contexts"]=contexts(text)
            if e["filename"] in SMALL_FULLTEXT:
                observed["full_text"]=text
    return observed

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--parent-manifest",required=True); ap.add_argument("--output",required=True); ap.add_argument("--git-sha",default=""); args=ap.parse_args()
    out={"benchmark":"NMIR-V2-0105A6G","git_sha":args.git_sha,"parent_manifest_sha256_expected":PARENT_MANIFEST_SHA256,"sm_null_reproduction_permission_percent":0,"observed_bsm_residual_permission_percent":0,"scientific_semantic_pass_classified":False}
    try:
        _,ar=verify_parent(args.parent_manifest)
        out["parent_manifest_verified"]=True
        files=[]
        for e in sorted(ar["files"],key=lambda x:x["filename"]):
            files.append(audit_file(e))
        out["files"]=files
        out["file_count"]=len(files)
        out["exact_match_count"]=sum(x["exact_byte_match"] for x in files)
        passed=len(files)==EXPECTED_AR_FILES and all(x["exact_byte_match"] for x in files)
        out["status"]="PASS_0105A6G_ARGON_DIRECT_PROVIDER_BYTES_RECOVERED_NONDISCOVERY" if passed else "BLOCKED_0105A6G_ARGON_DIRECT_PROVIDER_TRANSPORT_OR_BYTE_MISMATCH"
    except Exception as e:
        out["status"]="BLOCKED_0105A6G_ARGON_DIRECT_PROVIDER_TRANSPORT_OR_BYTE_MISMATCH"; out["error"]=type(e).__name__+": "+str(e)[:1000]
    raw=(json.dumps(out,indent=2,sort_keys=True)+"\n").encode(); pathlib.Path(args.output).write_bytes(raw); print(raw.decode(),end=""); print("result_sha256="+sha256(raw))
if __name__=="__main__": main()
