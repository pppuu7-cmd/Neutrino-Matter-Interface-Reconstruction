#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.error, urllib.request
from pathlib import Path

URL='https://export.arxiv.org/e-print/2304.12236'
SOURCE_SHA='111c41e49dd50880bc6b00aca95a2479216622b47235fcb68e2a02e22456a149'
MEMBERS={
 'main.tex':'2c25f03bfadc482a81a8f490efd15df3481988485630f92a255bb3f3c4c3708e',
 'MyBibFile.bib':'0055d6eb0585c44f2074b8f29712c38e1c645154d88830074fb7bff37b00e20c',
}
TAGS=['contours_working_0.1','4.3a1','4.2.1','4.2','4.1.4','4.1.3','4.1.2','4.1.1','4.1','4.0','3.2.1','3.2','3.1','3.0','2.0.1','2.0','1.0.1','1.0']

def contexts(text, needle='PISA', radius=240):
    out=[]; low=text.lower(); n=needle.lower(); start=0
    while True:
        i=low.find(n,start)
        if i<0: break
        out.append(text[max(0,i-radius):min(len(text),i+len(needle)+radius)])
        start=i+len(needle)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'0105a5b-R1i1','git_sha':a.git_sha,'classification':None,'authority_url':URL,'authority_bytes':None,'authority_sha256':None,'member_byte_locks':{},'pisa_occurrences':[],'qualified_version_matches':[],'matched_tags':[],
         'pisa_repository_content_inspected':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1i1-authority-only'})
        with urllib.request.urlopen(req,timeout=60) as r: raw=r.read(); status=int(r.status)
        if status!=200: raise RuntimeError(f'HTTP {status}')
        out['authority_bytes']=len(raw); out['authority_sha256']=hashlib.sha256(raw).hexdigest()
        if out['authority_sha256']!=SOURCE_SHA: raise RuntimeError('whole-source SHA256 mismatch')
        tf=tarfile.open(fileobj=io.BytesIO(raw),mode='r:*')
        texts={}
        for name,expected in MEMBERS.items():
            try: m=tf.getmember(name)
            except KeyError: raise RuntimeError(f'missing frozen member: {name}')
            f=tf.extractfile(m)
            if f is None: raise RuntimeError(f'unreadable frozen member: {name}')
            b=f.read(); got=hashlib.sha256(b).hexdigest()
            out['member_byte_locks'][name]={'bytes':len(b),'sha256':got,'expected_sha256':expected,'pass':got==expected}
            if got!=expected: raise RuntimeError(f'member SHA256 mismatch: {name}')
            texts[name]=b.decode('utf-8','replace')
        for name,text in texts.items():
            for c in contexts(text): out['pisa_occurrences'].append({'member':name,'context':c})
            for tag in TAGS:
                escaped=re.escape(tag)
                forms=[
                    ('PISA '+tag, rf'(?i)\bPISA\s+{escaped}(?![A-Za-z0-9.])'),
                    ('PISA v'+tag, rf'(?i)\bPISA\s+v{escaped}(?![A-Za-z0-9.])'),
                    ('PISA version '+tag, rf'(?i)\bPISA\s+version\s+{escaped}(?![A-Za-z0-9.])'),
                    ('PISA release '+tag, rf'(?i)\bPISA\s+release\s+{escaped}(?![A-Za-z0-9.])'),
                ]
                for form,pat in forms:
                    for m in re.finditer(pat,text):
                        c=text[max(0,m.start()-240):min(len(text),m.end()+240)]
                        out['qualified_version_matches'].append({'member':name,'tag':tag,'form':form,'context':c})
        out['matched_tags']=sorted({x['tag'] for x in out['qualified_version_matches']})
        if not out['pisa_occurrences']:
            out['classification']='BLOCKED_0105A5B_R1I1_PISA_NOT_REFERENCED_BY_ICECUBE_SOURCE'
        elif len(out['matched_tags'])==1:
            out['classification']='PASS_0105A5B_R1I1_PISA_USAGE_AND_VERSION_UNIQUELY_DISCRIMINATED_NONDISCOVERY'
        else:
            out['classification']='BLOCKED_0105A5B_R1I1_PISA_REFERENCED_VERSION_NOT_UNIQUELY_DISCRIMINATED'
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, tarfile.TarError, OSError, RuntimeError) as e:
        out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1I1'; out['error']=f'{type(e).__name__}: {e}'
    canon=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(canon).hexdigest()
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
