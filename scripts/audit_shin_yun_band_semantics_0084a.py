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
                if f: parts.append(f.read().decode('utf-8','replace'))
    return norm('\n'.join(parts))

def has(p,t): return bool(re.search(p,t,re.I|re.S))
def block(pattern,t,n=2200):
    m=re.search(pattern,t,re.I|re.S)
    return m.group(0)[:n] if m else ''

def audit(blob):
    h=hashlib.sha256(blob).hexdigest()
    if h!=SHA:
        return {'classification':'INFRASTRUCTURE_FAIL_ARCHIVE_HASH','archive_sha256':h,'expected_sha256':SHA}
    t=text_from(blob)
    body=block(r'We eventually find the constraint from SN1987A.{0,2200}',t)
    # TeX source wraps U(1)_{B-L} in math delimiters; anchor on the invariant prose
    # and SN1987A observation rather than markup spelling.
    concl=block(r'We have revisited the constraint.{0,180}?SN1987A.{0,1900}',t)
    checks={
      'excluded_region_explicit':has(r'parameter\s+space\s+excluded\s+by\s+SN1987A|regions?[^\.]{0,180}excluded\s+by\s+SN1987A',body or t),
      'reabsorption_explicit':has(r'gross\s+emission\s+rate[^\.]{0,180}reabsorption',body or t),
      'T_upper_body':has(r'e\^\\prime\s*<\s*10\^\{-11\}',body),
      'T_high_body_value':has(r'e\^\\prime\s*>\s*1\.5\s*\\times\s*10\^\{-8\}',body),
      'L_low_body':has(r'e\^\\prime\s*m_\{\\gamma\^\\prime\}\s*<\s*7\.4\s*\\times\s*10\^\{-10\}',body),
      'L_high_body_value':has(r'e\^\\prime\s*m_\{\\gamma\^\\prime\}\s*>\s*1\.2\s*\\times\s*10\^\{-5\}',body),
      'body_2me_allowed':has(r'are\s+allowed\s+for\s*\$?m_\{\\gamma\^\\prime\}\s*<\s*2m_e',body),
      'conclusion_revisited_SN1987A':has(r'revisited\s+the\s+constraint.{0,180}SN1987A',concl),
      'T_high_conclusion_value':has(r'e\^\\prime\s*>\s*1\.5\s*\\times\s*10\^\{-8\}',concl),
      'L_high_conclusion_value':has(r'e\^\\prime\s*m_\{\\gamma\^\\prime\}\s*>\s*1\.2\s*\\times\s*10\^\{-5\}',concl),
      'conclusion_1mev_domain':has(r'm_\{\\gamma\^\\prime\}\s*<\s*1[^;]{0,35}MeV',concl),
      'conclusion_allowed_word':has(r'allowed',concl),
    }
    passed=bool(body and concl) and all(checks.values())
    return {
      'classification':'PASS_SHIN_YUN_SN1987A_BAND_SEMANTICS' if passed else 'BLOCKED_SHIN_YUN_SN1987A_BAND_SEMANTICS',
      'archive_sha256':h,
      'checks':checks,
      'semantic_output':{
        'transverse_low_boundary':"e' < 1e-11 for m_gamma' < 20 MeV",
        'transverse_high_allowed_body':"e' > 1.5e-8 allowed for m_gamma' < 2 m_e",
        'transverse_high_allowed_conclusion':"e' > 1.5e-8 allowed for m_gamma' < 1 MeV",
        'longitudinal_low_allowed':"e' m_gamma' < 7.4e-10 MeV for m_gamma' < 20 MeV",
        'longitudinal_high_allowed_body':"e' m_gamma' > 1.2e-5 MeV allowed for m_gamma' < 2 m_e",
        'longitudinal_high_allowed_conclusion':"e' m_gamma' > 1.2e-5 MeV allowed for m_gamma' < 1 MeV",
        'domain_policy':'retain body <2 m_e and conclusion <1 MeV as distinct source-statement-conditioned domains; do not numerically identify or replace either in 0084a',
        'topology_guard':'the source explicitly labels an excluded SN1987A region while separately supplying high-coupling allowed/reabsorbed branches, so the low-coupling boundary cannot be promoted to exclusion of all larger couplings'
      },
      'source_blocks':{'body':body,'conclusion':concl}
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
    print(json.dumps({'classification':d['classification'],'archive_sha256':d['archive_sha256'],'checks':d.get('checks')},indent=2))
    if d['classification'].startswith('INFRASTRUCTURE_FAIL'): raise SystemExit(2)
if __name__=='__main__': main()
