import gzip
import io
import tarfile

from scripts.audit_fayet_fifth_force_authority_0079 import extract_text_members, sha256


def test_extract_plain_text():
    data = b"plain B-L epsilon source"
    out = extract_text_members(data)
    assert out["source.tex"].startswith("plain B-L")


def test_extract_gzip_text():
    data = gzip.compress(b"\\documentclass{article} B-L epsilon")
    out = extract_text_members(data)
    assert "B-L epsilon" in out["source.tex"]


def test_extract_tar_text_only():
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w") as tf:
        tex = b"B-L long-range source"
        ti = tarfile.TarInfo("paper.tex")
        ti.size = len(tex)
        tf.addfile(ti, io.BytesIO(tex))
        png = b"not text"
        pi = tarfile.TarInfo("figure.png")
        pi.size = len(png)
        tf.addfile(pi, io.BytesIO(png))
    out = extract_text_members(buf.getvalue())
    assert list(out) == ["paper.tex"]
    assert out["paper.tex"] == "B-L long-range source"


def test_sha256_is_deterministic():
    assert sha256(b"nm") == sha256(b"nm")
