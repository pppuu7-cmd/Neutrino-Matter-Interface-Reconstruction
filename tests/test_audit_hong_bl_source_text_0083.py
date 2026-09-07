import importlib.util, pathlib, io, tarfile

P=pathlib.Path(__file__).resolve().parents[1]/"scripts"/"audit_hong_bl_source_text_0083.py"
spec=importlib.util.spec_from_file_location("m0083",P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_anchor_patterns_accept_source_style_statement():
    s=r"For the $U(1)_{B-L}$ gauge boson, when its mass is lower than $\mathcal{O}(0.1)\,{\rm MeV}$, we obtain the cooling bound $e^{\prime}<10^{-13}$."
    s=m.compact(s)
    assert m.has_bl(s)
    assert m.has_eprime_bound(s)
    assert m.has_low_mass_domain(s)
    assert m.has_cooling_result_context(s)
    assert not m.exact_mass_inequality(s)

def test_exact_mass_requires_explicit_nonapproximate_inequality():
    s=m.compact(r"For $U(1)_{B-L}$ cooling, $m_{Z'}<0.1\,{\rm MeV}$ and $e^{\prime}<10^{-13}$ are excluded above the coupling bound.")
    assert m.exact_mass_inequality(s)

def test_big_o_is_not_exact_endpoint():
    s=m.compact(r"for masses lower than $\mathcal{O}(0.1)\,{\rm MeV}$")
    assert not m.exact_mass_inequality(s)

def test_bibliography_not_needed_for_tex_inventory():
    raw=io.BytesIO()
    with tarfile.open(fileobj=raw,mode="w") as tf:
        for name,content in [("main.tex",b"hello"),("refs.bib",b"ignore")]:
            info=tarfile.TarInfo(name); info.size=len(content); tf.addfile(info,io.BytesIO(content))
    files=m.tex_files_from_archive(raw.getvalue())
    assert [x[0] for x in files]==["main.tex"]
