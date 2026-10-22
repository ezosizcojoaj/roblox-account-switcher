from __future__ import annotations

import customtkinter as ctk

from rasm.core.account_store import AccountStore
from rasm.core.session_manager import SessionManager


class SwitcherWindow(ctk.CTk):
    def __init__(self, store: AccountStore, session_manager: SessionManager) -> None:
        super().__init__()
        self.store = store
        self.sessions = session_manager

        self.title("roblox-account-switcher")
        self.geometry("640x480")
        ctk.set_appearance_mode("dark")

        self._build_layout()

    def _build_layout(self) -> None:
        header = ctk.CTkLabel(self, text="Saved Accounts", font=("Segoe UI", 18, "bold"))
        header.pack(pady=12)

        self.list_frame = ctk.CTkScrollableFrame(self, width=580, height=340)
        self.list_frame.pack(padx=20, pady=8, fill="both", expand=True)

        self.refresh()

    def refresh(self) -> None:
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        for account in self.store:
            row = ctk.CTkFrame(self.list_frame)
            row.pack(fill="x", pady=4)
            label = ctk.CTkLabel(row, text=f"{account.label}  ·  {account.robux} R$")
            label.pack(side="left", padx=10)
            btn = ctk.CTkButton(
                row,
                text="Switch",
                width=90,
                command=lambda uid=account.user_id: self._on_switch(uid),
            )
            btn.pack(side="right", padx=10)

    def _on_switch(self, user_id: str) -> None:
        ok = self.sessions.switch_to(user_id)
        self.refresh()
        if not ok:
            ctk.CTkLabel(self, text="Switch failed — see logs").pack()