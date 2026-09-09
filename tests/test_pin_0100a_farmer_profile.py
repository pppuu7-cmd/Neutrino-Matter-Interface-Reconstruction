import io
import tarfile

import pytest

from scripts.pin_0100a_farmer_profile import MODEL_TOKEN, parse_mesa_profile, scan_archive


def fake_profile(n=40):
    lines = [
        "1 2 3",
        "model_number star_age version_number",
        "1 2.0 7624",
        "",
        "1 2 3 4",
        "zone radius logRho ye",
    ]
    # MESA profiles are often surface->centre. Canonicalization must sort radius.
    for i in range(n, 0, -1):
        radius_rsun = 1.0e-5 * i
        logrho = 8.0 + 0.01 * i
        ye = 0.46 + 1.0e-4 * i
        lines.append(f"{i} {radius_rsun:.12e} {logrho:.12e} {ye:.12e}")
    return ("\n".join(lines) + "\n").encode()


def test_parse_mesa_profile_normalizes_and_validates():
    out = parse_mesa_profile(fake_profile())
    rows = out["rows"]
    assert len(rows) == 40
    assert rows[0][0] < rows[-1][0]
    assert all(rows[i + 1][0] > rows[i][0] for i in range(len(rows) - 1))
    assert all(rho > 0 for _, rho, _ in rows)
    assert all(0 < ye <= 1 for _, _, ye in rows)
    assert out["source_columns"] == {"radius": "radius", "rho": "logRho", "ye": "ye"}


def test_parse_mesa_profile_rejects_missing_ye():
    data = b"zone radius logRho\n1 1e-5 8.0\n" * 40
    with pytest.raises(ValueError):
        parse_mesa_profile(data)


@pytest.mark.parametrize("tar_mode", ["w:gz", "w"])
def test_scan_archive_selects_exact_model_token_for_compressed_or_plain_tar(tmp_path, tar_mode):
    # The real Zenodo asset is MD5-authoritative even if filename suffix and
    # container compression disagree, so scanner behavior must not depend on suffix.
    archive = tmp_path / "profiles.tar.gz"
    with tarfile.open(archive, tar_mode) as tf:
        good = fake_profile()
        info = tarfile.TarInfo(name=f"models/{MODEL_TOKEN}/final_profile.data")
        info.size = len(good)
        tf.addfile(info, io.BytesIO(good))

        other = fake_profile()
        info2 = tarfile.TarInfo(name="models/25_other_model/final_profile.data")
        info2.size = len(other)
        tf.addfile(info2, io.BytesIO(other))

    found = scan_archive(archive)
    assert len(found) == 1
    assert MODEL_TOKEN in found[0]["member_path"]
    assert len(found[0]["member_sha256"]) == 64
