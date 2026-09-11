#!/usr/bin/env python3
import argparse, hashlib, json, re
from pathlib import Path

ROOTS = [Path('research'), Path('scripts'), Path('tests'), Path('.github/workflows')]
EXCLUDED = {
    'research/prereg/0105a5b_r1e_repository_authority_route_inventory_preregistration.md',
    'scripts/audit_0105a5b_r1e_repository_authority_route_inventory.py',
    'tests/test_0105a5b_r1e_repository_authority_route_inventory.py',
    '.github/workflows/nmir_v2_0105a5b_r1e_repository_authority_route_inventory.yml',
    'research/NMIR_V2_CURRENT_FRONT.md',
    'research/NMIR_V2_RECOVERY.md',
}
SOURCE_MARKERS = [
    '0105a5b', 'r1d', 'external computational authority', 'upstream authority'
]
HIT_TERMS = [
    'zenodo', 'github', 'repository', 'artifact', 'response matrix',
    'derivative table', 'nuisance response', 'systematic response',
    'systematic derivative', 'likelihood code'
]
URL_RE = re.compile(r'https?://[^\s<>"\')\]]+')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--git-sha', required=True)
    args = ap.parse_args()

    related = []
    hits = []
    unreadable = []
    for root in ROOTS:
        if not root.exists():
            continue
        for path in sorted(p for p in root.rglob('*') if p.is_file()):
            rel = path.as_posix()
            if rel in EXCLUDED or '/artifacts/' in rel:
                continue
            try:
                text = path.read_text(encoding='utf-8')
            except Exception as exc:
                unreadable.append({'path': rel, 'error': repr(exc)})
                continue
            low = text.lower()
            if not any(m in low for m in SOURCE_MARKERS):
                continue
            related.append(rel)
            for lineno, line in enumerate(text.splitlines(), 1):
                lline = line.lower()
                urls = URL_RE.findall(line)
                terms = sorted({t for t in HIT_TERMS if t in lline})
                if urls or terms:
                    hits.append({
                        'path': rel,
                        'line': lineno,
                        'urls': sorted(set(urls)),
                        'terms': terms,
                        'line_sha256': hashlib.sha256(line.encode('utf-8')).hexdigest(),
                    })

    related = sorted(set(related))
    hits = sorted(hits, key=lambda x: (x['path'], x['line'], x['urls'], x['terms']))
    canonical = json.dumps({'related_files': related, 'hits': hits}, sort_keys=True, separators=(',', ':')).encode()
    classification = (
        'PASS_0105A5B_R1E_REPOSITORY_AUTHORITY_ROUTE_INVENTORY_EMITTED_NONDISCOVERY'
        if related else
        'BLOCKED_0105A5B_R1E_REPOSITORY_AUTHORITY_ROUTE_INVENTORY_EMPTY_OR_UNREADABLE'
    )
    out = {
        'gate': '0105a5b-R1e',
        'git_sha': args.git_sha,
        'classification': classification,
        'related_file_count': len(related),
        'related_files': related,
        'hit_count': len(hits),
        'hits': hits,
        'canonical_inventory_sha256': hashlib.sha256(canonical).hexdigest(),
        'unreadable_files': unreadable,
        'network_requests_executed': False,
        'external_files_acquired': False,
        'links_followed': False,
        'standard_3nu_executed': False,
        'systematic_monte_carlo_executed': False,
        'observed_bsm_residual_inspected': False,
        'observed_bsm_residual_permission_percent': 0,
        'systematic_monte_carlo_execution_permission_percent': 0,
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
