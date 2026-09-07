#!/usr/bin/env python3
import hashlib, io, json, re, tarfile, time, urllib.request

URL="https://export.arxiv.org/e-print/2012.05427v3"
ARCHIVE_SHA256="6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc"
EP=r"e(?:\^\{?\\prime\}?|_?\\prime|')"
NUM=r"(?:(?P<factor>\d+(?:\.\d+)?)\s*(?:\\times|×)\s*)?10\^\{?(?P<exp>[+-]?\d+)\}?"

def sha256(b): return hashlib.sha256(b).hexdigest()

def fetch(url):
    last=None
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"NMIR-0083a-r1/1.0"})
            with urllib.request.urlopen(req,timeout=90) as r:return r.read()
        except Exception as e:
            last=e; time.sleep(2**i)
    raise RuntimeError(f"fetch failed: {last}")

def compact(s):
    s=re.sub(r"(?<!\\)%.*","",s).replace("\n"," ")
    s=re.sub(r"\\(?:mathrm|text|rm|mbox)\s*\{([^{}]*)\}",r"\1",s)
    s=re.sub(r"\{\\(?:mathrm|text|rm|mbox)\s+([^{}]+)\}",r"\1",s)
    s=s.replace("\\,"," ").replace("\\!","").replace("~"," ")
    return re.sub(r"\s+"," ",s)

def tex_files(raw):
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
        out=[]
        for m in tf.getmembers():
            n=m.name.lstrip("./")
            if not (m.isfile() and n.lower().endswith('.tex')): continue
            b=tf.extractfile(m).read()
            try:t=b.decode('utf-8')
            except UnicodeDecodeError:t=b.decode('latin-1')
            out.append((n,compact(t)))
        return out

def val(f,e): return float(f or 1.0)*10.0**int(e)

def relations(text):
    out=[]
    up=re.compile(EP+r"\s*(?:<|\\lesssim|\\leq|\\le)\s*"+NUM,re.I)
    for m in up.finditer(text): out.append({'kind':'upper_bound','start':m.start(),'end':m.end(),'expression':m.group(0),'low':None,'high':val(m.group('factor'),m.group('exp'))})
    ap=re.compile(EP+r"\s*(?:\\sim|≈|~)\s*"+NUM,re.I)
    for m in ap.finditer(text): out.append({'kind':'approx_value','start':m.start(),'end':m.end(),'expression':m.group(0),'low':None,'high':val(m.group('factor'),m.group('exp'))})
    left=r"(?:(?P<lf>\d+(?:\.\d+)?)\s*(?:\\times|×)\s*)?10\^\{?(?P<le>[+-]?\d+)\}?"
    right=r"(?:(?P<rf>\d+(?:\.\d+)?)\s*(?:\\times|×)\s*)?10\^\{?(?P<re>[+-]?\d+)\}?"
    ip=re.compile(left+r"\s*<\s*"+EP+r"\s*<\s*"+right,re.I)
    ints=[]
    for m in ip.finditer(text):
        r={'kind':'interval','start':m.start(),'end':m.end(),'expression':m.group(0),'low':val(m.group('lf'),m.group('le')),'high':val(m.group('rf'),m.group('re'))}
        ints.append(r); out.append(r)
    out=[r for r in out if r['kind']=='interval' or not any(i['start']<=r['start'] and r['end']<=i['end'] for i in ints)]
    return sorted(out,key=lambda r:(r['start'],r['end'],r['kind']))

def statement(text,start,end):
    left=max(text.rfind('.',0,start),text.rfind('!',0,start),text.rfind('?',0,start))
    rights=[p for p in (text.find('.',end),text.find('!',end),text.find('?',end)) if p!=-1]
    right=min(rights) if rights else min(len(text),end+1200)
    return text[left+1:right+1].strip()

def context(text,start,end,radius=1000): return text[max(0,start-radius):min(len(text),end+radius)]

def observation(stmt,ctx):
    s=stmt.lower()
    if re.search(r"cas\s*a|cassiopeia\s*a",s): return 'Cas A'
    if 'ns1987a' in s: return 'NS1987A'
    if 'sn1987a' in s: return 'SN1987A'
    c=ctx.lower()
    # General abstract/result scope when multiple young-NS remnants appear nearby but no single observation is attached to this statement.
    if 'young neutron star' in c or 'young ns' in c: return 'general_young_NS'
    return 'unresolved'

def role(kind,stmt):
    s=stmt.lower()
    if kind=='interval' and ('further excluded' in s or 'further exclude' in s or re.search(r"excluded.{0,100}\bif\b",s)): return 'conditional_additional_exclusion'
    if 'little alteration' in s or 'little modification' in s or ('standard cooling' in s and ('fit' in s or 'compatible' in s)): return 'standard_cooling_compatibility'
    if kind=='approx_value' and ('hint' in s or 'possibility' in s or 'evidence' in s or 'imply' in s): return 'possible_hint'
    if 'hint' in s or 'possibility' in s: return 'possible_hint'
    if any(k in s for k in ['constraint','bound','excluded','exclusion']): return 'constraint_bound'
    return 'unresolved'

def eta_scope(stmt):
    t=stmt.replace(' ','')
    pats=[
      r"\\?eta(?:=|<|>|\\lesssim|\\gtrsim)10\^\{?[+-]?\d+\}?",
      r"10\^\{?[+-]?\d+\}?<\\?eta<10\^\{?[+-]?\d+\}?",
    ]
    out=[]
    for p in pats:
        for m in re.finditer(p,t,re.I):
            if m.group(0) not in out: out.append(m.group(0))
    return out

def mass_scope(stmt):
    pats=[
      r"m_\{?\\gamma\^?\\prime\}?\s*(?:<|\\lesssim)\s*T_c\s*\([^)]*\)\s*=\s*\\mathcal\{O\}\s*\(\s*0\.1\s*\)\s*MeV",
      r"mass\s+is\s+lower\s+than\s*\$?\\mathcal\{O\}\s*\(\s*0\.1\s*\)\s*MeV",
      r"m_\{?\\gamma\^?\\prime\}?\s*(?:<|\\lesssim)\s*0\.1\s*-\s*1\s*MeV",
      r"mass\s+around\s*\$?eV",
    ]
    out=[]
    for p in pats:
        for m in re.finditer(p,stmt,re.I):
            if m.group(0) not in out: out.append(m.group(0))
    return out

def eq_label(stmt,expr):
    pos=stmt.find(expr)
    if pos<0:return None
    m=re.search(r"\\label\{(eq:[^{}]+)\}",stmt[pos:pos+220],re.I)
    return m.group(1) if m else None

def record(file,text,r):
    st=statement(text,r['start'],r['end']); ctx=context(text,r['start'],r['end'])
    obs=observation(st,ctx); ro=role(r['kind'],st)
    return {'file':file,'kind':r['kind'],'expression':r['expression'],'low':r['low'],'high':r['high'],
            'observation':obs,'role':ro,'eta_scope':eta_scope(st),'mass_scope':mass_scope(st),
            'equation_label':eq_label(st,r['expression']),'branch_resolved':obs!='unresolved' and ro!='unresolved',
            'statement':st,'excerpt':ctx}

def tuple_key(r): return (r['observation'],r['role'],tuple(r['eta_scope']),tuple(r['mass_scope']),r['equation_label'])

def audit(fetcher=fetch):
    raw=fetcher(URL)
    if sha256(raw)!=ARCHIVE_SHA256: raise RuntimeError('archive SHA mismatch')
    rec=[]
    for f,t in tex_files(raw):
        for rr in relations(t):
            ctx=context(t,rr['start'],rr['end'])
            if not re.search(r"B.?L|U\(1\)|Cas\s*A|Cassiopeia|NS1987A|SN1987A|cooling|bound|constraint|excluded|hint",ctx,re.I): continue
            x=record(f,t,rr)
            # Numeric benchmarks with no result role are not branch statements under the prereg extraction universe.
            if x['role']!='unresolved': rec.append(x)
    unresolved=[r for r in rec if not r['branch_resolved']]
    constraints=[r for r in rec if r['branch_resolved'] and r['role']=='constraint_bound']
    groups={}; contradictions=[]
    for r in constraints:
        if r['kind']=='upper_bound': groups.setdefault(tuple_key(r),[]).append(r['high'])
    for k,vs in groups.items():
        u=[]
        for v in vs:
            if not any(abs(v-q)<=max(1e-300,abs(v)*1e-12) for q in u):u.append(v)
        if len(u)>1: contradictions.append({'branch_tuple':list(k),'values':sorted(u)})
    if contradictions: cls='SCIENTIFIC_FAIL_HONG_B_L_BRANCH_SCOPE_IDENTITY'
    elif rec and not unresolved and constraints: cls='PASS_HONG_B_L_BRANCH_SCOPE_IDENTITY'
    else: cls='BLOCKED_HONG_B_L_BRANCH_SCOPE_IDENTITY'
    summaries=[]
    for r in rec:
        s={k:r[k] for k in ['kind','low','high','observation','role','eta_scope','mass_scope','equation_label','branch_resolved']}
        if s not in summaries:summaries.append(s)
    return {'iteration':'0083a-r1','parent_gate':'0083a','classification':cls,'archive_sha256':sha256(raw),
            'record_count':len(rec),'unresolved_count':len(unresolved),'constraint_branch_count':len(constraints),
            'contradictions':contradictions,'branch_summaries':summaries,'records':rec,'unresolved_records':unresolved,
            'guard':'Conformance rerun of frozen 0083a only; exact Hong TeX source statements, no figure geometry, no O(0.1 MeV)->exact endpoint, no cross-paper conversion/union, no BSM response scan.'}

def main():
    r=audit(); fn='hong_bl_branch_scope_0083a_r1.json'
    with open(fn,'w') as f: json.dump(r,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({k:r[k] for k in ['iteration','classification','archive_sha256','record_count','unresolved_count','constraint_branch_count','contradictions','branch_summaries']},indent=2,sort_keys=True))
    if r['classification']!='PASS_HONG_B_L_BRANCH_SCOPE_IDENTITY': raise SystemExit(2)
if __name__=='__main__': main()
