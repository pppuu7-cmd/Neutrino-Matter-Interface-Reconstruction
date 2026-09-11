#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.parse, urllib.request
from pathlib import Path

PREREG='6da043ddbfc8dd3ef40fbe02892d9315e1a944ca'
URL='https://arxiv.org/e-print/2003.10630'
SHA='2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114'
SIZE=446096
CANDIDATES={
 'authors.tex':6826,
 'commands.tex':3979,
 'main.bbl':37145,
 'main.bib':45756,
 'main.tex':30063,
 'supplemental.tex':9705,
}
LEX={
 'F1':[
  r'poisson',r'multinomial',r'fixed[- ]?total',r'fixed[- ]?(?:number|count)',
  r'number of events',r'event count',r'events? (?:are |is )?generated',r'generated events?',
  r'pseudo[- ]?data',r'pseudodata',r'\btoy(?:s)?\b',r'extended likelihood',r'roofit',
 ],
 'F7':[
  r'3152',r'3154',r'steady[- ]?state',r'background',r'normalization',
  r'central value',r'\bevents?\b',r'\bcounts?\b',
 ],
}

class Redirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  u=urllib.parse.urlparse(urllib.parse.urljoin(req.full_url,newurl)); h=(u.hostname or '').lower()
  if not (h=='arxiv.org' or h.endswith('.arxiv.org')): raise RuntimeError('cross-provider redirect')
  return super().redirect_request(req,fp,code,msg,headers,newurl)

def windows(name,text,patterns):
 lines=text.splitlines(); rx=[re.compile(p,re.I) for p in patterns]; out=[]
 for i,line in enumerate(lines):
  matched=[p.pattern for p in rx if p.search(line)]
  if matched:
   a=max(0,i-4); b=min(len(lines),i+5)
   out.append({'member':name,'line':i+1,'matched_patterns':matched,'context_start_line':a+1,'context_end_line':b,'context':'\n'.join(f'{j+1}: {lines[j]}' for j in range(a,b))})
 return out

def provisional_status(item,hits):
 text='\n'.join(h['context'] for h in hits).lower()
 if item=='F1':
  law=bool(re.search(r'poisson|multinomial|fixed[- ]?(?:total|number|count)',text))
  relevance=bool(re.search(r'event|count|pseudo|data|generat|draw|sampl|fluctuat|toy',text))
  return 'EXPLICIT_CANDIDATE_REQUIRES_LITERAL_REVIEW' if law and relevance else 'BLOCKED_INCOMPLETE_OR_AMBIGUOUS'
 both=('3152' in text and '3154' in text)
 relation=bool(re.search(r'preceden|override|distinct|different|central|nominal|normalization|background|event|count',text))
 return 'EXPLICIT_CANDIDATE_REQUIRES_LITERAL_REVIEW' if both and relation else 'BLOCKED_INCOMPLETE_OR_AMBIGUOUS'

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
 out={
  'gate':'NMIR-V2-0105A6Q5G2','preregistration_commit':PREREG,'git_sha':a.git_sha,
  'candidate_set':CANDIDATES,'f4_inherited_status':'RESOLVED_EXPLICIT_SEPARATE_ALTERNATIVE_FITS',
  'f6_inherited_status':'RESOLVED_EXPLICIT_SEPARATE_SYSTEMATIC_FITS',
  'likelihood_evaluated':False,'pseudo_data_generated':False,'optimizer_executed':False,
  'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,
  'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,
 }
 try:
  req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-q5g2-semantic/1.0'})
  with urllib.request.build_opener(Redirect()).open(req,timeout=90) as r:
   raw=r.read(); status=int(getattr(r,'status',r.getcode())); final=r.geturl()
  sha=hashlib.sha256(raw).hexdigest(); out['source']={'status':status,'final_url':final,'bytes':len(raw),'sha256':sha}
  if sha!=SHA or len(raw)!=SIZE:
   out['source_text_inspected']=False; out['classification']='FAIL_0105A6Q5G2_SOURCE_BYTE_IDENTITY_MISMATCH'
  else:
   evidence={k:[] for k in LEX}; observed={}
   with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
    byname={m.name:m for m in tf.getmembers()}
    for name,expected in CANDIDATES.items():
     m=byname.get(name)
     if m is None or not m.isfile() or m.size!=expected: raise RuntimeError('frozen candidate metadata mismatch: '+name)
     f=tf.extractfile(m)
     if f is None: raise RuntimeError('candidate extraction failed: '+name)
     payload=f.read(); observed[name]={'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest()}
     text=payload.decode('utf-8',errors='replace')
     for item,pats in LEX.items(): evidence[item].extend(windows(name,text,pats))
   out['candidate_bytes']=observed; out['evidence']=evidence
   out['provisional_item_status']={k:provisional_status(k,evidence[k]) for k in ('F1','F7')}
   # Fail closed: lexical coincidence alone never promotes a semantic PASS.
   # Final literal adjudication is made only from the retained windows against the frozen prereg criteria.
   out['classification']='BLOCKED_0105A6Q5G2_MAIN_ANALYSIS_SOURCE_F1_F7_CONTRACT_INCOMPLETE'
   out['source_text_inspected']=True
 except Exception as e:
  out['error']=type(e).__name__+': '+str(e); out['source_text_inspected']=False
  out['classification']='BLOCKED_0105A6Q5G2_SOURCE_TRANSPORT_OR_EXTRACTION_FAILURE'
 data=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(data)
 print('CLASSIFICATION='+out['classification']); print('RESULT_SHA256='+hashlib.sha256(data).hexdigest()); print('PROVISIONAL_ITEM_STATUS='+json.dumps(out.get('provisional_item_status',{}),sort_keys=True))
if __name__=='__main__': main()
