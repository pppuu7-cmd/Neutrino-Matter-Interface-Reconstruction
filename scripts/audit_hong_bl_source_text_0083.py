#!/usr/bin/env python3
import hashlib, io, json, re, tarfile, time, urllib.request

URL="https://export.arxiv.org/e-print/2012.05427v3"
ARCHIVE_SHA256="6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc"

def sha256(b): return hashlib.sha256(b).hexdigest()

def fetch(url):
    last=None
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"NMIR-0083/1.1"})
            with urllib.request.urlopen(req,timeout=90) as r:return r.read()
        except Exception as e:
            last=e; time.sleep(2**i)
    raise RuntimeError(f"fetch failed: {last}")

def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)

def compact(s):
    s=strip_comments(s)
    s=s.replace("\n"," ")
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

def extract_eprime_upper_bounds(s):
    """Return explicit source-native e' upper bounds of form factor*10^exp."""
    t=s.replace(" ","")
    eprime=r"e(?:\^\{?\\prime\}?|_?\\prime|')"
    op=r"(?:<|\\lesssim|\\leq|\\le)"
    num=r"(?:(?P<factor>\d+(?:\.\d+)?)\\times)?10\^\{?(?P<exp>[+-]?\d+)\}?"
    out=[]
    for m in re.finditer(eprime+op+num,t,re.I):
        factor=float(m.group("factor") or 1.0); exp=int(m.group("exp"))
        out.append({"expression":m.group(0),"factor":factor,"exponent":exp,"value":factor*(10.0**exp)})
    # deterministic de-duplication by numeric value + expression
    uniq=[]
    for x in out:
        if any(abs(x["value"]-u["value"])<=max(1e-300,abs(x["value"])*1e-15) and x["expression"]==u["expression"] for u in uniq):
            continue
        uniq.append(x)
    return uniq

def has_low_mass_domain(s):
    t=s.lower().replace(" ","")
    return bool("0.1" in t and "mev" in t and
                ("mathcal{o}" in t or "order" in t or re.search(r"m[_^{\\a-z0-9'}]*[<≤]",t)))

def has_cooling_result_context(s):
    t=s.lower()
    return any(k in t for k in ["cooling","bound","constraint","excluded","obtain the bound","we find"])

def exact_mass_inequality(s):
    t=s.lower().replace(" ","")
    inequality=bool(re.search(r"m(?:_\{?[^\s=<>]{0,40}\}?|\^\{?[^\s=<>]{0,20}\}?)?[<>]=?0?\.1(?:\\,)?mev",t))
    if not inequality:
        inequality=bool(re.search(r"0?\.1(?:\\,)?mev[<>]=?m",t))
    approximate=any(x in t for x in ["mathcal{o}","approximately","approx","about","orderof","order(0.1",r"\sim0.1"])
    return bool(inequality and not approximate)

def audit(fetcher=fetch):
    raw=fetcher(URL)
    if sha256(raw)!=ARCHIVE_SHA256: raise RuntimeError("archive SHA mismatch")
    files=tex_files_from_archive(raw)
    records=[]
    all_anchor=False; all_exact=False
    anchor_values=[]
    for name,txt0 in files:
        txt=compact(txt0)
        seed_contexts=[]
        for pat in [r"10\^\{?[+-]?\d+\}?",r"0\.1.{0,80}MeV",r"B.{0,12}L"]:
            seed_contexts.extend(contexts(txt,pat))
        seen=set()
        for c in seed_contexts:
            key=hashlib.sha256(c.encode()).hexdigest()
            if key in seen: continue
            seen.add(key)
            bounds=extract_eprime_upper_bounds(c)
            flags={
              "bl":bool(has_bl(c)),
              "eprime_numeric_upper_bound":bool(bounds),
              "low_mass_domain":bool(has_low_mass_domain(c)),
              "cooling_or_constraint_context":bool(has_cooling_result_context(c)),
              "exact_finite_mass_inequality":bool(exact_mass_inequality(c)),
            }
            anchor=all([flags["bl"],flags["eprime_numeric_upper_bound"],flags["low_mass_domain"],flags["cooling_or_constraint_context"]])
            exact=anchor and flags["exact_finite_mass_inequality"]
            if anchor:
                anchor_values.extend(x["value"] for x in bounds)
            all_anchor=all_anchor or anchor; all_exact=all_exact or exact
            if any(flags.values()):
                records.append({"file":name,"flags":flags,"eprime_upper_bounds":bounds,
                                "anchor_candidate":bool(anchor),"exact_candidate":bool(exact),"excerpt":c})
    distinct_anchor_values=[]
    for v in sorted(anchor_values):
        if not any(abs(v-u)<=max(1e-300,abs(v)*1e-12) for u in distinct_anchor_values): distinct_anchor_values.append(v)
    if all_anchor and all_exact:
        cls="PASS_HONG_B_L_SOURCE_TEXT_ANALYTICAL_ANCHOR / PASS_HONG_B_L_EXACT_FINITE_MASS_TEXT_AUTHORITY"
    elif all_anchor:
        cls="PASS_HONG_B_L_SOURCE_TEXT_ANALYTICAL_ANCHOR / BLOCKED_HONG_B_L_EXACT_FINITE_MASS_TEXT_AUTHORITY"
    else:
        cls="BLOCKED_HONG_B_L_SOURCE_TEXT_ANALYTICAL_AUTHORITY"
    return {"iteration":"0083","classification":cls,"archive_sha256":sha256(raw),
            "tex_file_count":len(files),"distinct_anchor_upper_bound_values":distinct_anchor_values,
            "records":records,
            "guard":"Exact frozen Hong 2012.05427v3 TeX text only; no figure pixels/path geometry/manual reading, no cross-paper conversion, no post-result replacement of O(0.1 MeV) by an exact endpoint. Public arXiv metadata wording is not substituted for source-archive TeX."}

def main():
    r=audit(); fn="hong_bl_source_text_0083.json"
    with open(fn,"w") as f: json.dump(r,f,indent=2,sort_keys=True); f.write("\n")
    print(json.dumps({"iteration":r["iteration"],"classification":r["classification"],
                      "archive_sha256":r["archive_sha256"],"tex_file_count":r["tex_file_count"],
                      "distinct_anchor_upper_bound_values":r["distinct_anchor_upper_bound_values"]},indent=2,sort_keys=True))
    if r["classification"]=="BLOCKED_HONG_B_L_SOURCE_TEXT_ANALYTICAL_AUTHORITY": raise SystemExit(2)

if __name__=="__main__": main()
