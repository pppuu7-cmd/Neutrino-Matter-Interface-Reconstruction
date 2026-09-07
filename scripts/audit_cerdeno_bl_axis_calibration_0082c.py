#!/usr/bin/env python3
import hashlib, io, json, math, re, tarfile, time, urllib.request
import pymupdf

URL = "https://export.arxiv.org/e-print/2106.11660v3"
ARCHIVE_SHA256 = "f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d"
ASSET = "Figures/BL_constraints.pdf"
ASSET_SHA256 = "6557571159bd7d279e9b78e026c79c2974fd487db86dcf3f60b566e54318d07f"
TOL = 0.015
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺−", "0123456789-+-")

def sha256(b): return hashlib.sha256(b).hexdigest()

def fetch(url):
    last = None
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent":"NMIR-0082c/1.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except Exception as e:
            last = e; time.sleep(2**i)
    raise RuntimeError(f"fetch failed: {last}")

def norm(s):
    return s.translate(SUP).replace("–","-").replace("—","-").strip()

def spans(page):
    out=[]
    raw=page.get_text("dict")
    for bi,b in enumerate(raw.get("blocks",[])):
        for li,ln in enumerate(b.get("lines",[])):
            for si,sp in enumerate(ln.get("spans",[])):
                txt=sp.get("text","").strip()
                if not txt: continue
                x0,y0,x1,y1=sp["bbox"]
                out.append({"text":txt,"size":float(sp.get("size",0.0)),"x0":x0,"y0":y0,"x1":x1,"y1":y1,
                            "xc":(x0+x1)/2,"yc":(y0+y1)/2,"block":bi,"line":li,"span":si})
    return out

def direct_power(text):
    t=norm(text).replace(" ","").replace("^","")
    m=re.fullmatch(r"10([+-]?\d+)",t)
    return int(m.group(1)) if m else None

def fragment_token(text):
    t=norm(text).replace(" ","")
    return t if re.fullmatch(r"[+-]?\d+|[+-]",t) else None

def reconstruct_power_ticks(ss):
    ticks=[]
    # direct single-span forms
    for s in ss:
        e=direct_power(s["text"])
        if e is not None:
            ticks.append({"value":10.0**e,"exponent":e,"xc":s["xc"],"yc":s["yc"],"source":[s["text"]]})
    # fragmented 10 + superscript sign/digits on same source line
    for base in ss:
        if norm(base["text"]).replace(" ","") != "10": continue
        cand=[]
        for s in ss:
            if s is base or s["block"]!=base["block"] or s["line"]!=base["line"]: continue
            tok=fragment_token(s["text"])
            if tok is None or s["size"] >= base["size"]-1e-6: continue
            if s["x0"] < base["x1"]-1.0 or s["x0"] > base["x1"]+14.0: continue
            # upper-right superscript; permit small overlap in vertical boxes from PDF font metrics
            if s["yc"] > base["yc"]+1.0: continue
            cand.append((s,tok))
        cand.sort(key=lambda z:z[0]["x0"])
        # form contiguous prefix up to sign + two digits
        pieces=[]; last_x=base["x1"]
        for s,tok in cand:
            if s["x0"]-last_x > 4.5: break
            pieces.append((s,tok)); last_x=s["x1"]
            joined="".join(t for _,t in pieces)
            if re.fullmatch(r"[+-]?\d+",joined):
                e=int(joined)
                xmax=max(x[0]["x1"] for x in pieces)
                xmin=base["x0"]
                ymin=min([base["y0"]]+[x[0]["y0"] for x in pieces]); ymax=max([base["y1"]]+[x[0]["y1"] for x in pieces])
                ticks.append({"value":10.0**e,"exponent":e,"xc":(xmin+xmax)/2,"yc":(ymin+ymax)/2,
                              "source":[base["text"]]+[x[0]["text"] for x in pieces]})
    return ticks

def ordinary_decimal_ticks(ss):
    out=[]
    for s in ss:
        t=norm(s["text"]).replace(" ","")
        try: v=float(t)
        except Exception: continue
        if math.isfinite(v) and v>0:
            out.append({"value":v,"exponent":math.log10(v),"xc":s["xc"],"yc":s["yc"],"source":[s["text"]]})
    return out

def select_axis_ticks(page, ss, axis):
    W,H=page.rect.width,page.rect.height
    candidates=reconstruct_power_ticks(ss)+ordinary_decimal_ticks(ss)
    if axis=="x":
        cand=[t for t in candidates if t["yc"]>=0.78*H and 0.05*W<=t["xc"]<=0.95*W]
        coord="xc"
    else:
        cand=[t for t in candidates if t["xc"]<=0.22*W and 0.05*H<=t["yc"]<=0.95*H]
        coord="yc"
    # remove exact duplicate reconstruction at same coordinate/value, but preserve same exponent at distinct coordinates for explicit failure check
    uniq=[]
    for t in sorted(cand,key=lambda q:(q[coord],q["exponent"])):
        if any(abs(t[coord]-u[coord])<0.5 and abs(t["exponent"]-u["exponent"])<1e-9 for u in uniq): continue
        uniq.append(t)
    return uniq,coord

def linfit(xs,ys):
    n=len(xs); xm=sum(xs)/n; ym=sum(ys)/n
    den=sum((x-xm)**2 for x in xs)
    if den<=0: raise ValueError("degenerate coordinates")
    a=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/den
    b=ym-a*xm
    return a,b

def calibration(ticks,coord):
    # Keep only values represented once; duplicated exponent at distinct coordinates is a frozen failure, not silently resolved.
    duplicate_exponents=[]
    for i,t in enumerate(ticks):
        for u in ticks[i+1:]:
            if abs(t["exponent"]-u["exponent"])<1e-9 and abs(t[coord]-u[coord])>=0.5:
                duplicate_exponents.append(t["exponent"])
    xs=[t[coord] for t in ticks]; ys=[t["exponent"] for t in ticks]
    result={"tick_count":len(ticks),"span_decades":(max(ys)-min(ys)) if ys else 0.0,"duplicate_exponents":sorted(set(duplicate_exponents)),"ticks":ticks}
    if len(ticks)<4:
        result.update({"fit":None,"max_abs_residual":None,"max_abs_loo_residual":None,"passed":False,"reason":"fewer_than_4_ticks"}); return result
    a,b=linfit(xs,ys)
    residuals=[y-(a*x+b) for x,y in zip(xs,ys)]
    loo=[]
    for i,(x,y) in enumerate(zip(xs,ys)):
        x2=xs[:i]+xs[i+1:]; y2=ys[:i]+ys[i+1:]
        aa,bb=linfit(x2,y2); loo.append(y-(aa*x+bb))
    # axis-direction monotonicity: PDF x increases right; PDF y increases downward while physical y increases upward => negative slope.
    expected_sign = 1 if coord=="xc" else -1
    sign_ok = a*expected_sign>0
    passed=(len(ticks)>=4 and result["span_decades"]>=3.0 and not result["duplicate_exponents"] and
            max(abs(r) for r in residuals)<=TOL and max(abs(r) for r in loo)<=TOL and sign_ok)
    result.update({"fit":{"a":a,"b":b},"residuals":residuals,"loo_residuals":loo,
                   "max_abs_residual":max(abs(r) for r in residuals),"max_abs_loo_residual":max(abs(r) for r in loo),
                   "slope_sign_ok":sign_ok,"passed":passed})
    return result

def audit(fetcher=fetch):
    raw=fetcher(URL)
    if sha256(raw)!=ARCHIVE_SHA256: raise RuntimeError("archive SHA mismatch")
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
        members={m.name.lstrip("./"):m for m in tf.getmembers() if m.isfile()}
        if ASSET not in members: raise RuntimeError("asset missing")
        pdf=tf.extractfile(members[ASSET]).read()
    if sha256(pdf)!=ASSET_SHA256: raise RuntimeError("asset SHA mismatch")
    doc=pymupdf.open(stream=pdf,filetype="pdf")
    if len(doc)!=1: raise RuntimeError("expected one-page asset")
    page=doc[0]; ss=spans(page)
    xt,xc=select_axis_ticks(page,ss,"x"); yt,yc=select_axis_ticks(page,ss,"y")
    xr=calibration(xt,xc); yr=calibration(yt,yc)
    if xr["passed"] and yr["passed"]: cls="PASS_CERDENO_B_L_AXIS_CALIBRATION"
    elif xr["tick_count"]<4 or yr["tick_count"]<4: cls="BLOCKED_CERDENO_B_L_AXIS_CALIBRATION"
    else: cls="SCIENTIFIC_FAIL_CERDENO_B_L_AXIS_CALIBRATION"
    return {"iteration":"0082c","classification":cls,"archive_sha256":sha256(raw),"asset":ASSET,"asset_sha256":sha256(pdf),
            "page_size":[page.rect.width,page.rect.height],"x":xr,"y":yr,"tolerance_decade":TOL,
            "guard":"Axis calibration only; no curve/path/color identity, contour extraction, excluded-side assignment, cross-paper conversion/union, global envelope or BSM response scan."}

def main():
    r=audit()
    fn="cerdeno_bl_axis_calibration_0082c.json"
    with open(fn,"w") as f: json.dump(r,f,indent=2,sort_keys=True); f.write("\n")
    print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"]!="PASS_CERDENO_B_L_AXIS_CALIBRATION": raise SystemExit(2)

if __name__=="__main__": main()
