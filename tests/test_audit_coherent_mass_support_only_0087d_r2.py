import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_coherent_mass_support_only_0087d_r2 as m


def test_exact_bl_token_variants_accept():
    for text in [
        "B-L model",
        "$B-L$ model",
        r"$B\!-\!L$ model",
        r"$B\! - \!L$ model",
        "B − L model",
    ]:
        assert m.bl_context_r2(text), text


def test_generic_b_l_adjacency_rejected():
    for text in [
        "Universal B model limits and L_mu-L_tau comparison",
        "B coupling plotted with L constraints",
        "background BLEND rate",
        "B L model",
        "B, L observables",
    ]:
        assert not m.bl_context_r2(text), text


def test_figure_candidates_keep_only_semantic_bl_figure():
    tex = [("main.tex", r'''
\begin{figure}
\includegraphics{rate.pdf}
\caption{Expected event rate for universal vector model.}
\end{figure}
\begin{figure}
\includegraphics{universal.pdf}
\caption{Excluded regions in the mediator mass plane for a universal model with B and L observables.}
\end{figure}
\begin{figure*}
\includegraphics*[width=.7\linewidth]{Coherent_Results_B-L.pdf}
\includegraphics{Comparison_B-L.pdf}
\caption{Excluded regions in the $M_{Z'}-g_{Z'}$ plane for the $B\! - \!L$ model.}
\end{figure*}
\begin{figure}
\includegraphics{lmutau.pdf}
\caption{Excluded regions in the mediator mass plane for the L_mu-L_tau model.}
\end{figure}
''')]
    members = {
        "rate.pdf": b"x",
        "universal.pdf": b"x",
        "Coherent_Results_B-L.pdf": b"x",
        "Comparison_B-L.pdf": b"x",
        "lmutau.pdf": b"x",
    }
    r = m.r1.figure_candidates_r1(tex, members)
    assert [x["resolved"] for x in r] == [
        "Coherent_Results_B-L.pdf",
        "Comparison_B-L.pdf",
    ]
