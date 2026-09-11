import importlib.util
import json
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_0105a6q5a_argon_official_release_provenance_inventory.py"
spec = importlib.util.spec_from_file_location("q5a", SCRIPT)
q5a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q5a)


def test_terminal_precedence_and_pass():
    assert q5a.classify(True, True, True, True, True) == q5a.CLASS_PASS
    assert q5a.classify(False, False, False, False, False) == q5a.CLASS_LOCAL
    assert q5a.classify(True, False, False, False, False) == q5a.CLASS_TRANSPORT
    assert q5a.classify(True, True, False, False, False) == q5a.CLASS_ORNL
    assert q5a.classify(True, True, True, False, False) == q5a.CLASS_ZENODO
    assert q5a.classify(True, True, True, True, False) == q5a.CLASS_ARXIV


def test_ornl_exact_route_predicate():
    html = b'<html><a href="https://zenodo.org/records/3903810?x=1">Data release from CEvNS on argon</a></html>'
    out = q5a.inspect_ornl(html)
    assert out["pass"] is True
    assert out["matching_anchor_count"] == 1
    bad = q5a.inspect_ornl(b'<a href="https://zenodo.org/records/999">Data release on argon</a>')
    assert bad["pass"] is False


def test_zenodo_metadata_only_predicate():
    payload = json.dumps({
        "id": 3903810,
        "doi": "10.5281/zenodo.3903810",
        "metadata": {"version": "1.0", "title": q5a.EXPECTED_TITLE},
        "files": [{"key": f"f{i}", "size": i + 1, "checksum": "md5:x"} for i in range(24)],
    }).encode()
    out = q5a.inspect_zenodo(payload)
    assert out["pass"] is True
    assert out["file_count"] == 24
    assert len(out["files"]) == 24


def test_zenodo_file_count_is_frozen():
    payload = json.dumps({
        "id": 3903810,
        "doi": "10.5281/zenodo.3903810",
        "metadata": {"version": "1.0", "title": q5a.EXPECTED_TITLE},
        "files": [],
    }).encode()
    assert q5a.inspect_zenodo(payload)["pass"] is False


def test_arxiv_head_only_metadata_predicate():
    html = f'''<html><head>
    <meta name="citation_title" content="{q5a.EXPECTED_TITLE}">
    <meta name="citation_arxiv_id" content="2006.12659">
    <link rel="canonical" href="https://arxiv.org/abs/2006.12659">
    </head><body>UNINSPECTED SCIENTIFIC BODY</body></html>'''.encode()
    out = q5a.inspect_arxiv(html)
    assert out["pass"] is True
    assert out["id_match"] is True
    assert out["title_match"] is True


def test_local_binding_requires_every_frozen_token(tmp_path):
    good = '''Classification: `PASS_0105A3_COHERENT_ZENODO_DIRECT_BYTE_LOCK_NONTERMINAL`
implementation/execution SHA: `6ab2b940be4431c6fd7cad8048e10764a88eb086`
workflow run: `34418207408`
successful run attempt: `3`
job: `102834981270`
uploaded artifact: `10147580844`, `nmir-v2-0105a3-coherent-byte-lock`
artifact ZIP SHA256 reported by GitHub Actions: `b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4`
Ar Zenodo record: `3903810`, DOI `10.5281/zenodo.3903810`, frozen version `1.0`, 24 files
total frozen file count: 37
normalized byte-manifest SHA256: `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`
CsI: 13/13 files
Ar: 24/24 files
all_provider_md5_match = true
all_sha256_recorded = true
'''
    p = tmp_path / "authority.md"
    p.write_text(good, encoding="utf-8")
    assert q5a.check_local(p)["pass"] is True
    p.write_text(good.replace("24/24", "23/24", 1), encoding="utf-8")
    assert q5a.check_local(p)["pass"] is False


def test_redirect_provider_boundaries():
    assert q5a.RedirectRecorder._same_provider("ornl", "coherent.ornl.gov")
    assert q5a.RedirectRecorder._same_provider("zenodo", "zenodo.org")
    assert q5a.RedirectRecorder._same_provider("arxiv", "export.arxiv.org")
    assert not q5a.RedirectRecorder._same_provider("ornl", "zenodo.org")
    assert not q5a.RedirectRecorder._same_provider("zenodo", "doi.org")
