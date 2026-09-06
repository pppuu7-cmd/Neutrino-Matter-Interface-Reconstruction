# NMIR preregistration — resonant induced orbital electron capture source-class gate

Date: 2026-09-06
Gate: G8 / F0-F6 source, flavor and integrated-area classification before target ranking

## Motivation
The highest-value OPEN passive-SM survivor is a genuine target-specific resonance. A new 2026 proposal by Akhmedov, Lasserre and Maturi (arXiv:2608.25001) makes the relevant channel explicit: resonant induced orbital electron capture (RIOEC)

`anti-nu_e + [e^- + (Z,A)] -> (Z-1,A)*`.

Because the final atomic+nuclear state is one body, the entrance is resonant. For a continuous source the useful rate is controlled by the integrated resonance strength times the source spectral intensity at the resonance, not by the peak cross section alone.

Primary source: https://arxiv.org/abs/2608.25001
Historical source: Kells & Schiffer, Phys. Rev. C 28, 2162 (1983), DOI 10.1103/PhysRevC.28.2162.
Thermal solar source authority to be matched in the next target-specific step: Haxton & Lin, Phys. Lett. B 486, 263-271 (2000), DOI 10.1016/S0370-2693(00)00764-4.

## Frozen prospective questions
1. **Flavor gate:** ordinary pp-chain/CNO/B16 solar production is `nu_e`, whereas RIOEC requires incident `anti-nu_e`. Standard flavor oscillations do not turn neutrinos into antineutrinos. Therefore the B16 thermonuclear source contribution to RIOEC must be exactly zero in the SM accounting used by NMIR.
2. **Source-class separation:** thermal solar pair processes can produce neutrinos and antineutrinos and therefore form a distinct allowed source class. They must not inherit the B16 flux normalization or line strengths.
3. **Integrated-area gate:** for a normalized Lorentzian resonance `L(E;E_R,Gamma)`, `sigma(E)=B0 L`, the area is `integral sigma dE = B0`; narrowing `Gamma` cannot increase this area.
4. **Continuous-profile gate:** if the source spectral density varies slowly across the resonance, `integral phi(E) sigma(E)dE -> B0 phi(E_R)` as `Gamma/source_scale -> 0`.
5. **No gain multiplication:** no RIOEC resonance gain may be multiplied by B16 capture, focusing, structured-column or many-body gains unless the source/flavor and target-specific entrance-strength gates independently pass.

## Prospective pass/fail contract
- PASS source/flavor class gate if software tests enforce `B16 thermonuclear nu_e -> RIOEC rate = 0` and permit only an explicitly tagged `anti-nu_e` source.
- PASS area gate if numerical integration conserves `B0` to <=1e-5 relative for a sufficiently wide integration window and demonstrates no area growth under linewidth narrowing.
- PASS smooth-source overlap if the numerical convolution approaches `B0*phi(E_R)` to <=1e-3 relative for a source profile much broader than the resonance.
- This iteration MUST NOT claim a target-specific W/kg ceiling. That requires a measured/evaluated candidate entrance strength and a physical thermal-solar anti-nu_e spectrum.

## Outcome classes frozen in advance
- `RIOEC_B16_FLAVOR_NO_GO_PASS`: dominant thermonuclear solar B16 source excluded for this resonance channel.
- `RIOEC_AREA_PROFILE_PASS`: integrated-strength/source-profile theorem reproduced numerically.
- `G8_TARGET_SPECIFIC_OPEN`: remains until a real candidate is folded with a physical anti-nu_e source spectrum.
