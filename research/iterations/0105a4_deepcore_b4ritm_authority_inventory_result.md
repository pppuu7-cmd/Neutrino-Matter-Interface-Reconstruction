# 0105a4 — DeepCore B4RITM authority inventory result

Status: `PASS_0105A4_B4RITM_AUTHORITY_INVENTORY_PINNED_NONDISCOVERY`

This is an authority/provenance result only. It is not a neutrino-physics result, does not evaluate an observed residual, and does not authorize BSM interpretation.

## Frozen authority

- Dataset persistent ID: `doi:10.7910/DVN/B4RITM`
- Dataverse dataset version: `1.1`
- Provider endpoint: `https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/B4RITM`
- Hosted workflow run: `34418458353`
- Hosted job: `102688456198`
- Head SHA: `abde96ad8226dbf2e426b92093efa5b4df8e55dc`
- Artifact ID: `10129986472`
- Artifact name: `nmir-v2-0105a4-deepcore-b4ritm-inventory`
- Artifact digest: `sha256:9eb6259647f7479e1b05a5c1a841737a5a577f454575fc9eb2484dd44a9f132b`

## Frozen inventory

Exactly four unrestricted provider files were returned by the pinned dataset version:

1. `DNN_uncertainty_splines.pckl`
   - bytes: `438500`
   - provider file ID: `6660756`
   - persistent ID: `doi:10.7910/DVN/B4RITM/PRGLAR`
   - provider MD5: `cf76ce7b74baa183f54930c21918a3df`
2. `oscNext_data_IC86.11-18.pckl`
   - bytes: `1445962`
   - provider file ID: `6660758`
   - persistent ID: `doi:10.7910/DVN/B4RITM/DIOZGU`
   - provider MD5: `95e1236193931562959b8547312c74ed`
3. `oscNext_genie_level7_v02.00_pass2.120000.pckl`
   - bytes: `25054422`
   - provider file ID: `6660757`
   - persistent ID: `doi:10.7910/DVN/B4RITM/EEIBWL`
   - provider MD5: `b2dcbf606438088bdee3a8a7b8a1df4e`
4. `oscNext_muongun_level7_v02.00_pass2.140000.pckl`
   - bytes: `12162293`
   - provider file ID: `6660755`
   - persistent ID: `doi:10.7910/DVN/B4RITM/I3XG5M`
   - provider MD5: `9c25d2ff8c16ea944d58a9eaa56dc60a`

## Guards verified

The hosted manifest records:

- `semantic_scope_only = true`
- `binary_content_consumed = false`
- `observed_residual_execution_allowed = false`
- `sterile_authority_substitution_forbidden = true`
- `sterile_authority_substitution_detected = false`
- `bsm_interpretation_allowed = false`

`doi:10.7910/DVN/QKL28Z` remains a separate sterile-control authority and is not a substitute for the frozen B4RITM propagation authority.

## Interpretation

0105a4 closes the metadata-level identity/version/inventory gate for the DeepCore B4RITM authority. It does **not** yet create a byte-level lock of the four payloads. Before any payload parsing or standalone 3nu reproduction, NMIR v2 must prospectively freeze a byte-lock gate that verifies the provider MD5 values and records independent SHA256 values for the exact consumed bytes.

Observed BSM residual permission remains `0%`.
