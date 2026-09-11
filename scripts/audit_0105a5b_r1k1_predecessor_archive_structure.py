#!/usr/bin/env python3
import argparse, hashlib, io, json, tarfile, urllib.request, urllib.error
from pathlib import Path

URL='https://export.arxiv.org/e-print/1902.07771'
EXPECTED_SHA256='d095d23daf4dc08848b7f3ff5977daaf554db966034ca9d3460e4b88d7c3790a'
SUFFIXES=('.tex','.txt','.bib','.sty','.cls')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'0105a5b-R1k1','git_sha':a.git_sha,'classification':None,'url':URL,'expected_source_sha256':EXPECTED_SHA256,'observed_source_sha256':None,'members':[],'source_text_candidates':[],
         'member_payload_read':False,'source_text_inspected':False,'pisa_repository_content_inspected':False,'standard_3nu_executed':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-v2-R1k1-structure-only'})
        with urllib.request.urlopen(req,timeout=60) as r: raw=r.read()
        out['observed_source_sha256']=hashlib.sha256(raw).hexdigest()
        if out['observed_source_sha256'] != EXPECTED_SHA256:
            out['classification']='BLOCKED_0105A5B_R1K1_SOURCE_BYTE_IDENTITY_MISMATCH'
        else:
            with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tf:
                for m in tf.getmembers():
                    typ='file' if m.isfile() else ('dir' if m.isdir() else 'other')
                    out['members'].append({'name':m.name,'type':typ,'size':int(m.size)})
            out['source_text_candidates']=[x['name'] for x in out['members'] if x['type']=='file' and x['name'].lower().endswith(SUFFIXES)]
            out['classification']='PASS_0105A5B_R1K1_PREDECESSOR_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY' if out['members'] else 'INFRASTRUCTURE_FAIL_0105A5B_R1K1'
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, tarfile.TarError) as e:
        out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1K1'; out['error']=f'{type(e).__name__}: {e}'
    canon=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(canon).hexdigest()
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

if __name__=='__main__': main()
