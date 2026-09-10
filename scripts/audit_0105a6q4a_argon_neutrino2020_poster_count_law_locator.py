#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, tempfile, urllib.request
from pathlib import Path

BENCHMARK='NMIR-V2-0105A6Q4A'
PREREG_COMMIT='578f211209a8074df33d783ac6f204f71f2e99ad'
PARENT_SHA256='039bb01dc39021ce0c5a48995f9b4acbcac9a2762d9435acc0079ef81b5df396'
PARENT_CLASS='BLOCKED_0105A6Q4_PRESENTATION_HAS_NO_COUNT_LAW_CANDIDATE_PAGES'
URL='https://zenodo.org/records/4252695/files/JCZNeutrino2020CENNS10Landscape.pdf?download=1'
MD5='c00fe90b1e16f3069ff6970308ee8345'

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
    req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-0105a6q4a/1.0'})
    with urllib.request.urlopen(req,timeout=120) as r:b=r.read()
    if md5(b)!=MD5 or not b.startswith(b'%PDF-'): raise RuntimeError('provider MD5/PDF identity mismatch')
    p.write_bytes(b); return b
def pages(pdf):
    with tempfile.TemporaryDirectory() as td:
        o=Path(td)/'all.txt'; subprocess.run(['pdftotext','-layout',str(pdf),str(o)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE); raw=o.read_text(errors='replace')
    q=raw.split('\f')
    if q and not q[-1].strip():q.pop()
    if not q: raise RuntimeError('no PDF pages extracted')
    return [norm(x) for x in q]
def run(parent,pdf):
    pb=parent.read_bytes()
    if h256(pb)!=PARENT_SHA256 or json.loads(pb).get('classification')!=PARENT_CLASS: raise ValueError('parent q4 identity/class mismatch')
    b=pdf.read_bytes() if pdf.exists() else download(pdf)
    if md5(b)!=MD5 or not b.startswith(b'%PDF-'): raise ValueError('poster identity mismatch')
    pp=pages(pdf); cand=[]
    for i,t in enumerate(pp,1):
        f=flags(t)
        if f['categories']:cand.append({'physical_page':i,'normalized_text_sha256':h256(t.encode()),**f})
    cls='PASS_0105A6Q4A_POSTER_CANDIDATE_PAGES_LOCATED_NONDISCOVERY' if cand else 'BLOCKED_0105A6Q4A_POSTER_HAS_NO_COUNT_LAW_CANDIDATE_PAGES'
    return {'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'parent_q4_result_sha256':PARENT_SHA256,'source':{'record':4252695,'filename':'JCZNeutrino2020CENNS10Landscape.pdf','provider_md5':MD5,'computed_md5':md5(b),'size':len(b),'sha256':h256(b)},'physical_page_count':len(pp),'candidate_pages':[x['physical_page'] for x in cand],'candidate_records':cand,'page_text_retained':False,'classification':cls,'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}
def main():
    a=argparse.ArgumentParser();a.add_argument('--parent-q4-result',required=True);a.add_argument('--poster',required=True);a.add_argument('--output',required=True);a.add_argument('--git-sha',required=True);x=a.parse_args()
    try:r=run(Path(x.parent_q4_result),Path(x.poster));r['git_sha']=x.git_sha
    except Exception as e:r={'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'git_sha':x.git_sha,'classification':'BLOCKED_0105A6Q4A_POSTER_TRANSPORT_OR_IDENTITY_FAILURE','error_type':type(e).__name__,'error_message':str(e),'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}
    o=Path(x.output);o.parent.mkdir(parents=True,exist_ok=True);o.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__':main()
