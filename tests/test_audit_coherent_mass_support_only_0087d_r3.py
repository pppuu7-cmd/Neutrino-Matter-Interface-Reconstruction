import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_coherent_mass_support_only_0087d_r3 as m


def test_constraint_mass_plane_semantics():
    assert m.constraint_mass_plane_context("Excluded regions in the M_{Z'}-g_{Z'} plane for the B-L model")
    assert m.constraint_mass_plane_context("constraints on coupling g_{Z'} versus mediator mass M_{Z'}")
    assert not m.constraint_mass_plane_context("Differential event rates for B-L with M_{Z'}=10 MeV and coupling g_{Z'}")
    assert not m.constraint_mass_plane_context("Binned recoil spectrum for the B-L benchmark M_{Z'}=10 MeV")


def test_mixed_figures_keep_constraint_only():
    tex=[("main.tex", r'''
\begin{figure}
\includegraphics{rate.pdf}
\caption{Differential predicted event rates for the $B-L$ model with $M_{Z'}=10$ MeV and coupling $g_{Z'}$.}
\end{figure}
\begin{figure*}
\includegraphics*[width=.7\linewidth]{Coherent_Results_B-L.pdf}
\includegraphics{Comparison_B-L.pdf}
\caption{Excluded regions in the $M_{Z'}-g_{Z'}$ plane for the $B\!-\!L$ model at 90\% C.L.}
\end{figure*}
''')]
    members={"rate.pdf":b"x","Coherent_Results_B-L.pdf":b"x","Comparison_B-L.pdf":b"x"}
    got=m.figure_candidates_r3(tex,members)
    assert [x["resolved"] for x in got] == ["Coherent_Results_B-L.pdf","Comparison_B-L.pdf"]
