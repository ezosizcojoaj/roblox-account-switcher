from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PathsConfig(BaseModel):
    vault_dir: Path = Field(default=Path("vault"))
    log_dir: Path = Field(default=Path("logs"))
    cookie_jar: Path = Field(default=Path("vault/cookies.bin"))


class CryptoConfig(BaseModel):
    secret_key: str = Field(default="change-me-on-first-run")
    cipher: Literal["AES-256-GCM"] = "AES-256-GCM"


class RobloxConfig(BaseModel):
    launch_uri: str = "roblox://experiences/start"
    browser_launch: bool = True
    keep_alive_seconds: int = 30
    user_agent: str = "WEAO-3PService/0.1 roblox-account-switcher/2.4.1"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="RASM_", env_file=".env", extra="ignore")

    paths: PathsConfig = PathsConfig()
    crypto: CryptoConfig = CryptoConfig()
    roblox: RobloxConfig = RobloxConfig()
    theme: Literal["dark", "light"] = "dark"


def load_settings() -> Settings:
    return Settings()