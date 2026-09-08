# NMIR iteration 0089 — G9 frozen-discrete-map exact derivative authority

Date: 2026-09-08

## Classification

`PASS_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY`

0089 authorizes an exact derivative evaluator for the **actual frozen trapezoidal projected-mass map** on every open Model-S radial-knot interval. It does not itself authorize turning roots, a monotone partition, multiimage areas, a G9 kernel, persistent-source convolution, or BSM work.

## Prospective authority
- prereg: `research/prereg/0089_g9_frozen_discrete_map_derivative_authority.md`
- frozen prereg commit: `b64dd44f483e1753ebbcbb60e3f68f06a21f7ad5`
- prereg SHA256 in authoritative artifact: `4f14154cabd97151a38dffd3467db9b50ee7865e7a8c3825299031717dee5579`

0089 was frozen after 0088 closed terminally and before any Model-S derivative values/signs/roots were inspected.

## Hosted authority
- workflow: `.github/workflows/0089-g9-frozen-discrete-map-derivative-authority.yml`
- head SHA: `aeb51b1499597a75fdf749f38c715ecd2746a15d`
- run: `34204310210`
- job: `101990111998`
- workflow conclusion: `success`
- artifact: `10047184672`
- artifact ZIP SHA256: `2093b05093c81de00d464d7b5b55efe20be4d33ae056c52482ad92406b408a56`
- raw `g9_0089_derivative_authority.json` SHA256: `4093c574c83ee0c2ef4d2f0043a579558af1b008e66324880bc8cf35f259dc2c`
- dedicated tests: PASS

Pinned authority bytes matched exactly:
- Model-S git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- frozen `gravity_extended.py` git blob SHA1 `f8d48fb4eae87ff9c1f98ef543dae27c5f359e9c`.

## V1 — finite-sum identity over every Model-S interval
Parsed Model-S:
- knots: `2402`;
- open radial-knot intervals: `2401`.

The three preregistered points q=`1/4,1/2,3/4` were checked in **every** interval:
- point count: `7203`;
- maximum symmetric relative mass discrepancy: `1.0515670787751558e-14`;
- frozen threshold: `5e-13`;
- PASS.

Worst V1 point:
- interval `358`;
- q=`0.75`;
- x=`0.088995625`;
- finite-sum mass `3.0835804934894205e32 g`;
- authoritative map mass `3.083580493489453e32 g`.

Thus the dimensionless finite-sum representation used for the derivative is numerically identical to the frozen authoritative map far inside the preregistered tolerance.

## V2 — independent 80-digit derivative reference
The preregistered deterministic stratification selected exactly `64` intervals spanning the ordered profile, including edge/control neighborhoods. At q=`1/4,1/2,3/4`:
- derivative-reference points: `192`;
- max h vs h/2 80-digit five-point replica discrepancy: `1.977759571654202e-11`;
- max analytic vs h/2 high-precision reference discrepancy: `7.473825379514015e-12`;
- frozen threshold for each: `1e-8`;
- PASS.

Worst analytic/reference point:
- interval `2400`;
- q=`0.75`;
- x=`0.999999125`;
- analytic derivative `8.398417830852664e23 g/x`;
- 80-digit reference `8.398417830789895e23 g/x`;
- symmetric relative error `7.473825379514015e-12`.

The worst reference-replica point was interval `2399`, q=`0.75`, x=`0.99999565`, with discrepancy `1.977759571654202e-11`.

## V3 — preregistered toy profiles
All three passed:
- constant density;
- monotone linear density `(4,3,2,1)`;
- non-monotone positive density `(1,3,2,4)`.

Their maximum analytic/reference derivative discrepancies were all below `1.64e-12`; mass identities were at ~`1e-16` scale.

## V4 — piece-boundary integrity
- positive fixed knots checked: `2401`;
- failures: `0`;
- exact interior knots were rejected as derivative points as preregistered;
- authoritative mass remained finite/positive.

This preserves the critical fact that the frozen trapezoidal map can be non-smooth at source knots; 0089 does not invent a derivative through them.

## New methodological conclusion
0088's continuous-quadrature locator and the actual frozen map are now cleanly separated. 0089 shows that the frozen map itself admits an exact piecewise algebraic derivative, with no adaptive/composite quadrature and no result-selected grid.

This removes the specific 0088 Simpson-convergence failure mechanism from the next G9 root-certification attempt. It does **not** guarantee root certification: radial knots are genuine piece boundaries of the discrete algorithm, and roots/sign changes must still be prospectively audited without smoothing or post-hoc node insertion.

## Next gate
A separately preregistered 0089a may now use the exact 0089 derivative to certify turning structure piece-by-piece, treating all 2401 open Model-S radial intervals as source-fixed pieces and all exact knots as fixed boundaries. No root positions/sign results may be inspected before the 0089a acceptance contract is frozen.
