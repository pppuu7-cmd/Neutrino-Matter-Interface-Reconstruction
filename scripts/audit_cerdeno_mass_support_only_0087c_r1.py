#!/usr/bin/env python3
"""NMIR 0087c-r1 parser-conformance wrapper.

Scientific contract is unchanged from prereg 0087c. The only repair is
source-native positive exponent handling described in the 0087c amendment.
"""
import json
import pathlib
import re

import audit_cerdeno_mass_support_only_0087c as base


def direct_power_r1(text):
    raw=text.strip()
    n=base.norm(raw).strip()
    # A direct power requires source-native power syntax: caret or Unicode
    # superscript. Ordinary 102 / '10 2' is not a power token.
    has_caret="^" in raw
    has_super=any(c in raw for c in "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺")
    if not (has_caret or has_super):
        return None
    if has_caret:
        t=n.replace(" ","")
        m=re.fullmatch(r"10\^\{?([+-]?\d+)\}?",t)
        return int(m.group(1)) if m else None
    t=n.replace(" ","").replace("{","").replace("}","")
    m=re.fullmatch(r"10([+-]?\d+)",t)
    return int(m.group(1)) if m else None


def reconstruct_signed_powers_r1(ss,W,H):
    ticks=[]
    for s in ss:
        if not (s["yc"]>=0.75*H and 0.05*W<=s["xc"]<=0.95*W):
            continue
        e=direct_power_r1(s["text"])
        if e is not None:
            ticks.append({"exponent":e,"xc":s["xc"],"yc":s["yc"],"source":[s["text"]],"source_ids":[s["id"]]})

    # Split base 10 + source-native smaller superscript fragments.
    # A digits-only smaller/raised fragment is positive; an explicit '-' text
    # fragment is required for a negative exponent. No vector-stroke sign is used.
    for b in ss:
        if base.norm(b["text"]).replace(" ","")!="10":
            continue
        if not (b["yc"]>=0.75*H and 0.05*W<=b["xc"]<=0.95*W):
            continue
        cand=[]
        for s in ss:
            if s["id"]==b["id"] or s["size"]>=b["size"]-1e-6:
                continue
            tok=base.norm(s["text"]).replace(" ","")
            if not re.fullmatch(r"[+-]?\d+|[+-]",tok):
                continue
            if s["x0"] < b["x1"]-1.0 or s["x0"] > b["x1"]+16.0:
                continue
            if abs(s["yc"]-b["yc"])>7.0 or s["yc"]>b["yc"]+1.5:
                continue
            cand.append((s,tok))
        cand.sort(key=lambda z:z[0]["x0"])
        pieces=[]; last=b["x1"]
        for s,tok in cand:
            if s["x0"]-last>4.5:
                break
            pieces.append((s,tok)); last=s["x1"]
            joined="".join(x for _,x in pieces)
            if re.fullmatch(r"[+-]?\d+",joined):
                # Do not finalize a standalone sign; digits are required.
                if joined in {"+","-"}:
                    continue
                e=int(joined)
                ids=[b["id"]]+[p[0]["id"] for p in pieces]
                texts=[b["text"]]+[p[0]["text"] for p in pieces]
                x0=min([b["x0"]]+[p[0]["x0"] for p in pieces]); x1=max([b["x1"]]+[p[0]["x1"] for p in pieces])
                y0=min([b["y0"]]+[p[0]["y0"] for p in pieces]); y1=max([b["y1"]]+[p[0]["y1"] for p in pieces])
                ticks.append({"exponent":e,"xc":(x0+x1)/2,"yc":(y0+y1)/2,"source":texts,"source_ids":ids})
                # If this was digits-only, it is a complete positive exponent.
                # If an explicit sign was first, keep scanning until digits joined.
                if not joined.startswith(("+","-")) or len(joined)>1:
                    break

    uniq=[]
    for t in sorted(ticks,key=lambda q:q["xc"]):
        if any(abs(t["xc"]-u["xc"])<0.75 and t["exponent"]==u["exponent"] for u in uniq):
            continue
        uniq.append(t)
    return uniq


base.direct_power=direct_power_r1
base.reconstruct_signed_powers=reconstruct_signed_powers_r1


def audit(fetcher=base.fetch):
    r=base.audit(fetcher=fetcher)
    r["iteration"]="0087c-r1"
    r["parent_gate"]="0087c"
    r["parser_conformance"]="accept source-native positive caret/superscript exponents and digits-only raised split exponent; ordinary 102/10-space-2 remains rejected; no missing minus synthesis"
    return r


def main():
    fn=pathlib.Path("cerdeno_mass_support_only_0087c_r1.json")
    try:
        r=audit()
    except (OSError,RuntimeError,base.pymupdf.FileDataError) as e:
        r={"iteration":"0087c-r1","parent_gate":"0087c","classification":"INFRASTRUCTURE_FAIL_0087C","reason":repr(e)}
    fn.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(3)
    if r["classification"]!="PASS_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY":
        raise SystemExit(2)

if __name__=="__main__": main()
