import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'scripts'/'audit_0105a6q4ft_suh_2025_manifest_transport_diagnostic.py'
s=importlib.util.spec_from_file_location('q4ft',P); q=s.loader.load_module()

def test_frozen_endpoints_and_prereg():
    assert q.PREREG_COMMIT=='df83de59bf8cb66fcfe8009f3228f2b3a5b78174'
    assert q.CEEM_URL=='https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html'
    assert q.SEARCH_URL.startswith('https://scholarworks.iu.edu/dspace/discover?query=')

def test_title_is_exact_q4f_title():
    assert q.TITLE=='TOWARDS AN IMPROVED MEASUREMENT OF THE CEVNS PROCESS WITH THE CENNS-10 LAR DETECTOR'
