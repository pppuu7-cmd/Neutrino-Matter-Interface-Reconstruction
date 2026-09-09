import hashlib
import io
import tarfile

from scripts import pin_0100c1b_presn_auxiliary_manifest as mod


def make_tar(path):
    with tarfile.open(path, "w:gz") as tf:
        for name, data in {
            "pre_sn_neutrino/README": b"mapping notes\n",
            "pre_sn_neutrino/inlist_project": b"mesa config\n",
            "pre_sn_neutrino/other.dat": b"x\n",
        }.items():
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tf.addfile(info, io.BytesIO(data))
    return hashlib.md5(path.read_bytes()).hexdigest()


def test_inventory_finds_filename_candidates_without_snapshot_selection(tmp_path, monkeypatch):
    p = tmp_path / "pre_sn_neutrino.tar.gz"
    md5 = make_tar(p)
    monkeypatch.setattr(mod, "EXPECTED_MD5", md5)
    out = mod.inventory(p, "abc")
    assert out["status"] == "PASS_0100C1B_AUXILIARY_MANIFEST_LOCK_DISCOVERY_NONTERMINAL"
    names = [x["path"] for x in out["mapping_candidate_members"]]
    assert any("README" in n for n in names)
    assert any("inlist" in n for n in names)
    assert out["content_based_snapshot_selection_performed"] is False
    assert out["snapshot_mapping_authority_closed"] is False


def test_hash_mismatch_blocks(tmp_path):
    p = tmp_path / "bad.tar.gz"
    p.write_bytes(b"wrong")
    out = mod.inventory(p)
    assert out["status"] == "BLOCKED_0100C1B_AUXILIARY_ARCHIVE_HASH_MISMATCH"
