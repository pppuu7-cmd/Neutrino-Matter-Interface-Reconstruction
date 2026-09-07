# NMIR preregistration 0064 — G8 target-specific thermal-solar anti-nu_e RIOEC provenance feasibility

Date frozen: 2026-09-07
Status at freeze: PROSPECTIVE / NO RESULT-DEPENDENT CLASSIFICATION INSPECTED
Parent authority: iteration 0063 and reconciled `research/RECOVERY.md` / `research/NMIR_FUNNEL.md` identify G8/F2-F4 provenance feasibility as the highest-value OPEN gate.

## Scientific question
Can NMIR independently freeze both prerequisites required for a target-specific Standard-Model RIOEC fold without importing chat-carried numbers, ordinary solar `nu_e` flux, guessed resonance area, or post-hoc matrix elements?

Required prerequisites:
1. a physical thermal-solar electron-antineutrino spectral density `dPhi_anti_nue/dE` in the relevant eV-keV window, with recoverable primary provenance and normalization;
2. at least one target-specific RIOEC entrance-strength package containing enough independently evaluated nuclear/atomic information to determine the resonance energy and integrated entrance strength/width: target identity, parent/daughter states, `Q_epsilon` (or equivalent mass difference), daughter excitation `E_x`, captured-shell binding energy `E_b`, physical width(s), and a weak matrix-element/ft/B(GT)/equivalent normalization that fixes the entrance strength rather than assuming it.

## Funnel scope
- F0 objective: passive Standard-Model interaction/detection rate; any daughter or detector release energy is excluded from neutrino-supplied power.
- F1 channel: resonant inverse orbital electron capture (RIOEC), `anti-nu_e + [e^- + (Z,A)] -> (Z-1,A)^*`.
- F2 crossing/production: entrance strength must be tied to independently known EC/beta weak data or an explicit evaluated calculation.
- F3 kinematics/source overlap: ordinary pp-chain/CNO/B8 solar `nu_e` flux is forbidden; only a physical `anti-nu_e` source spectrum may be used.
- F4 microscopic strength: no guessed Breit-Wigner area or unit-strength normalization.
- F5-F7 W/kg/event ranking is forbidden until this provenance gate passes.

## Evidence inclusion criteria
A source-spectrum authority qualifies only if it provides enough information to recover a normalized Earth-arriving thermal-solar `anti-nu_e` spectrum (analytic expression, table, machine-readable data, or fully specified model) and clearly identifies the production process and flavor/particle identity.

A target authority qualifies only if it provides enough independent quantities to reconstruct the target-specific resonance and entrance strength. Candidate lists that report only a kinematic match, Q value, or nominal resonance energy do not pass F4.

Primary papers, evaluated nuclear-data resources, official atomic-data resources, and machine-readable supplements are preferred. Secondary compilations may be used only as navigation and must not be the sole quantitative authority.

## Prospective classifications
1. `PASS_G8_RIOEC_PROVENANCE_READY`
   - both a normalized physical thermal-solar `anti-nu_e` spectrum and at least one independently strength-calibrated target package are recoverably frozen.
   - next action: preregister the target-specific spectral fold and W/kg/events/kg/s calculation.

2. `BLOCKED_SOURCE_SPECTRUM`
   - no recoverable normalized physical thermal-solar `anti-nu_e` spectrum satisfying the criteria is available.

3. `BLOCKED_ENTRANCE_STRENGTH`
   - a usable source spectrum exists, but no audited target candidate has independently sufficient entrance-strength/width information.

4. `BLOCKED_SOURCE_OR_ENTRANCE_STRENGTH`
   - both sides remain insufficient or at least one side is insufficient and the other cannot be established strongly enough to justify a numerical fold.

5. `FAIL_CHANNEL_IDENTITY`
   - a proposed source is actually `nu_e` rather than `anti-nu_e`, or the cited target process does not match the required crossed channel.

## Mandatory guards
- Never substitute ordinary solar `nu_e` flux for `anti-nu_e`.
- Never infer `anti-nu_e` from standard flavor oscillation; flavor oscillation does not perform particle-antiparticle conversion in the standard propagation problem.
- Never assign a resonance area from linewidth alone.
- Never multiply a candidate kinematic resonance by the total source flux; use only the physical spectral density at/through the resonance after a later fold.
- Never treat a theoretical candidate list as independently evaluated entrance strength unless the weak normalization is explicitly supplied and recoverable.
- If evaluated data are incomplete, classify BLOCKED rather than estimate missing matrix elements from convenience.

## Reproducibility/provenance output
Freeze a machine-readable ledger in `data/g8_rioec_provenance_authority_0064.json` with source/target records, DOI/arXiv/official-database identifiers, exact supplied quantities, missing quantities, channel identity, and inclusion/exclusion reason. Preserve immutable result in `research/iterations/0064_g8_rioec_provenance_feasibility.md` and reconcile `RECOVERY.md` / `NMIR_FUNNEL.md`.

## Scientific vs infrastructure failure
Unavailable webpage/API access, malformed downloads, or repository-write failure is infrastructure failure and does not change scientific classification. Absence of a required physical quantity after an adequate primary-authority audit is a scientific provenance blocker.
