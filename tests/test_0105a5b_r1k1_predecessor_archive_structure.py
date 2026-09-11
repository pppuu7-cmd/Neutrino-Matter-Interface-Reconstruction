from pathlib import Path

S=Path('scripts/audit_0105a5b_r1k1_predecessor_archive_structure.py').read_text()
P=Path('research/prereg/0105a5b_r1k1_predecessor_archive_structure_preregistration.md').read_text()

def test_exact_lock_and_candidate_rule():
    assert "EXPECTED_SHA256='d095d23daf4dc08848b7f3ff5977daaf554db966034ca9d3460e4b88d7c3790a'" in S
    assert "SUFFIXES=('.tex','.txt','.bib','.sty','.cls')" in S

def test_no_payload_read_path():
    assert '.extractfile(' not in S
    assert "'member_payload_read':False" in S
    assert "'source_text_inspected':False" in S

def test_fail_closed_identity():
    assert 'BLOCKED_0105A5B_R1K1_SOURCE_BYTE_IDENTITY_MISMATCH' in S
    assert 'PASS_0105A5B_R1K1_PREDECESSOR_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY' in S
    assert 'd095d23daf4dc08848b7f3ff5977daaf554db966034ca9d3460e4b88d7c3790a' in P
