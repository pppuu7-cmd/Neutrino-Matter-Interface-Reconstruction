#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

REPO_URL = "https://api.github.com/repos/mceq-project/MCEq"
RELEASES_URL = "https://api.github.com/repos/mceq-project/MCEq/releases?per_page=100"
TAGS_URL = "https://api.github.com/repos/mceq-project/MCEq/tags?per_page=100"
ALLOWED_URLS = [REPO_URL, RELEASES_URL, TAGS_URL]
HEX40 = re.compile(r"^[0-9a-fA-F]{40}$")


def fetch_json(url):
    if url not in ALLOWED_URLS:
        raise RuntimeError(f"prohibited endpoint: {url}")
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "NMIR-v2-0105a5b-R1f-metadata-only",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
        status = int(resp.status)
        ctype = resp.headers.get("Content-Type", "")
        final_url = resp.geturl()
    parsed = json.loads(raw.decode("utf-8"))
    return {
        "requested_url": url,
        "final_url": final_url,
        "status": status,
        "content_type": ctype,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "json": parsed,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()

    result = {
        "gate": "0105a5b-R1f",
        "git_sha": args.git_sha,
        "classification": None,
        "requests": {},
        "repository": None,
        "releases": [],
        "tags": [],
        "network_requests_executed": True,
        "source_code_inspected": False,
        "readme_inspected": False,
        "source_archives_downloaded": False,
        "standard_3nu_executed": False,
        "systematic_monte_carlo_executed": False,
        "observed_bsm_residual_inspected": False,
        "observed_bsm_residual_permission_percent": 0,
        "systematic_monte_carlo_execution_permission_percent": 0,
    }

    try:
        repo = fetch_json(REPO_URL)
        releases = fetch_json(RELEASES_URL)
        tags = fetch_json(TAGS_URL)
        for key, obj in [("repository", repo), ("releases", releases), ("tags", tags)]:
            result["requests"][key] = {k: obj[k] for k in ["requested_url", "final_url", "status", "content_type", "bytes", "sha256"]}

        rj = repo["json"]
        result["repository"] = {
            "full_name": rj.get("full_name"),
            "owner_login": (rj.get("owner") or {}).get("login"),
            "html_url": rj.get("html_url"),
            "homepage": rj.get("homepage"),
            "description": rj.get("description"),
            "archived": rj.get("archived"),
            "default_branch": rj.get("default_branch"),
            "created_at": rj.get("created_at"),
            "updated_at": rj.get("updated_at"),
            "pushed_at": rj.get("pushed_at"),
        }
        if not isinstance(releases["json"], list) or not isinstance(tags["json"], list):
            raise ValueError("releases/tags response is not a JSON array")
        result["releases"] = [
            {
                "tag_name": x.get("tag_name"),
                "target_commitish": x.get("target_commitish"),
                "draft": x.get("draft"),
                "prerelease": x.get("prerelease"),
                "published_at": x.get("published_at"),
                "html_url": x.get("html_url"),
            }
            for x in releases["json"]
        ]
        result["tags"] = [
            {"name": x.get("name"), "commit_sha": (x.get("commit") or {}).get("sha")}
            for x in tags["json"]
        ]

        all_200 = all(x["status"] == 200 for x in [repo, releases, tags])
        identity_ok = result["repository"]["full_name"] == "mceq-project/MCEq" and result["repository"]["owner_login"] == "mceq-project"
        tags_ok = len(result["tags"]) > 0 and all(HEX40.fullmatch(x["commit_sha"] or "") for x in result["tags"])
        if all_200 and identity_ok and tags_ok:
            result["classification"] = "PASS_0105A5B_R1F_MCEQ_REPOSITORY_METADATA_PINNABLE_NONDISCOVERY"
        else:
            result["classification"] = "BLOCKED_0105A5B_R1F_MCEQ_REPOSITORY_METADATA_NOT_PINNABLE"
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
        result["classification"] = "INFRASTRUCTURE_FAIL_0105A5B_R1F_MCEQ_METADATA_TRANSPORT"
        result["transport_error"] = f"{type(exc).__name__}: {exc}"

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    result["canonical_result_sha256_before_self_field"] = hashlib.sha256(canonical).hexdigest()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
