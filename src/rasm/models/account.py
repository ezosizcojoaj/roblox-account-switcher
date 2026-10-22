from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class RobloxAccount(BaseModel):
    user_id: str
    username: str
    display_name: str = ""
    roblosecurity: str = Field(..., repr=False)
    avatar_url: Optional[str] = None
    robux: int = 0
    is_premium: bool = False
    created_at: int = 0
    last_used: int = 0
    last_synced: int = 0
    tags: list[str] = Field(default_factory=list)

    @property
    def label(self) -> str:
        return self.display_name or self.username