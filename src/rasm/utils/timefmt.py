from __future__ import annotations

from datetime import datetime, timezone


def unix_to_human(ts: int) -> str:
    if ts <= 0:
        return "never"
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def human_to_unix(text: str) -> int:
    dt = datetime.strptime(text, "%Y-%m-%d %H:%M UTC").replace(tzinfo=timezone.utc)
    return int(dt.timestamp())