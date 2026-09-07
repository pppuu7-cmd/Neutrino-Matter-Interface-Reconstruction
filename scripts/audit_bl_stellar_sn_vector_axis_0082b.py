#!/usr/bin/env python3
import hashlib, io, json, math, os, re, tarfile, time, urllib.request
import pymupdf

SOURCES={
"hong_shin_yun_2021":{"url":"https://export.arxiv.org/e-print/2012.05427v3","sha":"6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc","asset":"B-LConstraints.pdf","coupling":"eprime"},
"cerdeno_et_al_2021":{"url":"https://export.arxiv.org/e-print/2106.11660v3","sha":"f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d","asset":"Figures/BL_constraints.pdf","coupling":"gbl"},
"shin_yun_2022":{"url":"https://export.arxiv.org/e-print/2110.03362v2","sha":"7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd","asset":"B-L_Constraints.pdf","coupling":"eprime"}}
SUP=str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺","0123456789-+")
def sha(b): return hashlib.sha256(b).hexdigest()
def fetch(url):
    last=None
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"NMIR-0082b/1.0"})
            with urllib.request.urlopen(req,timeout=90) as r:return r.read()
        except Exception as e:
            last=e; time.sleep(2**i)
    raise RuntimeError(f"fetch failed: {last}")
def norm(s):
    return s.translate(SUP).replace("−","-").replace("–","-").replace("′","'").replace("’","'").replace("ε","e").replace("ϵ","e").replace("γ","gamma").replace("Γ","Gamma")
def parse_num(s):
    t=norm(s).strip().replace(" ","").replace("×","x")
    t=t.strip("[](){}:,;")
    # 10^-6, 10-6, 10^−6
    m=re.fullmatch(r"10\^?([+-]?\d+)",t)
    if m:
        e=int(m.group(1)); return 10.0**e
    # common PDF extraction 10−6 already normalized to 10-6
    m=re.fullmatch(r"10([+-]\d+)",t)
    if m:
        e=int(m.group(1)); return 10.0**e
    try:
        v=float(t)
        if math.isfinite(v) and v>0:return v
    except: pass
    return None
def decade_span(vals):
    vals=[v for v in vals if v and v>0]
    return math.log10(max(vals)/min(vals)) if len(vals)>=2 else 0.0
def spans(page):
    out=[]
    raw=page.get_text("dict")
    for b in raw.get("blocks",[]):
        for ln in b.get("lines",[]):
            for sp in ln.get("spans",[]):
                txt=sp.get("text","").strip()
                if txt:
                    x0,y0,x1,y1=sp["bbox"];out.append({"text":txt,"x0":x0,"y0":y0,"x1":x1,"y1":y1,"xc":(x0+x1)/2,"yc":(y0+y1)/2})
    return out
def axis_identity(text,coupling):
    n=norm(text).lower().replace(" ","")
    unit=any(u.lower() in n for u in ("ev","kev","mev","gev"))
    mass=unit and ("mass" in n or "m_" in n or "m{" in n or "mgamma" in n or "mz" in n or "mγ" in text.lower() or "m" in n)
    if coupling=="eprime":
        coup=("e'" in norm(text).lower() or "e′" in text.lower() or "e’" in text.lower() or "ε" in text or "ϵ" in text)
    else:
        compact=norm(text).lower().replace(" ","").replace("_","")
        coup=("gb-l" in compact or "gbl" in compact or ("g" in compact and "b-l" in compact))
    return {"mass_axis_identity":bool(mass),"coupling_axis_identity":bool(coup),"energy_unit_present":bool(unit)}
def inspect_asset(data,key,cfg):
    doc=pymupdf.open(stream=data,filetype="pdf")
    if len(doc)!=1:
        return {"asset":cfg["asset"],"asset_sha256":sha(data),"page_count":len(doc),"blocked_multi_page":True,"passed":False}
    p=doc[0]; W,H=p.rect.width,p.rect.height
    ss=spans(p); text=" ".join(x["text"] for x in ss)
    drawings=p.get_drawings(); path_items=sum(len(d.get("items",[])) for d in drawings)
    images=p.get_images(full=True)
    # text-derived numeric candidates; source geometry only used to associate axis bands.
    xraw=[]; yraw=[]
    for sp in ss:
        v=parse_num(sp["text"])
        if v is None: continue
        if sp["yc"] >= 0.78*H and 0.05*W <= sp["xc"] <= 0.95*W:xraw.append({**sp,"value":v})
        if sp["xc"] <= 0.22*W and 0.05*H <= sp["yc"] <= 0.95*H:yraw.append({**sp,"value":v})
    # deterministic adjacent span joining for split powers of ten within same axis bands.
    for a in ss:
        if norm(a["text"]).strip()=="10":
            for b in ss:
                if b is a: continue
                if abs(b["x0"]-a["x1"])<=8 and abs(b["yc"]-a["yc"])<=8:
                    exp=norm(b["text"]).strip()
                    if re.fullmatch(r"[+-]?\d+",exp):
                        v=10.0**int(exp)
                        xc=(a["xc"]+b["xc"])/2;yc=(a["yc"]+b["yc"])/2
                        rec={"text":a["text"]+b["text"],"xc":xc,"yc":yc,"value":v}
                        if yc>=0.78*H and 0.05*W<=xc<=0.95*W:xraw.append(rec)
                        if xc<=0.22*W and 0.05*H<=yc<=0.95*H:yraw.append(rec)
    def uniq(rs):
        d={}
        for r in rs:d.setdefault(round(math.log10(r["value"]),9),r)
        return [d[k] for k in sorted(d)]
    xs,ys=uniq(xraw),uniq(yraw)
    ident=axis_identity(text,cfg["coupling"])
    checks={
      "single_page":True,"zero_image_xobjects":len(images)==0,"drawing_count_ge_10":len(drawings)>=10,
      "text_count_ge_10":len(ss)>=10,"mass_axis_identity":ident["mass_axis_identity"],"coupling_axis_identity":ident["coupling_axis_identity"],
      "x_anchor_count_ge_4":len(xs)>=4,"y_anchor_count_ge_4":len(ys)>=4,"x_span_ge_3dec":decade_span([r["value"] for r in xs])>=3.0,"y_span_ge_3dec":decade_span([r["value"] for r in ys])>=3.0}
    return {"asset":cfg["asset"],"asset_sha256":sha(data),"bytes":len(data),"page_count":1,"page_size":[W,H],"drawing_count":len(drawings),"path_item_count":path_items,"image_xobject_count":len(images),"text_span_count":len(ss),"text_inventory":text,"axis_identity":ident,"x_anchors":xs,"y_anchors":ys,"x_span_decade":decade_span([r["value"] for r in xs]),"y_span_decade":decade_span([r["value"] for r in ys]),"checks":checks,"passed":all(checks.values())}
def audit(fetcher=fetch):
    out={}
    for key,cfg in SOURCES.items():
        raw=fetcher(cfg["url"])
        if sha(raw)!=cfg["sha"]:raise RuntimeError(f"archive SHA mismatch {key}")
        with tarfile.open(fileobj=io.BytesIO(raw),mode="r:*") as tf:
            members={m.name.lstrip("./"):m for m in tf.getmembers() if m.isfile()}
            if cfg["asset"] not in members:raise RuntimeError(f"missing asset {cfg['asset']}")
            data=tf.extractfile(members[cfg["asset"]]).read()
        out[key]=inspect_asset(data,key,cfg)
    passed=all(v["passed"] for v in out.values())
    return {"iteration":"0082b","classification":"PASS_B_L_STELLAR_SN_VECTOR_AXIS_AUTHORITY" if passed else "BLOCKED_B_L_STELLAR_SN_VECTOR_AXIS_AUTHORITY","sources":out,"guard":"Vector integrity, native axis text identity and tick-anchor sufficiency only; no curve color/path semantic selection, axis fit, contour extraction, excluded-side assignment, cross-paper conversion/union, global envelope or response scan."}
def main():
    r=audit(); fn="bl_stellar_sn_vector_axis_0082b.json"
    with open(fn,"w") as f:json.dump(r,f,indent=2,sort_keys=True);f.write("\n")
    print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"].startswith("BLOCKED_"):raise SystemExit(2)
if __name__=="__main__":main()
