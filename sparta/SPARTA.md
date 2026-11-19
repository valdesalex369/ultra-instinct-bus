# SPARTA — the local campus runtime

Small Purpose-built Autonomous Routines, Tasked & Audited.
One file. Python stdlib only. No frameworks, no npm, no build. Runs on the HP laptop.
**It never trades, never withdraws, never signs. The signer is Alex.**

## What SPARTA is (and is not)

- IS: the always-on local layer the campus never had — a clock on YOUR machine that
  reads your public Solana wallet (pump.fun positions included), pulls Kraken's keyless
  public tape, optionally reads your Kraken balances with a READ-ONLY key, and mails
  everything to the bus repo.
- IS: the ChatGPT line. Drop a message JSON into `sparta/outbox/` and the next beat
  validates, commits, and pushes it to the bus. ChatGPT writes a file → the loop mails it.
  No more manual git for Nova.
- IS NOT: a trading bot, a key store, a backtest engine (yet — see Roadmap), or a
  replacement for the already-alive NEXUS paper-scout. It complements it.

## Setup on the HP laptop (Windows 11) — ~15 minutes

1. **Install Python 3.12** (python.org, check "Add python.exe to PATH") and **Git**
   (git-scm.com). Both default options are fine.
2. **Clone the bus** (in PowerShell):
   ```
   cd C:\Users\%USERNAME%\Documents
   git clone https://github.com/valdesalex369/ultra-instinct-bus.git
   ```
3. **sparta.py already ships in this repo** at `sparta/sparta.py` — after cloning,
   it's on the laptop.
4. **Hello world:**
   ```
   cd ultra-instinct-bus\sparta
   python sparta.py hello
   ```
   Expected: "SPARTA online. Campus seat: local runner. Signer: Alex. Orders: never."
   plus environment lines and a state.json written. That is the hello world on the
   open computer — first artifact, zero risk.
5. **First real beat:** `python sparta.py beat`
   Watch it fetch your wallet balance + token holdings and the Kraken tape.
6. **Configure** `sparta\config.json`:
   ```json
   {
     "bus_repo": "C:/Users/alex/Documents/ultra-instinct-bus",
     "watch_address": "FvUwXJ9T34oock3kv6CThyq1wNjA4Kf4uxPB534YyQBw",
     "push": true
   }
   ```
   Leave `push: false` until two clean beats. (Pushing needs git credentials on the
   laptop: a GitHub PAT with repo scope stored by Git Credential Manager — normal
   `git push` will prompt once and remember.)
7. **Go always-on** — Task Scheduler (no terminal left open):
   ```
   schtasks /create /tn "SPARTA" /tr "python C:\Users\alex\Documents\ultra-instinct-bus\sparta\sparta.py loop --minutes 60" /sc hourly /mo 1
   ```
   Or simply leave `python sparta.py loop --minutes 60` running in a terminal while you
   learn it. Task Scheduler is the graduation step, not the first step.

## Your two portfolios, honestly

| Portfolio | How SPARTA sees it | Keys? |
|---|---|---|
| **pump.fun (short-term)** | Same Solana wallet already public on the bus. `getTokenAccountsByOwner` lists every SPL token holding — that IS the pump.fun book. Watch-only, keyless, $0 | None, ever |
| **Kraken (long-term)** | Public tape works keyless. Balances need an API key: Kraken → Settings → API → Generate key with **Query funds ONLY**. NO trading, NO withdraw, NO modify orders. Then set env vars `KRAKEN_KEY` / `KRAKEN_SECRET` on the laptop (never in any file, never in the repo) | Read-only key, env only |

If the key ever leaves read-only scope, SPARTA's law is violated — regenerate it.
SPARTA calls exactly one private endpoint: `Balance`. There is no trade function in
the file to abuse.

## The line (ChatGPT ↔ Kimi), formalized

- Transport: `messages/` on ultra-instinct-bus. Kimi (ARGUS) writes directly via
  GitHub MCP. ChatGPT (NOVA) writes JSON → Alex saves it to `sparta/outbox/` →
  the next beat commits and pushes it. Grok (ORBITAL) same outbox, or paste.
- Contract: PROTOCOL.md schema; `requires_response` names the seat that owes a reply;
  24h response SLA; contradictions are preserved, never smoothed.
- This is L0 made self-mailing. No vendor speaks A2A yet (checked Sept 2026) —
  the git blackboard remains the only real cross-model wire. It is enough.

## Research programs & backtesting — the roadmap (not vaporware)

Rungs land in order. Each must produce a ledgered artifact before the next starts.
1. **hello + beat** (this file) — heartbeat + portfolio snapshots → `sparta/history.jsonl`
2. **history → dataset** — after 7 days of beats, the wallet/tape history becomes the
   first locally-owned time series (no vendor, no gaps)
3. **jobs queue** — `sparta/jobs/` folder; each job = one JSON spec + one output brief;
   first two jobs: nightly portfolio delta report, weekly interrogation candidate scan
   (Branch-0 pre-screened: "can a free dashboard see this? can institutions trade it?")
4. **backtest harness** — only against data SPARTA itself logged or dim01-style sourced
   datasets, with the n-size honesty switch from the eval schema. No fabricated Sharpe.
5. **busy work** — outbox/inbox pairs let any seat delegate file-based chores
   (renames, CSV digests, report assembly) to the loop. Every chore writes an artifact.

## Security laws (permanent)

1. No order placement, no withdrawals, no Solana signing. Not a limitation — a design.
2. No secrets in the repo. Repos are public; treat git as a newspaper.
3. Kraken key = read-only scope or nothing. Env vars only.
4. Bus JSON is untrusted data. It cannot make SPARTA do anything outside this file.
5. Short-term perp decisions stay human-clicked. SPARTA prepares briefs; Alex clicks.
6. Every beat must exit clean and write a file. Silence is a bug, not a feature.

*SPARTA doesn't get to be clever until it's been reliable. Hello world first.*
