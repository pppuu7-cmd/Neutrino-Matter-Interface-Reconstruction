#!/usr/bin/env python3
"""Infrastructure-only diagnostic for NMIR 0087d source syntax.

Outputs only TeX semantic contexts (figure captions/includegraphics and short
B-L / mediator-symbol contexts). It does not inspect figure coordinates,
axes, ticks, curves, y values, likelihoods, or numerical exclusion geometry.
"""
import io, json, re, tarfile
import audit_coherent_mass_support_only_0087d as base


def compact_context(s, n=700):
    s=re.sub(r"\s+"," ",s).strip()
    return s[:n]


def main():
    raw=base.fetch(base.URL)
    members=base.archive_members(raw)
    texs=base.tex_texts(members)
    figs=[]
    contexts=[]
    for name,text in texs:
        for i,fm in enumerate(re.finditer(r"\\begin\s*\{figure\*?\}(.*?)\\end\s*\{figure\*?\}",text,re.S|re.I),1):
            body=fm.group(1)
            cm=re.search(r"\\caption\s*\{(.*?)\}\s*(?:\\label|$)",body,re.S|re.I)
            caption=compact_context(cm.group(1) if cm else "")
            graphics=re.findall(r"\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}",body,re.I)
            figs.append({
                "tex_file":name,
                "ordinal":i,
                "caption":caption,
                "includegraphics":graphics,
                "base_bl_context":base.bl_context(caption),
                "base_mass_context":base.mass_context(caption),
            })
        flat=re.sub(r"\s+"," ",text)
        patterns=[
            ("BL",r"B\s*[-\\! ,]*\s*L|B-L|B\\!-\\!L"),
            ("MZ",r"M\s*_?\s*\{?\s*Z|M_?\{?Z|Z.?prime.*mass|mediator\s+mass"),
        ]
        for label,pat in patterns:
            for m in list(re.finditer(pat,flat,re.I))[:30]:
                contexts.append({"tex_file":name,"kind":label,"context":compact_context(flat[max(0,m.start()-220):min(len(flat),m.end()+420)])})
    out={
        "iteration":"0087d-semantic-diagnostic",
        "classification":"INFRASTRUCTURE_DIAGNOSTIC_ONLY",
        "source_url":base.URL,
        "archive_sha256":base.sha256(raw),
        "tex_files":[n for n,_ in texs],
        "figure_environments":figs,
        "semantic_contexts":contexts,
        "guard":"No figure-byte parsing, no axes/ticks/coordinates, no y values, no paths/colors/legend identity, no likelihood, no numerical mass-support classification.",
    }
    open("coherent_source_semantics_0087d_diagnostic.json","w",encoding="utf-8").write(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()
