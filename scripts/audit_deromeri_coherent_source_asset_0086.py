#!/usr/bin/env python3
import hashlib, io, json, os, pathlib, tarfile, urllib.request

URL = "https://export.arxiv.org/e-print/2211.11905v2"
TEXT_EXTS = {".tex", ".txt", ".bib", ".sty", ".cls"}


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def inventory(data):
    out = []
    seen = set()
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as tf:
        for m in tf.getmembers():
            p = pathlib.PurePosixPath(m.name)
            if p.is_absolute() or ".." in p.parts:
                raise RuntimeError(f"unsafe_member:{m.name}")
            if m.name in seen:
                raise RuntimeError(f"duplicate_member:{m.name}")
            seen.add(m.name)
            if m.isdir():
                continue
            if not m.isfile():
                raise RuntimeError(f"unsupported_member_type:{m.name}")
            f = tf.extractfile(m)
            if f is None:
                raise RuntimeError(f"unreadable_member:{m.name}")
            b = f.read()
            out.append({
                "path": m.name,
                "size": len(b),
                "sha256": sha256(b),
                "source_text_candidate": pathlib.PurePosixPath(m.name).suffix.lower() in TEXT_EXTS,
            })
    out.sort(key=lambda x: x["path"])
    return out


def main():
    out_path = os.environ.get("NMIR_0086_OUTPUT", "artifacts/deromeri_coherent_source_asset_0086.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    result = {
        "gate": "0086",
        "source": "arXiv:2211.11905v2",
        "url": URL,
        "classification": "INFRASTRUCTURE_FAIL",
    }
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "NMIR-reproducibility-audit/1.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        result["archive_size"] = len(data)
        result["archive_sha256"] = sha256(data)
        inv1 = inventory(data)
        inv2 = inventory(data)
        result["inventory_pass_1"] = inv1
        result["inventory_pass_2_sha256"] = sha256(json.dumps(inv2, sort_keys=True, separators=(",", ":")).encode())
        result["inventory_pass_1_sha256"] = sha256(json.dumps(inv1, sort_keys=True, separators=(",", ":")).encode())
        result["member_count"] = len(inv1)
        result["source_text_candidate_count"] = sum(x["source_text_candidate"] for x in inv1)
        if inv1 != inv2:
            result["classification"] = "INFRASTRUCTURE_FAIL_REPRODUCIBILITY"
        elif result["source_text_candidate_count"] < 1:
            result["classification"] = "BLOCKED_DEROMERI_SOURCE_TEXT_ASSET_AUTHORITY"
        else:
            result["classification"] = "PASS_DEROMERI_COHERENT_UPDATED_SOURCE_ASSET_AUTHORITY"
    except Exception as e:
        result["error"] = f"{type(e).__name__}:{e}"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps({k: result.get(k) for k in ["classification","archive_size","archive_sha256","member_count","source_text_candidate_count","error"]}, sort_keys=True))
    if result["classification"] == "PASS_DEROMERI_COHERENT_UPDATED_SOURCE_ASSET_AUTHORITY":
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
