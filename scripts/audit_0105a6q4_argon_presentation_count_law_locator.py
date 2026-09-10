#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, tempfile, urllib.request
from pathlib import Path

BENCHMARK='NMIR-V2-0105A6Q4'
PREREG_COMMIT='7c497f6c20df351aa2d9ee033663c2da330186d2'
PARENT_SHA256='32f7d67f3f669a3809dd2b699c3a3f561f27d97d96010b0fd8f1beae7d190037'
PARENT_CLASS='BLOCKED_0105A6Q3_PSEUDODATA_COUNT_LAW_STILL_NOT_EXPLICIT'
URL='https://zenodo.org/records/3904508/files/m7s2019_Zettlemoyer-Jacob.pdf?download=1'
MD5='090a0273868c98d26ed1f4a31effb4a8'

def h256(b): return hashlib.sha256(b).hexdigest()
def md5(b): return hashlib.md5(b).hexdigest()
def norm(t): return re.sub(r'\s+',' ',t.lower()).strip()
def flags(t):
    t=norm(t); l1=bool(re.search(r'pseudo[- ]data',t)); l2=bool(re.search(r'poisson(?:ian)?|fixed total|fixed number|fixed event count|number of events is fixed|multinomial|bootstrap|resampl(?:e|ed|ing)',t)); gen=bool(re.search(r'\bgenerat(?:e|ed|es|ing|ion)\b',t)); count=bool(re.search(r'number of events|event counts?',t)); api=bool(re.search(r'roomcstudy|generatebinned|numevents|\bextended\b',t)); l3=gen or count or api; l4=bool(re.search(r'roofit|rooabspdf|roomcstudy|likelihood code|fit machinery',t)) or (l1 and 'ttree' in t); cats=[]
    if l1 and l2: cats.append('DIRECT_COUNT_LAW_CANDIDATE')
    if l1 and l3 and l4: cats.append('IMPLEMENTATION_CONTRACT_CANDIDATE')
    if l1 and gen and count: cats.append('COUNT_GENERATION_CANDIDATE')
    return {'L1':l1,'L2':l2,'L3':l3,'L4':l4,'generation_token':gen,'count_token':count,'categories':cats}
def download(p):
    req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-0105a6q4/1.0'})
    with urllib.request.urlopen(req,timeout=120) as r:b=r.read()
    if md5(b)!=MD5 or not b.startswith(b'%PDF-'): raise RuntimeError('provider MD5/PDF identity mismatch')
    p.write_bytes(b); return b
def pages(pdf):
    with tempfile.TemporaryDirectory() as td:
        o=Path(td)/'all.txt'; subprocess.run(['pdftotext','-layout',str(pdf),str(o)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE); raw=o.read_text(errors='replace')
    q=raw.split('\f');
    if q and not q[-1].strip():q.pop()
    if not q: raise RuntimeError('no PDF pages extracted')
    return [norm(x) for x in q]
def run(parent,pdf):
    pb=parent.read_bytes()
    if h256(pb)!=PARENT_SHA256 or json.loads(pb).get('classification')!=PARENT_CLASS: raise ValueError('parent q3 identity/class mismatch')
    b=pdf.read_bytes() if pdf.exists() else download(pdf)
    if md5(b)!=MD5 or not b.startswith(b'%PDF-'): raise ValueError('presentation identity mismatch')
    pp=pages(pdf); cand=[]
    for i,t in enumerate(pp,1):
        f=flags(t)
        if f['categories']:cand.append({'physical_page':i,'normalized_text_sha256':h256(t.encode()),**f})
    cls='PASS_0105A6Q4_PRESENTATION_CANDIDATE_PAGES_LOCATED_NONDISCOVERY' if cand else 'BLOCKED_0105A6Q4_PRESENTATION_HAS_NO_COUNT_LAW_CANDIDATE_PAGES'
    return {'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'parent_q3_result_sha256':PARENT_SHA256,'source':{'record':3904508,'filename':'m7s2019_Zettlemoyer-Jacob.pdf','provider_md5':MD5,'computed_md5':md5(b),'size':len(b),'sha256':h256(b)},'physical_page_count':len(pp),'candidate_pages':[x['physical_page'] for x in cand],'candidate_records':cand,'page_text_retained':False,'classification':cls,'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}
def main():
    a=argparse.ArgumentParser();a.add_argument('--parent-q3-result',required=True);a.add_argument('--presentation',required=True);a.add_argument('--output',required=True);a.add_argument('--git-sha',required=True);x=a.parse_args()
    try:r=run(Path(x.parent_q3_result),Path(x.presentation));r['git_sha']=x.git_sha
    except Exception as e:r={'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'git_sha':x.git_sha,'classification':'BLOCKED_0105A6Q4_PRESENTATION_TRANSPORT_OR_IDENTITY_FAILURE','error_type':type(e).__name__,'error_message':str(e),'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}
    o=Path(x.output);o.parent.mkdir(parents=True,exist_ok=True);o.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__':main()
