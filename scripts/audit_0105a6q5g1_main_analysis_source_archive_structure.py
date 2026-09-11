#!/usr/bin/env python3
import argparse, hashlib, io, json, tarfile, urllib.parse, urllib.request
from pathlib import Path
PREREG='7197fe98682ead93a0264ac0d4b77a6fc54f5d15'; URL='https://arxiv.org/e-print/2003.10630'; SHA='2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114'; SIZE=446096
SUFFIXES=('.tex','.sty','.cls','.bib','.bbl','.txt','.md','.rst')
class R(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  h=(urllib.parse.urlparse(urllib.parse.urljoin(req.full_url,newurl)).hostname or '').lower()
  if not (h=='arxiv.org' or h.endswith('.arxiv.org')): raise RuntimeError('cross-provider redirect')
  return super().redirect_request(req,fp,code,msg,headers,newurl)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
 out={'gate':'NMIR-V2-0105A6Q5G1','preregistration_commit':PREREG,'git_sha':a.git_sha,'member_content_read':False,'source_text_inspected':False,'likelihood_evaluated':False,'pseudo_data_generated':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
 try:
  req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-q5g1-structure/1.0'})
  with urllib.request.build_opener(R()).open(req,timeout=90) as r: b=r.read(); status=int(getattr(r,'status',r.getcode())); final=r.geturl()
  sha=hashlib.sha256(b).hexdigest(); out['source']={'status':status,'final_url':final,'bytes':len(b),'sha256':sha}
  if sha!=SHA or len(b)!=SIZE: out['classification']='FAIL_0105A6Q5G1_SOURCE_BYTE_IDENTITY_MISMATCH'
  else:
   members=[]
   with tarfile.open(fileobj=io.BytesIO(b),mode='r:*') as tf:
    for m in tf.getmembers(): members.append({'name':m.name,'type':('file' if m.isfile() else 'dir' if m.isdir() else 'other'),'size':m.size,'candidate':m.isfile() and m.name.casefold().endswith(SUFFIXES)})
   out['members']=members; out['member_count']=len(members); out['candidates']=[x for x in members if x['candidate']]; out['candidate_count']=len(out['candidates'])
   out['classification']='PASS_0105A6Q5G1_MAIN_ANALYSIS_SOURCE_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY' if out['candidates'] else 'BLOCKED_0105A6Q5G1_NO_SOURCE_TEXT_CANDIDATES'
 except Exception as e:
  out['error']=type(e).__name__+': '+str(e); out['classification']='BLOCKED_0105A6Q5G1_SOURCE_TRANSPORT_OR_ARCHIVE_STRUCTURE_FAILURE'
 data=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(data)
 print('CLASSIFICATION='+out['classification']); print('RESULT_SHA256='+hashlib.sha256(data).hexdigest()); print('CANDIDATE_COUNT='+str(out.get('candidate_count')))
if __name__=='__main__': main()
