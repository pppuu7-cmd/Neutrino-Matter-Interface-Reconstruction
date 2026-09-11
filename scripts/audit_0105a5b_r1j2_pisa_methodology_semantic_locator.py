#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.error, urllib.request
from pathlib import Path
URL='https://export.arxiv.org/e-print/1803.05390'
SHA='e8d26d85195764037765661fb2e5236ec4284a712adbfd9738b7c3908593c6be'
CANDS=['bits.sty','elsarticle.cls','main.tex','numcompress.sty','sample.bib','text/ack.tex','text/aeff.tex','text/bench.tex','text/flux.tex','text/intro.tex','text/motiv.tex','text/nmo.tex','text/osc.tex','text/reco.tex','text/res.tex','text/significance.tex','text/stages.tex','text/stages_techniques_intro.tex','text/summary.tex','text/toy.tex','text/valid.tex']
TAGS=['contours_working_0.1','4.3a1','4.2.1','4.2','4.1.4','4.1.3','4.1.2','4.1.1','4.1','4.0','3.2.1','3.2','3.1','3.0','2.0.1','2.0','1.0.1','1.0']
HEX40=re.compile(r'(?i)(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])')
def ctx(text,i,j,r=320): return text[max(0,i-r):min(len(text),j+r)]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
 out={'gate':'0105a5b-R1j2','git_sha':a.git_sha,'classification':None,'source_sha256':None,'member_locks':{},'pisa_occurrences':[],'repo_literals':[],'nearby_hex40':[],'nearby_frozen_tags':[],'explicit_tag_forms':[],'nearby_version_words':[],'pisa_repository_content_fetched':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
 try:
  req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1j2-semantic-authority-only'})
  with urllib.request.urlopen(req,timeout=60) as r: raw=r.read()
  got=hashlib.sha256(raw).hexdigest(); out['source_sha256']=got
  if got!=SHA: raise RuntimeError('source SHA256 mismatch')
  tf=tarfile.open(fileobj=io.BytesIO(raw),mode='r:*')
  for name in CANDS:
   try: m=tf.getmember(name)
   except KeyError: raise RuntimeError(f'missing frozen member {name}')
   f=tf.extractfile(m)
   if f is None: raise RuntimeError(f'unreadable frozen member {name}')
   b=f.read(); out['member_locks'][name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}; text=b.decode('utf-8','replace'); low=text.lower()
   for pm in re.finditer('pisa',text,re.I):
    c=ctx(text,pm.start(),pm.end()); out['pisa_occurrences'].append({'member':name,'context':c})
    cl=c.lower()
    if 'github.com/icecube/pisa' in cl or 'icecube/pisa' in cl: out['repo_literals'].append({'member':name,'context':c})
    for hm in HEX40.finditer(c): out['nearby_hex40'].append({'member':name,'token':hm.group(0),'context':c})
    for tag in TAGS:
     if tag.lower() in cl: out['nearby_frozen_tags'].append({'member':name,'tag':tag,'context':c})
     esc=re.escape(tag)
     for label,pat in [('plain',rf'(?i)\bPISA\s+{esc}(?![A-Za-z0-9.])'),('v',rf'(?i)\bPISA\s+v{esc}(?![A-Za-z0-9.])'),('version',rf'(?i)\bPISA\s+version\s+{esc}(?![A-Za-z0-9.])'),('release',rf'(?i)\bPISA\s+release\s+{esc}(?![A-Za-z0-9.])')]:
      if re.search(pat,c): out['explicit_tag_forms'].append({'member':name,'tag':tag,'form':label,'context':c})
    if re.search(r'(?i)version', text[max(0,pm.start()-160):min(len(text),pm.end()+160)]): out['nearby_version_words'].append({'member':name,'context':text[max(0,pm.start()-160):min(len(text),pm.end()+160)]})
  unique_explicit=sorted({x['tag'] for x in out['explicit_tag_forms']})
  immutable=(len(out['nearby_hex40'])>0 or len(unique_explicit)==1)
  if not out['pisa_occurrences']: out['classification']='BLOCKED_0105A5B_R1J2_NO_PISA_SEMANTIC_EVIDENCE'
  elif immutable: out['classification']='PASS_0105A5B_R1J2_PISA_METHODOLOGY_EXPLICIT_IMPLEMENTATION_AUTHORITY_FOUND_NONDISCOVERY'
  else: out['classification']='BLOCKED_0105A5B_R1J2_PISA_METHODOLOGY_IMPLEMENTATION_STATE_NOT_IMMUTABLY_IDENTIFIED'
 except (urllib.error.URLError,urllib.error.HTTPError,TimeoutError,OSError,tarfile.TarError,RuntimeError) as e:
  out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1J2'; out['error']=f'{type(e).__name__}: {e}'
 canon=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(canon).hexdigest()
 p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
