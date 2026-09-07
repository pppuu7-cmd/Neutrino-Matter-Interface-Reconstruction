import io
import pymupdf
from scripts.audit_bl_stellar_sn_vector_axis_0082b import parse_num, decade_span, axis_identity, inspect_asset

def test_parse_power_forms():
    assert parse_num('10⁻⁶') == 1e-6
    assert parse_num('10^-3') == 1e-3
    assert parse_num('0.01') == 1e-2

def test_decade_span():
    assert decade_span([1e-6,1e-3,1]) == 6

def test_axis_identity_native_conventions():
    assert axis_identity("mγ′ [MeV]   e′", "eprime")["mass_axis_identity"]
    assert axis_identity("mγ′ [MeV]   e′", "eprime")["coupling_axis_identity"]
    assert axis_identity("m Z' [MeV] gB-L", "gbl")["coupling_axis_identity"]

def make_pdf(coupling='eprime'):
    d=pymupdf.open(); p=d.new_page(width=600,height=400)
    p.insert_text((240,385),"mγ′ [MeV]" if coupling=='eprime' else "m Z' [MeV]")
    p.insert_text((15,200),"e′" if coupling=='eprime' else "gB-L", rotate=90)
    for i,t in enumerate(["10⁻⁶","10⁻⁴","10⁻²","1","100"]):p.insert_text((80+i*90,365),t)
    for i,t in enumerate(["10⁻¹²","10⁻¹⁰","10⁻⁸","10⁻⁶","10⁻⁴"]):p.insert_text((5,330-i*65),t)
    for i in range(12):
        p.draw_line((60+i*3,40),(500-i*2,300),color=(0,0,0))
    return d.tobytes()

def test_vector_axis_fixture_passes():
    data=make_pdf('eprime')
    r=inspect_asset(data,'x',{'asset':'x.pdf','coupling':'eprime'})
    assert r['checks']['zero_image_xobjects']
    assert r['checks']['x_anchor_count_ge_4']
    assert r['checks']['y_anchor_count_ge_4']
    assert r['checks']['x_span_ge_3dec']
    assert r['checks']['y_span_ge_3dec']
