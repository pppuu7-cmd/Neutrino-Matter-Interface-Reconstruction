#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.error, urllib.request
from pathlib import Path

URL='https://export.arxiv.org/e-print/astro-ph/0611266v1'
EXPECTED_SHA256='f128800ae1eb18fb58c27ce91941b726f1bbf42a7f7ac17a273664f3a81da0f7'
MEMBER='uncertainflux.tex'
LABEL_RE=re.compile(r'(?<![A-Za-z])([WYZ])\s*(?:\^\s*\{?\s*([+-])\s*\}?|([+-]))')
TERM_RE=re.compile(r'\b(uncertaint(?:y|ies)|errors?|parameters?|variations?|vary|flux|pions?|kaons?)\b',re.I)

def contexts(lines, indices, radius=3):
    out=[]; seen=set()
    for i in sorted(indices):
        lo=max(0,i-radius); hi=min(len(lines),i+radius+1)
        key=(lo,hi)
        if key in seen: continue
        seen.add(key)
        out.append({'start_line':lo+1,'end_line':hi,'text':'\n'.join(lines[lo:hi])})
    return out

def inspect_text(text):
    lines=text.splitlines()
    label_hits=[]; term_hits=[]; families=set(); signs=set()
    for i,line in enumerate(lines):
        ms=list(LABEL_RE.finditer(line))
        if ms:
            label_hits.append(i)
            for m in ms:
                families.add(m.group(1)); signs.add(m.group(2) or m.group(3))
        if TERM_RE.search(line): term_hits.append(i)
    explicit_variation=bool(re.search(r'\b(vary|variation|variations|uncertainty|uncertainties|error|errors|parameter|parameters)\b',text,re.I))
    flux_link=bool(re.search(r'(?is)(W|Y|Z).{0,500}(flux|pion|kaon)|(flux|pion|kaon).{0,500}(W|Y|Z)',text))
    passed=families=={'W','Y','Z'} and '+' in signs and '-' in signs and explicit_variation and flux_link
    return {
        'families':sorted(families),'signs':sorted(signs),
        'label_contexts':contexts(lines,label_hits),
        'term_contexts':contexts(lines,term_hits),
        'explicit_variation_language':explicit_variation,
        'named_family_flux_link_present':flux_link,
        'semantic_pass':passed,
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'0105a5b-R1l2','git_sha':a.git_sha,'classification':None,'url':URL,'expected_source_sha256':EXPECTED_SHA256,'source_sha256':None,'byte_lock_verified':False,'candidate_member':MEMBER,'member_payload_read':False,'source_text_inspected':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1l2-semantic-authority-only'})
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
        out.update(inspect_text(text))
        out['candidate_text_sha256']=hashlib.sha256(text.encode('utf-8')).hexdigest()
        out['classification']='PASS_0105A5B_R1L2_BARR2006_PRIMARY_NUISANCE_SEMANTICS_LOCATED_NONDISCOVERY' if out['semantic_pass'] else 'BLOCKED_0105A5B_R1L2_BARR2006_PRIMARY_NUISANCE_SEMANTICS_INCOMPLETE'
    except (urllib.error.URLError,urllib.error.HTTPError,TimeoutError,OSError,tarfile.TarError,RuntimeError) as e:
        out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1L2'; out['error']=f'{type(e).__name__}: {e}'
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

if __name__=='__main__': main()
