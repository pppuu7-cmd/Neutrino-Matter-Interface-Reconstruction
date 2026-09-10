# 0105a6q4ft — q4f transport-only endpoint diagnostic

Status: **PROSPECTIVE TRANSPORT DIAGNOSTIC; NO SCIENTIFIC CRITERIA CHANGE**

Parent q4f is permanently retained as `BLOCKED_0105A6Q4F_INSTITUTIONAL_METADATA_IDENTITY_FAILURE` with run/job/artifact `34539208459 / 103077779431 / 10176594931` and inner result SHA256 `4999d18324655199ebb367e054aa092aa190c2bb74ec00d4d46a907368a72719`.

Purpose: determine which already-frozen metadata transport produced the q4f HTTP 404. This diagnostic cannot reclassify q4f and cannot inspect target dissertation content.

Frozen endpoints, copied from q4f without alteration:
1. `https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html`
2. ScholarWorks discovery route generated exactly by q4f from the exact frozen title.

For each endpoint q4ft may record only: requested URL, HTTP status or transport exception, final URL, response byte count, response SHA256 and content-type header. It must not parse page semantics, extract PDF links, download a PDF, run `pdftotext`, inspect observed data/residuals or alter any q4f metadata matching rule.

Decision classes:
- both endpoints transport with HTTP 200: `PASS_0105A6Q4FT_FROZEN_ENDPOINT_TRANSPORT_DIAGNOSTIC_NONDISCOVERY`;
- otherwise: `BLOCKED_0105A6Q4FT_FROZEN_ENDPOINT_TRANSPORT_DIAGNOSTIC_IDENTIFIED` with per-endpoint evidence.

A diagnostic BLOCKED is expected to identify a transport repair target only. Any repaired authority-manifest execution must be a new prospectively registered gate and must preserve q4f author/title/year/official-IU criteria exactly.

Always: no PDF content inspection; systematic MC permission 0%; observed BSM residual permission 0%; NMIR v1 frozen at 100%.