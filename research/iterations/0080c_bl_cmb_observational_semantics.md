# NMIR Iteration 0080c — conservative current-CMB observational semantics

Date: 2026-09-07
Classification: **PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_95CL_SEMANTICS**

Prospective authority was frozen in `research/prereg/0080c_bl_cmb_observational_semantics.md`, commit `34f3413f634ae03a01a40dd76afa0388236fc6ab`, before any contour-path extraction. The pinned primary source is Esseili & Kribs, arXiv `2308.07955v2`, source archive SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`; `neff_arXiv_v2.tex` SHA256 `f77b577688b3609c574985b05fc9a213709c958ded60a511478357f1f881d678`.

The primary TeX satisfies every frozen semantics check. It states that current Planck constraints exclude roughly `Delta N_eff >= 0.3-0.4` depending on dataset; later it calls `Delta N_eff^CMB <= 0.3-0.4` at 95% C.L. a conservative analysis, says the dark- and light-blue regions are ruled out, and the green region is strongly disfavored. Figure 5 maps `0.05, 0.1, 0.2, 0.3, 0.4, 0.5` to pink, red, orange, green, light blue, dark blue; Figure 6 explicitly uses the same convention for the Dirac case.

The prospectively frozen NMIR rule therefore remains unchanged: **hard current-CMB exclusion is `Delta N_eff >= 0.4` at 95% C.L.**, represented by light-blue plus dark-blue regions only. The green `0.3 <= Delta N_eff < 0.4` region is not part of the hard excluded polygon and may only be called strongly disfavored.

The first hosted run/job `34161423753/101863884618`, artifact `10032719610`, is permanently classified **IMPLEMENTATION_INVALID_TEX_PARSER_FALSE_NEGATIVES**, not a scientific BLOCKED result. Its own raw context contained the required primary phrases, while the parser incorrectly required literal `0.3-0.4`, expanded macro spelling, and `Fig.` capitalization. The physics/semantics contract was not changed. Parser-only fix commit `60b711b8411b101b342dd91dbbc991a3bd0ded64` accepts the primary TeX punctuation/macro spelling without changing any endpoint or criterion.

Authoritative corrected hosted run/job: `34161487414/101864078212`. Dedicated tests: `3 passed in 0.04s`. Artifact `10032738989`, 2322 bytes; artifact ZIP SHA256 `bcdef158881eec04c098014acfa934fb734638271c7aea265a0da3a3dd54e726`; raw JSON SHA256 `95e1bb45150f54c3c23a9f8d3db6f49dba17102dc563de267cb56f8a77cd5bd6`. Artifact bytes were independently downloaded and hash-checked. Machine-readable result: `data/esseili_kribs_cmb_semantics_0080c.json`, commit `cb50516c2de84c1ed7cc8df1aed888a4e8930e11`.

Scientific consequence: a separately preregistered vector-geometry gate may now materialize the light-blue plus dark-blue hard-excluded regions in the Majorana and Dirac CMB panels using the already validated 0080b physical-coordinate transforms. No scenario union/intersection, BBN combination, global B-L envelope union, or BSM response/enhancement calculation is authorized by 0080c itself.
