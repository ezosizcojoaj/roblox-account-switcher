from __future__ import annotations

from pathlib import Path
from typing import Iterable

from rasm.models.account import RobloxAccount
from rasm.utils.cookie_parser import extract_roblosecurity


class CookieImporter:
    """Bulk-import accounts from a plaintext cookie file (one per line)."""

    def __init__(self, source: Path) -> None:
        self.source = source

    def parse(self) -> Iterable[RobloxAccount]:
        if not self.source.exists():
            return
        for line in self.source.read_text(encoding="utf-8").splitlines():
            cookie = extract_roblosecurity(line)
            if not cookie:
                continue
            yield RobloxAccount(
                user_id=f"pending-{hash(cookie) & 0xFFFFFF:x}",
                username="(unverified)",
                roblosecurity=cookie,
            )