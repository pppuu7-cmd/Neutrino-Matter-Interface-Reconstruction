import io
import tarfile

from scripts.audit_na64_b_minus_l_numerical_asset_0086b import run


def make_tar(files):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tf:
        for name, data in files.items():
            raw = data.encode() if isinstance(data, str) else data
            info = tarfile.TarInfo(name)
            info.size = len(raw)
            tf.addfile(info, io.BytesIO(raw))
    return buf.getvalue()


def test_passes_source_native_vector_asset_with_bl_limit_cl_context():
    src = make_tar({
        "main.tex": r"""
        We derive 90\% confidence-level exclusion limits for the $B-L$ scenario.
        Figure~\ref{fig:bl} shows the B-L constraint.
        \includegraphics{fig_bl}
        """,
        "fig_bl.eps": "%!PS-Adobe-3.0 EPSF-3.0\nnewpath 0 0 moveto 1 1 lineto stroke\n",
    })
    out = run(src, "fixture")
    assert out["classification"] == "PASS_NA64_B_L_NUMERICAL_ASSET_AUTHORITY"
    assert out["semantics"]["ok"] is True
    assert len(out["vector_candidates"]) == 1
    assert out["guards"]["coordinate_transform_performed"] is False


def test_blocks_when_only_raster_like_pdf_without_vector_probe():
    src = make_tar({
        "main.tex": r"""
        We derive 90\% confidence-level exclusion limits for the $B-L$ scenario.
        \includegraphics{fig_bl.pdf}
        """,
        "fig_bl.pdf": b"not-a-real-pdf",
    })
    out = run(src, "fixture")
    assert out["classification"] == "BLOCKED_NA64_B_L_RASTER_ONLY_GEOMETRY"


def test_does_not_accept_unlinked_generic_numeric_asset_without_semantics():
    src = make_tar({"main.tex": "A generic detector note.", "points.csv": "x,y\n1,2\n"})
    out = run(src, "fixture")
    assert out["classification"] == "BLOCKED_NA64_B_L_ASSET_ACCESS"
    assert out["semantics"]["ok"] is False
