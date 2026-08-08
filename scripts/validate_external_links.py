#!/usr/bin/env python3
"""Check external links in Markdown documents.

This validator is intended for scheduled/advisory use because remote sites may
rate-limit, block automation, or fail transiently.
"""

from __future__ import annotations

import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from docs_common import DOCS_ROOT, relative

URL_RE = re.compile(r"https?://[^\s)>\]]+")
USER_AGENT = "Brk-Trkr-Docs-Link-Checker/1.0"


def check(url: str) -> tuple[bool, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
    try:
        with urlopen(request, timeout=15) as response:
            code = getattr(response, "status", 200)
            return 200 <= code < 400, str(code)
    except HTTPError as exc:
        if exc.code in {403, 405, 429}:
            request = Request(url, headers={"User-Agent": USER_AGENT}, method="GET")
            try:
                with urlopen(request, timeout=15) as response:
                    code = getattr(response, "status", 200)
                    return 200 <= code < 400, str(code)
            except (HTTPError, URLError, TimeoutError) as retry_exc:
                return False, str(retry_exc)
        return False, str(exc.code)
    except (URLError, TimeoutError) as exc:
        return False, str(exc)


def main() -> int:
    urls: dict[str, list[str]] = {}
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for url in URL_RE.findall(text):
            cleaned = url.rstrip(".,;:'\"")
            urls.setdefault(cleaned, []).append(relative(path))

    failures: list[str] = []
    for url in sorted(urls):
        ok, result = check(url)
        print(f"{'OK' if ok else 'FAIL'} {result} {url}")
        if not ok:
            failures.append(f"{url} ({result}) referenced by {', '.join(sorted(set(urls[url]))) }")
        time.sleep(0.1)

    if failures:
        print("External link audit found failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"External link audit passed for {len(urls)} unique URLs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
