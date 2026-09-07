import hashlib
import pytest

pymupdf = pytest.importorskip("pymupdf")
from scripts.audit_esseili_kribs_vector_integrity_0080a import sha256, inspect_pdf


def test_sha256_fixture():
    assert sha256(b"NMIR-0080a") == "8078a2d6adcfbd81e44d5130e52437a34cbf999094ee02a23378f1d088b8c2c9"


def test_generated_vector_pdf_passes():
    doc = pymupdf.open()
    page = doc.new_page(width=200, height=100)
    page.draw_line((10, 10), (190, 90))
    page.insert_text((20, 50), "10^-3 gX")
    raw = doc.tobytes()
    r = inspect_pdf(raw, "synthetic.pdf")
    assert r["integrity_pass"] is True
    assert r["image_xobject_count"] == 0
    assert r["drawing_count"] > 0
    assert r["path_item_count"] > 0
    assert r["word_count"] > 0


def test_raster_backed_pdf_fails_vector_native():
    doc = pymupdf.open()
    page = doc.new_page(width=100, height=100)
    pix = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, 2, 2), False)
    pix.clear_with(255)
    page.insert_image(pymupdf.Rect(0, 0, 100, 100), pixmap=pix)
    raw = doc.tobytes()
    r = inspect_pdf(raw, "raster.pdf")
    assert r["image_xobject_count"] > 0
    assert r["vector_native_pass"] is False
