# 0105a5b R1d stage 1 — external computational authority evidence bundle

Date: 2026-09-10
Scope: NMIR v2 only. NMIR v1 remains frozen.

## Classification

`R1D_STAGE1_EVIDENCE_COMPLETE_UNCLASSIFIED_GATE`

This stage is not an R1d PASS, BLOCKED or structural FAIL. It is an authority-evidence acquisition step under the prospectively frozen R1d gate. No oscillated expectation, likelihood, nuisance fit, observed-minus-null residual, BSM quantity or significance was computed.

## Hosted provenance

Workflow/head: `e2cf9ad198d0841c062586527b27436c0f5d9ae3`.
Run/job: `34451616410/102788411481`.
Artifact: `10141761649`, `deepcore-0105a5b-r1d-external-authority-evidence`.
Provider artifact digest and independently downloaded ZIP SHA256: `b53a238bc72107f74a1e8a9480f629fc5d73976707539e3e904412f3057d13b0`.
Inner `r1d_result.json` SHA256: `b0ad5613a262d41d2a5c262e9831b94a824552c7db3d769f727516724ad38404`.
Dedicated tests: `3 passed`.

Locked source hashes:
- B4RITM `example.ipynb` SHA256: `900acac6e74cced45e0b894017340b7aa0a64ccb615365b865cc7b4ae87be1a3` (provider MD5 `fd9ac548e6a6f136efb6c61058cc822f`);
- B4RITM `readme.md` SHA256: `0f8e7bbc6059d18376843370e36e98a0cfa69fbc4bd767df694c6d65f861149f`;
- exact arXiv source archive for IceCube analysis `2304.12236` SHA256: `111c41e49dd50880bc6b00aca95a2479216622b47235fcb68e2a02e22456a149`;
- extracted `main.tex` SHA256: `2c25f03bfadc482a81a8f490efd15df3481988485630f92a255bb3f3c4c3708e`;
- extracted bibliography SHA256: `0055d6eb0585c44f2074b8f29712c38e1c645154d88830074fb7bff37b00e20c`.

## Authority recovered

The IceCube publication explicitly states that atmospheric hadronic-yield variations are computed with MCEq, following Barr et al., by perturbing hadron-yield model parameters and propagating derivatives of the lepton flux. It specifies that the modifications used Sibyll2.3c and the GSF cosmic-ray flux as the starting point. It also states that the six fit-relevant hadronic parameters are selected from the larger Barr-region construction, with low-energy pion regions grouped where degenerate.

The exact bibliography pins the upstream Barr authority as Barr, Gaisser, Robbins & Stanev, Phys. Rev. D 74, 094009 (2006), arXiv:astro-ph/0611266, and the MCEq/Sibyll authority as Fedynitch et al., Phys. Rev. D 100, 103018 (2019), arXiv:1806.04140.

For DIS-CSMS, the publication gives substantial semantics: GENIE/GRV98 is the nominal model; CSMS is the alternative; the largest model difference was parameterized in energy and inelasticity as one event reweighting nuisance; below 100 GeV the correction derived at 100 GeV is held fixed to avoid a discontinuity; nuisance value 0 corresponds to GENIE and 1 approximates CSMS, with prior centered at 0 and width 1.0. The exact bibliography pins CSMS to Cooper-Sarkar, Mertsch & Sarkar, JHEP 08 (2011) 042, arXiv:1106.3723.

## What remains unresolved

The stage-1 literal search does not recover the release-internal column names `BarrWP`, `BarrWM`, `BarrYP`, `BarrYM`, `BarrZP`, `BarrZM` verbatim from the README/notebook/publication source. That absence is not yet a R1d BLOCKED verdict because the frozen authority order explicitly allows the original upstream Barr/MCEq authority cited by IceCube. The next step must inspect those exact upstream authorities and establish the mapping between IceCube's six released nuisance columns and the Barr-region/charge definitions, together with reproducible software/model provenance.

DIS-CSMS semantics are much closer to complete, but the exact executable event-reweighting function must still be pinned from an explicitly cited original authority/release-native implementation before R1d PASS can be declared.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`.
