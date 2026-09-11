#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.error, urllib.request
from pathlib import Path

URL='https://export.arxiv.org/e-print/1106.3723v1'
EXPECTED_SHA256='274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce'
MEMBER='nucross.tex'
TERM_RE=re.compile(r'\b(uncertaint(?:y|ies)|errors?|PDF|parton|cross[ -]?section|neutrino|antineutrino|normalization|scale|variations?)\b',re.I)
PERCENT_RE=re.compile(r'(?<!\d)(\d+(?:\.\d+)?)\s*(?:\\?%|percent\b)',re.I)

def contexts(lines, indices, radius=3):
    out=[]; seen=set()
    for i in sorted(indices):
        lo=max(0,i-radius); hi=min(len(lines),i+radius+1)
        key=(lo,hi)
        if key in seen: continue
        seen.add(key); out.append({'start_line':lo+1,'end_line':hi,'text':'\n'.join(lines[lo:hi])})
    return out

def inspect_text(text):
    lines=text.splitlines(); term_hits=[]; quantitative_hits=[]
    for i,line in enumerate(lines):
        if TERM_RE.search(line): term_hits.append(i)
        window=' '.join(lines[max(0,i-2):min(len(lines),i+3)])
        if PERCENT_RE.search(window) and re.search(r'uncert|error|PDF|cross[ -]?section|QCD|prediction',window,re.I): quantitative_hits.append(i)
    explicit_prescription=bool(quantitative_hits) or bool(re.search(r'(?is)(uncertaint(?:y|ies)|errors?).{0,350}(PDF|parton|scale|cross[ -]?section)|(PDF|parton|scale|cross[ -]?section).{0,350}(uncertaint(?:y|ies)|errors?)',text))
    nu_anu=bool(re.search(r'(?is)neutrino.{0,300}antineutrino|antineutrino.{0,300}neutrino',text))
    quantitative=bool(quantitative_hits)
    passed=explicit_prescription and quantitative
    return {'term_contexts':contexts(lines,term_hits),'quantitative_uncertainty_contexts':contexts(lines,quantitative_hits),'explicit_uncertainty_prescription_present':explicit_prescription,'quantitative_uncertainty_present':quantitative,'neutrino_antineutrino_joint_context_present':nu_anu,'semantic_pass':passed}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'0105a5b-R1m2','git_sha':a.git_sha,'classification':None,'url':URL,'expected_source_sha256':EXPECTED_SHA256,'source_sha256':None,'byte_lock_verified':False,'candidate_member':MEMBER,'member_payload_read':False,'source_text_inspected':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1m2-semantic-authority-only'})
        with urllib.request.urlopen(req,timeout=60) as r: raw=r.read(); out['http_status']=int(r.status); out['final_url']=r.geturl()
        out['source_sha256']=hashlib.sha256(raw).hexdigest()
        if out['http_status']!=200 or out['source_sha256']!=EXPECTED_SHA256: raise RuntimeError('frozen source byte lock failed')
        out['byte_lock_verified']=True
        with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tf:
            names=[m.name for m in tf.getmembers() if m.isfile() and m.name.lower().endswith(('.tex','.ltx','.txt','.bib','.sty','.cls'))]
            if names!=[MEMBER]: raise RuntimeError(f'frozen candidate set mismatch: {names!r}')
            f=tf.extractfile(MEMBER)
            if f is None: raise RuntimeError('candidate member unavailable')
            text=f.read().decode('utf-8',errors='replace'); out['member_payload_read']=True; out['source_text_inspected']=True
        out.update(inspect_text(text)); out['candidate_text_sha256']=hashlib.sha256(text.encode('utf-8')).hexdigest()
        out['classification']='PASS_0105A5B_R1M2_CSMS2011_PRIMARY_DIS_UNCERTAINTY_SEMANTICS_LOCATED_NONDISCOVERY' if out['semantic_pass'] else 'BLOCKED_0105A5B_R1M2_CSMS2011_PRIMARY_DIS_UNCERTAINTY_SEMANTICS_INCOMPLETE'
    except (urllib.error.URLError,urllib.error.HTTPError,TimeoutError,OSError,tarfile.TarError,RuntimeError) as e:
        out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1M2'; out['error']=f'{type(e).__name__}: {e}'
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

if __name__=='__main__': main()
