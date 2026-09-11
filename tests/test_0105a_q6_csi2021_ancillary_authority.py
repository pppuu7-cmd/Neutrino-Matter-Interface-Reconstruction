from scripts.audit_0105a_q6_csi2021_ancillary_authority import classify

BASE = '''With this supplemental material, we provide selected, unbinned data events relevant for this result.
All events selected with PE < 250 and 0 ≤ trec < 12 µs are included.
Events with energy 60 ≤ PE < 250 or trec ≥ 6 µs are not used for measuring the CEvNS cross
section but used for a search for light dark matter produced at the SNS.
Observed data are given in dataBeamOnAC.txt and dataBeamOnC.txt.
These two files contain all data relevant for this measurement.'''

def test_f1_pass_requires_primary_semantics():
    r = classify(BASE, {})
    assert r['f1']['status'].startswith('PASS_0105A_Q6_F1_')

def test_f1_fail_closed_when_region_rule_missing():
    r = classify(BASE.replace('60 ≤ PE < 250', '60 < PE < 250'), {})
    assert r['f1']['status'].startswith('BLOCKED_0105A_Q6_F1_')

def test_f7_not_promoted_by_literals_or_numeric_files():
    r = classify(BASE + ' 3152 3154 ', {'dataBeamOnC.txt': '3152\n3154\n'})
    assert r['f7']['literal_3152_present']
    assert r['f7']['literal_3154_present']
    assert r['f7']['status'].startswith('BLOCKED_0105A_Q6_F7_')

def test_hard_no_posthoc_numeric_precedence():
    r = classify(BASE, {'dataBeamOnC.txt': '\n'.join(['1 1'] * 3154)})
    assert r['f7']['status'].startswith('BLOCKED_0105A_Q6_F7_')
