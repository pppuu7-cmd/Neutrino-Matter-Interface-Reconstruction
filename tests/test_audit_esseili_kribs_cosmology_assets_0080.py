from scripts.audit_esseili_kribs_cosmology_assets_0080 import resolve_graphic, sha256


def test_sha256_stable():
    assert sha256(b"NMIR-0080") == "28f67ae4fbf0ae0a8ea99229bd6b9df17793b151291a04c505111cd9b380243c"


def test_resolve_extensionless_unique_pdf():
    names = ["figures/foo.pdf", "other/bar.png"]
    assert resolve_graphic("figures/foo", names) == ["figures/foo.pdf"]


def test_resolve_by_unique_basename_only():
    names = ["paper/figs/cmb.pdf", "paper/other.dat"]
    assert resolve_graphic("figs/cmb", names) == ["paper/figs/cmb.pdf"]


def test_ambiguous_basename_fails_closed():
    names = ["a/cmb.pdf", "b/cmb.pdf"]
    assert resolve_graphic("cmb", names) == []
