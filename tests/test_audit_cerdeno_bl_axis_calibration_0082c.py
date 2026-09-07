import importlib.util, pathlib, math

P=pathlib.Path(__file__).resolve().parents[1]/"scripts"/"audit_cerdeno_bl_axis_calibration_0082c.py"
spec=importlib.util.spec_from_file_location("m0082c",P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_direct_power_parser():
    assert m.direct_power("10−6")==-6
    assert m.direct_power("10^-4")==-4
    assert m.direct_power("1e-4") is None

def test_linear_calibration_pass_x():
    ticks=[]
    for i,e in enumerate([-5,-4,-3,-2,-1,0]):
        ticks.append({"value":10.0**e,"exponent":float(e),"xc":100.0+20.0*i,"yc":300.0,"source":[str(e)]})
    r=m.calibration(ticks,"xc")
    assert r["passed"]
    assert r["max_abs_residual"] < 1e-12
    assert r["max_abs_loo_residual"] < 1e-12

def test_linear_calibration_pass_y_negative_slope():
    ticks=[]
    for i,e in enumerate([-4,-5,-6,-7,-8]):
        ticks.append({"value":10.0**e,"exponent":float(e),"xc":40.0,"yc":100.0+25.0*i,"source":[str(e)]})
    r=m.calibration(ticks,"yc")
    assert r["passed"]
    assert r["fit"]["a"] < 0

def test_duplicate_exponent_at_distinct_coordinate_fails():
    ticks=[
      {"value":1e-5,"exponent":-5.0,"xc":10.0,"yc":0,"source":["-5"]},
      {"value":1e-4,"exponent":-4.0,"xc":20.0,"yc":0,"source":["-4"]},
      {"value":1e-3,"exponent":-3.0,"xc":30.0,"yc":0,"source":["-3"]},
      {"value":1e-2,"exponent":-2.0,"xc":40.0,"yc":0,"source":["-2"]},
      {"value":1e-2,"exponent":-2.0,"xc":50.0,"yc":0,"source":["-2dup"]},
    ]
    r=m.calibration(ticks,"xc")
    assert not r["passed"]
    assert -2.0 in r["duplicate_exponents"]

def test_fewer_than_four_ticks_blocks_calibration():
    ticks=[{"value":10.0**e,"exponent":float(e),"xc":i,"yc":0,"source":[str(e)]} for i,e in enumerate([-3,-2,-1])]
    r=m.calibration(ticks,"xc")
    assert not r["passed"]
    assert r["reason"]=="fewer_than_4_ticks"
