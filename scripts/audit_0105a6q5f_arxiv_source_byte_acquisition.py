#!/usr/bin/env python3
import argparse, hashlib, json, urllib.parse, urllib.request
from pathlib import Path
PREREG='cc4a01a55bb8232325a82df48b0ac220a7a0bef5'
URL='https://arxiv.org/e-print/2006.12659'
class SameArxiv(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        h=(urllib.parse.urlparse(urllib.parse.urljoin(req.full_url,newurl)).hostname or '').lower()
        if not (h=='arxiv.org' or h.endswith('.arxiv.org')): raise RuntimeError('cross-provider redirect')
        return super().redirect_request(req,fp,code,msg,headers,newurl)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'NMIR-V2-0105A6Q5F','preregistration_commit':PREREG,'git_sha':a.git_sha,'source_text_inspected':False,'archive_members_extracted':False,'keywords_searched':False,'likelihood_evaluated':False,'observed_bsm_residual_inspected':False,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-q5f-authority-byte-lock/1.0'})
        with urllib.request.build_opener(SameArxiv()).open(req,timeout=90) as r:
            b=r.read(); status=int(getattr(r,'status',r.getcode())); final=r.geturl(); headers=r.headers
        host=(urllib.parse.urlparse(final).hostname or '').lower(); ok=status==200 and len(b)>0 and (host=='arxiv.org' or host.endswith('.arxiv.org'))
        out['source']={'requested_url':URL,'final_url':final,'status':status,'bytes':len(b),'content_type':headers.get('Content-Type'),'etag':headers.get('ETag'),'last_modified':headers.get('Last-Modified'),'md5':hashlib.md5(b).hexdigest(),'sha256':hashlib.sha256(b).hexdigest()}
        out['classification']='PASS_0105A6Q5F_ARXIV_2006_12659_SOURCE_BYTES_ACQUIRED_NONDISCOVERY' if ok else 'BLOCKED_0105A6Q5F_ARXIV_SOURCE_TRANSPORT_FAILURE'
    except Exception as e:
        out['error']=type(e).__name__+': '+str(e); out['classification']='BLOCKED_0105A6Q5F_ARXIV_SOURCE_TRANSPORT_FAILURE'
    payload=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(payload)
    print('CLASSIFICATION='+out['classification']); print('RESULT_SHA256='+hashlib.sha256(payload).hexdigest())
if __name__=='__main__': main()
