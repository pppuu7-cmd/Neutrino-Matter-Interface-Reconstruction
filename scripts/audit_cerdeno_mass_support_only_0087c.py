#!/usr/bin/env python3
"""NMIR 0087c — Cerdeño mass-support-only authority."""
from __future__ import annotations

import hashlib
import io
import json
import math
import pathlib
import re
import tarfile
import time
import urllib.request

import pymupdf

URL="https://export.arxiv.org/e-print/2106.11660v3"
ARCHIVE_SHA256="f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d"
ASSET="Figures/BL_constraints.pdf"
ASSET_SHA256="6557571159bd7d279e9b78e026c79c2974fd487db86dcf3f60b566e54318d07f"
TARGET=[6.845530367110015e-6,1.4057345497828417]
RESID_TOL=0.015
FRAME_TOL=1.5
SUP=str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺−", "0123456789-+-")


def sha256(b): return hashlib.sha256(b).hexdigest()


def fetch(url):
    last=None
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"NMIR-0087c/1.0"})
            with urllib.request.urlopen(req,timeout=90) as r: return r.read()
        except Exception as e:
            last=e; time.sleep(2**i)
    raise RuntimeError(f"fetch failed: {last}")


def strip_comments(s): return re.sub(r"(?<!\\)%.*", "", s)

def norm(s):
    return s.translate(SUP).replace("–","-").replace("—","-").replace("′","'").replace("’","'").strip()


def tex_members(raw):
    out=[]
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
        for m in tf.getmembers():
            if m.isfile() and m.name.lower().endswith(".tex"):
                b=tf.extractfile(m).read()
                try: t=b.decode("utf-8")
                except UnicodeDecodeError: t=b.decode("latin-1")
                out.append((m.name,strip_comments(t)))
    return out


def explicit_text_route(texs):
    """Conservative same-context two-endpoint detector; no inferred intervals."""
    hits=[]
    # Normalize TeX spacing but retain mathematical signs/units.
    for name,text in texs:
        flat=re.sub(r"\s+"," ",text)
        # Only short contexts that mention B-L and either constraints or mediator/vector.
        for m in re.finditer(r"B\s*[-\\]?\s*L",flat,re.I):
            lo=max(0,m.start()-280); hi=min(len(flat),m.end()+420)
            ctx=flat[lo:hi]
            if not re.search(r"constraint|bound|mediator|vector|Z.?prime|Z.?['\\]",ctx,re.I):
                continue
            # Explicit interval syntax requires two numerical endpoints and a physical unit.
            # Examples matched: 10^{-3} ... 10^{2} MeV; 0.1--100 MeV.
            pows=re.findall(r"10\s*\^?\s*\{?\s*([+-]?\d+)\s*\}?",ctx)
            decimals=re.findall(r"(?<![\w^])([0-9]+(?:\.[0-9]+)?)\s*(eV|keV|MeV|GeV)",ctx,re.I)
            units=re.findall(r"(?:\\mathrm\s*\{\s*)?(eV|keV|MeV|GeV)\s*\}?",ctx,re.I)
            if len(pows)>=2 and units:
                # Do not promote because one trailing unit can belong to another quantity unless explicit range punctuation is present.
                if re.search(r"10\s*\^?.{0,25}(?:-|--|\\text\{to\}|\\le|<).{0,25}10\s*\^?",ctx,re.I):
                    hits.append({"file":name,"context":ctx,"kind":"powers_with_explicit_range_syntax"})
            if len(decimals)>=2 and re.search(r"(?:-|--|to|\\le|<)",ctx,re.I):
                hits.append({"file":name,"context":ctx,"kind":"unit_attached_decimals_with_range_syntax"})
    # Route A is intentionally authority-conservative: report candidates, but only auto-PASS if a simple
    # same-unit decimal interval is syntactically extractable without interpretation.
    simple=[]
    for h in hits:
        ctx=h["context"]
        pat=re.compile(r"([0-9]+(?:\.[0-9]+)?)\s*(eV|keV|MeV|GeV)\s*(?:--?|to)\s*([0-9]+(?:\.[0-9]+)?)\s*\2",re.I)
        mm=pat.search(ctx)
        if mm:
            simple.append((float(mm.group(1)),float(mm.group(3)),mm.group(2),h))
    if len(simple)==1:
        a,b,u,h=simple[0]
        if a>b: a,b=b,a
        factor={"ev":1.0,"kev":1e3,"mev":1e6,"gev":1e9}[u.lower()]
        return {"passed":True,"interval_eV":[a*factor,b*factor],"authority_hit":h,"candidate_hit_count":len(hits)}
    return {"passed":False,"candidate_hit_count":len(hits),"reason":"no_unique_simple_explicit_same_unit_interval","candidate_hits":[{"file":h["file"],"kind":h["kind"]} for h in hits[:20]]}


def spans(page):
    out=[]
    raw=page.get_text("dict")
    for bi,b in enumerate(raw.get("blocks",[])):
        for li,ln in enumerate(b.get("lines",[])):
            for si,sp in enumerate(ln.get("spans",[])):
                txt=sp.get("text","").strip()
                if not txt: continue
                x0,y0,x1,y1=sp["bbox"]
                out.append({"id":f"{bi}:{li}:{si}","text":txt,"size":float(sp.get("size",0)),
                            "x0":x0,"y0":y0,"x1":x1,"y1":y1,"xc":(x0+x1)/2,"yc":(y0+y1)/2})
    return out


def direct_power(text):
    t=norm(text).replace(" ","").replace("^","").replace("{","").replace("}","")
    m=re.fullmatch(r"10([+-]\d+)",t)
    return int(m.group(1)) if m else None


def reconstruct_signed_powers(ss,W,H):
    ticks=[]
    # direct signed power tokens
    for s in ss:
        if not (s["yc"]>=0.75*H and 0.05*W<=s["xc"]<=0.95*W): continue
        e=direct_power(s["text"])
        if e is not None:
            ticks.append({"exponent":e,"xc":s["xc"],"yc":s["yc"],"source":[s["text"]],"source_ids":[s["id"]]})
    # split base '10' plus one or more smaller exponent fragments; sign must exist in source text fragments.
    for base in ss:
        if norm(base["text"]).replace(" ","")!="10": continue
        if not (base["yc"]>=0.75*H and 0.05*W<=base["xc"]<=0.95*W): continue
        cand=[]
        for s in ss:
            if s["id"]==base["id"] or s["size"]>=base["size"]-1e-6: continue
            tok=norm(s["text"]).replace(" ","")
            if not re.fullmatch(r"[+-]?\d+|[+-]",tok): continue
            if s["x0"] < base["x1"]-1.0 or s["x0"]>base["x1"]+16.0: continue
            if abs(s["yc"]-base["yc"])>7.0 or s["yc"]>base["yc"]+1.5: continue
            cand.append((s,tok))
        cand.sort(key=lambda z:z[0]["x0"])
        pieces=[]; last=base["x1"]
        for s,tok in cand:
            if s["x0"]-last>4.5: break
            pieces.append((s,tok)); last=s["x1"]
            joined="".join(x for _,x in pieces)
            if re.fullmatch(r"[+-]\d+",joined):
                e=int(joined)
                ids=[base["id"]]+[p[0]["id"] for p in pieces]
                texts=[base["text"]]+[p[0]["text"] for p in pieces]
                x0=min([base["x0"]]+[p[0]["x0"] for p in pieces]); x1=max([base["x1"]]+[p[0]["x1"] for p in pieces])
                y0=min([base["y0"]]+[p[0]["y0"] for p in pieces]); y1=max([base["y1"]]+[p[0]["y1"] for p in pieces])
                ticks.append({"exponent":e,"xc":(x0+x1)/2,"yc":(y0+y1)/2,"source":texts,"source_ids":ids})
    uniq=[]
    for t in sorted(ticks,key=lambda q:q["xc"]):
        if any(abs(t["xc"]-u["xc"])<0.75 and t["exponent"]==u["exponent"] for u in uniq): continue
        uniq.append(t)
    return uniq


def axis_identity(ss):
    text=" ".join(s["text"] for s in ss)
    n=norm(text).lower().replace(" ","")
    units=[]
    for u in ("GeV","MeV","keV","eV"):
        if u.lower() in n: units.append(u)
    mass=bool(re.search(r"m[_\s{]*(?:z|z'|zprime|v|gamma|a)",n,re.I)) or ("mass" in n and bool(units))
    # Avoid pretending a unique unit if several energy units occur elsewhere on the page.
    # Identify axis-unit candidates from bottom-band spans and neighboring text.
    return {"mass_symbol_present":mass,"page_energy_units":units,"full_text":text}


def linfit(xs,ys):
    xm=sum(xs)/len(xs); ym=sum(ys)/len(ys)
    den=sum((x-xm)**2 for x in xs)
    if den<=0: raise ValueError("degenerate x anchors")
    a=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/den
    return a,ym-a*xm


def frame_candidates(page,left,right):
    W,H=page.rect.width,page.rect.height
    out=[]
    for di,d in enumerate(page.get_drawings()):
        for item in d.get("items",[]):
            if not item: continue
            if item[0]=="re":
                r=item[1]
                if r.width>=0.35*W and r.height>=0.25*H:
                    dl=abs(r.x0-left); dr=abs(r.x1-right)
                    out.append({"drawing":di,"kind":"rect","x0":float(r.x0),"x1":float(r.x1),"y0":float(r.y0),"y1":float(r.y1),"left_delta":dl,"right_delta":dr,"matched":dl<=FRAME_TOL and dr<=FRAME_TOL})
            elif item[0]=="l":
                p0,p1=item[1],item[2]
                if abs(p0.y-p1.y)<=0.75 and abs(p1.x-p0.x)>=0.35*W and max(p0.y,p1.y)>=0.45*H:
                    x0=min(p0.x,p1.x); x1=max(p0.x,p1.x)
                    dl=abs(x0-left);dr=abs(x1-right)
                    out.append({"drawing":di,"kind":"horizontal_line","x0":float(x0),"x1":float(x1),"y":float((p0.y+p1.y)/2),"left_delta":dl,"right_delta":dr,"matched":dl<=FRAME_TOL and dr<=FRAME_TOL})
    return out


def bottom_axis_unit(ss,W,H,ticks):
    if not ticks: return None,[]
    xmin=min(t["xc"] for t in ticks); xmax=max(t["xc"] for t in ticks)
    cand=[]
    for s in ss:
        if s["yc"]<0.70*H: continue
        txt=norm(s["text"])
        for u in ("GeV","MeV","keV","eV"):
            if re.search(rf"(?<![A-Za-z]){u}(?![A-Za-z])",txt,re.I):
                cand.append({"unit":u,"text":s["text"],"xc":s["xc"],"yc":s["yc"],"id":s["id"]})
    units=sorted(set(c["unit"].lower() for c in cand))
    if len(units)==1:
        canon={"gev":"GeV","mev":"MeV","kev":"keV","ev":"eV"}[units[0]]
        return canon,cand
    return None,cand


def route_b(pdf):
    doc=pymupdf.open(stream=pdf,filetype="pdf")
    if len(doc)!=1: return {"passed":False,"reason":"not_one_page"}
    page=doc[0];W,H=page.rect.width,page.rect.height
    ss=spans(page); ident=axis_identity(ss)
    ticks=reconstruct_signed_powers(ss,W,H)
    unit,unit_hits=bottom_axis_unit(ss,W,H,ticks)
    res={"page_size":[W,H],"text_span_count":len(ss),"image_xobject_count":len(page.get_images(full=True)),"mass_axis_identity":ident["mass_symbol_present"],"bottom_axis_unit":unit,"bottom_axis_unit_hits":unit_hits,"ticks":ticks,"tick_count":len(ticks)}
    if len(ticks)<3:
        res.update({"passed":False,"reason":"fewer_than_3_signed_x_ticks"}); return res
    exps=[float(t["exponent"]) for t in ticks]; xs=[t["xc"] for t in ticks]
    # Source-native x axis must be monotonically increasing in exponent with position and unique.
    if any(exps[i+1]<=exps[i] for i in range(len(exps)-1)) or len(set(exps))!=len(exps):
        res.update({"passed":False,"reason":"signed_x_ticks_not_strictly_monotone_unique"}); return res
    span=max(exps)-min(exps)
    a,b=linfit(xs,exps)
    residuals=[y-(a*x+b) for x,y in zip(xs,exps)]
    maxres=max(abs(r) for r in residuals)
    frames=frame_candidates(page,min(xs),max(xs))
    matched=[f for f in frames if f["matched"]]
    res.update({"span_decades":span,"fit":{"a":a,"b":b},"residuals":residuals,"max_abs_residual":maxres,"frame_candidates":frames,"matched_frame_count":len(matched)})
    if not ident["mass_symbol_present"] or unit is None:
        res.update({"passed":False,"reason":"mass_axis_identity_or_unique_bottom_unit_missing"}); return res
    if span<2.0 or a<=0 or maxres>RESID_TOL:
        res.update({"passed":False,"reason":"x_axis_fit_or_span_failed"}); return res
    if len(matched)!=1:
        res.update({"passed":False,"reason":"no_unique_frame_anchored_outer_x_ticks"}); return res
    factor={"eV":1.0,"keV":1e3,"MeV":1e6,"GeV":1e9}[unit]
    interval=[10.0**min(exps)*factor,10.0**max(exps)*factor]
    res.update({"passed":True,"interval_eV":interval,"outer_exponents":[min(exps),max(exps)],"unit_factor_to_eV":factor})
    return res


def threat(interval):
    a,b=interval;t0,t1=TARGET
    if b<t0: return {"classification":"PROVABLY_MASS_DISJOINT","side":"below_target","separation_decades":math.log10(t0/b)}
    if a>t1: return {"classification":"PROVABLY_MASS_DISJOINT","side":"above_target","separation_decades":math.log10(a/t1)}
    lo,hi=max(a,t0),min(b,t1)
    return {"classification":"MASS_OVERLAP_THREAT","overlap_interval_eV":[lo,hi],"overlap_width_decades":max(0.0,math.log10(hi/lo))}


def audit(fetcher=fetch):
    raw=fetcher(URL)
    if sha256(raw)!=ARCHIVE_SHA256: raise RuntimeError("archive SHA mismatch")
    texs=tex_members(raw)
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
        members={m.name.lstrip("./"):m for m in tf.getmembers() if m.isfile()}
        if ASSET not in members: raise RuntimeError("asset missing")
        pdf=tf.extractfile(members[ASSET]).read()
    if sha256(pdf)!=ASSET_SHA256: raise RuntimeError("asset SHA mismatch")
    A=explicit_text_route(texs)
    B=route_b(pdf)
    intervals=[]
    if A.get("passed"): intervals.append(("A",A["interval_eV"]))
    if B.get("passed"): intervals.append(("B",B["interval_eV"]))
    contradiction=False
    if len(intervals)>=2:
        ref=intervals[0][1]
        for _,iv in intervals[1:]:
            contradiction |= any(abs(math.log10(x/y))>RESID_TOL for x,y in zip(ref,iv))
    if contradiction:
        cls="SCIENTIFIC_FAIL_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY"; interval=None
    elif intervals:
        # If both independently pass and agree, use the common first interval.
        cls="PASS_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY"; interval=intervals[0][1]
    else:
        cls="BLOCKED_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY"; interval=None
    return {"iteration":"0087c","classification":cls,"archive_sha256":sha256(raw),"asset_sha256":sha256(pdf),"route_A":A,"route_B":B,"certified_mass_support_eV":interval,"0087b_target_eV":TARGET,"threat_result":None if interval is None else threat(interval),"guard":"Mass-support-only authority. No y calibration, curve/path/color/legend identity, excluded-side assignment, raster/OCR/manual sign recovery, provisional-0082b endpoint import, global envelope or BSM response scan."}


def main():
    fn=pathlib.Path("cerdeno_mass_support_only_0087c.json")
    try: r=audit()
    except (OSError,RuntimeError,pymupdf.FileDataError) as e:
        r={"iteration":"0087c","classification":"INFRASTRUCTURE_FAIL_0087C","reason":repr(e)}
    fn.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(3)
    if r["classification"]!="PASS_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY":
        raise SystemExit(2)

if __name__=="__main__": main()
