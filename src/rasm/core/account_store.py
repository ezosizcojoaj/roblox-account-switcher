from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator, Optional

from loguru import logger

from rasm.core.crypto import VaultCipher
from rasm.models.account import RobloxAccount


class AccountStore:
    """Encrypted, on-disk store of Roblox accounts and their cookies."""

    def __init__(self, vault_dir: Path, secret_key: str) -> None:
        self.vault_dir = vault_dir
        self.vault_dir.mkdir(parents=True, exist_ok=True)
        self.index_file = vault_dir / "accounts.enc"
        self._cipher = VaultCipher(secret_key)
        self._accounts: dict[str, RobloxAccount] = {}

    def __len__(self) -> int:
        return len(self._accounts)

    def __iter__(self) -> Iterator[RobloxAccount]:
        return iter(self._accounts.values())

    def load(self) -> None:
        if not self.index_file.exists():
            return
        try:
            raw = self._cipher.decrypt(self.index_file.read_bytes())
            payload = json.loads(raw)
            self._accounts = {
                a["user_id"]: RobloxAccount.model_validate(a) for a in payload
            }
        except Exception as exc:  # noqa: BLE001
            logger.error("failed to load vault: {}", exc)

    def save(self) -> None:
        payload = [a.model_dump() for a in self._accounts.values()]
        blob = self._cipher.encrypt(json.dumps(payload).encode("utf-8"))
        self.index_file.write_bytes(blob)

    def upsert(self, account: RobloxAccount) -> None:
        self._accounts[account.user_id] = account
        self.save()

    def remove(self, user_id: str) -> bool:
        if user_id in self._accounts:
            del self._accounts[user_id]
            self.save()
            return True
        return False

    def get(self, user_id: str) -> Optional[RobloxAccount]:
        return self._accounts.get(user_id)