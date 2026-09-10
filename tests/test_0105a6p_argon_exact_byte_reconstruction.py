import hashlib
from scripts.audit_0105a6p_argon_exact_byte_reconstruction import reconstruct, matches, TRANSFORMS


def identity(raw):
    return (len(raw), hashlib.md5(raw).hexdigest(), hashlib.sha256(raw).hexdigest(), "central")


def test_identity_exact_match_is_accepted():
    raw = b"abc\n"
    hit = reconstruct(raw, identity(raw))
    assert hit is not None
    assert hit[0] == "identity"
    assert hit[1] == raw


def test_missing_final_lf_can_be_cryptographically_reconstructed():
    official = b"abc\n"
    carrier = b"abc"
    hit = reconstruct(carrier, identity(official))
    assert hit is not None
    assert hit[0] == "append_LF"
    assert hit[1] == official


def test_missing_final_crlf_can_be_cryptographically_reconstructed():
    official = b"abc\r\n"
    carrier = b"abc"
    hit = reconstruct(carrier, identity(official))
    assert hit is not None
    assert hit[0] == "append_CRLF"
    assert hit[1] == official


def test_internal_whitespace_or_numeric_change_is_rejected():
    official = b"1 2 3\n"
    carrier = b"1  2 3"
    assert reconstruct(carrier, identity(official)) is None


def test_no_transform_removes_bytes():
    raw = b"abc\nextra"
    official = b"abc\n"
    assert reconstruct(raw, identity(official)) is None


def test_transform_family_is_exactly_frozen():
    assert [name for name, _ in TRANSFORMS] == ["identity", "append_LF", "append_CRLF"]
