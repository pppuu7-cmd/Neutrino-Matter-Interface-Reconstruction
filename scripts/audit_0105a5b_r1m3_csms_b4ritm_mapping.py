#!/usr/bin/env python3
import argparse, hashlib, json, re, subprocess
from pathlib import Path

PATH_TOKENS=('b4ritm','deepcore','icecube','0105a5b')
ROOTS=('research/','data/','scripts/','theory/')
EXCLUDE_TOKENS=('r1m3_csms_b4ritm_mapping','0105a5b_r1m3')
ANCHOR_RE=re.compile(r'\b(CSMS|Cooper[- ]Sarkar|DIS|cross[- ]?section)\b',re.I)
EXPERIMENT_RE=re.compile(r'\b(IceCube|DeepCore|B4RITM)\b',re.I)
BUCKETS={
 'identifier':re.compile(r'(?i)(nuisance|parameter|systematic|direction|identifier|name\s*[:=]|cross[- ]?section[^\n]{0,80}(?:uncertaint|nuisance|systematic))'),
 'transform':re.compile(r'(?i)(reweight|event[- ]?weight|weight(?:ing)?\s+(?:function|ratio|factor)|multiplicative|scale\s+factor|response\s+function|transform(?:ation)?|ratio\s*\(|d\s*log|derivative)'),
 'orientation':re.compile(r'(?i)(up/down|up\s+and\s+down|plus/minus|positive/negative|sign\s+convention|orientation|\+\s*/\s*-|[-+]?1\s*sigma)'),
 'prior_range':re.compile(r'(?i)(prior|range|amplitude|width|sigma|standard deviation|\b\d+(?:\.\d+)?\s*%|\[-?\d[^\]]*,[^\]]+\])'),
 'covariance':re.compile(r'(?i)(covariance|correlation|correlated|uncorrelated|normalization\s+convention|normalisation\s+convention|correlation\s+matrix)')
}

def tracked_files():
    out=subprocess.check_output(['git','ls-files'],text=True).splitlines()
    selected=[]
    for p in sorted(out):
        low=p.lower()
        if not p.startswith(ROOTS): continue
        if not any(t in low for t in PATH_TOKENS): continue
        if any(t in low for t in EXCLUDE_TOKENS): continue
        selected.append(p)
    return selected

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()

def contexts(text, radius=500):
    out=[]
    for m in ANCHOR_RE.finditer(text):
        lo=max(0,m.start()-radius); hi=min(len(text),m.end()+radius)
        chunk=text[lo:hi]
        if EXPERIMENT_RE.search(chunk): out.append(chunk)
    return out

def lexical_diagnostics(texts):
    evidence={k:[] for k in BUCKETS}
    anchored_context_count=0
    for path,text in texts:
        for chunk in contexts(text):
            anchored_context_count+=1
            for key,rx in BUCKETS.items():
                if rx.search(chunk):
                    evidence[key].append({'path':path,'context_sha256':sha256_bytes(chunk.encode()),'excerpt':chunk[:1200]})
    return anchored_context_count,evidence

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    result={'gate':'0105a5b-R1m3','git_sha':a.git_sha,'classification':None,'corpus_rule':'tracked path under research/data/scripts/theory containing b4ritm/deepcore/icecube/0105a5b; R1m3 self-files excluded','corpus':[],'anchored_context_count':0,'evidence':{},'lexical_bucket_hits':{},'scientific_mapping_complete_machine_claim':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'network_requests_executed':False}
    try:
        texts=[]
        paths=tracked_files()
        if not paths: raise RuntimeError('frozen corpus path rule selected zero tracked files')
        for path in paths:
            b=Path(path).read_bytes(); entry={'path':path,'sha256':sha256_bytes(b),'bytes':len(b),'readable_utf8':False}
            try:
                text=b.decode('utf-8'); entry['readable_utf8']=True; texts.append((path,text))
            except UnicodeDecodeError:
                pass
            result['corpus'].append(entry)
        nctx,evidence=lexical_diagnostics(texts)
        result['anchored_context_count']=nctx; result['evidence']=evidence
        result['lexical_bucket_hits']={k:len(v) for k,v in evidence.items()}
        # Amendment 01: lexical presence is diagnostic only. Negative/absence statements
        # can contain the same words, so hosted code must not self-promote to a
        # scientific PASS. Classification is performed only after artifact review
        # against the original five-element preregistered semantic contract.
        result['classification']='EVIDENCE_BUNDLE_ONLY_0105A5B_R1M3_UNCLASSIFIED'
    except (OSError,subprocess.SubprocessError,RuntimeError) as e:
        result['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1M3'; result['error']=f'{type(e).__name__}: {e}'
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')

if __name__=='__main__': main()
