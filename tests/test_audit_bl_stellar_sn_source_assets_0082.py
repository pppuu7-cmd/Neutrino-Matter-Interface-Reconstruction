import io
import tarfile

from scripts.audit_bl_stellar_sn_source_assets_0082 import (
    SOURCES,
    classify,
    inspect_archive,
)


def make_tar(files):
    bio = io.BytesIO()
    with tarfile.open(fileobj=bio, mode="w:gz") as tf:
        for name, content in files.items():
            b = content.encode("utf-8") if isinstance(content, str) else content
            info = tarfile.TarInfo(name=name)
            info.size = len(b)
            tf.addfile(info, io.BytesIO(b))
    return bio.getvalue()


def cfg(key):
    return SOURCES[key]


def test_vector_referenced_b_l_source_passes():
    raw = make_tar({
        "main.tex": r"We derive a U(1)_{B-L} gauge boson constraint from SN1987A. \\includegraphics{fig7}",
        "fig7.pdf": b"%PDF-fixture",
    })
    r = inspect_archive(raw, "hong_shin_yun_2021", cfg("hong_shin_yun_2021"))
    assert r["status"] == "PASS_SOURCE_AUTHORITY"
    assert r["referenced_vector_assets"] == ["fig7.pdf"]


def test_raster_only_source_is_partial_not_blocked():
    raw = make_tar({
        "paper.tex": r"Bounds on the B-L gauge boson from SN1987A. \\includegraphics{constraint.png}",
        "constraint.png": b"raster",
    })
    r = inspect_archive(raw, "cerdeno_et_al_2021", cfg("cerdeno_et_al_2021"))
    assert r["status"] == "PARTIAL_SOURCE_AUTHORITY"
    assert not r["candidate_machine_native_route"]


def test_missing_explicit_b_l_semantics_blocks():
    raw = make_tar({
        "main.tex": r"A generic new vector mediator constraint from SN1987A. \\includegraphics{f.pdf}",
        "f.pdf": b"%PDF-fixture",
    })
    r = inspect_archive(raw, "cerdeno_et_al_2021", cfg("cerdeno_et_al_2021"))
    assert r["status"] == "BLOCKED_SOURCE_AUTHORITY"


def test_shin_yun_revisit_requires_modes_and_sn1987a():
    raw = make_tar({
        "main.tex": r"For the U(1)_{B-L} gauge boson the SN1987A constraint is revisited. The transverse contribution is strengthened and a longitudinal excluded region is found. \\includegraphics{bl.pdf}",
        "bl.pdf": b"%PDF-fixture",
    })
    r = inspect_archive(raw, "shin_yun_2022", cfg("shin_yun_2022"))
    assert r["status"] == "PASS_SOURCE_AUTHORITY"
    assert r["shin_yun_revisit_semantics_pass"] is True


def test_overall_pass_requires_all_three_and_revisit():
    raw_old = make_tar({"a.tex": r"U(1)_{B-L} gauge boson constraint bound. \\includegraphics{x.pdf}", "x.pdf": b"x"})
    raw_new = make_tar({"b.tex": r"U(1)_{B-L} SN1987A constraint revisited; transverse and longitudinal excluded modes. \\includegraphics{y.pdf}", "y.pdf": b"y"})
    results = {
        "hong_shin_yun_2021": inspect_archive(raw_old, "hong_shin_yun_2021", cfg("hong_shin_yun_2021")),
        "cerdeno_et_al_2021": inspect_archive(raw_old, "cerdeno_et_al_2021", cfg("cerdeno_et_al_2021")),
        "shin_yun_2022": inspect_archive(raw_new, "shin_yun_2022", cfg("shin_yun_2022")),
    }
    assert classify(results) == "PASS_B_L_STELLAR_SN_PRIMARY_SOURCE_ASSET_AUTHORITY"
