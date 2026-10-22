# Contributing to roblox-account-switcher

Thanks for helping improve the multi-account switcher for Roblox.

## Development setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m rasm.main
```

## Guidelines

- Keep the vault encrypted at rest — never log raw `.ROBLOSECURITY` cookies.
- New Roblox endpoints go in `src/rasm/services/roblox_api.py`.
- UI changes belong in `src/rasm/ui/`; keep it CustomTkinter-only.
- Add a test under `tests/` for anything touching `core/` or `utils/`.

## Pull requests

1. Fork and branch from `main`.
2. Run `pytest -q` before opening a PR.
3. Describe which Roblox client version you tested against.