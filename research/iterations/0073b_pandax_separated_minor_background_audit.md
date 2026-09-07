# Iteration 0073b — PandaX separated minor-background primary-data audit

Date: 2026-09-07
Classification: **BLOCKED_PRIMARY_LIKELIHOOD_INPUTS**
Frozen prereg: `research/prereg/0073b_pandax_separated_minor_background_author_data_audit.md`, commit `750dcc8c6e433e761ca31b47c42c8c11567471bd`.

## Question
Can public primary/official sources provide separate reconstructed-energy templates for neutron, solar-8B, accidental, and surface/wall backgrounds for the exact PandaX-4T 0.63 tonne-year commissioning selection used in arXiv:2206.02339 / PRL 129, 161804?

## Result
No. The permitted public-primary routes were exhausted without materializing the required four separated 0–30 keV templates.

The official PandaX data-release index exposes the commissioning `PandaX-4T: First Analysis` release and later analysis releases. The commissioning page lists only `eff_RDQ_graph.root` and `PandaX4T_Data_ne.xlsx`; it does not publish separate 30-bin neutron, 8B, accidental, or surface/wall templates for the 2206.02339 analysis. No dedicated public release for PRL 129, 161804 was found.

The SCOAP3 record for DOI `10.1103/PhysRevLett.129.161804` exposes PDF and XML fulltext only, with no supplementary numerical template package. Exact HEPData searches by DOI, arXiv ID, and paper title produced no matching record. Public author/code/data searches likewise produced no same-analysis numerical package containing the four separated templates.

A dedicated PandaX-4T neutron-background primary paper exists and is tied to the 0.63 tonne-year commissioning exposure, but it does not supply the complete set of four same-selection reconstructed-energy templates needed by the frozen likelihood. Other PandaX releases/analyses cannot be substituted because no primary provenance establishes identity of their selection/response/template shapes with the 2206.02339 0–30 keV analysis.

## Frozen scientific consequence
0073a remains valid: the exact 30 observed bins and 301-point primary efficiency curve are accepted. But Fig. 3 publishes neutron + 8B + accidental + wall/surface as one grouped family while the likelihood uses distinct nuisance widths. Therefore the full-profile PandaX/De-Romeri B-L likelihood is not identifiable from current public primary inputs without an unfrozen decomposition assumption.

No proportional splitting, raster/manual digitization, Asimov substitution, cross-analysis template borrowing, or B-L calculation was performed.

The PandaX full-profile route is therefore retired as **BLOCKED_PRIMARY_LIKELIHOOD_INPUTS**. This is a data-authority blocker, not evidence against B-L physics.

Machine-readable audit: `data/pandax_separated_minor_background_audit_0073b.json`, commit `db7e863322a2e02a6f71f9b30b26f2e118aa1f6f`.

## Next action
Move to a different compatible primary B-L constraint family. Highest-value next route: prospectively freeze an independent COHERENT CsI+Ar CEvNS B-L likelihood/contour reproduction using primary public data and the explicit B-L convention of Cadeddu et al. Do not weaken the PandaX nuisance model.

`NMIR_READINESS` remains 89%: a route was correctly retired but no new physical external envelope was closed.
