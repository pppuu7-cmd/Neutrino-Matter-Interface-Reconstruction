from __future__ import annotations

import mpmath as mp

from scripts.g9_mesh_free_narrow_preimage_replica_0089e import (
    branch_interval,
    git_blob_sha1,
    merge_touching,
    toy_checks,
)


def test_git_blob_sha1_known_payload():
    assert git_blob_sha1(b"test\n") == "9daeafb9864cf43055ae93beb0afd6c7d144bfa4"


def test_frozen_toy_checks_pass():
    assert toy_checks() == {
        "monotone_linear": True,
        "one_turn_quadratic": True,
        "narrow_linear": True,
    }


def test_mesh_free_narrow_linear_interval():
    with mp.workdps(60):
        y = lambda x: mp.mpf("1e9") * (x - mp.mpf("0.5"))
        iv, roots = branch_interval(y, mp.mpf("0"), mp.mpf("1"), mp.mpf("1"), 7)
        assert iv is not None
        assert iv[2] == 7
        assert abs((iv[1] - iv[0]) - mp.mpf("2e-9")) < mp.mpf("1e-18")
        assert len(roots) == 3


def test_merge_touching_preserves_parent_identity():
    with mp.workdps(60):
        rows = merge_touching([
            (mp.mpf("0.1"), mp.mpf("0.2"), 0),
            (mp.mpf("0.2"), mp.mpf("0.3"), 1),
        ])
        assert len(rows) == 1
        assert rows[0][2] == [0, 1]
