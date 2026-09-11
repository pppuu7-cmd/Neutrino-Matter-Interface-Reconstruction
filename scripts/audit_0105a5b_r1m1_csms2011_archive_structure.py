#!/usr/bin/env python3
import argparse, hashlib, io, json, tarfile, urllib.error, urllib.request
from pathlib import Path, PurePosixPath
URL='https://export.arxiv.org/e-print/1106.3723v1'
EXPECTED_SHA256='274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce'
EXTS=('.tex','.ltx','.txt','.bib','.sty','.cls')
def safe_name(name):
    p=PurePosixPath(name); return bool(name) and not p.is_absolute() and '..' not in p.parts
def member_type(m):
    if m.isfile(): return 'file'
    if m.isdir(): return 'dir'
    if m.issym(): return 'symlink'
    if m.islnk(): return 'hardlink'
    return 'other'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'0105a5b-R1m1','git_sha':a.git_sha,'classification':None,'url':URL,'expected_source_sha256':EXPECTED_SHA256,'http_status':None,'final_url':None,'bytes':None,'source_sha256':None,'byte_lock_verified':False,'archive_opened':False,'member_payload_read':False,'source_text_inspected':False,'csms_nuisance_semantics_inferred':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'members':[],'source_text_candidates':[],'manifest_sha256':None}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1m1-archive-structure-only'})
        with urllib.request.urlopen(req,timeout=60) as r:
            raw=r.read(); out['http_status']=int(r.status); out['final_url']=r.geturl()
        out['bytes']=len(raw); out['source_sha256']=hashlib.sha256(raw).hexdigest()
        if out['http_status']!=200 or not raw or out['source_sha256']!=EXPECTED_SHA256: raise RuntimeError('frozen source byte lock failed')
        out['byte_lock_verified']=True
        with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tf:
            out['archive_opened']=True
            for m in tf.getmembers():
                if not safe_name(m.name): raise RuntimeError(f'unsafe archive member: {m.name!r}')
                rec={'name':m.name,'type':member_type(m),'size':int(m.size)}; out['members'].append(rec)
                if m.isfile() and m.name.lower().endswith(EXTS): out['source_text_candidates'].append(m.name)
        manifest={'members':out['members'],'source_text_candidates':out['source_text_candidates']}
        out['manifest_sha256']=hashlib.sha256(json.dumps(manifest,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        out['classification']='PASS_0105A5B_R1M1_CSMS2011_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY'
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, tarfile.TarError, RuntimeError) as e:
        out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1M1'; out['error']=f'{type(e).__name__}: {e}'
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
