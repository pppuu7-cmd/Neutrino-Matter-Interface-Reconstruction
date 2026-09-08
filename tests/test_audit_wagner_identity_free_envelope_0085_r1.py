import importlib.util, io, pathlib, sys, tarfile

SCRIPTS=pathlib.Path(__file__).resolve().parents[1]/'scripts'
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0,str(SCRIPTS))
P=SCRIPTS/'audit_wagner_identity_free_envelope_0085_r1.py'
spec=importlib.util.spec_from_file_location('m0085r1',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


def test_math_delimiters_removed_but_source_words_preserved():
    s=r'The left panel shows $95 \%$ CL upper bounds for $B-L$ vector Yukawa.'
    n=m.normalize_tex_r1(s)
    assert '$' not in n
    assert '95 % cl upper bounds' in n
    assert 'b-l' in n
    assert 'vector yukawa' in n


def test_exact_source_style_caption_authority_passes():
    tex=r'''\begin{figure}\includegraphics{WEP_figure6.eps}\caption{The left panel shows $95 \%$ CL upper bounds on the strength of a vector Yukawa interaction coupled to $\tilde q=B-L$.}\end{figure}'''
    buf=io.BytesIO()
    with tarfile.open(fileobj=buf,mode='w:gz') as tf:
        raw=tex.encode()
        info=tarfile.TarInfo('WEP10.tex'); info.size=len(raw); tf.addfile(info,io.BytesIO(raw))
    buf.seek(0)
    with tarfile.open(fileobj=buf,mode='r:gz') as tf:
        a=m.base.source_text_authority(tf)
    assert a['upper_bounds_95cl']
    assert a['B_minus_L']
    assert a['figure6_context']
    assert a['vector_yukawa']


def test_frozen_geometry_constants_unchanged():
    assert m.base.EXPECTED=={'blue':4,'red':1,'orange':1,'magenta':2}
    assert m.base.MASS_CLIP_EV==1e-6
    assert m.base.EPS_SHA256=='4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882'
