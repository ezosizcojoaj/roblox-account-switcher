from __future__ import annotations

import sys
from pathlib import Path

from loguru import logger

from rasm.bootstrap import AppBootstrap
from rasm.config.settings import load_settings


def _setup_logging(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    logger.add(log_dir / "rasm_{time:YYYYMMDD}.log", rotation="5 MB", retention="7 days")


def main() -> int:
    settings = load_settings()
    _setup_logging(settings.paths.log_dir)
    logger.info("roblox-account-switcher v{} starting", __import__("rasm").__version__)
    app = AppBootstrap(settings)
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())