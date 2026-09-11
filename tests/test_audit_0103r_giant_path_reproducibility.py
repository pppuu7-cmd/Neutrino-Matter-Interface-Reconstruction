import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0103r_giant_path_reproducibility.py"
spec=importlib.util.spec_from_file_location("audit0103r",P)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)


def test_0103r_path_reproducibility():
    r=mod.run_audit()
    assert r["status"]=="PASS_0103R_GIANT_PATH_REPRODUCIBILITY_ENGINEERING_ONLY"
    assert all(r["gates"].values())
    assert r["metrics"]["scope"]=="ENGINEERING_ONLY_NOT_BETELGEUSE"
    assert r["canonical_sha256"]==r["repeat_sha256"]
