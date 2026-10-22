from __future__ import annotations

import subprocess
from pathlib import Path

from loguru import logger

from rasm.config.settings import RobloxConfig


class RobloxLauncher:
    """Spawns the Roblox client with a specific account cookie injected."""

    def __init__(self, config: RobloxConfig) -> None:
        self.config = config

    def launch_with_cookie(self, roblosecurity: str) -> None:
        # Roblox reads the cookie from the Windows credential manager; we push it
        # through the launcher protocol and let the client pick it up.
        uri = f"{self.config.launch_uri}?cookie={roblosecurity}"
        if self.config.browser_launch:
            subprocess.Popen(["cmd", "/c", "start", "", uri], shell=False)
        else:
            self._direct_launch(uri)

    def _direct_launch(self, uri: str) -> None:
        exe = Path.home() / "AppData/Local/Roblox/Versions"
        candidates = list(exe.glob("version-*/RobloxPlayerBeta.exe"))
        if not candidates:
            raise FileNotFoundError("RobloxPlayerBeta.exe not found")
        logger.debug("launching {}", candidates[0])
        subprocess.Popen([str(candidates[0]), "-task", "StartGame", uri])