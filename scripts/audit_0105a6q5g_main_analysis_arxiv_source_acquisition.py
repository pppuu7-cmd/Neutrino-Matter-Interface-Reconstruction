#!/usr/bin/env python3
import argparse, hashlib, json, urllib.parse, urllib.request
from pathlib import Path
PREREG='e88ced9395b09c99b9634f39b8c11df5133fe754'
URL='https://arxiv.org/e-print/2003.10630'
class Redirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  u=urllib.parse.urlparse(urllib.parse.urljoin(req.full_url,newurl)); h=(u.hostname or '').lower()
  if not (h=='arxiv.org' or h.endswith('.arxiv.org')): raise RuntimeError('cross-provider redirect')
  return super().redirect_request(req,fp,code,msg,headers,newurl)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
 out={'gate':'NMIR-V2-0105A6Q5G','preregistration_commit':PREREG,'git_sha':a.git_sha,'archive_opened':False,'member_listed':False,'source_text_inspected':False,'likelihood_evaluated':False,'pseudo_data_generated':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
 try:
  req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-q5g-source-byte-lock/1.0'})
  with urllib.request.build_opener(Redirect()).open(req,timeout=90) as r:
   b=r.read(); status=int(getattr(r,'status',r.getcode())); final=r.geturl(); ctype=r.headers.get('Content-Type','')
  h=(urllib.parse.urlparse(final).hostname or '').lower()
  out['source']={'status':status,'final_url':final,'bytes':len(b),'content_type':ctype,'md5':hashlib.md5(b).hexdigest(),'sha256':hashlib.sha256(b).hexdigest()}
  if not (h=='arxiv.org' or h.endswith('.arxiv.org')): out['classification']='FAIL_0105A6Q5G_MAIN_ANALYSIS_PROVIDER_IDENTITY_FAILURE'
  elif status==200 and len(b)>0: out['classification']='PASS_0105A6Q5G_MAIN_ANALYSIS_ARXIV_SOURCE_BYTES_ACQUIRED_NONDISCOVERY'
  else: out['classification']='BLOCKED_0105A6Q5G_MAIN_ANALYSIS_SOURCE_TRANSPORT_FAILURE'
 except Exception as e:
  out['error']=type(e).__name__+': '+str(e); out['classification']='BLOCKED_0105A6Q5G_MAIN_ANALYSIS_SOURCE_TRANSPORT_FAILURE'
 data=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(data)
 print('CLASSIFICATION='+out['classification']); print('RESULT_SHA256='+hashlib.sha256(data).hexdigest()); print('SOURCE_SHA256='+out.get('source',{}).get('sha256',''))
if __name__=='__main__': main()
