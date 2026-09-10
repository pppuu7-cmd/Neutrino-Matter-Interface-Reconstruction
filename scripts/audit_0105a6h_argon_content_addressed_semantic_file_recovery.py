#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, urllib.request

MIRROR_REPO="Newtrinos-org/Newtrinos.jl"
MIRROR_COMMIT="fa87689ddedae1929e33d66ad1f0efa1b7cce206"
MIRROR_DIR="src/experiments/coherent/coherent_2020/lAr"
EXPECTED={
"LArParametersAnlA.yaml":(4906,"cc9f2c60ce0c17809453e0caad9c4a38","a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e"),
"readYAMLParameters.py":(1814,"708becd2d56cec1c2e672038581b8c7c","3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6"),
"PlotExtractedData.C":(14020,"1161762465460efdda35d4494a0d8547","c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f"),
"CENNS10AnlAEfficiency.txt":(1804,"77139f1bb79dcf972a3a0ecc28a4a8f5","21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2"),
}
UA="NMIR-v2-0105a6h-byte-carrier/1.0"

def sha256(b): return hashlib.sha256(b).hexdigest()
def md5(b): return hashlib.md5(b).hexdigest()
def fetch(name):
    url=f"https://raw.githubusercontent.com/{MIRROR_REPO}/{MIRROR_COMMIT}/{MIRROR_DIR}/{name}"
    req=urllib.request.Request(url,headers={"User-Agent":UA})
    with urllib.request.urlopen(req,timeout=60) as r: return r.read(),r.geturl()
def decode(b): return b.decode("utf-8")
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); ap.add_argument("--git-sha",default=""); args=ap.parse_args()
    out={"benchmark":"NMIR-V2-0105A6H","git_sha":args.git_sha,"mirror_authority":False,"sm_null_reproduction_permission_percent":0,"observed_bsm_residual_permission_percent":0,"files":[]}
    for name,(size0,md50,sha0) in EXPECTED.items():
        try:
            b,res=fetch(name); obs={"filename":name,"resolved_url":res,"size":len(b),"md5":md5(b),"sha256":sha256(b)}
            obs["gates"]={"size_match":len(b)==size0,"md5_match":md5(b)==md50,"sha256_match":sha256(b)==sha0}
            ok=all(obs["gates"].values()); obs["classification"]="ACCEPTED_AS_OFFICIAL_BYTE_EQUIVALENT" if ok else "REJECTED_NOT_BYTE_EQUIVALENT"
            if ok: obs["full_text"]=decode(b)
        except Exception as e:
            obs={"filename":name,"classification":"REJECTED_NOT_BYTE_EQUIVALENT","error":type(e).__name__+": "+str(e)[:500]}
        out["files"].append(obs)
    n=sum(x["classification"]=="ACCEPTED_AS_OFFICIAL_BYTE_EQUIVALENT" for x in out["files"]); out["accepted_count"]=n
    out["status"]="PASS_0105A6H_FOUR_SEMANTIC_FILES_BYTE_EQUIVALENT_NONDISCOVERY" if n==4 else "BLOCKED_0105A6H_SEMANTIC_FILE_BYTE_EQUIVALENCE_INCOMPLETE"
    raw=(json.dumps(out,indent=2,sort_keys=True)+"\n").encode(); pathlib.Path(args.output).write_bytes(raw); print(raw.decode(),end=""); print("result_sha256="+sha256(raw))
if __name__=="__main__": main()
