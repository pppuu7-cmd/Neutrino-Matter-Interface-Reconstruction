#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import pathlib
import re
import subprocess
import tempfile

REMOTE = "https://code.ornl.gov/COHERENT/codeExamples_dataRelease_april2018.git"
TERMS = (
    "likelihood", "loglikelihood", "log likelihood", "nll", "chi2", "chi-square",
    "poisson", "gaussian", "constraint", "profile", "nuisance", "covariance",
    "correlation", "minuit", "fit", "background", "efficiency", "acceptance",
    "quenching", "prompt neutron", "steady state",
)
MAX_TEXT_BYTES = 25_000_000


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, stderr=subprocess.STDOUT, text=True).strip()


def decode_text(b):
    if len(b) > MAX_TEXT_BYTES:
        return None
    for enc in ("utf-8", "latin-1"):
        try:
            s = b.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        return None
    if not s:
        return ""
    sample = s[:10000]
    printable = sum(ch.isprintable() or ch in "\r\n\t" for ch in sample)
    if printable / max(1, len(sample)) < 0.90:
        return None
    return s


def term_hits(text):
    lo = text.lower()
    out = {}
    for t in TERMS:
        hits = [m.start() for m in re.finditer(re.escape(t), lo)]
        if hits:
            out[t] = {"count": len(hits), "first_offsets": hits[:12]}
    return out


def resolve_remote():
    sym = run("git", "ls-remote", "--symref", REMOTE, "HEAD")
    lines = [x for x in sym.splitlines() if x.strip()]
    ref = None
    head = None
    for line in lines:
        if line.startswith("ref:") and line.endswith("\tHEAD"):
            ref = line.split()[1]
        elif line.endswith("\tHEAD") and not line.startswith("ref:"):
            head = line.split()[0]
    if not ref or not head or not re.fullmatch(r"[0-9a-f]{40}", head):
        raise RuntimeError("could not deterministically resolve remote HEAD")
    return ref, head, sym


def inventory_repo(ref, head):
    with tempfile.TemporaryDirectory() as td:
        repo = pathlib.Path(td) / "repo"
        subprocess.check_call(["git", "clone", "--no-checkout", "--filter=blob:none", REMOTE, str(repo)])
        subprocess.check_call(["git", "-C", str(repo), "checkout", "--detach", head])
        observed = run("git", "rev-parse", "HEAD", cwd=repo)
        if observed != head:
            raise RuntimeError("checked-out commit differs from resolved HEAD")
        tree = run("git", "rev-parse", "HEAD^{tree}", cwd=repo)
        timestamp = run("git", "show", "-s", "--format=%cI", "HEAD", cwd=repo)
        subject = run("git", "show", "-s", "--format=%s", "HEAD", cwd=repo)
        files = run("git", "ls-files", cwd=repo).splitlines()
        entries = []
        for rel in sorted(files):
            p = repo / rel
            b = p.read_bytes()
            text = decode_text(b)
            entry = {
                "path": rel,
                "size_bytes": len(b),
                "sha256": sha256_bytes(b),
                "text_decodable": text is not None,
            }
            if text is not None:
                entry["term_hits"] = term_hits(text)
            entries.append(entry)
        return {
            "remote": REMOTE,
            "default_ref": ref,
            "commit_sha": head,
            "tree_sha": tree,
            "commit_timestamp": timestamp,
            "commit_subject": subject,
            "tracked_file_count": len(entries),
            "files": entries,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", default=os.environ.get("GITHUB_SHA", ""))
    args = ap.parse_args()
    result = {
        "benchmark": "NMIR-V2-0105A6E",
        "stage": "official_ornl_example_code_authority_inventory_only",
        "git_sha": args.git_sha,
        "sm_null_reproduction_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "scientific_pass_classified": False,
        "terms": list(TERMS),
    }
    try:
        ref, head, raw = resolve_remote()
        result["remote_ls_remote_sha256"] = sha256_bytes((raw + "\n").encode())
        result["repository"] = inventory_repo(ref, head)
        result["status"] = "EVIDENCE_ACQUIRED_REQUIRES_INDEPENDENT_SEMANTIC_CLASSIFICATION"
    except Exception as e:
        result["status"] = "BLOCKED_0105A6E_ORNL_TRANSPORT_OR_IDENTITY"
        result["error"] = type(e).__name__ + ": " + str(e)[:1000]
    raw = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    pathlib.Path(args.output).write_bytes(raw)
    print(raw.decode(), end="")
    print("result_sha256=" + sha256_bytes(raw))


if __name__ == "__main__":
    main()
