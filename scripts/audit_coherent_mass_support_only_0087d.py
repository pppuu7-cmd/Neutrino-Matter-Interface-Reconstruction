#!/usr/bin/env python3
"""NMIR 0087d — COHERENT B-L mass-support-only authority."""
from __future__ import annotations

import hashlib, io, json, math, pathlib, re, tarfile, time, urllib.request
import pymupdf

URL="https://export.arxiv.org/e-print/2008.05022v3"
TARGET=[6.845530367110015e-6,1.4057345497828417]
RESID_TOL=0.015
FRAME_TOL=1.5
CROSS_TOL=0.03
SUP=str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺−", "0123456789-+-")


def sha256(b): return hashlib.sha256(b).hexdigest()

def fetch(url):
    last=None
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"NMIR-0087d/1.0"})
            with urllib.request.urlopen(req,timeout=90) as r: return r.read()
        except Exception as e:
            last=e; time.sleep(2**i)
    raise RuntimeError(f"fetch failed: {last}")

def strip_comments(s): return re.sub(r"(?<!\\)%.*", "", s)
def norm(s): return s.translate(SUP).replace("–","-").replace("—","-").replace("′","'").replace("’","'").strip()

def decode(b):
    try:return b.decode("utf-8")
    except UnicodeDecodeError:return b.decode("latin-1")

def archive_members(raw):
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
        return {m.name.lstrip("./"):tf.extractfile(m).read() for m in tf.getmembers() if m.isfile()}

def tex_texts(members):
    return [(n,strip_comments(decode(b))) for n,b in members.items() if n.lower().endswith(".tex")]

def bl_context(s):
    q=re.sub(r"\s+"," ",s)
    return bool(re.search(r"B\s*(?:-|\\!|\\,|\\text\s*\{?[- ]?\}?)*\s*L|B-L|B\\!-\\!L",q,re.I))

def mass_context(s):
    q=s.lower()
    return bool(re.search(r"m\s*_?\s*\{?\s*z|m_?\{?z|z.?prime.*mass|mediator\s+mass|boson\s+mass",q,re.I))

def unit_factor(u): return {"ev":1.0,"kev":1e3,"mev":1e6,"gev":1e9}[u.lower()]

def number_value(s):
    s=s.strip().replace("{","").replace("}","")
    m=re.fullmatch(r"10\s*\^\s*([+-]?\d+)",s)
    if m:return 10.0**int(m.group(1))
    m=re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)(?:\s*[eE]\s*([+-]?\d+))?",s)
    if m:return float(m.group(1))*(10.0**int(m.group(2) or 0))
    return None

def explicit_text_route(texs):
    hits=[]
    # TeX-friendly number + unit expressions.
    num=r"(?:10\s*\^\s*\{?\s*[+-]?\d+\s*\}?|[0-9]+(?:\.[0-9]+)?(?:\s*[eE]\s*[+-]?\d+)?)"
    unit=r"(?:\\?mathrm\s*\{\s*)?(eV|keV|MeV|GeV)\s*\}?"
    range_re=re.compile(rf"({num})\s*{unit}\s*(?:--?|\\text\s*\{{\s*to\s*\}}|\bto\b|\\leq?|<|\\lesssim)\s*({num})\s*{unit}",re.I)
    between_re=re.compile(rf"between\s+({num})\s*{unit}\s+and\s+({num})\s*{unit}",re.I)
    for name,text in texs:
        flat=re.sub(r"\s+"," ",text)
        for m in re.finditer(r"B\s*[-\\! ,]*\s*L|B-L|B\\!-\\!L",flat,re.I):
            ctx=flat[max(0,m.start()-500):min(len(flat),m.end()+700)]
            if not mass_context(ctx): continue
            for rr in (range_re,between_re):
                for z in rr.finditer(ctx):
                    # groups: number1,unit1,number2,unit2
                    v1=number_value(z.group(1));u1=z.group(2);v2=number_value(z.group(3));u2=z.group(4)
                    if v1 is None or v2 is None: continue
                    a=v1*unit_factor(u1);b=v2*unit_factor(u2)
                    if a>b:a,b=b,a
                    if a>0 and b>a:
                        hits.append({"file":name,"interval_eV":[a,b],"match":z.group(0),"context":ctx})
    uniq=[]
    for h in hits:
        if not any(all(abs(math.log10(x/y))<1e-9 for x,y in zip(h["interval_eV"],u["interval_eV"])) for u in uniq): uniq.append(h)
    if len(uniq)==1:
        return {"passed":True,"interval_eV":uniq[0]["interval_eV"],"authority_hit":uniq[0],"unique_interval_count":1}
    return {"passed":False,"reason":"no_unique_explicit_BL_mass_interval","unique_interval_count":len(uniq),"candidate_hits":[{"file":h["file"],"interval_eV":h["interval_eV"],"match":h["match"]} for h in uniq[:20]]}

def figure_candidates(texs,members):
    out=[]
    for name,text in texs:
        for fm in re.finditer(r"\\begin\s*\{figure\*?\}(.*?)\\end\s*\{figure\*?\}",text,re.S|re.I):
            body=fm.group(1)
            cm=re.search(r"\\caption\s*\{(.*?)\}\s*(?:\\label|$)",body,re.S|re.I)
            caption=re.sub(r"\s+"," ",cm.group(1) if cm else body)
            if not (bl_context(caption) and mass_context(caption)): continue
            graphics=re.findall(r"\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}",body,re.I)
            for g in graphics:
                g=g.strip();base=pathlib.PurePosixPath(name).parent
                tries=[str(base/g),g]
                if not pathlib.PurePosixPath(g).suffix:
                    for ext in (".pdf",".eps",".ps",".svg",".png",".jpg",".jpeg"):
                        tries.extend([str(base/(g+ext)),g+ext])
                resolved=next((t.lstrip("./") for t in tries if t.lstrip("./") in members),None)
                out.append({"tex_file":name,"caption":caption,"includegraphics":g,"resolved":resolved})
    return out

def spans(page):
    out=[]
    raw=page.get_text("dict")
    for bi,b in enumerate(raw.get("blocks",[])):
      for li,ln in enumerate(b.get("lines",[])):
       for si,sp in enumerate(ln.get("spans",[])):
        txt=sp.get("text","").strip()
        if txt:
         x0,y0,x1,y1=sp["bbox"]
         out.append({"id":f"{bi}:{li}:{si}","text":txt,"size":float(sp.get("size",0)),"x0":x0,"y0":y0,"x1":x1,"y1":y1,"xc":(x0+x1)/2,"yc":(y0+y1)/2})
    return out

def direct_power(text):
    raw=text.strip();n=norm(raw).replace(" ","")
    if "^" in raw:
        m=re.fullmatch(r"10\^\{?([+-]?\d+)\}?",n)
        return int(m.group(1)) if m else None
    if any(c in raw for c in "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺"):
        m=re.fullmatch(r"10([+-]?\d+)",n)
        return int(m.group(1)) if m else None
    return None

def reconstruct_ticks(ss,W,H):
    ticks=[]
    for s in ss:
        if s["yc"]<0.68*H or not (0.04*W<=s["xc"]<=0.96*W):continue
        e=direct_power(s["text"])
        if e is not None:ticks.append({"exponent":e,"xc":s["xc"],"yc":s["yc"],"source":[s["text"]],"ids":[s["id"]]})
    for b in ss:
        if norm(b["text"]).replace(" ","")!="10":continue
        if b["yc"]<0.68*H or not (0.04*W<=b["xc"]<=0.96*W):continue
        cand=[]
        for s in ss:
            if s["id"]==b["id"] or s["size"]>=b["size"]-1e-6:continue
            tok=norm(s["text"]).replace(" ","")
            if not re.fullmatch(r"[+-]?\d+|[+-]",tok):continue
            if s["x0"]<b["x1"]-1.0 or s["x0"]>b["x1"]+18.0:continue
            if abs(s["yc"]-b["yc"])>8.0 or s["yc"]>b["yc"]+2.0:continue
            cand.append((s,tok))
        cand.sort(key=lambda q:q[0]["x0"])
        pieces=[];last=b["x1"]
        for s,tok in cand:
            if s["x0"]-last>5.0:break
            pieces.append((s,tok));last=s["x1"]
            joined="".join(q for _,q in pieces)
            if re.fullmatch(r"[+-]?\d+",joined) and joined not in {"+","-"}:
                xs=[b["x0"],b["x1"]]+sum(([p[0]["x0"],p[0]["x1"]] for p in pieces),[])
                ys=[b["y0"],b["y1"]]+sum(([p[0]["y0"],p[0]["y1"]] for p in pieces),[])
                ticks.append({"exponent":int(joined),"xc":(min(xs)+max(xs))/2,"yc":(min(ys)+max(ys))/2,"source":[b["text"]]+[p[0]["text"] for p in pieces],"ids":[b["id"]]+[p[0]["id"] for p in pieces]});break
    uniq=[]
    for t in sorted(ticks,key=lambda x:x["xc"]):
        if any(abs(t["xc"]-u["xc"])<0.8 and t["exponent"]==u["exponent"] for u in uniq):continue
        uniq.append(t)
    return uniq

def x_axis_unit(ss,H):
    hits=[]
    for s in ss:
        if s["yc"]<0.62*H:continue
        t=norm(s["text"])
        for u in ("GeV","MeV","keV","eV"):
            if re.search(rf"(?<![A-Za-z]){u}(?![A-Za-z])",t,re.I):hits.append({"unit":u,"text":s["text"],"xc":s["xc"],"yc":s["yc"]})
    us=sorted(set(h["unit"].lower() for h in hits))
    return ({"gev":"GeV","mev":"MeV","kev":"keV","ev":"eV"}[us[0]] if len(us)==1 else None),hits

def mass_axis_identity(ss):
    text=" ".join(s["text"] for s in ss);q=norm(text).lower().replace(" ","")
    return bool(re.search(r"m_?\{?z|m[z]|z.?prime.*mass|mediator.*mass",q,re.I))

def fit(xs,ys):
    xm=sum(xs)/len(xs);ym=sum(ys)/len(ys);den=sum((x-xm)**2 for x in xs)
    if den<=0:raise ValueError("degenerate tick x")
    a=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/den;return a,ym-a*xm

def frames(page,left,right):
    W,H=page.rect.width,page.rect.height;out=[]
    for di,d in enumerate(page.get_drawings()):
      for item in d.get("items",[]):
       if not item:continue
       if item[0]=="re":
        r=item[1]
        if r.width>=.35*W and r.height>=.25*H:
         dl,dr=abs(r.x0-left),abs(r.x1-right);out.append({"drawing":di,"kind":"rect","x0":float(r.x0),"x1":float(r.x1),"y0":float(r.y0),"y1":float(r.y1),"left_delta":dl,"right_delta":dr,"matched":dl<=FRAME_TOL and dr<=FRAME_TOL})
       elif item[0]=="l":
        p0,p1=item[1],item[2]
        if abs(p0.y-p1.y)<=.75 and abs(p1.x-p0.x)>=.35*W:
         x0,x1=min(p0.x,p1.x),max(p0.x,p1.x);dl,dr=abs(x0-left),abs(x1-right);out.append({"drawing":di,"kind":"hline","x0":float(x0),"x1":float(x1),"y":float((p0.y+p1.y)/2),"left_delta":dl,"right_delta":dr,"matched":dl<=FRAME_TOL and dr<=FRAME_TOL})
    return out

def pdf_route(blob):
    doc=pymupdf.open(stream=blob,filetype="pdf")
    if len(doc)!=1:return {"passed":False,"reason":"figure_not_one_page"}
    p=doc[0];W,H=p.rect.width,p.rect.height;ss=spans(p);ticks=reconstruct_ticks(ss,W,H);u,uh=x_axis_unit(ss,H)
    r={"page_size":[W,H],"text_span_count":len(ss),"image_xobject_count":len(p.get_images(full=True)),"mass_axis_identity":mass_axis_identity(ss),"x_axis_unit":u,"unit_hits":uh,"ticks":ticks,"tick_count":len(ticks)}
    if p.get_images(full=True):r.update({"passed":False,"reason":"figure_contains_raster_image_xobjects"});return r
    if len(ticks)<3:r.update({"passed":False,"reason":"fewer_than_3_source_native_x_ticks"});return r
    exps=[float(t["exponent"]) for t in ticks];xs=[t["xc"] for t in ticks]
    if any(exps[i+1]<=exps[i] for i in range(len(exps)-1)) or len(set(exps))!=len(exps):r.update({"passed":False,"reason":"ticks_not_strictly_monotone_unique"});return r
    a,b=fit(xs,exps);res=[y-(a*x+b) for x,y in zip(xs,exps)];mx=max(abs(z) for z in res);fr=frames(p,min(xs),max(xs));matched=[z for z in fr if z["matched"]]
    r.update({"span_decades":max(exps)-min(exps),"fit":{"a":a,"b":b},"residuals":res,"max_abs_residual":mx,"frame_candidates":fr,"matched_frame_count":len(matched)})
    if not r["mass_axis_identity"] or u is None:r.update({"passed":False,"reason":"mass_axis_identity_or_unique_unit_missing"});return r
    if max(exps)-min(exps)<2 or a<=0 or mx>RESID_TOL:r.update({"passed":False,"reason":"x_fit_or_span_failed"});return r
    if len(matched)!=1:r.update({"passed":False,"reason":"no_unique_frame_anchored_outer_ticks"});return r
    fac=unit_factor(u);iv=[10**min(exps)*fac,10**max(exps)*fac];r.update({"passed":True,"interval_eV":iv});return r

def route_b(cands,members):
    results=[]
    for c in cands:
        rec=dict(c)
        if not c["resolved"]:rec.update({"passed":False,"reason":"asset_unresolved"})
        else:
            b=members[c["resolved"]];rec["asset_sha256"]=sha256(b);ext=pathlib.PurePosixPath(c["resolved"]).suffix.lower();rec["asset_type"]=ext
            if ext==".pdf":rec["diagnostic"]=pdf_route(b);rec["passed"]=rec["diagnostic"].get("passed",False);rec["interval_eV"]=rec["diagnostic"].get("interval_eV")
            else:rec.update({"passed":False,"reason":"non_PDF_source_native_asset_not_supported_without_visual_or_conversion_in_this_gate"})
        results.append(rec)
    passed=[r for r in results if r.get("passed")]
    uniq=[]
    for r in passed:
        iv=r["interval_eV"]
        if not any(all(abs(math.log10(x/y))<1e-9 for x,y in zip(iv,u["interval_eV"])) for u in uniq):uniq.append(r)
    if len(uniq)==1:return {"passed":True,"interval_eV":uniq[0]["interval_eV"],"accepted_asset":uniq[0],"candidate_results":results}
    return {"passed":False,"reason":"no_unique_source_native_BL_figure_mass_interval","unique_passing_interval_count":len(uniq),"candidate_results":results}

def threat(iv):
    a,b=iv;t0,t1=TARGET
    if b<t0:return {"classification":"PROVABLY_MASS_DISJOINT","side":"below_target","separation_decades":math.log10(t0/b)}
    if a>t1:return {"classification":"PROVABLY_MASS_DISJOINT","side":"above_target","separation_decades":math.log10(a/t1)}
    lo,hi=max(a,t0),min(b,t1);w=max(0.0,math.log10(hi/lo));tw=math.log10(t1/t0)
    return {"classification":"MASS_OVERLAP_THREAT","overlap_interval_eV":[lo,hi],"overlap_width_decades":w,"overlap_fraction_target_log_width":w/tw}

def audit(fetcher=fetch):
    raw=fetcher(URL);members=archive_members(raw);texs=tex_texts(members)
    joined="\n".join(t for _,t in texs)
    source_ok=("COHERENT" in joined and bl_context(joined) and ("CsI" in joined or "argon" in joined.lower()))
    if not source_ok:raise RuntimeError("arXiv source semantic identity mismatch")
    A=explicit_text_route(texs);cands=figure_candidates(texs,members);B=route_b(cands,members)
    ivs=[]
    if A.get("passed"):ivs.append(("A",A["interval_eV"]))
    if B.get("passed"):ivs.append(("B",B["interval_eV"]))
    contradiction=False
    if len(ivs)>1:
        ref=ivs[0][1]
        contradiction=any(any(abs(math.log10(x/y))>CROSS_TOL for x,y in zip(ref,iv)) for _,iv in ivs[1:])
    if contradiction:cls="SCIENTIFIC_FAIL_COHERENT_MASS_SUPPORT_SOURCE_INCONSISTENCY";iv=None
    elif ivs:cls="PASS_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY";iv=ivs[0][1]
    else:cls="BLOCKED_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY";iv=None
    return {"iteration":"0087d","classification":cls,"source_url":URL,"archive_sha256":sha256(raw),"source_semantic_identity_ok":source_ok,"tex_files":[n for n,_ in texs],"candidate_BL_mass_figures":cands,"route_A":A,"route_B":B,"certified_mass_support_eV":iv,"0087b_target_eV":TARGET,"threat_result":None if iv is None else threat(iv),"guard":"Mass support only; no B-L likelihood, no 0074c reopening, no y calibration, no curve/color/path identity, no raster/OCR/manual reading, no global allowed region, no BSM response scan."}
def main():
    fn=pathlib.Path("coherent_mass_support_only_0087d.json")
    try:r=audit()
    except (OSError,RuntimeError,pymupdf.FileDataError,tarfile.TarError) as e:r={"iteration":"0087d","classification":"INFRASTRUCTURE_FAIL_0087D","reason":repr(e)}
    fn.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n",encoding="utf-8");print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"].startswith("INFRASTRUCTURE_FAIL"):raise SystemExit(3)
    if r["classification"]!="PASS_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY":raise SystemExit(2)
if __name__=="__main__":main()
