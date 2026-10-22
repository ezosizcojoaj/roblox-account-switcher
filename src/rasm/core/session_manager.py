from __future__ import annotations

import time
from typing import Optional

import psutil
from loguru import logger

from rasm.core.account_store import AccountStore
from rasm.config.settings import RobloxConfig
from rasm.models.account import RobloxAccount
from rasm.services.roblox_api import RobloxApiClient
from rasm.services.launcher import RobloxLauncher


class SessionManager:
    """Handles switching between accounts by killing/relaunching the Roblox client."""

    def __init__(self, store: AccountStore, config: RobloxConfig) -> None:
        self.store = store
        self.config = config
        self.api = RobloxApiClient(user_agent=config.user_agent)
        self.launcher = RobloxLauncher(config)

    def refresh_account(self, account: RobloxAccount) -> RobloxAccount:
        info = self.api.fetch_user_info(account.roblosecurity)
        account.display_name = info.get("displayName", account.display_name)
        account.robux = info.get("robux", account.robux)
        account.last_synced = int(time.time())
        self.store.upsert(account)
        return account

    def switch_to(self, user_id: str) -> bool:
        account = self.store.get(user_id)
        if account is None:
            logger.warning("switch failed: unknown account {}", user_id)
            return False

        self._kill_roblox_processes()
        time.sleep(1.5)

        try:
            self.launcher.launch_with_cookie(account.roblosecurity)
            account.last_used = int(time.time())
            self.store.upsert(account)
            logger.info("switched to {} ({})", account.username, account.user_id)
            return True
        except Exception as exc:  # noqa: BLE001
            logger.error("launch failed: {}", exc)
            return False

    @staticmethod
    def _kill_roblox_processes() -> None:
        for proc in psutil.process_iter(["name"]):
            name: Optional[str] = proc.info.get("name") or ""
            if name.lower().startswith("robloxplayerbeta"):
                try:
                    proc.terminate()
                except psutil.Error:
                    pass