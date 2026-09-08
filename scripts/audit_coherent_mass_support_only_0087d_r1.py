#!/usr/bin/env python3
"""NMIR 0087d-r1 parser-conformance wrapper.

Scientific contract is unchanged from prereg 0087d. The only repair is
support for standard LaTeX `\\includegraphics*` asset invocation.
"""
import json, pathlib, re
import audit_coherent_mass_support_only_0087d as base


def figure_candidates_r1(texs,members):
    out=[]
    for name,text in texs:
        for fm in re.finditer(r"\\begin\s*\{figure\*?\}(.*?)\\end\s*\{figure\*?\}",text,re.S|re.I):
            body=fm.group(1)
            cm=re.search(r"\\caption\s*\{(.*?)\}\s*(?:\\label|$)",body,re.S|re.I)
            caption=re.sub(r"\s+"," ",cm.group(1) if cm else body)
            if not (base.bl_context(caption) and base.mass_context(caption)):
                continue
            graphics=re.findall(r"\\includegraphics\*?(?:\[[^\]]*\])?\s*\{([^}]+)\}",body,re.I)
            for g in graphics:
                g=g.strip();root=pathlib.PurePosixPath(name).parent
                tries=[str(root/g),g]
                if not pathlib.PurePosixPath(g).suffix:
                    for ext in (".pdf",".eps",".ps",".svg",".png",".jpg",".jpeg"):
                        tries.extend([str(root/(g+ext)),g+ext])
                resolved=next((t.lstrip("./") for t in tries if t.lstrip("./") in members),None)
                out.append({"tex_file":name,"caption":caption,"includegraphics":g,"resolved":resolved})
    return out


base.figure_candidates=figure_candidates_r1


def audit(fetcher=base.fetch):
    r=base.audit(fetcher=fetcher)
    r["iteration"]="0087d-r1"
    r["parent_gate"]="0087d"
    r["parser_conformance"]="accept standard starred and unstarred LaTeX includegraphics invocation only"
    return r


def main():
    fn=pathlib.Path("coherent_mass_support_only_0087d_r1.json")
    try:
        r=audit()
    except (OSError,RuntimeError,base.pymupdf.FileDataError,base.tarfile.TarError) as e:
        r={"iteration":"0087d-r1","parent_gate":"0087d","classification":"INFRASTRUCTURE_FAIL_0087D","reason":repr(e)}
    fn.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2,sort_keys=True))
    if r["classification"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(3)
    if r["classification"]!="PASS_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY":
        raise SystemExit(2)

if __name__=="__main__": main()
