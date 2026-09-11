#!/usr/bin/env python3
import argparse, hashlib, json, urllib.request, urllib.error
from pathlib import Path

CANDIDATES = {
"mceq108":"d6246a179075a43a14b3839fa7e600277518f813",
"mceq_1_1_1":"03200f418cce6240d5f5427ec7aa108868b8ca71",
"release_1_1_2":"bcee968da8021016558d033088e348c54fdffc7f",
"release_1_1_3":"344a573d5e87a82a187fd53d3647b4145472c1ac",
"release_1_2_0":"7f10aae90d1714997216edcf82a099628d1ff3c6",
"release_1_2_1":"dc71cd599e56d9eeda8bfa16a55dcc5d8a478109",
"release_1_2_2":"23108b123bb5173a08761add0e95678e93776ba9",
"release_1_2_3":"de7ebb7e4c127726cb12c0beb269f81ce865358c",
"release_1_2_4":"3e87560f7a25f9579cfe7a0144156beae3fe9610",
"release_1_2_5":"23ab910d3e346c68d769267780602b0bae37b7a8",
"release_1_2_6":"553a0a62e17f86e11a80b80aa9ffcf528157ac81"}
BASE="https://api.github.com/repos/mceq-project/MCEq/commits/"

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',required=True); p.add_argument('--git-sha',required=True); a=p.parse_args()
    out={"gate":"0105a5b-R1g","git_sha":a.git_sha,"classification":None,"candidates":[],"source_code_inspected":False,"trees_or_blobs_inspected":False,"standard_3nu_executed":False,"systematic_monte_carlo_executed":False,"observed_bsm_residual_inspected":False,"observed_bsm_residual_permission_percent":0,"systematic_monte_carlo_execution_permission_percent":0}
    try:
      ok=True
      for tag,sha in CANDIDATES.items():
        url=BASE+sha
        req=urllib.request.Request(url,headers={"User-Agent":"NMIR-v2-R1g-metadata-only","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"})
        with urllib.request.urlopen(req,timeout=30) as r:
          raw=r.read(); status=int(r.status); d=json.loads(raw.decode())
        match=(status==200 and d.get('sha')==sha); ok &= match
        out['candidates'].append({"tag":tag,"frozen_sha":sha,"status":status,"sha_match":match,"response_bytes":len(raw),"response_sha256":hashlib.sha256(raw).hexdigest(),"author_date":((d.get('commit') or {}).get('author') or {}).get('date'),"committer_date":((d.get('commit') or {}).get('committer') or {}).get('date'),"parent_shas":[x.get('sha') for x in d.get('parents',[])]})
      out['classification']="PASS_0105A5B_R1G_MCEQ_HISTORICAL_RELEASE_LINEAGE_PINNED_NONDISCOVERY" if ok else "BLOCKED_0105A5B_R1G_MCEQ_HISTORICAL_RELEASE_LINEAGE_INCOMPLETE"
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
      out['classification']="INFRASTRUCTURE_FAIL_0105A5B_R1G"; out['transport_error']=f"{type(e).__name__}: {e}"
    b=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_result_sha256_before_self_field']=hashlib.sha256(b).hexdigest()
    path=Path(a.output); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
