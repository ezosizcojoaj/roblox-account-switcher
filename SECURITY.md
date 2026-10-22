# Security Policy

## Reporting

If you find a vulnerability in roblox-account-switcher (e.g. vault decryption
bypass, cookie leak in logs, unsafe process handling), please open a private
security advisory on GitHub rather than a public issue.

## Scope

- `src/rasm/core/crypto.py` — vault encryption
- `src/rasm/core/account_store.py` — on-disk storage
- `src/rasm/services/launcher.py` — process spawning

## Handling of credentials

`.ROBLOSECURITY` cookies are equivalent to full account access. They are
stored encrypted (AES-256-GCM) inside `vault/accounts.enc` and are never
written to logs. The `vault/` directory is git-ignored by default.

## Disclaimer

This tool is provided for educational and personal-use purposes. Using it
to access accounts you do not own violates Roblox's Terms of Service.
Use at your own risk.