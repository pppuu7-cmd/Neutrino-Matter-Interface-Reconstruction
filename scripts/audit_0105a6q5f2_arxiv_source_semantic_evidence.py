#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.parse, urllib.request
from pathlib import Path

PREREG='58e32cedffb6c173079f8098513dbc1e81fbb4b6'
URL='https://arxiv.org/e-print/2006.12659'
SHA='5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde'
SIZE=23805
CANDIDATES={
 'authors_els.tex':4985,
 'CENNS10DataReleaseCompanion.bbl':1308,
 'CENNS10DataReleaseCompanion.bib':1274,
 'CENNS10DataReleaseCompanion.tex':27656,
}
LEX={
 'F1':[r'poisson',r'multinomial',r'fixed[- ]?(?:total|number|count)',r'(?:number|count) of events.{0,80}(?:generat|draw|sampl|fluctuat)',r'(?:generat|draw|sampl|fluctuat).{0,80}(?:number|count) of events'],
 'F4':[r'systematic',r'one[- ]?sigma',r'1\\?sigma',r'\\pm',r'plus.?minus',r'interpol',r'morph',r'excursion',r'(?:separate|independent).{0,80}(?:fit|likelihood|pdf)',r'(?:fit|likelihood|pdf).{0,80}(?:separate|independent)'],
 'F6':[r'correlat',r'uncorrelat',r'independent',r'simultaneous',r'joint(?:ly)?',r'separate(?:ly)?',r'covarian',r'nuisance'],
 'F7':[r'3152',r'3154',r'(?:central|nominal).{0,80}(?:event|count|normalization)',r'(?:event|count|normalization).{0,80}(?:central|nominal)',r'preceden',r'override'],
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

def explicit_status(item,hits):
 text='\n'.join(h['context'] for h in hits).lower()
 if item=='F1':
  explicit=bool(re.search(r'poisson|multinomial|fixed[- ]?(?:total|number|count)',text)) and bool(re.search(r'event|count|pseudo|data|generat|draw|sampl|fluctuat',text))
 elif item=='F4':
  explicit=bool(re.search(r'systematic|sigma|\\pm|plus.?minus',text)) and bool(re.search(r'interpol|morph|excursion|separate.{0,80}(?:fit|likelihood|pdf)|(?:fit|likelihood|pdf).{0,80}separate',text))
 elif item=='F6':
  explicit=bool(re.search(r'correlat|uncorrelat|independent|simultaneous|joint|separate|covarian',text)) and bool(re.search(r'systematic|nuisance|pdf|likelihood|fit',text))
 else:
  explicit=('3152' in text and '3154' in text and bool(re.search(r'preceden|override|central|nominal|normalization|event|count',text)))
 return 'EXPLICIT_CANDIDATE_REQUIRES_LITERAL_REVIEW' if explicit else 'BLOCKED_INCOMPLETE_OR_AMBIGUOUS'

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
 out={'gate':'NMIR-V2-0105A6Q5F2','preregistration_commit':PREREG,'git_sha':a.git_sha,'candidate_set':CANDIDATES,'likelihood_evaluated':False,'pseudo_data_generated':False,'optimizer_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
 try:
  req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-q5f2-semantic/1.0'})
  with urllib.request.build_opener(Redirect()).open(req,timeout=90) as r: raw=r.read(); status=int(getattr(r,'status',r.getcode())); final=r.geturl()
  sha=hashlib.sha256(raw).hexdigest(); out['source']={'status':status,'final_url':final,'bytes':len(raw),'sha256':sha}
  if sha!=SHA or len(raw)!=SIZE:
   out['classification']='FAIL_0105A6Q5F2_SOURCE_BYTE_IDENTITY_MISMATCH'
  else:
   evidence={k:[] for k in LEX}; observed={}
   with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
    byname={m.name:m for m in tf.getmembers()}
    for name,expected in CANDIDATES.items():
     m=byname.get(name)
     if m is None or not m.isfile() or m.size!=expected: raise RuntimeError('frozen candidate metadata mismatch: '+name)
     payload=tf.extractfile(m).read(); observed[name]={'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest()}
     text=payload.decode('utf-8',errors='replace')
     for item,pats in LEX.items(): evidence[item].extend(windows(name,text,pats))
   out['candidate_bytes']=observed; out['evidence']=evidence
   out['item_status']={k:explicit_status(k,evidence[k]) for k in ('F1','F4','F6','F7')}
   # This hosted gate is conservative: lexical evidence is retained, but automatic lexical coincidence is never promoted to a complete semantic contract.
   out['classification']='BLOCKED_0105A6Q5F2_ARXIV_SOURCE_SEMANTIC_CONTRACT_INCOMPLETE' if any(v=='BLOCKED_INCOMPLETE_OR_AMBIGUOUS' for v in out['item_status'].values()) else 'BLOCKED_0105A6Q5F2_ARXIV_SOURCE_SEMANTIC_CONTRACT_INCOMPLETE'
  out['source_text_inspected']=True
 except Exception as e:
  out['error']=type(e).__name__+': '+str(e); out['source_text_inspected']=False; out['classification']='BLOCKED_0105A6Q5F2_SOURCE_TRANSPORT_OR_EXTRACTION_FAILURE'
 data=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(data)
 print('CLASSIFICATION='+out['classification']); print('RESULT_SHA256='+hashlib.sha256(data).hexdigest()); print('ITEM_STATUS='+json.dumps(out.get('item_status',{}),sort_keys=True))
if __name__=='__main__': main()
