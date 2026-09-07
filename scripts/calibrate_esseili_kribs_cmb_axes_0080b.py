#!/usr/bin/env python3
import hashlib
import io
import json
import math
import tarfile
import urllib.request

import pymupdf

SOURCE_URL = "https://export.arxiv.org/e-print/2308.07955v2"
SOURCE_SHA256 = "484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c"
ASSETS = {
    "majorana": ("Presentation/CnstrntPlotMajoranaNeff.pdf", "8b5c5839fada534ed10d79768335050814765a6ec00bddcb51e75cc0f64e7837"),
    "dirac": ("Presentation/CnstrntPlotDiracNeff.pdf", "c06b66e5cb35c3b1cae341da393e9b638d3f3f536cef09a3ca5431600fb2ed4a"),
}
X_TEXT_TO_EXP = {"10-6":-6,"10-5":-5,"10-4":-4,"10-3":-3,"10-2":-2,"0.1":-1,"1":0,"10":1,"102":2,"103":3}
Y_TEXT_TO_EXP = {f"10-{i}":-i for i in range(17, 2, -1)}
LEVEL_TEXTS = {"0.05","0.1","0.2","0.3","0.4","0.5"}


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fetch_source():
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent":"NMIR-CMB-axis-calibration/0080b"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def ols(xs, ys):
    n = len(xs)
    xm = sum(xs)/n
    ym = sum(ys)/n
    sxx = sum((x-xm)**2 for x in xs)
    if sxx == 0:
        raise ValueError("zero x variance")
    a = sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sxx
    b = ym-a*xm
    residuals = [a*x+b-y for x,y in zip(xs,ys)]
    return a,b,residuals


def loo_residuals(xs, ys):
    out=[]
    for i in range(len(xs)):
        xx=xs[:i]+xs[i+1:]
        yy=ys[:i]+ys[i+1:]
        a,b,_=ols(xx,yy)
        out.append(a*xs[i]+b-ys[i])
    return out


def inspect(data: bytes, name: str):
    doc=pymupdf.open(stream=data,filetype="pdf")
    page=doc[0]
    words=[]
    for w in page.get_text("words"):
        words.append({"text":w[4],"x0":w[0],"y0":w[1],"x1":w[2],"y1":w[3],"xc":(w[0]+w[2])/2,"yc":(w[1]+w[3])/2})

    x_candidates=[]
    for w in words:
        if w["text"] in X_TEXT_TO_EXP and 430 <= w["yc"] <= 462:
            x_candidates.append({**w,"exponent":X_TEXT_TO_EXP[w["text"]]})
    # require one per exponent; sorting by exponent is independent of geometry
    x_candidates=sorted(x_candidates,key=lambda z:z["exponent"])

    y_candidates=[]
    for w in words:
        if w["text"] in Y_TEXT_TO_EXP and w["xc"] < 68 and w["yc"] < 435:
            y_candidates.append({**w,"exponent":Y_TEXT_TO_EXP[w["text"]]})
    y_candidates=sorted(y_candidates,key=lambda z:z["exponent"])

    x_exps=[z["exponent"] for z in x_candidates]
    y_exps=[z["exponent"] for z in y_candidates]
    x_unique=(x_exps==list(range(-6,4)))
    y_unique=(y_exps==list(range(-17,-2)))

    x_fit=None; y_fit=None
    if x_unique:
        xs=[z["xc"] for z in x_candidates]; ys=x_exps
        a,b,res=ols(xs,ys); loo=loo_residuals(xs,ys)
        x_fit={"a":a,"b":b,"residuals_decade":res,"loo_residuals_decade":loo,"max_abs_residual_decade":max(map(abs,res)),"max_abs_loo_decade":max(map(abs,loo))}
    if y_unique:
        xs=[z["yc"] for z in y_candidates]; ys=y_exps
        a,b,res=ols(xs,ys); loo=loo_residuals(xs,ys)
        y_fit={"a":a,"b":b,"residuals_decade":res,"loo_residuals_decade":loo,"max_abs_residual_decade":max(map(abs,res)),"max_abs_loo_decade":max(map(abs,loo))}

    levels=[w for w in words if w["text"] in LEVEL_TEXTS and w["yc"] < 400]
    checks={
        "x_tick_count_10":len(x_candidates)==10,
        "y_tick_count_15":len(y_candidates)==15,
        "x_exact_exponents":x_unique,
        "y_exact_exponents":y_unique,
        "x_fit_residual_le_0p015":bool(x_fit and x_fit["max_abs_residual_decade"]<=0.015),
        "x_loo_residual_le_0p015":bool(x_fit and x_fit["max_abs_loo_decade"]<=0.015),
        "y_fit_residual_le_0p015":bool(y_fit and y_fit["max_abs_residual_decade"]<=0.015),
        "y_loo_residual_le_0p015":bool(y_fit and y_fit["max_abs_loo_decade"]<=0.015),
    }
    return {"asset":name,"asset_sha256":sha256(data),"x_ticks":x_candidates,"y_ticks":y_candidates,"x_fit":x_fit,"y_fit":y_fit,"delta_neff_text_inventory":levels,"checks":checks}


def audit():
    raw=fetch_source()
    if sha256(raw)!=SOURCE_SHA256:
        raise RuntimeError("source SHA mismatch")
    out={}
    with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
        members={m.name.lstrip("./"):m for m in tf.getmembers() if m.isfile()}
        for scenario,(asset,expected_sha) in ASSETS.items():
            fh=tf.extractfile(members[asset])
            if fh is None: raise RuntimeError(f"cannot extract {asset}")
            data=fh.read()
            if sha256(data)!=expected_sha: raise RuntimeError(f"asset SHA mismatch {asset}")
            out[scenario]=inspect(data,asset)

    maj=out["majorana"]; d=out["dirac"]
    cross_x=[]; cross_y=[]
    if maj["x_fit"] and d["x_fit"]:
        for t in maj["x_ticks"]:
            x=t["xc"]
            cross_x.append((maj["x_fit"]["a"]*x+maj["x_fit"]["b"])-(d["x_fit"]["a"]*x+d["x_fit"]["b"]))
    if maj["y_fit"] and d["y_fit"]:
        for t in maj["y_ticks"]:
            y=t["yc"]
            cross_y.append((maj["y_fit"]["a"]*y+maj["y_fit"]["b"])-(d["y_fit"]["a"]*y+d["y_fit"]["b"]))
    cross={
        "x_differences_decade":cross_x,
        "y_differences_decade":cross_y,
        "max_abs_x_difference_decade":max(map(abs,cross_x)) if cross_x else math.inf,
        "max_abs_y_difference_decade":max(map(abs,cross_y)) if cross_y else math.inf,
    }
    cross["x_pass_le_1e-5"]=cross["max_abs_x_difference_decade"]<=1e-5
    cross["y_pass_le_1e-5"]=cross["max_abs_y_difference_decade"]<=1e-5
    all_panel_checks=all(all(v for v in r["checks"].values()) for r in out.values())
    passed=all_panel_checks and cross["x_pass_le_1e-5"] and cross["y_pass_le_1e-5"]
    return {
        "iteration":"0080b",
        "classification":"PASS_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION" if passed else "SCIENTIFIC_FAIL_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION",
        "source_sha256":SOURCE_SHA256,
        "panels":out,
        "cross_panel_replication":cross,
        "guard":"Axis calibration and text-level inventory only; no path/color selection, Planck threshold choice, excluded-region materialization, scenario union, global envelope union, or BSM response scan."
    }


def main():
    r=audit()
    with open("esseili_kribs_cmb_axis_calibration_0080b.json","w",encoding="utf-8") as f:
        json.dump(r,f,indent=2,sort_keys=True); f.write("\n")
    print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"].startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(2)

if __name__=="__main__":
    main()
