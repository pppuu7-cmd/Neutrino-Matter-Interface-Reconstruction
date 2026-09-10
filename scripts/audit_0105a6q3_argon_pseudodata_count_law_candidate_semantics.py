#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, tempfile, urllib.request
from pathlib import Path

BENCHMARK='NMIR-V2-0105A6Q3'
PREREG_COMMIT='be5e6b6d381b8b2667466768edcf2f175fce8996'
PARENT_RESULT_SHA256='c0d913c442130817b7b59e2a785784b40b85e3c501ce9309699a55b0e66e88f3'
PARENT_CLASS='PASS_0105A6Q2_CANDIDATE_PAGES_LOCATED_NONDISCOVERY'
THESIS_URL='https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download'
THESIS_SIZE=34641327
THESIS_SHA256='6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9'
PAGES=[145,152,153]
PAGE_HASHES={145:'5a96deead926de7effdc82a6f9d8f842c57ad848ddbfd315b25f9726d1677c42',152:'922b45c4a92f1dc0085b506dcd59e627c394d05d7b70951c6d2bd19bdbb73cea',153:'96622db01938d38707e3a9945cd34c581ae08debada402ffc434bd5de5adbd52'}
MAX_WINDOW=1200

def sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def shaf(p:Path)->str:return sha(p.read_bytes())
def norm(t:str)->str:return re.sub(r'\s+',' ',t.lower()).strip()

def download(p:Path):
    req=urllib.request.Request(THESIS_URL,headers={'User-Agent':'NMIR-0105a6q3/1.0'})
    with urllib.request.urlopen(req,timeout=120) as r:data=r.read()
    if len(data)!=THESIS_SIZE or sha(data)!=THESIS_SHA256:raise RuntimeError('institutional thesis byte identity mismatch')
    p.write_bytes(data)

def extract_page(pdf:Path,page:int)->str:
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/f'p{page}.txt'
        subprocess.run(['pdftotext','-f',str(page),'-l',str(page),'-layout',str(pdf),str(out)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
        return norm(out.read_text(encoding='utf-8',errors='replace'))

def window(t:str):
    terms=['pseudo data','pseudo-data','generated','generate','generation','number of events','event count','poisson','fixed total','fixed number','multinomial','bootstrap','resampl','roofit','roomcstudy','numevents','extended']
    pos=[t.find(x) for x in terms if t.find(x)>=0]
    if not pos:return None
    c=min(pos); s=max(0,c-MAX_WINDOW//2); e=min(len(t),s+MAX_WINDOW); s=max(0,e-MAX_WINDOW); return t[s:e]

def classify(pages:dict[int,str]):
    joined=' '.join(pages[p] for p in PAGES)
    pseudo_poisson=bool(re.search(r'(?:pseudo[- ]data|event(?:s| counts?)?|number of events).{0,300}(?:poisson|poissonian)|(?:poisson|poissonian).{0,300}(?:pseudo[- ]data|event(?:s| counts?)?|number of events)',joined))
    poisson_total=bool(re.search(r'(?:total|number).{0,150}(?:events|count).{0,200}(?:poisson|poissonian)|(?:poisson|poissonian).{0,200}(?:total|number).{0,150}(?:events|count)',joined))
    extended_poisson=bool(re.search(r'extended.{0,250}(?:poisson|poissonian).{0,250}(?:event|count|pseudo)|(?:poisson|poissonian).{0,250}extended.{0,250}(?:event|count|pseudo)',joined))
    q3p=pseudo_poisson or poisson_total or extended_poisson
    fixed=bool(re.search(r'(?:pseudo[- ]data|event|count).{0,300}(?:fixed number|fixed total|fixed event count|number of events is fixed)|(?:fixed number|fixed total|fixed event count|number of events is fixed).{0,300}(?:pseudo[- ]data|event|count)',joined))
    multinomial=bool(re.search(r'multinomial.{0,250}(?:pseudo|event|count)|(?:pseudo|event|count).{0,250}multinomial',joined))
    q3f=fixed or multinomial
    other=bool(re.search(r'(?:bootstrap|resampl(?:e|ed|ing)?).{0,250}(?:pseudo|event|count)|(?:pseudo|event|count).{0,250}(?:bootstrap|resampl(?:e|ed|ing)?)',joined))
    cats=[]
    if q3p:cats.append('Q3-P')
    if q3f:cats.append('Q3-F')
    if other:cats.append('Q3-O')
    if len(cats)==1: cls='PASS_0105A6Q3_EXPLICIT_PSEUDODATA_COUNT_LAW_SECONDARY_AUTHORITY_NONDISCOVERY'; detected=cats[0]
    elif not cats: cls='BLOCKED_0105A6Q3_PSEUDODATA_COUNT_LAW_STILL_NOT_EXPLICIT'; detected='NONE'
    else: cls='BLOCKED_0105A6Q3_CONFLICTING_PSEUDODATA_COUNT_LAW_AUTHORITY'; detected='CONFLICT'
    return detected,cls,{'poisson':{'pseudo_near_poisson':pseudo_poisson,'explicit_poisson_total':poisson_total,'extended_plus_poisson':extended_poisson},'fixed':{'fixed_total':fixed,'multinomial':multinomial},'other':{'bootstrap_or_resampling':other}}

def run(parent:Path,thesis:Path):
    if shaf(parent)!=PARENT_RESULT_SHA256:raise ValueError('q2 parent result SHA mismatch')
    p=json.loads(parent.read_text())
    if p.get('classification')!=PARENT_CLASS or p.get('candidate_pages')!=PAGES:raise ValueError('q2 parent classification/candidate set mismatch')
    if not thesis.exists():download(thesis)
    if thesis.stat().st_size!=THESIS_SIZE or shaf(thesis)!=THESIS_SHA256:raise ValueError('thesis identity mismatch')
    pp={page:extract_page(thesis,page) for page in PAGES}
    observed={page:sha(pp[page].encode()) for page in PAGES}
    if observed!=PAGE_HASHES:raise ValueError(f'candidate page hash mismatch: {observed}')
    detected,cls,markers=classify(pp)
    return {'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'parent_q2_result_sha256':PARENT_RESULT_SHA256,'candidate_pages':PAGES,'page_receipts':{str(x):{'normalized_text_sha256':observed[x],'bounded_window':window(pp[x])} for x in PAGES},'detected_count_law_category':detected,'markers':markers,'classification':cls,'full_page_text_retained':False,'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':100 if cls.startswith('PASS_') else 0,'systematic_monte_carlo_execution_permission_percent':0,'tierA_exact_collaboration_internal_likelihood':'BLOCKED','observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--parent-q2-result',required=True);ap.add_argument('--thesis',required=True);ap.add_argument('--output',required=True);ap.add_argument('--git-sha',required=True);a=ap.parse_args()
    try:r=run(Path(a.parent_q2_result),Path(a.thesis));r['git_sha']=a.git_sha
    except Exception as e:r={'benchmark':BENCHMARK,'preregistration_commit':PREREG_COMMIT,'git_sha':a.git_sha,'classification':'BLOCKED_0105A6Q3_SOURCE_OR_CANDIDATE_INTEGRITY_FAILURE','error_type':type(e).__name__,'error_message':str(e),'pseudo_data_generated':False,'likelihood_evaluated':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0,'observed_bsm_residual_inspected':False}
    o=Path(a.output);o.parent.mkdir(parents=True,exist_ok=True);o.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__':main()
