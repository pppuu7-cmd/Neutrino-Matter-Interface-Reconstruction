from scripts.audit_esseili_kribs_cmb_semantics_0080c import classify_text, norm


def synthetic_source():
    return r'''
    \caption{Calculations of $\Delta N_{\rm eff}$ for the ``Majorana'' neutrino case. The regions correspond to $\Delta N_{\rm eff}=0.05$ (pink), $0.1$ (red), $0.2$ (orange), $0.3$ (green), $0.4$ (light blue), and $0.5$ (dark blue). Current constraints from Planck data exclude $\Delta N_{\rm eff}\gtrsim 0.3-0.4$ (depending on the choice of dataset).}
    \caption{Same as Fig.~\ref{fig:majoranaNeff}, but for the ``Dirac'' neutrino case. As before, the regions correspond to the same values and colors.}
    Comparing these observations to our results, a conservative analysis suggests $\Delta N_{\rm eff}\lesssim 0.3-0.4$ to 95\% C.L., and hence the regions labeled dark and light blue are ruled out, with the green region strongly disfavored.
    '''


def test_synthetic_primary_semantics_pass():
    r=classify_text(synthetic_source())
    assert r["classification"] == "PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_95CL_SEMANTICS"
    assert r["frozen_nmir_semantics"]["hard_exclusion_delta_neff_min"] == 0.4


def test_missing_ruled_out_phrase_blocks():
    t=synthetic_source().replace("dark and light blue are ruled out", "colors are discussed")
    r=classify_text(t)
    assert r["classification"] == "BLOCKED_COSMOLOGY_B_L_CMB_OBSERVATIONAL_SEMANTICS"


def test_norm_whitespace_only():
    assert norm("a\n  b\t c") == "a b c"
