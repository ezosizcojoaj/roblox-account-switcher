from __future__ import annotations

import re

_COOKIE_RE = re.compile(r"\.ROBLOSECURITY\s*[=:]\s*([A-Za-z0-9_|%-]{100,})")


def extract_roblosecurity(raw: str) -> str | None:
    """Extract a .ROBLOSECURITY cookie from a pasted browser header dump."""
    match = _COOKIE_RE.search(raw)
    if match:
        return match.group(1)
    stripped = raw.strip().strip(";")
    if stripped.startswith("_"):
        return stripped
    return None


def mask_cookie(cookie: str) -> str:
    if len(cookie) < 12:
        return "****"
    return f"{cookie[:4]}...{cookie[-4:]}"