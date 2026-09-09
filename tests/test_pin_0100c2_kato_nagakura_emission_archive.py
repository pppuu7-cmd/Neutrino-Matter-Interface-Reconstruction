import hashlib
import io
from pathlib import Path
import zipfile

from scripts import pin_0100c2_kato_nagakura_emission_archive as mod


def make_archive(path: Path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        lc = "1 10.0 1 2 3\n2 5.0 1 2 3\n3 1.0 1 2 3\n"
        zf.writestr("MESA/lightcurvem25.dat", lc)
        for step in (1, 2, 3):
            zf.writestr(f"MESA/25/spectrum{step}.dat", "1.0 1 2 3\n2.0 2 3 4\n")
    return hashlib.md5(path.read_bytes()).hexdigest()


def test_parse_lightcurve_step_time_columns():
    out = mod.parse_lightcurve(b"1 10.0 1\n2 5.0 2\n")
    assert out["row_count"] == 2
    assert out["steps"] == [1, 2]
    assert out["time_to_bounce_s_min"] == 5.0


def test_inventory_maps_spectrum_filename_steps_to_lightcurve(tmp_path, monkeypatch):
    p = tmp_path / "MESA_25M.zip"
    md5 = make_archive(p)
    monkeypatch.setattr(mod, "EXPECTED_MD5", md5)
    out = mod.inventory_archive(p, "abc")
    assert out["status"] == "PASS_0100C2_EMISSION_ARCHIVE_INVENTORIED_NONTERMINAL"
    assert out["lightcurve"]["member_path"].endswith("lightcurvem25.dat")
    assert out["spectrum_mapping"]["spectrum_step_count"] == 3
    assert out["spectrum_mapping"]["orphan_spectrum_steps"] == []
    assert out["snapshot_selection_performed"] is False
    assert out["terminal_physics_execution_allowed"] is False


def test_hash_mismatch_is_block_not_fail(tmp_path):
    p = tmp_path / "bad.zip"
    p.write_bytes(b"not the frozen archive")
    out = mod.inventory_archive(p)
    assert out["status"] == "BLOCKED_0100C2_EMISSION_ARCHIVE_HASH_MISMATCH"
    assert out["terminal_physics_execution_allowed"] is False
