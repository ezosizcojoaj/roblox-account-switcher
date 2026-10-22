from __future__ import annotations

import requests
from loguru import logger


class RobloxApiClient:
    """Thin wrapper over the Roblox web endpoints used by the switcher."""

    BASE = "https://users.roblox.com/v1"
    ECONOMY = "https://economy.roblox.com/v1"

    def __init__(self, user_agent: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})

    def fetch_user_info(self, roblosecurity: str) -> dict:
        cookies = {".ROBLOSECURITY": roblosecurity}
        try:
            me = self.session.get(f"{self.BASE}/users/authenticated", cookies=cookies, timeout=10).json()
            user_id = me.get("id")
            if not user_id:
                return {}
            profile = self.session.get(f"{self.BASE}/users/{user_id}", timeout=10).json()
            currency = self.session.get(
                f"{self.ECONOMY}/users/{user_id}/currency", cookies=cookies, timeout=10
            ).json()
            return {
                "id": str(user_id),
                "displayName": profile.get("displayName", ""),
                "robux": currency.get("robux", 0),
            }
        except requests.RequestException as exc:
            logger.warning("roblox api error: {}", exc)
            return {}

    def validate_cookie(self, roblosecurity: str) -> bool:
        cookies = {".ROBLOSECURITY": roblosecurity}
        try:
            resp = self.session.get(f"{self.BASE}/users/authenticated", cookies=cookies, timeout=8)
            return resp.status_code == 200
        except requests.RequestException:
            return False