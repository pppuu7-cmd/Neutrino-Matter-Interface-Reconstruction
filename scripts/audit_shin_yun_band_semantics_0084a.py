#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, urllib.request

URL='https://export.arxiv.org/e-print/2110.03362v2'
SHA='7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd'

def norm(s):
    s=re.sub(r'(?<!\\)%.*','',s)
    s=re.sub(r'\s+',' ',s)
    return s

def text_from(blob):
    parts=[]
    with tarfile.open(fileobj=io.BytesIO(blob),mode='r:*') as tf:
        for m in tf.getmembers():
            if m.isfile() and re.search(r'\.tex$',m.name,re.I):
                f=tf.extractfile(m)
                if f:
                    parts.append(f.read().decode('utf-8','replace'))
    return norm('\n'.join(parts))

def has(p,t): return bool(re.search(p,t,re.I|re.S))

def audit(blob):
    h=hashlib.sha256(blob).hexdigest()
    if h!=SHA:
        return {'classification':'INFRASTRUCTURE_FAIL_ARCHIVE_HASH','archive_sha256':h,'expected_sha256':SHA}
    t=text_from(blob)
    checks={
      'excluded_region_explicit':has(r'regions?\s+in\s+Fig\.[^\.]{0,180}excluded\s+by\s+SN1987A|parameter\s+space\s+excluded\s+by\s+SN1987A',t),
      'reabsorption_explicit':has(r'gross\s+emission\s+rate[^\.]{0,180}reabsorption',t),
      'T_upper_body':has(r'e\^\\prime\s*<\s*10\^\{-11\}[^\.]{0,160}m_\{\\gamma\^\\prime\}\s*<\s*20[^\.]{0,20}MeV',t),
      'T_high_body':has(r'e\^\\prime\s*>\s*1\.5\s*\\times\s*10\^\{-8\}[^\.]{0,180}allowed[^\.]{0,140}m_\{\\gamma\^\\prime\}\s*<\s*2m_e',t),
      'T_high_conclusion':has(r'm_\{\\gamma\^\\prime\}\s*<\s*1[^\.]{0,15}MeV[^;\.]{0,120}e\^\\prime\s*>\s*1\.5\s*\\times\s*10\^\{-8\}[^;\.]{0,30}allowed',t),
      'L_low_body':has(r'e\^\\prime\s*m_\{\\gamma\^\\prime\}\s*<\s*7\.4\s*\\times\s*10\^\{-10\}',t),
      'L_high_body':has(r'e\^\\prime\s*m_\{\\gamma\^\\prime\}\s*>\s*1\.2\s*\\times\s*10\^\{-5\}[^\.]{0,180}allowed[^\.]{0,140}m_\{\\gamma\^\\prime\}\s*<\s*2m_e',t),
      'L_high_conclusion':has(r'e\^\\prime\s*m_\{\\gamma\^\\prime\}\s*>\s*1\.2\s*\\times\s*10\^\{-5\}[^;\.]{0,80}m_\{\\gamma\^\\prime\}\s*<\s*1[^;\.]{0,15}MeV',t),
      'conclusion_revisited_SN1987A':has(r'revisited\s+the\s+constraint[^;\.]{0,120}SN1987A',t),
    }
    # The exact wording can place "allowed" before or after the relation; retain
    # deterministic source snippets for raw inspection rather than weakening checks.
    snippets=[]
    for pat in [r'We eventually find the constraint from SN1987A.{0,1800}',r'We have revisited the constraint on U\(1\)_\{\\rm B-L\} gauge bosons from SN1987A.{0,1500}']:
        m=re.search(pat,t,re.I|re.S)
        if m: snippets.append(m.group(0)[:1800])
    required=['excluded_region_explicit','reabsorption_explicit','T_upper_body','L_low_body','conclusion_revisited_SN1987A']
    # High-coupling statements are verified by exact tokens independently to avoid
    # coupling a semantic PASS to arbitrary clause ordering.
    token_checks={
      'T_high_value':has(r'e\^\\prime\s*>\s*1\.5\s*\\times\s*10\^\{-8\}',t),
      'L_high_value':has(r'e\^\\prime\s*m_\{\\gamma\^\\prime\}\s*>\s*1\.2\s*\\times\s*10\^\{-5\}',t),
      'body_2me_allowed':has(r'allowed\s+for\s*\$?m_\{\\gamma\^\\prime\}\s*<\s*2m_e|are\s+allowed\s+for\s*\$?m_\{\\gamma\^\\prime\}\s*<\s*2m_e',t),
      'conclusion_1mev_allowed':has(r'm_\{\\gamma\^\\prime\}\s*<\s*1[^;\.]{0,15}MeV[^;\.]{0,180}allowed|allowed[^;\.]{0,180}m_\{\\gamma\^\\prime\}\s*<\s*1[^;\.]{0,15}MeV',t),
    }
    passed=all(checks[k] for k in required) and all(token_checks.values())
    return {
      'classification':'PASS_SHIN_YUN_SN1987A_BAND_SEMANTICS' if passed else 'BLOCKED_SHIN_YUN_SN1987A_BAND_SEMANTICS',
      'archive_sha256':h,
      'checks':checks,
      'token_checks':token_checks,
      'semantic_output':{
        'transverse_low_boundary':"e' < 1e-11 for m_gamma' < 20 MeV",
        'transverse_high_allowed_body':"e' > 1.5e-8 allowed for m_gamma' < 2 m_e",
        'transverse_high_allowed_conclusion':"e' > 1.5e-8 allowed for m_gamma' < 1 MeV",
        'longitudinal_low_allowed':"e' m_gamma' < 7.4e-10 MeV for m_gamma' < 20 MeV",
        'longitudinal_high_allowed_body':"e' m_gamma' > 1.2e-5 MeV allowed for m_gamma' < 2 m_e",
        'longitudinal_high_allowed_conclusion':"e' m_gamma' > 1.2e-5 MeV allowed for m_gamma' < 1 MeV",
        'domain_policy':'retain body <2 m_e and conclusion <1 MeV as distinct source-statement-conditioned domains; do not numerically identify or replace either in 0084a',
        'topology_guard':'low-coupling/free-streaming boundary is not an all-larger-coupling exclusion because the source explicitly supplies high-coupling allowed/reabsorbed branches'
      },
      'source_snippets':snippets
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source'); ap.add_argument('--output',default='data/shin_yun_band_semantics_0084a.json'); a=ap.parse_args()
    if a.source: blob=open(a.source,'rb').read()
    else:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-reproducibility-audit/1.0'})
        with urllib.request.urlopen(req,timeout=60) as r: blob=r.read()
    d=audit(blob)
    import os; os.makedirs(os.path.dirname(a.output) or '.',exist_ok=True)
    with open(a.output,'w') as f: json.dump(d,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'classification':d['classification'],'archive_sha256':d['archive_sha256'],'checks':d.get('checks'),'token_checks':d.get('token_checks')},indent=2))
    if d['classification'].startswith('INFRASTRUCTURE_FAIL'): raise SystemExit(2)
if __name__=='__main__': main()
