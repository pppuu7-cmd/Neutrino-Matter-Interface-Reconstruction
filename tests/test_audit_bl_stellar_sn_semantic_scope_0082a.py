import io
import tarfile

from scripts.audit_bl_stellar_sn_semantic_scope_0082a import (
    parse_figures,
    parameter_convention,
    shin_revision,
)


def test_same_environment_caption_selects_constraint_not_hint():
    text = r'''
We study the U(1)_{B-L} constraint from SN1987A.
\begin{figure}
\includegraphics{constraint}
\caption{Constraints on the U(1)_{B-L} gauge boson from SN1987A.}
\label{fig:c}
\end{figure}

\begin{figure}
\includegraphics{hint}
\caption{A possible B-L hint region.}
\label{fig:h}
\end{figure}
'''
    figs = parse_figures(text, ["constraint.pdf", "hint.pdf"])
    assert figs[0]["accepted_bl_constraint_figure"] is True
    assert "SN1987A" in figs[0]["scope_tags"]
    assert figs[0]["resolved_assets"]["constraint"] == ["constraint.pdf"]
    assert figs[1]["accepted_bl_constraint_figure"] is False


def test_adjacent_text_can_supply_bl_identity_but_filename_cannot():
    text = r'''
For the U(1)_{B-L} model we derive the following exclusion bound for a young neutron star.
\begin{figure}
\includegraphics{generic_name}
\caption{The resulting constraint.}
\end{figure}
'''
    figs = parse_figures(text, ["generic_name.pdf"])
    assert figs[0]["accepted_bl_constraint_figure"] is True
    assert "young_neutron_star_cooling" in figs[0]["scope_tags"]


def test_parameter_convention_requires_coupling_and_mass():
    text = r"The B-L gauge coupling is $g_{B-L}$. The gauge boson mass $m_{Z'}$ is quoted in MeV."
    r = parameter_convention(text)
    assert r["passed"] is True
    assert "MeV" in r["unit_tokens"]
    bad = parameter_convention(r"We discuss a B-L gauge coupling $g_{B-L}$ only.")
    assert bad["passed"] is False


def test_shin_revision_is_scope_limited():
    text = r'''
For the U(1)_{B-L} gauge boson we revisit the previous SN1987A constraint.
The transverse contribution gives a stronger bound, and a new longitudinal excluded region appears.
We compare separately with NS1987A and Cas A cooling constraints.
'''
    r = shin_revision(text)
    assert r["revised_sn1987a_transverse"] is True
    assert r["new_sn1987a_longitudinal_region"] is True
    assert r["explicit_replace_ns1987a"] is False
    assert r["explicit_replace_cas_a"] is False
    assert r["explicit_replace_young_ns"] is False


def test_explicit_ns_replacement_is_detected_only_when_stated():
    text = r'''
In the U(1)_{B-L} model we revisit SN1987A; transverse and longitudinal bounds are improved.
We also revise the NS1987A constraint using the new emissivity.
'''
    r = shin_revision(text)
    assert r["explicit_replace_ns1987a"] is True
