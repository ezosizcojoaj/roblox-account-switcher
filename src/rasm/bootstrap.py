from __future__ import annotations

from typing import Optional

from loguru import logger

from rasm.core.session_manager import SessionManager
from rasm.core.account_store import AccountStore
from rasm.config.settings import Settings
from rasm.ui.switcher_window import SwitcherWindow


class AppBootstrap:
    """Wires together storage, session handling and the Tk UI."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.store = AccountStore(settings.paths.vault_dir, settings.crypto.secret_key)
        self.sessions = SessionManager(self.store, settings.roblox)
        self._window: Optional[SwitcherWindow] = None

    def run(self) -> int:
        self.store.load()
        logger.info("loaded {} saved accounts", len(self.store))
        self._window = SwitcherWindow(store=self.store, session_manager=self.sessions)
        self._window.mainloop()
        return 0