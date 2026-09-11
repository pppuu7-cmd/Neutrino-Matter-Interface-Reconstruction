#!/usr/bin/env python3
import argparse, hashlib, json, unicodedata, urllib.request
from pathlib import Path

PREREG='8fb5121c97918b726a95f3440a1f15b5457c751d'
GATE='NMIR-V2-0105A6Q5B'
URL='https://zenodo.org/api/records/3903810'
TITLE='COHERENT Collaboration data release from the first detection of coherent elastic neutrino-nucleus scattering on argon'
PARENT='research/iterations/0105a6q5a2_argon_official_release_structural_provenance_pass_20260911.md'
PARENT_CLASS='PASS_0105A6Q5A2_ARGON_OFFICIAL_RELEASE_STRUCTURAL_PROVENANCE_BOUND_NONDISCOVERY'
PARENT_IDS=['34548098074','103104972721','10179757861','0fd133a8664e2e4dffacb93f76bc9b6456da776ba12917fcb1f1886dd72611a5','46a2cc9b0fe6f8416dcde20203cc9535599cb43d9cf215cb2b07c9e7b1f9f339']
SUFFIXES=('.py','.c','.cc','.cpp','.h','.yaml','.yml','.json')
TOKENS=('parameter','efficien','likelihood','fit','roo','plot','extract','systematic')

def norm(x): return unicodedata.normalize('NFKC',str(x or '')).casefold()
def parent_ok():
    t=Path(PARENT).read_text(); return PARENT_CLASS in t and all(x in t for x in PARENT_IDS)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':GATE,'preregistration_commit':PREREG,'git_sha':a.git_sha,'parent_binding_pass':parent_ok(),
         'release_file_bytes_downloaded':False,'scientific_release_content_inspected':False,'pseudo_data_generated':False,'likelihood_evaluated':False,'observed_bsm_residual_inspected':False,
         'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-q5b-metadata-locator/1.0','Accept':'application/json'})
        with urllib.request.urlopen(req,timeout=60) as r: b=r.read(); status=getattr(r,'status',200); final=r.geturl(); ctype=r.headers.get('Content-Type','')
        out['provider']={'requested_url':URL,'final_url':final,'status':status,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'content_type':ctype}
        data=json.loads(b); meta=data.get('metadata') or {}; files=data.get('files') or []
        idok=data.get('id')==3903810 and data.get('doi')=='10.5281/zenodo.3903810' and str(meta.get('version'))=='1.0' and norm(meta.get('title'))==norm(TITLE) and len(files)==24
        out['zenodo_identity_pass']=idok; out['metadata_file_count']=len(files); cand=[]
        for f in files:
            key=str(f.get('key') or ''); nk=norm(key)
            if nk.endswith(SUFFIXES) or any(tok in nk for tok in TOKENS):
                links=f.get('links') or {}
                cand.append({'key':key,'size':f.get('size'),'checksum':f.get('checksum'),'links':{k:links.get(k) for k in sorted(links)}})
        out['candidates']=cand; out['candidate_count']=len(cand)
        if not out['parent_binding_pass']: cls='BLOCKED_0105A6Q5B_PARENT_PROVENANCE_BINDING_FAILURE'
        elif not idok: cls='BLOCKED_0105A6Q5B_ZENODO_METADATA_IDENTITY_FAILURE'
        elif not cand: cls='BLOCKED_0105A6Q5B_NO_SEMANTIC_FILE_CANDIDATES'
        else: cls='PASS_0105A6Q5B_ARGON_OFFICIAL_SEMANTIC_FILE_CANDIDATES_LOCATED_NONDISCOVERY'
    except Exception as e:
        out['error']=type(e).__name__+': '+str(e); cls='BLOCKED_0105A6Q5B_PROVIDER_TRANSPORT_FAILURE'
    out['classification']=cls
    payload=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(payload)
    print('CLASSIFICATION='+cls); print('RESULT_SHA256='+hashlib.sha256(payload).hexdigest()); print('CANDIDATE_COUNT='+str(out.get('candidate_count')))
if __name__=='__main__': main()
