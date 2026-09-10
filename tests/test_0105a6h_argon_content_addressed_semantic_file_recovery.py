import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0105a6h_argon_content_addressed_semantic_file_recovery.py"
s=importlib.util.spec_from_file_location("a6h",P); a6h=importlib.util.module_from_spec(s); s.loader.exec_module(a6h)

def test_mirror_location_frozen():
    assert a6h.MIRROR_REPO=="Newtrinos-org/Newtrinos.jl"
    assert a6h.MIRROR_COMMIT=="fa87689ddedae1929e33d66ad1f0efa1b7cce206"

def test_exact_four_files_only():
    assert set(a6h.EXPECTED)=={"LArParametersAnlA.yaml","readYAMLParameters.py","PlotExtractedData.C","CENNS10AnlAEfficiency.txt"}

def test_yaml_official_hash_frozen():
    assert a6h.EXPECTED["LArParametersAnlA.yaml"]==(4906,"cc9f2c60ce0c17809453e0caad9c4a38","a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e")

def test_mirror_never_becomes_authority():
    t=P.read_text().lower()
    assert '"mirror_authority":false' in t
    assert '"sm_null_reproduction_permission_percent":0' in t
    assert '"observed_bsm_residual_permission_percent":0' in t

def test_no_normalization_before_hashing():
    t=P.read_text().lower()
    assert "replace(" not in t
    assert "strip()" not in t
