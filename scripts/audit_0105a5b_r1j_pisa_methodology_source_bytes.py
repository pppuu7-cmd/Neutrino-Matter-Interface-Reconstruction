#!/usr/bin/env python3
import argparse, hashlib, json, urllib.error, urllib.request
from pathlib import Path

URL='https://export.arxiv.org/e-print/1803.05390'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'0105a5b-R1j','git_sha':a.git_sha,'classification':None,'url':URL,'http_status':None,'final_url':None,'content_type':None,'bytes':None,'md5':None,'sha256':None,
         'archive_opened':False,'member_listed':False,'source_text_inspected':False,'pisa_repository_content_inspected':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1j-byte-acquisition-only'})
        with urllib.request.urlopen(req,timeout=60) as r:
            raw=r.read(); out['http_status']=int(r.status); out['final_url']=r.geturl(); out['content_type']=r.headers.get('Content-Type')
        out['bytes']=len(raw); out['md5']=hashlib.md5(raw).hexdigest(); out['sha256']=hashlib.sha256(raw).hexdigest()
        if out['http_status']==200 and len(raw)>0:
            out['classification']='PASS_0105A5B_R1J_PISA_METHODOLOGY_SOURCE_BYTES_ACQUIRED_NONDISCOVERY'
        else:
            out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1J'
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
        out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1J'; out['error']=f'{type(e).__name__}: {e}'
    canon=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(canon).hexdigest()
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
