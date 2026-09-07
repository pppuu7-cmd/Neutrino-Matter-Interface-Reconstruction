#!/usr/bin/env python3
import hashlib, io, json, re, tarfile, time, urllib.request

URL="https://export.arxiv.org/e-print/2012.05427v3"
ARCHIVE_SHA256="6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc"

def sha256(b): return hashlib.sha256(b).hexdigest()

def fetch(url):
    last=None
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"NMIR-0083/1.0"})
            with urllib.request.urlopen(req,timeout=90) as r:return r.read()
        except Exception as e:
            last=e; time.sleep(2**i)
    raise RuntimeError(f"fetch failed: {last}")

def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)

def compact(s):
    s=strip_comments(s)
    s=s.replace("\n"," ")
    # Normalize both \rm{MeV} and {\rm MeV}-style unit wrappers without changing numerical content.
    s=re.sub(r"\\(?:mathrm|text|rm|mbox)\s*\{([^{}]*)\}",r"\1",s)
    s=re.sub(r"\{\\(?:mathrm|text|rm|mbox)\s+([^{}]+)\}",r"\1",s)
    s=s.replace("\\,"," ").replace("\\!","").replace("~"," ")
    s=re.sub(r"\s+"," ",s)
    return s

def tex_files_from_archive(raw):
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
        out=[]
        for m in tf.getmembers():
            name=m.name.lstrip("./")
            if not m.isfile() or not name.lower().endswith(".tex"): continue
            b=tf.extractfile(m).read()
            try: text=b.decode("utf-8")
            except UnicodeDecodeError: text=b.decode("latin-1")
            out.append((name,text))
    return out

def contexts(text, pattern, radius=700):
    out=[]
    for m in re.finditer(pattern,text,re.I|re.S):
        a=max(0,m.start()-radius); b=min(len(text),m.end()+radius)
        out.append(text[a:b])
    return out

def has_bl(s):
    t=s.lower().replace(" ","")
    return bool(re.search(r"b\\?[-!]\\?-?l|u\(1\).*b.*l",t,re.I))

def has_eprime_bound(s):
    t=s.replace(" ","")
    patterns=[
      r"e\^\{?\\prime\}?<10\^\{?-13\}?",
      r"e_?\\prime<10\^\{?-13\}?",
      r"e'<10\^\{?-13\}?",
      r"e\^\{?\\prime\}?\\lesssim10\^\{?-13\}?",
      r"e_?\\prime\\lesssim10\^\{?-13\}?",
    ]
    return any(re.search(p,t,re.I) for p in patterns)

def has_low_mass_domain(s):
    t=s.lower().replace(" ","")
    return ("0.1" in t and "mev" in t and
            ("mathcal{o}" in t or "order" in t or re.search(r"m[_^{\\a-z0-9'}]*[<≤]",t)))

def has_cooling_result_context(s):
    t=s.lower()
    return any(k in t for k in ["cooling","bound","constraint","excluded","obtain the bound","we find"])

def exact_mass_inequality(s):
    t=s.lower().replace(" ","")
    # Explicit finite numerical boundary only; reject big-O/approximate wording in the local clause.
    inequality=bool(re.search(r"m(?:_\{?[^\s=<>]{0,40}\}?|\^\{?[^\s=<>]{0,20}\}?)?[<>]=?0?\.1(?:\\,)?mev",t))
    if not inequality:
        inequality=bool(re.search(r"0?\.1(?:\\,)?mev[<>]=?m",t))
    approximate=any(x in t for x in ["mathcal{o}","approximately","approx","about","orderof","order(0.1",r"\sim0.1"])
    return inequality and not approximate

def audit(fetcher=fetch):
    raw=fetcher(URL)
    if sha256(raw)!=ARCHIVE_SHA256: raise RuntimeError("archive SHA mismatch")
    files=tex_files_from_archive(raw)
    records=[]
    all_anchor=False; all_exact=False
    for name,txt0 in files:
        txt=compact(txt0)
        seed_contexts=[]
        for pat in [r"10\^\{?-13\}?",r"0\.1.{0,80}MeV",r"B.{0,12}L"]:
            seed_contexts.extend(contexts(txt,pat))
        seen=set()
        for c in seed_contexts:
            key=hashlib.sha256(c.encode()).hexdigest()
            if key in seen: continue
            seen.add(key)
            flags={
              "bl":has_bl(c),
              "eprime_bound_1e_minus13":has_eprime_bound(c),
              "low_mass_domain":has_low_mass_domain(c),
              "cooling_or_constraint_context":has_cooling_result_context(c),
              "exact_finite_mass_inequality":exact_mass_inequality(c),
            }
            anchor=all([flags["bl"],flags["eprime_bound_1e_minus13"],flags["low_mass_domain"],flags["cooling_or_constraint_context"]])
            exact=anchor and flags["exact_finite_mass_inequality"]
            all_anchor=all_anchor or anchor; all_exact=all_exact or exact
            if any(flags.values()):
                records.append({"file":name,"flags":flags,"anchor_candidate":anchor,"exact_candidate":exact,"excerpt":c})
    if all_anchor and all_exact:
        cls="PASS_HONG_B_L_SOURCE_TEXT_ANALYTICAL_ANCHOR / PASS_HONG_B_L_EXACT_FINITE_MASS_TEXT_AUTHORITY"
    elif all_anchor:
        cls="PASS_HONG_B_L_SOURCE_TEXT_ANALYTICAL_ANCHOR / BLOCKED_HONG_B_L_EXACT_FINITE_MASS_TEXT_AUTHORITY"
    else:
        cls="BLOCKED_HONG_B_L_SOURCE_TEXT_ANALYTICAL_AUTHORITY"
    return {"iteration":"0083","classification":cls,"archive_sha256":sha256(raw),
            "tex_file_count":len(files),"records":records,
            "guard":"Exact frozen Hong 2012.05427v3 TeX text only; no figure pixels/path geometry/manual reading, no cross-paper conversion, no post-result replacement of O(0.1 MeV) by an exact endpoint."}

def main():
    r=audit(); fn="hong_bl_source_text_0083.json"
    with open(fn,"w") as f: json.dump(r,f,indent=2,sort_keys=True); f.write("\n")
    print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"]=="BLOCKED_HONG_B_L_SOURCE_TEXT_ANALYTICAL_AUTHORITY": raise SystemExit(2)

if __name__=="__main__": main()
