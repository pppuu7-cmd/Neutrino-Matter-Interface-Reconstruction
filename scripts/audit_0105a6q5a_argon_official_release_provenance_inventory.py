#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

PREREG_COMMIT = "1b487a2ea8bad7eecc6d02eff30e7f26be28315d"
GATE = "NMIR-V2-0105A6Q5A"
ORNL_URL = "https://coherent.ornl.gov/data-releases/"
ZENODO_URL = "https://zenodo.org/api/records/3903810"
ARXIV_URL = "https://arxiv.org/abs/2006.12659"
EXPECTED_TITLE = "COHERENT Collaboration data release from the first detection of coherent elastic neutrino-nucleus scattering on argon"
UA = "NMIR-0105a6q5a-provenance-inventory/1.0"

LOCAL_EXPECTED = {
    "classification": "PASS_0105A3_COHERENT_ZENODO_DIRECT_BYTE_LOCK_NONTERMINAL",
    "implementation": "6ab2b940be4431c6fd7cad8048e10764a88eb086",
    "run": "34418207408",
    "attempt": "3",
    "job": "102834981270",
    "artifact": "10147580844",
    "artifact_name": "nmir-v2-0105a3-coherent-byte-lock",
    "artifact_zip_sha256": "b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4",
    "record": "3903810",
    "doi": "10.5281/zenodo.3903810",
    "version": "1.0",
    "ar_files": "24",
    "csi_files": "13",
    "total_files": "37",
    "manifest_sha256": "5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091",
}

CLASS_PASS = "PASS_0105A6Q5A_ARGON_OFFICIAL_RELEASE_PROVENANCE_INVENTORY_BOUND_NONDISCOVERY"
CLASS_LOCAL = "BLOCKED_0105A6Q5A_LOCAL_0105A3_AUTHORITY_BINDING_FAILURE"
CLASS_ORNL = "BLOCKED_0105A6Q5A_ORNL_RELEASE_ROUTE_FAILURE"
CLASS_ZENODO = "BLOCKED_0105A6Q5A_ZENODO_RECORD_METADATA_FAILURE"
CLASS_ARXIV = "BLOCKED_0105A6Q5A_ARXIV_METADATA_FAILURE"
CLASS_TRANSPORT = "BLOCKED_0105A6Q5A_PROVIDER_TRANSPORT_FAILURE"


def norm(value):
    return " ".join(unicodedata.normalize("NFKC", str(value or "")).split()).casefold()


def sha256_bytes(payload):
    return hashlib.sha256(payload).hexdigest()


class RedirectRecorder(urllib.request.HTTPRedirectHandler):
    def __init__(self, provider):
        super().__init__()
        self.provider = provider
        self.redirects = []

    @staticmethod
    def _same_provider(provider, host):
        host = (host or "").split(":", 1)[0].casefold().rstrip(".")
        if provider == "ornl":
            return host == "ornl.gov" or host.endswith(".ornl.gov")
        if provider == "zenodo":
            return host == "zenodo.org" or host.endswith(".zenodo.org")
        if provider == "arxiv":
            return host == "arxiv.org" or host.endswith(".arxiv.org")
        return False

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        target = urllib.parse.urljoin(req.full_url, newurl)
        if not self._same_provider(self.provider, urllib.parse.urlparse(target).hostname):
            raise RuntimeError(f"cross-provider redirect rejected: {req.full_url} -> {target}")
        self.redirects.append({"status": int(code), "to": target})
        return super().redirect_request(req, fp, code, msg, headers, target)


def fetch(url, provider, attempts=3):
    errors = []
    for i in range(attempts):
        redirector = RedirectRecorder(provider)
        opener = urllib.request.build_opener(redirector)
        request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with opener.open(request, timeout=90) as response:
                payload = response.read()
                return {
                    "ok": int(getattr(response, "status", response.getcode())) == 200,
                    "requested_url": url,
                    "final_url": response.geturl(),
                    "status": int(getattr(response, "status", response.getcode())),
                    "redirect_count": len(redirector.redirects),
                    "bytes": len(payload),
                    "sha256": sha256_bytes(payload),
                    "content_type": response.headers.get("Content-Type"),
                    "error": None,
                    "payload": payload,
                }
        except urllib.error.HTTPError as exc:
            payload = exc.read()
            errors.append(f"HTTPError:{exc.code}")
            if i == attempts - 1:
                return {
                    "ok": False, "requested_url": url, "final_url": exc.geturl(),
                    "status": int(exc.code), "redirect_count": len(redirector.redirects),
                    "bytes": len(payload), "sha256": sha256_bytes(payload),
                    "content_type": exc.headers.get("Content-Type"), "error": errors[-1], "payload": payload,
                }
        except Exception as exc:
            errors.append(type(exc).__name__ + ":" + str(exc))
            if i == attempts - 1:
                return {
                    "ok": False, "requested_url": url, "final_url": None, "status": None,
                    "redirect_count": len(redirector.redirects), "bytes": 0, "sha256": None,
                    "content_type": None, "error": errors[-1], "payload": b"",
                }
        time.sleep(2)
    raise AssertionError("unreachable")


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = []
        self._href = None
        self._text = []

    def handle_starttag(self, tag, attrs):
        if tag.casefold() == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag.casefold() == "a" and self._href is not None:
            self.anchors.append((self._href, " ".join(self._text)))
            self._href = None
            self._text = []


class HeadMetadataParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_head = False
        self.in_title = False
        self.title = []
        self.meta = {}
        self.canonicals = []

    def handle_starttag(self, tag, attrs):
        tag = tag.casefold()
        attrs = {str(k).casefold(): v for k, v in attrs}
        if tag == "head": self.in_head = True
        if not self.in_head: return
        if tag == "title": self.in_title = True
        elif tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            if key and attrs.get("content") is not None:
                self.meta[key.casefold()] = attrs.get("content")
        elif tag == "link" and (attrs.get("rel") or "").casefold() == "canonical":
            if attrs.get("href"): self.canonicals.append(attrs["href"])

    def handle_data(self, data):
        if self.in_head and self.in_title: self.title.append(data)

    def handle_endtag(self, tag):
        tag = tag.casefold()
        if tag == "title": self.in_title = False
        elif tag == "head": self.in_head = False


def check_local(path):
    text = Path(path).read_text(encoding="utf-8")
    checks = {
        "classification": LOCAL_EXPECTED["classification"] in text,
        "implementation": LOCAL_EXPECTED["implementation"] in text,
        "run_attempt_job": all(x in text for x in (LOCAL_EXPECTED["run"], LOCAL_EXPECTED["attempt"], LOCAL_EXPECTED["job"])),
        "artifact": all(x in text for x in (LOCAL_EXPECTED["artifact"], LOCAL_EXPECTED["artifact_name"])),
        "artifact_zip_sha256": LOCAL_EXPECTED["artifact_zip_sha256"] in text,
        "argon_record_doi_version": all(x in text for x in (LOCAL_EXPECTED["record"], LOCAL_EXPECTED["doi"], "frozen version `1.0`", "24 files")),
        "split": "CsI: 13/13" in text and "Ar: 24/24" in text and "total frozen file count: 37" in text,
        "manifest_sha256": LOCAL_EXPECTED["manifest_sha256"] in text,
        "md5_sha256_authority": "all_provider_md5_match = true" in text and "all_sha256_recorded = true" in text,
    }
    return {"pass": all(checks.values()), "checks": checks, **LOCAL_EXPECTED}


def inspect_ornl(payload):
    parser = AnchorParser()
    parser.feed(payload.decode("utf-8", errors="replace"))
    parser.close()
    matches = 0
    for href, text in parser.anchors:
        ntext = norm(text)
        if "data release" not in ntext or "argon" not in ntext:
            continue
        resolved = urllib.parse.urlparse(urllib.parse.urljoin(ORNL_URL, href or ""))
        host = (resolved.hostname or "").casefold()
        path = resolved.path.rstrip("/")
        if (host == "zenodo.org" or host.endswith(".zenodo.org")) and re.search(r"/(?:record|records)/3903810$", path):
            matches += 1
    return {"pass": matches > 0, "matching_anchor_count": matches}


def inspect_zenodo(payload):
    data = json.loads(payload.decode("utf-8"))
    metadata = data.get("metadata") or {}
    files = data.get("files") or []
    title_match = norm(EXPECTED_TITLE) in norm(metadata.get("title"))
    checks = {
        "record_id_exact": data.get("id") == 3903810,
        "doi_exact": data.get("doi") == "10.5281/zenodo.3903810",
        "version_exact": str(metadata.get("version")) == "1.0",
        "title_match": title_match,
        "file_count_24": len(files) == 24,
    }
    inventory = []
    for f in files:
        inventory.append({"key": f.get("key"), "size": f.get("size"), "checksum": f.get("checksum")})
    return {"pass": all(checks.values()), "checks": checks, "record_id": data.get("id"), "doi": data.get("doi"), "version": metadata.get("version"), "title_match": title_match, "file_count": len(files), "files": inventory}


def inspect_arxiv(payload):
    parser = HeadMetadataParser()
    parser.feed(payload.decode("utf-8", errors="replace"))
    parser.close()
    citation_title = parser.meta.get("citation_title")
    head_title = " ".join(parser.title)
    arxiv_meta = parser.meta.get("citation_arxiv_id") or parser.meta.get("arxiv_id")
    canonical_ids = []
    for href in parser.canonicals:
        m = re.search(r"/abs/(2006\.12659)(?:v\d+)?/?$", urllib.parse.urlparse(href).path)
        if m: canonical_ids.append(m.group(1))
    id_match = (arxiv_meta or "").strip().removeprefix("arXiv:").split("v", 1)[0] == "2006.12659" or "2006.12659" in canonical_ids
    title_match = norm(EXPECTED_TITLE) in norm(citation_title) or norm(EXPECTED_TITLE) in norm(head_title)
    return {"pass": id_match and title_match, "id_match": id_match, "title_match": title_match, "canonical_id_match": "2006.12659" in canonical_ids, "citation_id_match": (arxiv_meta or "").strip().removeprefix("arXiv:").split("v", 1)[0] == "2006.12659"}


def sanitized_transport(item):
    return {k: item.get(k) for k in ("requested_url", "final_url", "status", "redirect_count", "bytes", "sha256", "content_type", "error", "ok")}


def classify(local_ok, transports_ok, ornl_ok, zenodo_ok, arxiv_ok):
    if not local_ok: return CLASS_LOCAL
    if not transports_ok: return CLASS_TRANSPORT
    if not ornl_ok: return CLASS_ORNL
    if not zenodo_ok: return CLASS_ZENODO
    if not arxiv_ok: return CLASS_ARXIV
    return CLASS_PASS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    ap.add_argument("--local-record", default="research/iterations/0105a3_coherent_direct_byte_lock_recovery_pass_20260910.md")
    args = ap.parse_args()

    local = check_local(args.local_record)
    providers = {}
    semantic = {"ornl": {"pass": False}, "zenodo": {"pass": False}, "arxiv": {"pass": False}}
    for name, url in (("ornl", ORNL_URL), ("zenodo", ZENODO_URL), ("arxiv", ARXIV_URL)):
        item = fetch(url, name)
        providers[name] = sanitized_transport(item)
        if item["ok"]:
            try:
                if name == "ornl": semantic[name] = inspect_ornl(item["payload"])
                elif name == "zenodo": semantic[name] = inspect_zenodo(item["payload"])
                else: semantic[name] = inspect_arxiv(item["payload"])
            except Exception as exc:
                semantic[name] = {"pass": False, "parse_error": type(exc).__name__}

    transports_ok = all(x["ok"] for x in providers.values())
    classification = classify(local["pass"], transports_ok, semantic["ornl"]["pass"], semantic["zenodo"]["pass"], semantic["arxiv"]["pass"])
    result = {
        "gate": GATE,
        "preregistration_commit": PREREG_COMMIT,
        "git_sha": args.git_sha,
        "complete": True,
        "classification": classification,
        "local_0105a3_binding": local,
        "providers": providers,
        "predicates": semantic,
        "release_file_bytes_downloaded": False,
        "release_file_bytes_rehashed": False,
        "scientific_release_content_inspected": False,
        "pseudo_data_generated": False,
        "likelihood_evaluated": False,
        "observed_bsm_residual_inspected": False,
        "systematic_monte_carlo_preregistration_permission_percent": 0,
        "systematic_monte_carlo_execution_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    out.write_bytes(data)
    print("CLASSIFICATION=" + classification)
    print("RESULT_SHA256=" + sha256_bytes(data))
    print("ZENODO_FILE_COUNT=" + str(semantic["zenodo"].get("file_count")))
    print("ORNL_ROUTE_MATCHES=" + str(semantic["ornl"].get("matching_anchor_count")))
    print("ARXIV_ID_MATCH=" + str(semantic["arxiv"].get("id_match")))
    print("ARXIV_TITLE_MATCH=" + str(semantic["arxiv"].get("title_match")))


if __name__ == "__main__":
    main()
