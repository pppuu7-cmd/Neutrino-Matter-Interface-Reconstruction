#!/usr/bin/env python3
"""NMIR 0087d-r3 Route-B semantic-conformance wrapper.

Scientific thresholds and geometry are unchanged.  This wrapper only enforces
the original Route-B requirement that a qualifying B-L figure be a
coupling-versus-mediator-mass constraint/limit figure, rather than any rate
figure mentioning a B-L benchmark mass.
"""
import json, pathlib, re
import audit_coherent_mass_support_only_0087d_r2 as r2

base = r2.base


def constraint_mass_plane_context(s: str) -> bool:
    q = re.sub(r"\s+", " ", s)
    constraint = bool(re.search(r"\b(?:excluded|exclusion|constraint|constraints|limit|limits|allowed)\b", q, re.I))
    coupling = bool(re.search(r"g\s*_?\s*\{?\s*Z|coupling", q, re.I))
    mass = base.mass_context(q)
    plane_or_relation = bool(re.search(r"\bplane\b|versus|\bvs\.?\b|[-–—]\s*g\s*_?\s*\{?\s*Z", q, re.I))
    return constraint and coupling and mass and plane_or_relation


def figure_candidates_r3(texs, members):
    out=[]
    for name,text in texs:
        for fm in re.finditer(r"\\begin\s*\{figure\*?\}(.*?)\\end\s*\{figure\*?\}", text, re.S|re.I):
            body=fm.group(1)
            cm=re.search(r"\\caption\s*\{(.*?)\}\s*(?:\\label|$)", body, re.S|re.I)
            caption=re.sub(r"\s+", " ", cm.group(1) if cm else body)
            if not (r2.bl_context_r2(caption) and constraint_mass_plane_context(caption)):
                continue
            graphics=re.findall(r"\\includegraphics\*?(?:\[[^\]]*\])?\s*\{([^}]+)\}", body, re.I)
            for g in graphics:
                g=g.strip(); root=pathlib.PurePosixPath(name).parent
                tries=[str(root/g), g]
                if not pathlib.PurePosixPath(g).suffix:
                    for ext in (".pdf",".eps",".ps",".svg",".png",".jpg",".jpeg"):
                        tries.extend([str(root/(g+ext)),g+ext])
                resolved=next((t.lstrip("./") for t in tries if t.lstrip("./") in members),None)
                out.append({"tex_file":name,"caption":caption,"includegraphics":g,"resolved":resolved})
    return out


base.bl_context = r2.bl_context_r2
base.figure_candidates = figure_candidates_r3


def audit(fetcher=base.fetch):
    r=base.audit(fetcher=fetcher)
    r["iteration"]="0087d-r3"
    r["parent_gate"]="0087d"
    r["parser_conformance"]=(
        "literal B-minus-L plus original Route-B explicit coupling-versus-"
        "mediator-mass constraint/limit figure semantics; starred/unstarred includegraphics retained"
    )
    return r


def main():
    fn=pathlib.Path("coherent_mass_support_only_0087d_r3.json")
    try:
        r=audit()
    except (OSError,RuntimeError,base.pymupdf.FileDataError,base.tarfile.TarError) as e:
        r={"iteration":"0087d-r3","parent_gate":"0087d","classification":"INFRASTRUCTURE_FAIL_0087D_R3","reason":repr(e)}
    fn.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(3)
    if r["classification"]!="PASS_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY":
        raise SystemExit(2)

if __name__=="__main__": main()
