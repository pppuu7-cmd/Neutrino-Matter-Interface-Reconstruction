#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, tempfile, urllib.request
from pathlib import Path

BENCHMARK='NMIR-V2-0105A6Q2'
PREREG_COMMIT='f1607e221b775feb0fbdb081986fca160d4cd155'
THESIS_URL='https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download'
THESIS_SIZE=34641327
THESIS_SHA256='6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9'
PARENT_RESULT_SHA256='f1d0495fd17ed99fef54086da373a666aa33ef49b3dd61e390297f507b63b201'
PARENT_CLASS='BLOCKED_0105A6Q1_PSEUDODATA_COUNT_LAW_NOT_EXPLICIT'

def sha(b: bytes)->str: return hashlib.sha256(b).hexdigest()
def shaf(p: Path)->str: return sha(p.read_bytes())
def norm(t:str)->str: return re.sub(r'\s+',' ',t.lower()).strip()

def download(path:Path):
    req=urllib.request.Request(THESIS_URL,headers={'User-Agent':'NMIR-0105a6q2/1.0'})
    with urllib.request.urlopen(req,timeout=120) as r: data=r.read()
    if len(data)!=THESIS_SIZE or sha(data)!=THESIS_SHA256: raise RuntimeError('institutional thesis byte identity mismatch')
    path.write_bytes(data)

def pages(pdf:Path):
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/'all.txt'
        subprocess.run(['pdftotext','-layout',str(pdf),str(out)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
        raw=out.read_text(encoding='utf-8',errors='replace')
    chunks=raw.split('\f')
    if chunks and not chunks[-1].strip(): chunks.pop()
    if len(chunks)<150: raise RuntimeError(f'unexpected page count {len(chunks)}')
    return [norm(x) for x in chunks]

def flags(t:str):
    # Production pages are normalized to lowercase. Normalize here too so the
    # pure predicate and its guards use the identical frozen lexical contract.
    t=norm(t)
    l1=bool(re.search(r'pseudo[- ]data',t))
    l2=bool(re.search(r'poisson(?:ian)?|fixed total|fixed number|fixed event count|number of events is fixed|multinomial|bootstrap|resampl(?:e|ed|ing)',t))
    gen=bool(re.search(r'\bgenerat(?:e|ed|es|ing|ion)\b',t))
    count=bool(re.search(r'number of events|event counts?',t))
    api=bool(re.search(r'roomcstudy|generatebinned|numevents|\bextended\b',t))
    l3=gen or count or api
    l4=bool(re.search(r'roofit|rooabspdf|roomcstudy|likelihood code|fit machinery',t)) or (l1 and 'ttree' in t)
    cats=[]
    if l1 and l2: cats.append('DIRECT_COUNT_LAW_CANDIDATE')
    if l1 and l3 and l4: cats.append('IMPLEMENTATION_CONTRACT_CANDIDATE')
    if l1 and gen and count: cats.append('COUNT_GENERATION_CANDIDATE')
    return {'L1':l1,'L2':l2,'L3':l3,'L4':l4,'generation_token':gen,'count_token':count,'categories':cats}

def run(parent:Path, thesis:Path):
    if shaf(parent)!=PARENT_RESULT_SHA256: raise ValueError('parent q1 result SHA mismatch')
    pobj=json.loads(parent.read_text())
    if pobj.get('classification')!=PARENT_CLASS: raise ValueError('unexpected parent classification')
    if not thesis.exists(): download(thesis)
    if thesis.stat().st_size!=THESIS_SIZE or shaf(thesis)!=THESIS_SHA256: raise ValueError('thesis identity mismatch')
    pp=pages(thesis)
    candidates=[]
    for i,t in enumerate(pp,1):
        f=flags(t)
        if f['categories']:
            candidates.append({'physical_page':i,'normalized_text_sha256':sha(t.encode()),**f})
    cls='PASS_0105A6Q2_CANDIDATE_PAGES_LOCATED_NONDISCOVERY' if candidates else 'BLOCKED_0105A6Q2_NO_ADDITIONAL_COUNT_LAW_CANDIDATE_PAGES'
    return {'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'parent_q1_result_sha256':PARENT_RESULT_SHA256,
            'source_identity':{'thesis_size':THESIS_SIZE,'thesis_sha256':THESIS_SHA256},'physical_page_count':len(pp),
            'candidate_pages':[x['physical_page'] for x in candidates],'candidate_records':candidates,'page_text_retained':False,
            'classification':cls,'pseudo_data_generated':False,'likelihood_evaluated':False,
            'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,
            'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--parent-q1-result',required=True); ap.add_argument('--thesis',required=True); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    try:
        r=run(Path(a.parent_q1_result),Path(a.thesis)); r['git_sha']=a.git_sha
    except Exception as e:
        r={'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'git_sha':a.git_sha,'classification':'BLOCKED_0105A6Q2_SOURCE_TRANSPORT_OR_LOCATOR_FAILURE','error_type':type(e).__name__,'error_message':str(e),'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__': main()
