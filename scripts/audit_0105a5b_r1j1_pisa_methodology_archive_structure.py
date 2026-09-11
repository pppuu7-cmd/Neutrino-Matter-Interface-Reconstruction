#!/usr/bin/env python3
import argparse, hashlib, io, json, tarfile, urllib.request, urllib.error
from pathlib import Path
URL='https://export.arxiv.org/e-print/1803.05390'
SHA='e8d26d85195764037765661fb2e5236ec4284a712adbfd9738b7c3908593c6be'
SUFFIXES=('.tex','.txt','.bib','.sty','.cls')
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
 out={'gate':'0105a5b-R1j1','git_sha':a.git_sha,'classification':None,'source_sha256':None,'members':[],'source_text_candidates':[],'source_text_inspected':False,'pisa_repository_content_inspected':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
 try:
  req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1j1-structure-only'})
  with urllib.request.urlopen(req,timeout=60) as r: raw=r.read()
  got=hashlib.sha256(raw).hexdigest(); out['source_sha256']=got
  if got!=SHA: raise RuntimeError('source SHA256 mismatch')
  tf=tarfile.open(fileobj=io.BytesIO(raw),mode='r:*')
  for m in tf.getmembers():
   rec={'name':m.name,'is_file':m.isfile(),'size':m.size}; out['members'].append(rec)
   if m.isfile() and m.name.lower().endswith(SUFFIXES): out['source_text_candidates'].append(m.name)
  out['classification']='PASS_0105A5B_R1J1_PISA_METHODOLOGY_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY' if out['source_text_candidates'] else 'BLOCKED_0105A5B_R1J1_NO_SOURCE_TEXT_CANDIDATES'
 except (urllib.error.URLError,urllib.error.HTTPError,TimeoutError,OSError,tarfile.TarError,RuntimeError) as e:
  out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1J1'; out['error']=f'{type(e).__name__}: {e}'
 canon=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(canon).hexdigest()
 p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
