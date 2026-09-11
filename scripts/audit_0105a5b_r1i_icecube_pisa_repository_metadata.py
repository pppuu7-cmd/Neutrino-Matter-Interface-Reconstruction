#!/usr/bin/env python3
import argparse, hashlib, json, re, urllib.error, urllib.request
from pathlib import Path

ENDPOINTS={
 'repository':'https://api.github.com/repos/icecube/pisa',
 'tags':'https://api.github.com/repos/icecube/pisa/tags?per_page=100',
 'releases':'https://api.github.com/repos/icecube/pisa/releases?per_page=100',
}
HEX40=re.compile(r'^[0-9a-f]{40}$')

def get_json(url):
    req=urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'NMIR-v2-R1i-metadata-only'})
    with urllib.request.urlopen(req,timeout=60) as r:
        raw=r.read(); status=int(r.status)
    if status!=200: raise RuntimeError(f'HTTP {status}: {url}')
    return raw,json.loads(raw.decode('utf-8'))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':'0105a5b-R1i','git_sha':a.git_sha,'classification':None,'endpoints':{},'tag_lineage':[],
         'readme_inspected':False,'implementation_inspected':False,'archive_inspected':False,'standard_3nu_executed':False,
         'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,
         'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
    try:
        parsed={}
        for k,u in ENDPOINTS.items():
            raw,obj=get_json(u); parsed[k]=obj
            out['endpoints'][k]={'url':u,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
        repo=parsed['repository']; tags=parsed['tags']; releases=parsed['releases']
        out['repository_identity']={'full_name':repo.get('full_name'),'owner_login':(repo.get('owner') or {}).get('login'),'private':repo.get('private'),'default_branch':repo.get('default_branch')}
        for t in tags:
            out['tag_lineage'].append({'name':t.get('name'),'commit_sha':(t.get('commit') or {}).get('sha')})
        out['release_metadata']=[{'tag_name':x.get('tag_name'),'name':x.get('name'),'draft':x.get('draft'),'prerelease':x.get('prerelease'),'published_at':x.get('published_at')} for x in releases]
        identity=(repo.get('full_name')=='icecube/pisa' and (repo.get('owner') or {}).get('login')=='icecube' and repo.get('private') is False)
        tags_ok=(len(out['tag_lineage'])>0 and all(bool(x['name']) and bool(HEX40.fullmatch(x['commit_sha'] or '')) for x in out['tag_lineage']))
        out['classification']='PASS_0105A5B_R1I_ICECUBE_PISA_METADATA_PINNABLE_NONDISCOVERY' if identity and tags_ok else 'BLOCKED_0105A5B_R1I_ICECUBE_PISA_METADATA_NOT_PINNABLE'
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, OSError, RuntimeError) as e:
        out['classification']='INFRASTRUCTURE_FAIL_0105A5B_R1I'; out['error']=f'{type(e).__name__}: {e}'
    canon=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(canon).hexdigest()
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
