import hashlib
import io
import tarfile
import zipfile

from scripts.pin_0101a2_hepdata_submission_export import inventory_package


def test_tar_submission_export_inventory(tmp_path):
    p = tmp_path / "submission.tar.gz"
    with tarfile.open(p, "w:gz") as tf:
        for name, data in {
            "submission.yaml": b"data_file: table1.yaml\n",
            "table1.yaml": b"name: table 1\n",
            "resources/dchi2_grid.txt": b"1 2 3\n",
        }.items():
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tf.addfile(info, io.BytesIO(data))
    out = inventory_package(p, "abc")
    assert out["status"] == "PASS_0101A2_HEPDATA_ORIGINAL_SUBMISSION_INVENTORIED_NONTERMINAL"
    assert out["package"]["container"] == "tar"
    assert out["submission_yaml_members"] == ["submission.yaml"]
    assert any("dchi2" in x["path"] for x in out["candidate_resource_members"])
    assert out["parameter_region_selected"] is False
    assert out["joint_global_likelihood_claim_allowed"] is False


def test_zip_submission_export_inventory(tmp_path):
    p = tmp_path / "submission.zip"
    with zipfile.ZipFile(p, "w") as zf:
        zf.writestr("submission.yaml", "data_file: table.yaml\n")
        zf.writestr("table.yaml", "name: table\n")
    out = inventory_package(p)
    assert out["status"].startswith("PASS_")
    assert out["package"]["container"] == "zip"
    assert out["package"]["member_count"] == 2


def test_unrecognized_export_is_block(tmp_path):
    p = tmp_path / "response.bin"
    p.write_bytes(b"forbidden or html")
    out = inventory_package(p)
    assert out["status"] == "BLOCKED_0101A2_HEPDATA_EXPORT_UNRECOGNIZED_CONTAINER"
    assert out["terminal_physics_execution_allowed"] is False
