import io, tarfile
from scripts.audit_bbn_tail_actionability_0087f import (
    EXPECTED_ARCHIVE_SHA256, route_a_candidates, route_b_candidates,
    new_vector_assets, classify,
)


def test_route_a_requires_bbn_coupling_and_mass_same_block():
    files={"main.tex": b"BBN helium Y_p and g_{B-L} coupling are discussed as a function of m_X mass."}
    hits=route_a_candidates(files)
    assert len(hits)==1
    assert hits[0]["file"]=="main.tex"


def test_route_b_only_machine_table_with_all_semantics():
    files={
        "curve.csv": b"mass_eV,gBL,DeltaYp\n1.0,1e-9,0.008\n1.5,2e-9,0.008\n",
        "notes.txt": b"mass gBL Yp",
    }
    hits=route_b_candidates(files)
    assert [h["file"] for h in hits]==["curve.csv"]


def test_known_bbn_vectors_are_not_new_assets():
    files={
        "Presentation/CnstrntPlotMajoranaYp.pdf": b"x",
        "Presentation/CnstrntPlotDiracYp.pdf": b"y",
        "Presentation/new_BBN_curve.svg": b"z",
    }
    hits=new_vector_assets(files)
    assert [h["file"] for h in hits]==["Presentation/new_BBN_curve.svg"]


def test_wrong_archive_hash_is_infrastructure_fail():
    bio=io.BytesIO()
    with tarfile.open(fileobj=bio,mode="w:gz") as tf:
        payload=b"test"
        info=tarfile.TarInfo("main.tex"); info.size=len(payload)
        tf.addfile(info,io.BytesIO(payload))
    r=classify(bio.getvalue())
    assert r["classification"]=="INFRASTRUCTURE_FAIL_PRIMARY_HASH_MISMATCH"
    assert r["expected_archive_sha256"]==EXPECTED_ARCHIVE_SHA256
