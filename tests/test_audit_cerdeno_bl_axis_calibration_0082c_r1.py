import importlib.util, pathlib

P=pathlib.Path(__file__).resolve().parents[1]/"scripts"/"audit_cerdeno_bl_axis_calibration_0082c_r1.py"
spec=importlib.util.spec_from_file_location("m0082cr1",P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_direct_power_parser():
    assert m.direct_power("10−6")==-6
    assert m.direct_power("10^-4")==-4
    assert m.direct_power("1e-4") is None

def test_geometric_fragment_join_does_not_require_pymupdf_line_id():
    ss=[
      {"id":"0:0:0","text":"10","size":10.0,"x0":10,"x1":20,"y0":90,"y1":110,"xc":15,"yc":100},
      {"id":"9:7:3","text":"-3","size":7.0,"x0":21,"x1":28,"y0":89,"y1":99,"xc":24.5,"yc":94},
    ]
    ticks=m.reconstruct_power_ticks(ss)
    assert len(ticks)==1
    assert ticks[0]["exponent"]==-3
    assert ticks[0]["explicit_sign"]

def test_linear_calibration_pass_x_and_y():
    xt=[{"value":10.0**e,"exponent":float(e),"xc":100+20*i,"yc":300,"source":[str(e)],"explicit_sign":e<0} for i,e in enumerate([-3,-2,-1,0])]
    yt=[{"value":10.0**e,"exponent":float(e),"xc":40,"yc":100+25*i,"source":[str(e)],"explicit_sign":e<0} for i,e in enumerate([-2,-3,-4,-5])]
    assert m.calibration(xt,"xc")["passed"]
    assert m.calibration(yt,"yc")["passed"]

def test_missing_sign_text_fragmentation_blocks_not_scientific_fail():
    ticks=[{"value":10.0**e,"exponent":float(e),"xc":100+20*i,"yc":300,"source":[str(e)],"explicit_sign":False} for i,e in enumerate([3,2,1,0])]
    r=m.calibration(ticks,"xc")
    assert not r["passed"]
    assert r["blocked"]
    assert r["reason"]=="axis_direction_requires_sign_not_present_in_source_native_text_spans"

def test_power_source_fragments_are_not_reused_as_decimal_ticks():
    ss=[
      {"id":"0","text":"10","size":10.0,"x0":10,"x1":20,"y0":90,"y1":110,"xc":15,"yc":100},
      {"id":"1","text":"3","size":7.0,"x0":21,"x1":25,"y0":89,"y1":99,"xc":23,"yc":94},
      {"id":"2","text":"2.5","size":10.0,"x0":50,"x1":60,"y0":90,"y1":110,"xc":55,"yc":100},
    ]
    powers=m.reconstruct_power_ticks(ss)
    excluded={sid for t in powers for sid in t["source_ids"]}
    dec=m.ordinary_decimal_ticks(ss,excluded)
    assert [d["value"] for d in dec]==[2.5]

def test_dominant_axis_cluster_rejects_corner_cross_axis_tick():
    cand=[
      {"xc":70,"yc":356,"exponent":-3,"value":1e-3},
      {"xc":190,"yc":356,"exponent":-2,"value":1e-2},
      {"xc":320,"yc":356,"exponent":-1,"value":1e-1},
      {"xc":450,"yc":356,"exponent":0,"value":1},
      {"xc":50,"yc":318,"exponent":-5,"value":1e-5},
    ]
    group,baseline=m.dominant_axis_cluster(cand,"x")
    assert len(group)==4
    assert abs(baseline-356)<1e-9

def test_duplicate_exponent_at_distinct_coordinate_fails():
    ticks=[
      {"value":1e-5,"exponent":-5.0,"xc":10.0,"yc":0,"source":["-5"],"explicit_sign":True},
      {"value":1e-4,"exponent":-4.0,"xc":20.0,"yc":0,"source":["-4"],"explicit_sign":True},
      {"value":1e-3,"exponent":-3.0,"xc":30.0,"yc":0,"source":["-3"],"explicit_sign":True},
      {"value":1e-2,"exponent":-2.0,"xc":40.0,"yc":0,"source":["-2"],"explicit_sign":True},
      {"value":1e-2,"exponent":-2.0,"xc":50.0,"yc":0,"source":["-2dup"],"explicit_sign":True},
    ]
    r=m.calibration(ticks,"xc")
    assert not r["passed"]
    assert -2.0 in r["duplicate_exponents"]
