# MUSE Desk — Operational Workflow v1.1

**Authority:** Alex (human principal) → Muse (sole chief of staff) → specialized agents. STEM is the deterministic authorization and budget gate. Sparta reviews, Nova verifies, Hunter/Argus gathers evidence, Nexus retains the ledger.

## Current reality

The repository contains real Git messages and an older desk/STATE.json, but this alone does **not** establish that Muse, Nova, or any worker is persistently online. Never infer live market/account state from desk/STATE.json without validating its `as_of` timestamp. Historical Orbital workflows are superseded by this document and PROTOCOL v1.1.

## Read-only desk

Run on a local clone:

```bash
python tools/desk_health.py --repo .                   # JSON status
python tools/desk_health.py --repo . --serve           # http://127.0.0.1:8765/
python -m unittest discover -s tests -p 'test_desk_health.py'
```

The interactive page supports Refresh and recipient filtering. Its source is local repository files; `git pull` is required to retrieve remote messages. `RECENT_POST_ONLY` is **not** proof of worker liveness. The endpoint does not touch wallets, accounts, exchange APIs, or external sites.

## Proposed verified handoff (not yet deployed)

1. Muse creates one bounded request, stamped with task ID, source, time and budget.
2. A separately authenticated Nova worker ingests it idempotently and replies with citations and limitations.
3. Sparta attempts to falsify it; `VETO` prevents promotion.
4. STEM verifies schema, provenance, idempotency, approvals and usage caps.
5. Muse closes the task and publishes a receipt referencing the actual review.
6. Alex approves any consequential external action through a trusted authenticated interface.

A message signed only by a JSON `from` field is insufficient identity proof. A claim of a live round trip requires an observed successful exchange between independently authenticated workers and a verifiable receipt.

## Release process

Code changes require an isolated branch, deterministic tests, review, and explicit human approval before merge/deploy. No self-modifying prompts, refusal-loop overrides, scheduled alert spam, auto trading, or automatic deployment.
