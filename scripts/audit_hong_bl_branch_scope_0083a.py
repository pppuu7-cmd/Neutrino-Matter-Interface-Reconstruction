#!/usr/bin/env python3
import hashlib, io, json, re, tarfile, time, urllib.request

URL="https://export.arxiv.org/e-print/2012.05427v3"
ARCHIVE_SHA256="6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc"

EP = r"e(?:\^\{?\\prime\}?|_?\\prime|')"
NUM = r"(?:(?P<factor>\d+(?:\.\d+)?)\s*(?:\\times|×)\s*)?10\^\{?(?P<exp>[+-]?\d+)\}?"

def sha256(b): return hashlib.sha256(b).hexdigest()

def fetch(url):
    last=None
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"NMIR-0083a/1.0"})
            with urllib.request.urlopen(req,timeout=90) as r:return r.read()
        except Exception as e:
            last=e; time.sleep(2**i)
    raise RuntimeError(f"fetch failed: {last}")

def strip_comments(s): return re.sub(r"(?<!\\)%.*", "", s)

def compact(s):
    s=strip_comments(s).replace("\n"," ")
    s=re.sub(r"\\(?:mathrm|text|rm|mbox)\s*\{([^{}]*)\}",r"\1",s)
    s=re.sub(r"\{\\(?:mathrm|text|rm|mbox)\s+([^{}]+)\}",r"\1",s)
    s=s.replace("\\,"," ").replace("\\!","").replace("~"," ")
    s=re.sub(r"\s+"," ",s)
    return s

def tex_files(raw):
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
        out=[]
        for m in tf.getmembers():
            n=m.name.lstrip("./")
            if m.isfile() and n.lower().endswith(".tex"):
                b=tf.extractfile(m).read()
                try: t=b.decode("utf-8")
                except UnicodeDecodeError: t=b.decode("latin-1")
                out.append((n,compact(t)))
        return out

def value(f,e): return float(f or 1.0)*(10.0**int(e))

def extract_relations(text):
    rel=[]
    # upper bounds
    p_upper=re.compile(EP+r"\s*(?P<op><|\\lesssim|\\leq|\\le)\s*"+NUM,re.I)
    for m in p_upper.finditer(text):
        rel.append({"kind":"upper_bound","start":m.start(),"end":m.end(),"expression":m.group(0),
                    "low":None,"high":value(m.group('factor'),m.group('exp'))})
    # approximate/hint value
    p_approx=re.compile(EP+r"\s*(?:\\sim|≈|~)\s*"+NUM,re.I)
    for m in p_approx.finditer(text):
        rel.append({"kind":"approx_value","start":m.start(),"end":m.end(),"expression":m.group(0),
                    "low":None,"high":value(m.group('factor'),m.group('exp'))})
    # intervals factor*10^e < e' < factor*10^e
    left_num=r"(?:(?P<lf>\d+(?:\.\d+)?)\s*(?:\\times|×)\s*)?10\^\{?(?P<le>[+-]?\d+)\}?"
    right_num=r"(?:(?P<rf>\d+(?:\.\d+)?)\s*(?:\\times|×)\s*)?10\^\{?(?P<re>[+-]?\d+)\}?"
    p_int=re.compile(left_num+r"\s*<\s*"+EP+r"\s*<\s*"+right_num,re.I)
    for m in p_int.finditer(text):
        rel.append({"kind":"interval","start":m.start(),"end":m.end(),"expression":m.group(0),
                    "low":value(m.group('lf'),m.group('le')),"high":value(m.group('rf'),m.group('re'))})
    # prefer intervals over contained upper bound appearances and dedupe exact spans/value
    ints=[r for r in rel if r['kind']=='interval']
    rel=[r for r in rel if r['kind']=='interval' or not any(i['start']<=r['start'] and r['end']<=i['end'] for i in ints)]
    uniq=[]
    for r in sorted(rel,key=lambda x:(x['start'],x['end'],x['kind'])):
        if any(r['start']==u['start'] and r['end']==u['end'] and r['kind']==u['kind'] for u in uniq): continue
        uniq.append(r)
    return uniq

def local_context(text,start,end,radius=1300):
    a=max(0,start-radius); b=min(len(text),end+radius)
    return text[a:b]

def nearest_before(text,pos,pattern,window=220):
    a=max(0,pos-window); sub=text[a:pos]
    ms=list(re.finditer(pattern,sub,re.I|re.S))
    return ms[-1].group(0) if ms else None

def observational_identity(ctx):
    low=ctx.lower()
    flags=[]
    if re.search(r"cas\s*a|cassiopeia\s*a",low): flags.append("Cas A")
    if "ns1987a" in low: flags.append("NS1987A")
    if "sn1987a" in low and "NS1987A" not in flags: flags.append("SN1987A")
    # Explicit relation sentence-level priority: find nearby sentence containing the relation later in caller.
    return flags

def sentence_around(text,start,end):
    left=max(text.rfind('.',0,start),text.rfind('!',0,start),text.rfind('?',0,start),text.rfind(';',0,start))
    right_candidates=[x for x in [text.find('.',end),text.find('!',end),text.find('?',end),text.find(';',end)] if x!=-1]
    right=min(right_candidates) if right_candidates else min(len(text),end+700)
    return text[left+1:right+1].strip()

def role_for(sentence,ctx,kind):
    s=sentence.lower(); c=ctx.lower()
    if any(k in s for k in ["hint","could imply","might imply","possibility","may argue"]): return "possible_hint"
    if kind=="approx_value" and any(k in c for k in ["hint","possibility","could imply"]): return "possible_hint"
    if kind=="interval" and ("further excluded" in s or "further exclude" in s): return "conditional_additional_exclusion"
    if any(k in s for k in ["little alteration","little modification","well described","standard cooling scenario"]): return "standard_cooling_compatibility"
    if any(k in s for k in ["constraint", "bound", "excluded", "exclusion"]): return "constraint_bound"
    # Search a slightly broader source-local context for equation-level statements introduced as a constraint.
    if any(k in c for k in ["constraint on the parameters", "obtain the bound", "resulting bound"]): return "constraint_bound"
    return "unresolved"

def eta_scope(ctx,sentence):
    target=(sentence+" "+ctx[:1000]).replace(" ","")
    vals=[]
    for m in re.finditer(r"eta(?:=|<|>|\\lesssim|\\gtrsim)10\^\{?([+-]?\d+)\}?",target,re.I): vals.append(m.group(0))
    # include source explicit eta interval if present
    for m in re.finditer(r"10\^\{?([+-]?\d+)\}?<eta<10\^\{?([+-]?\d+)\}?",target,re.I): vals.append(m.group(0))
    out=[]
    for x in vals:
        if x not in out: out.append(x)
    return out[:6]

def mass_scope(ctx,sentence):
    candidates=[]
    probe=sentence+" "+ctx
    pats=[
      r"m_\{?\\gamma\^?\\prime\}?\s*(?:<|\\lesssim)\s*T_c\s*\([^)]*\)\s*=\s*\\mathcal\{O\}\s*\(\s*0\.1\s*\)\s*MeV",
      r"mass\s+is\s+lower\s+than\s*\$?\\mathcal\{O\}\s*\(\s*0\.1\s*\)\s*MeV",
      r"m_\{?\\gamma\^?\\prime\}?\s*(?:<|\\lesssim)\s*0\.1\s*-\s*1\s*MeV",
      r"mass\s+around\s*\$?eV",
    ]
    for p in pats:
        m=re.search(p,probe,re.I)
        if m: candidates.append(m.group(0))
    return candidates[:3]

def equation_label(ctx,relation_expression):
    # Source labels normally follow the displayed relation within short distance.
    m=re.search(re.escape(relation_expression)+r".{0,160}?\\label\{([^{}]+)\}",ctx,re.I|re.S)
    return m.group(1) if m else None

def observation_from_sentence(sentence,ctx):
    s=sentence.lower()
    if re.search(r"cas\s*a|cassiopeia\s*a",s): return "Cas A"
    if "ns1987a" in s: return "NS1987A"
    if "sn1987a" in s: return "SN1987A"
    # Broader context: require unique source identity; otherwise general young NS.
    flags=observational_identity(ctx)
    if len(flags)==1: return flags[0]
    if "young neutron" in ctx.lower() or "young ns" in ctx.lower(): return "general_young_NS"
    return "unresolved"

def branch_record(file,text,r):
    ctx=local_context(text,r['start'],r['end'])
    sent=sentence_around(text,r['start'],r['end'])
    obs=observation_from_sentence(sent,ctx)
    role=role_for(sent,ctx,r['kind'])
    eta=eta_scope(ctx,sent)
    mass=mass_scope(ctx,sent)
    label=equation_label(ctx,r['expression'])
    return {"file":file,"kind":r['kind'],"expression":r['expression'],"low":r['low'],"high":r['high'],
            "observation":obs,"role":role,"eta_scope":eta,"mass_scope":mass,"equation_label":label,
            "branch_resolved":obs!="unresolved" and role!="unresolved","sentence":sent,"excerpt":ctx}

def tuple_key(r):
    return (r['observation'],r['role'],tuple(r['eta_scope']),tuple(r['mass_scope']),r['equation_label'])

def audit(fetcher=fetch):
    raw=fetcher(URL)
    if sha256(raw)!=ARCHIVE_SHA256: raise RuntimeError("archive SHA mismatch")
    records=[]
    for file,text in tex_files(raw):
        for rel in extract_relations(text):
            ctx=local_context(text,rel['start'],rel['end'])
            # Scope gate only B-L/young-NS numerical relations, not arbitrary e' definitions/benchmarks.
            if not re.search(r"B.?L|U\(1\)|Cas\s*A|Cassiopeia|NS1987A|SN1987A|cooling|bound|constraint|excluded|hint",ctx,re.I): continue
            records.append(branch_record(file,text,rel))
    # Keep only relations with physical result-role relevance; source benchmark parameter choices alone are excluded.
    relevant=[r for r in records if r['role']!="unresolved"]
    unresolved=[r for r in records if r['role']=="unresolved"]
    constraint_branches=[r for r in relevant if r['role']=="constraint_bound"]
    # Contradiction iff same resolved tuple has two distinct strict upper-bound high values.
    contradictions=[]
    groups={}
    for r in relevant:
        if not r['branch_resolved'] or r['kind']!="upper_bound": continue
        groups.setdefault(tuple_key(r),[]).append(r['high'])
    for k,vs in groups.items():
        uv=[]
        for v in vs:
            if not any(abs(v-u)<=max(1e-300,abs(v)*1e-12) for u in uv): uv.append(v)
        if len(uv)>1: contradictions.append({"branch_tuple":list(k),"values":sorted(uv)})
    all_resolved=bool(relevant) and all(r['branch_resolved'] for r in relevant)
    if contradictions:
        cls="SCIENTIFIC_FAIL_HONG_B_L_BRANCH_SCOPE_IDENTITY"
    elif all_resolved and constraint_branches:
        cls="PASS_HONG_B_L_BRANCH_SCOPE_IDENTITY"
    else:
        cls="BLOCKED_HONG_B_L_BRANCH_SCOPE_IDENTITY"
    # summarize unique value-role-observation tuples
    summaries=[]
    for r in relevant:
        s={k:r[k] for k in ['kind','low','high','observation','role','eta_scope','mass_scope','equation_label','branch_resolved']}
        if s not in summaries: summaries.append(s)
    return {"iteration":"0083a","classification":cls,"archive_sha256":sha256(raw),
            "relevant_record_count":len(relevant),"unresolved_record_count":len(unresolved),
            "constraint_branch_count":len(constraint_branches),"contradictions":contradictions,
            "branch_summaries":summaries,"records":relevant,"unresolved_records":unresolved,
            "guard":"Exact Hong 2012.05427v3 TeX branch/scope identity only; no figure geometry, no O(0.1 MeV)->exact endpoint, no cross-paper conversion/union, no BSM response scan."}

def main():
    r=audit(); fn="hong_bl_branch_scope_0083a.json"
    with open(fn,"w") as f: json.dump(r,f,indent=2,sort_keys=True); f.write("\n")
    print(json.dumps({k:r[k] for k in ['iteration','classification','archive_sha256','relevant_record_count','unresolved_record_count','constraint_branch_count','contradictions','branch_summaries']},indent=2,sort_keys=True))
    if r['classification']!="PASS_HONG_B_L_BRANCH_SCOPE_IDENTITY": raise SystemExit(2)

if __name__=="__main__": main()
