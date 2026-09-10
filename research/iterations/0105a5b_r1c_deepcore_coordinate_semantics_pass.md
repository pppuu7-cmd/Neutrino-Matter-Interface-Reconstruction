# 0105a5b R1c — DeepCore coordinate-semantics authority PASS

Date: 2026-09-10
Scope: NMIR v2 only. NMIR v1 remains frozen at `NMIR_READINESS: 100%`.

## Classification

`PASS_0105A5B_R1C_COORDINATE_SEMANTICS_AUTHORITY_NONDISCOVERY`

This is a NONDISCOVERY authority/reproduction-path result. It authorizes no observed residual, BSM fit, significance calculation, or likelihood reproduction by itself.

## Prospective chain

Parent preregistration: `research/prereg/0105a5b_r1c_deepcore_coordinate_semantics_preregistration.md`, frozen commit `a82b411ab55ee31479af5974bdd8b420ca0b3458`.

The first repaired hosted authority-evidence execution at head `02e7057e15b9362d6155584060a97f0b2a7fca0e`, run/job `34446592643/102772608169`, artifact `10139878085`, recovered the exact B4RITM v1.0 README statement that reconstructed variables are provided in the analysis binning such that events fall into the midpoint of their bin, together with the exact energy/coszen/PID bin boundaries and the explicit statement that MC reconstructed variables follow the same convention as `data.csv`.

Evidence artifact provider/independent ZIP SHA256: `c4e9450e772f07ca3c18a3ffb5db0f4ae972b00592ee032f501a61b4a8cc203a`. Inner `r1c_result.json` SHA256: `2fcd8103d25a4a53cc2cbf64539a8710242d33d6f58e2ba9ae402039d7b4a08f`.

Before any mapping execution, amendment `research/prereg/0105a5b_r1c_amendment_01_authority_derived_bin_index_mapping.md` was frozen at commit `1da3021dbcf5d9372012e8c392910d8830873c4a`. It fixed the deterministic mapping as strict interior containment in the authority-published bin boundaries, independently on `pid`, `reco_coszen`, and `reco_energy`, with no tolerance, nearest-neighbour rule, clipping, rounding repair, or residual-dependent choice.

Implementation commit: `563b96c74f983c4adad61a8f5df9f3643a3aeeec`.
Dedicated tests commit: `59a5c46f6a366df5a74886418f1a130ca5ce91a2`.
Hosted workflow/head: `aba34f036b8ded092aec19ac24b1b8690de9a9c2`.

## Authoritative hosted result

Run/job: `34451303840/102787437641`.
Artifact: `10141644643`, `deepcore-0105a5b-r1c-authority-bin-mapping`.
Provider artifact digest and independently downloaded ZIP SHA256: `4e0e7ca4bd9edce950cb8890cc58cca8bdf99624b9993780c83ac3b16e86ef6a`.
Inner `r1c_mapping_result.json` SHA256: `3391f2319a3876f16fb63cc45865c7f2c952658953b13853b4fa950f5626fd0f`.
Dedicated tests: `3 passed`.

Exact byte locks used by the hosted mapping include:
- `data.csv`: `68bdc3db7404d497a0c439fb2d95ab0b7ed9942ac4ed6dde236e761413360cfd`;
- `mc_nu_nc.csv`: `aab94b5e0e285135471d5eb7b27db3f818f40c423ed95f27af6d3ba06becf355`;
- `mc_nue_cc.csv`: `a968f274726dc4b316c6eb9d93901dacda13dc92528d1081887fd473a958cf8b`;
- `mc_numu_cc.csv`: `a3bc53223d8e6f9b9e43e36d277550976631315f5a00771dff2c588120410724`;
- `mc_nutau_cc.csv`: `7e8596016ae4a9fca8e2d805c132f3b89ac9a6eacfb1ea828a7347f6c0184f07`;
- `readme.md`: `0f8e7bbc6059d18376843370e36e98a0cfa69fbc4bd767df694c6d65f861149f`.

## Structural result

The hosted result reproduced all frozen invariants:
- 200 observed rows;
- 200 unique observed coordinate tuples;
- 200 unique native-MC reconstructed-coordinate tuples;
- 200 unique observed authority-bin keys;
- 200 unique MC authority-bin keys;
- exact equality of the two 200-cell key sets;
- exact `2 x 10 x 10` support on both sides.

The important R1b discrepancy is resolved semantically without rounding repair: observed PID labels are `[0.65, 0.88]`, MC PID labels are `[0.65, 0.875]`, but both `0.88` and `0.875` lie strictly inside the authority-published upper PID interval `(0.75, 1.0)` and therefore map to the same bin index under the prospectively frozen rule.

## Guards retained

The six Barr/MCEq nuisance directions (`BarrWP`, `BarrWM`, `BarrYP`, `BarrYM`, `BarrZP`, `BarrZM`) plus `DIS-CSMS` remain unresolved external-computational authorities. R1c PASS therefore does not yet authorize the standalone standard-3nu likelihood reproduction.

No oscillated expectation, likelihood, nuisance fit, observed-minus-null residual, BSM quantity, or significance was computed in R1c.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`.
