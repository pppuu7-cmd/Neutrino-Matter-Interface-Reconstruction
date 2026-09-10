#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, tempfile, urllib.request
from pathlib import Path
from urllib.parse import urlparse

BENCHMARK='NMIR-V2-0105A6Q4B'
PREREG_COMMIT='f0c8b72e55f37776c41bc6aca2f02d5b6c6b91a1'
PARENT_SHA256='f270cd8183003a2a328a5dc361858acf7a75074d0a205bd57305ab1ba259ab5c'
PARENT_CLASS='BLOCKED_0105A6Q4A_POSTER_HAS_NO_COUNT_LAW_CANDIDATE_PAGES'
URL='https://kicp-workshops.uchicago.edu/2018-CEvNS/depot/talk-zettlemoyer-jacob.pdf'
EXPECTED_HOST='kicp-workshops.uchicago.edu'
EXPECTED_PATH='/2018-CEvNS/depot/talk-zettlemoyer-jacob.pdf'

def h256(b): return hashlib.sha256(b).hexdigest()
def norm(t): return re.sub(r'\s+',' ',t.lower()).strip()
def flags(t):
    t=norm(t); l1=bool(re.search(r'pseudo[- ]data',t)); l2=bool(re.search(r'poisson(?:ian)?|fixed total|fixed number|fixed event count|number of events is fixed|multinomial|bootstrap|resampl(?:e|ed|ing)',t)); gen=bool(re.search(r'\bgenerat(?:e|ed|es|ing|ion)\b',t)); count=bool(re.search(r'number of events|event counts?',t)); api=bool(re.search(r'roomcstudy|generatebinned|numevents|\bextended\b',t)); l3=gen or count or api; l4=bool(re.search(r'roofit|rooabspdf|roomcstudy|likelihood code|fit machinery',t)) or (l1 and 'ttree' in t); cats=[]
    if l1 and l2: cats.append('DIRECT_COUNT_LAW_CANDIDATE')
    if l1 and l3 and l4: cats.append('IMPLEMENTATION_CONTRACT_CANDIDATE')
    if l1 and gen and count: cats.append('COUNT_GENERATION_CANDIDATE')
    return {'L1':l1,'L2':l2,'L3':l3,'L4':l4,'generation_token':gen,'count_token':count,'categories':cats}
def verify_url(url):
    p=urlparse(url)
    if p.scheme!='https' or p.hostname!=EXPECTED_HOST or p.path!=EXPECTED_PATH or p.query or p.fragment:
        raise RuntimeError('resolved provider URL identity mismatch')
def download(p):
    verify_url(URL)
    req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-0105a6q4b/1.0'})
    with urllib.request.urlopen(req,timeout=120) as r:
        final=r.geturl(); b=r.read()
    verify_url(final)
    if not b.startswith(b'%PDF-'): raise RuntimeError('provider response is not PDF')
    p.write_bytes(b); return b,final
def pages(pdf):
    with tempfile.TemporaryDirectory() as td:
        o=Path(td)/'all.txt'; subprocess.run(['pdftotext','-layout',str(pdf),str(o)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE); raw=o.read_text(errors='replace')
    q=raw.split('\f')
    if q and not q[-1].strip():q.pop()
    if not q: raise RuntimeError('no PDF pages extracted')
    return [norm(x) for x in q]
def run(parent,pdf):
    pb=parent.read_bytes(); pj=json.loads(pb)
    if h256(pb)!=PARENT_SHA256 or pj.get('classification')!=PARENT_CLASS: raise ValueError('parent q4a identity/class mismatch')
    if pdf.exists():
        b=pdf.read_bytes(); final=URL; verify_url(final)
    else: b,final=download(pdf)
    if not b.startswith(b'%PDF-'): raise ValueError('presentation identity mismatch')
    pp=pages(pdf); cand=[]
    for i,t in enumerate(pp,1):
        f=flags(t)
        if f['categories']:cand.append({'physical_page':i,'normalized_text_sha256':h256(t.encode()),**f})
    cls='PASS_0105A6Q4B_2018_PRESENTATION_CANDIDATE_PAGES_LOCATED_NONDISCOVERY' if cand else 'BLOCKED_0105A6Q4B_2018_PRESENTATION_HAS_NO_COUNT_LAW_CANDIDATE_PAGES'
    return {'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'parent_q4a_result_sha256':PARENT_SHA256,'source':{'provider_landing_page':'https://kicp-workshops.uchicago.edu/2018-CEvNS/presentations.php.html','speaker':'Jacob Zettlemoyer','title':'Status of COHERENT LAr','date':'2018-11-03','resolved_url':final,'size':len(b),'sha256':h256(b)},'physical_page_count':len(pp),'candidate_pages':[x['physical_page'] for x in cand],'candidate_records':cand,'page_text_retained':False,'classification':cls,'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}
def main():
    a=argparse.ArgumentParser();a.add_argument('--parent-q4a-result',required=True);a.add_argument('--presentation',required=True);a.add_argument('--output',required=True);a.add_argument('--git-sha',required=True);x=a.parse_args()
    try:r=run(Path(x.parent_q4a_result),Path(x.presentation));r['git_sha']=x.git_sha
    except Exception as e:r={'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'git_sha':x.git_sha,'classification':'BLOCKED_0105A6Q4B_2018_PRESENTATION_TRANSPORT_OR_IDENTITY_FAILURE','error_type':type(e).__name__,'error_message':str(e),'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}
    o=Path(x.output);o.parent.mkdir(parents=True,exist_ok=True);o.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__':main()
