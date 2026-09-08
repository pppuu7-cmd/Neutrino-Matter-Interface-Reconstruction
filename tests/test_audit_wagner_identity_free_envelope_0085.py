import importlib.util, io, math, pathlib, sys, tarfile

SCRIPTS=pathlib.Path(__file__).resolve().parents[1]/'scripts'
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0,str(SCRIPTS))
P=SCRIPTS/'audit_wagner_identity_free_envelope_0085.py'
spec=importlib.util.spec_from_file_location('m0085',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


def comp(cid, pts):
    q=[{'x':x,'y':y,'m_V_eV':10**x,'alpha':1.0,'g_BL':10**y} for x,y in pts]
    return {'anonymous_id':cid,'x_min':min(x for x,_ in pts),'x_max':max(x for x,_ in pts),'points':q}


def test_envelope_is_pointwise_min_and_name_order_invariant():
    cs=[comp('a',[(-6,-10),(-4,-9)]),comp('b',[(-6,-9),(-4,-11)])]
    for x in [-6,-5,-4]:
        a=m.envelope_at(cs,x); b=m.envelope_at(list(reversed(cs)),x)
        assert a is not None and b is not None
        assert math.isclose(a[0],b[0],abs_tol=1e-15)
    assert math.isclose(m.envelope_at(cs,-6)[0],-10,abs_tol=1e-15)
    assert math.isclose(m.envelope_at(cs,-4)[0],-11,abs_tol=1e-15)


def test_no_extrapolation_or_gap_bridge():
    c=comp('x',[(-6,-10),(-5,-9)])
    assert m.interp_component(c,-6.5) is None
    assert m.interp_component(c,-4.5) is None


def test_monotonic_x_guard():
    assert m.monotonic_x([(1,1),(2,2),(3,1)])
    assert not m.monotonic_x([(1,1),(3,2),(2,1)])


def test_transform_roundtrip_formula_positive():
    tr={'a_x':3.0018224354393763,'b_x':-7.051566622680237,'a_y':1.650456736852946,'b_y':-12.69366318007594}
    p=m.transform_eps((4.348,2.238),tr)
    assert p['m_V_eV']>0 and p['alpha']>0 and p['g_BL']>0
    xr=(p['log10_lambda_m']-tr['b_x'])/tr['a_x']; yr=(p['log10_alpha']-tr['b_y'])/tr['a_y']
    assert abs(xr-4.348)<1e-12 and abs(yr-2.238)<1e-12


def test_expected_topology_frozen_to_corrected_0072d():
    assert m.EXPECTED=={'blue':4,'red':1,'orange':1,'magenta':2}
    assert sum(m.EXPECTED.values())==8


def test_source_caption_accepts_exact_spaced_plural_wagner_wording():
    tex=r'''\begin{figure}\includegraphics{WEP_figure6.eps}\caption{The left panel shows $95 \%$ CL upper bounds on the strength of a vector Yukawa interaction coupled to $\tilde q=B-L$.}\end{figure}'''
    buf=io.BytesIO()
    with tarfile.open(fileobj=buf,mode='w:gz') as tf:
        raw=tex.encode()
        info=tarfile.TarInfo('WEP10.tex'); info.size=len(raw); tf.addfile(info,io.BytesIO(raw))
    buf.seek(0)
    with tarfile.open(fileobj=buf,mode='r:gz') as tf:
        a=m.source_text_authority(tf)
    assert a['upper_bounds_95cl']
    assert a['B_minus_L']
    assert a['figure6_context']
    assert a['vector_yukawa']
