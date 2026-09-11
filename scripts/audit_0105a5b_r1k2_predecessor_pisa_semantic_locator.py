#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.request, urllib.error
from pathlib import Path

URL='https://export.arxiv.org/e-print/1902.07771'
EXPECTED_SHA256='d095d23daf4dc08848b7f3ff5977daaf554db966034ca9d3460e4b88d7c3790a'
CANDIDATES=['history.txt','main.bib','main.tex','readme-epjc.txt','svjour3.cls','text/SampleAndReco.tex','text/abstract.tex','text/acknowledgement.tex','text/analysis.tex','text/conclusion.tex','text/icecube.tex','text/introduction.tex','text/results.tex','text/sensitivity.tex']
VERSION_RE=re.compile(r'(?i)\b(?:v\d+(?:\.\d+){0,2}|version\s+\d+(?:\.\d+){0,2}|release\s+\d+(?:\.\d+){0,2}|tag\s+[^\s,;(){}]+|commit\s+[0-9a-f]{7,40})\b')
HEX40_RE=re.compile(r'(?i)\b[0-9a-f]{40}\b')
REPO_RE=re.compile(r'(?i)(?:https?://[^\s{}<>]*pisa[^\s{}<>]*|icecube/pisa)')


def bounded_contexts(text, needle='pisa', radius=300):
    out=[]
    low=text.lower(); pos=0
    while True:
        i=low.find(needle,pos)
        if i<0: break
        lo=max(0,i-radius); hi=min(len(text),i+len(needle)+radius)
        out.append(text[lo:hi]); pos=i+len(needle)
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'0105a5b-R1k2','git_sha':a.git_sha,'classification':None,'url':URL,'expected_source_sha256':EXPECTED_SHA256,'observed_source_sha256':None,'candidate_set':CANDIDATES,'files':{},'repo_literals':[],'nearby_hex40':[],'nearby_version_forms':[],
         'pisa_repository_content_fetched':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1k2-bounded-semantic-locator'})
        with urllib.request.urlopen(req,timeout=60) as r: raw=r.read()
        out['observed_source_sha256']=hashlib.sha256(raw).hexdigest()
        if out['observed_source_sha256'] != EXPECTED_SHA256:
            out['classification']='BLOCKED_0105A5B_R1K2_SOURCE_BYTE_IDENTITY_MISMATCH'
        else:
            with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tf:
                names={m.name:m for m in tf.getmembers()}
                if set(CANDIDATES)-set(names):
                    out['classification']='BLOCKED_0105A5B_R1K2_FROZEN_CANDIDATE_SET_INCOMPLETE'
                else:
                    for name in CANDIDATES:
                        f=tf.extractfile(names[name]); data=f.read() if f else b''
                        text=data.decode('utf-8','replace')
                        ctx=bounded_contexts(text)
                        repos=sorted(set(REPO_RE.findall(text)))
                        hexes=[]; vers=[]
                        for c in ctx:
                            hexes += HEX40_RE.findall(c); vers += VERSION_RE.findall(c)
                        rec={'pisa_context_count':len(ctx),'pisa_contexts':ctx,'repo_literals':repos,'nearby_hex40':sorted(set(hexes)),'nearby_version_forms':sorted(set(vers))}
                        out['files'][name]=rec
                        out['repo_literals'] += repos; out['nearby_hex40'] += hexes; out['nearby_version_forms'] += vers
                    out['repo_literals']=sorted(set(out['repo_literals'])); out['nearby_hex40']=sorted(set(out['nearby_hex40'])); out['nearby_version_forms']=sorted(set(out['nearby_version_forms']))
                    out['classification']='PASS_0105A5B_R1K2_PREDECESSOR_PISA_IMMUTABLE_STATE_EXPLICIT_NONDISCOVERY' if (out['nearby_hex40'] or out['nearby_version_forms']) else 'BLOCKED_0105A5B_R1K2_PREDECESSOR_PISA_STATE_NOT_IMMUTABLY_IDENTIFIED'
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, tarfile.TarError) as e:
        out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1K2'; out['error']=f'{type(e).__name__}: {e}'
    canon=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(canon).hexdigest()
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

if __name__=='__main__': main()
