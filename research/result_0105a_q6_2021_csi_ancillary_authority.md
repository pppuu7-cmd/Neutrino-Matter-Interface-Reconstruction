# NMIR 0105a q6 result — 2021 CsI ancillary authority

Preregistration commit: `a98dfd80a4db5d4b291e0d049fd1f00da9794a48`
Date adjudicated: 2026-09-11
Scope: NONDISCOVERY authority audit only.

## Sources inspected after freeze

- Official COHERENT Released Data index identifying arXiv:2110.07730 ancillary material as the full 2021 CsI CEvNS dataset.
- COHERENT Collaboration arXiv:2110.07730v2 ancillary supplementary material.
- `dataBeamOnC.txt` and `dataBeamOnAC.txt` metadata/content structure.

## Evidence

The collaboration supplement explicitly defines the 2021 CsI selected-event sample in coincidence (C) and anti-coincidence (AC) regions, provides reconstructed PE and recoil time for each event, and states that the two event files contain all data relevant for that CsI measurement. It also states the CsI selection scope (`PE < 250`, `0 <= t_rec < 12 us`) and distinguishes the cross-section region from the additional light-dark-matter region.

This is strong primary evidence for the *CsI 2021 analysis*, but it is not the CENNS-10 liquid-argon Analysis-A authority targeted by NMIR 0105a F1/F7. It does not define the LAr elementary count law and does not establish the semantic role or precedence of LAr `3152` versus `3154`.

## Fail-closed adjudication

F1: `BLOCKED_0105A_Q6_F1_PRIMARY_SEMANTICS_SCOPE_MISMATCH`

F7: `BLOCKED_0105A_Q6_F7_PRIMARY_3152_3154_SEMANTICS_SCOPE_MISMATCH`

No transfer of CsI counting conventions to LAr is permitted. No discovery-readiness uplift follows from q6.
