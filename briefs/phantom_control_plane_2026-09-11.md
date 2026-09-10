# Phantom control plane — 2026-09-11

Build here: `valdesalex369/ultra-instinct-bus`.
Do not wait for a Grok “Phantom connector.” There is not one.

## What is already wired

- Public SOL watch: `FvUwXJ9T34oock3kv6CThyq1wNjA4Kf4uxPB534YyQBw`
- Mode: read-only (`desk/lead/WALLET.md`)
- Constitution: no agent signs; Alex countersigns (`README.md` Reality Clause)
- Phantom seat card already says “Never signs a tx.”

## Why perps were invisible

Phantom perps settle on Hyperliquid against the Ethereum address inside the same Phantom account, not the Solana address in WALLET.md.

Fix: add the 0x to `desk/lead/WALLET.md`, then:

```
python3 tools/recon_book.py --hl 0xYOUR_EVM
```

Query native + HIP-3 (`xyz` and `*`) because oil and NVDA on Phantom are HIP-3 markets.

## Localhost control plane

1. Read bus (this script)
2. Localhost signer UI on 127.0.0.1 with Phantom inject + click Approve
3. Policy gate from desk/STATE.json — human countersign required

No unattended market order from an LLM. No seed in the repo.
