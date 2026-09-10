import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_0105a6q4f_suh_2025_institutional_authority_manifest.py"
spec = importlib.util.spec_from_file_location("q4f", SCRIPT)
q4f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q4f)


def test_frozen_identity_constants():
    assert q4f.PREREG_COMMIT == "309aa7d389b541fb6818a56aec67f44cee65f50d"
    assert q4f.CEEM_URL == "https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html"
    assert q4f.YEAR == "2025"
    assert "CENNS-10 LAR DETECTOR" in q4f.TITLE


def test_official_iu_host_guard():
    assert q4f.official_iu("https://scholarworks.iu.edu/dspace/items/abc")
    assert q4f.official_iu("https://ceem.indiana.edu/x")
    assert not q4f.official_iu("https://example.com/x")
    assert not q4f.official_iu("https://iu.edu.example.com/x")


def test_discovery_only_accepts_official_item_urls():
    html = '''
      <a href="https://scholarworks.iu.edu/dspace/items/ae71e100-a414-4756-bf9e-be4808f675e5">ok</a>
      <a href="https://example.com/dspace/items/ae71e100-a414-4756-bf9e-be4808f675e5">bad</a>
      <a href="/dspace/items/11111111-2222-3333-4444-555555555555?x=1">relative</a>
    '''
    got = q4f.discover_item_urls(html, "https://scholarworks.iu.edu/dspace/discover")
    assert got == [
        "https://scholarworks.iu.edu/dspace/items/ae71e100-a414-4756-bf9e-be4808f675e5",
        "https://scholarworks.iu.edu/dspace/items/11111111-2222-3333-4444-555555555555",
    ]


def test_metadata_match_is_literal_not_semantic():
    good = f"Benjamin D Suh 2025 {q4f.TITLE}"
    assert q4f.exact_title_present(good)
    assert q4f.author_present(good)
    assert not q4f.exact_title_present("A related CENNS-10 analysis")
