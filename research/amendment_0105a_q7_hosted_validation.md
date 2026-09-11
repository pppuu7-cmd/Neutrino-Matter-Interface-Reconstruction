# NMIR 0105a q7 hosted-validation amendment

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: reproducibility/integrity validation of the already-preregistered q7 F7 criterion only; NONDISCOVERY.

The q7 scientific criterion was prospectively frozen at `ca909d318365dfb05b7b52c8abeacfbdd1f8bb7d` before q7 target-content inspection. The immutable scientific note at `4516909ca2d58f7e7cb541dd2e40f844f8f18f4f` records PASS, but NMIR policy requires a hosted raw-result/artifact validation before treating a green or prose result as fully validated authority.

This amendment does not change q7 criteria. The hosted validator must test exactly the four frozen q7 conditions:

1. arXiv:2003.10630v3 Table I contains Analysis-A SS/NSS `3154 +/- 25`;
2. v4 changes the same field to `3152 +/- 25`;
3. the primary arXiv version history identifies v4 as `fix typo in table 1`;
4. corrected `3152 +/- 25` persists in final/current primary authority and/or arXiv:2006.12659.

The validator must byte-hash all downloaded primary inputs, emit extracted evidence and a machine-readable result artifact, and fail closed if any frozen condition is not located. It must not inspect or execute observed BSM residuals, systematic Monte Carlo, or fit-improvement comparisons.

The hosted artifact may validate or overturn the prose q7 PASS; newest validated artifact-level state wins. No dependent scientific gate is authorized merely by workflow success.