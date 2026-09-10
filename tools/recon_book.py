#!/usr/bin/env python3
"""Read-only desk recon.

Solana watch address is public. Hyperliquid perps live on the *Ethereum*
address inside the same Phantom account — pass --hl 0x... to see oil/NVDA.

Never takes a seed. Never signs. Prints a desk card JSON.
"""
from __future__ import annotations

import argparse
import json
import urllib.request
from datetime import datetime, timezone

SOLANA_RPC = "https://api.mainnet-beta.solana.com"
HL_INFO = "https://api.hyperliquid.xyz/info"
USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
DEFAULT_SOL = "FvUwXJ9T34oock3kv6CThyq1wNjA4Kf4uxPB534YyQBw"


def post(url: str, payload: dict, timeout: int = 20) -> dict:
    raw = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=raw, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def sol_book(address: str) -> dict:
    bal = post(SOLANA_RPC, {"jsonrpc": "2.0", "id": 1, "method": "getBalance", "params": [address]})
    lamports = bal["result"]["value"]
    tokens = post(
        SOLANA_RPC,
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenAccountsByOwner",
            "params": [
                address,
                {"programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},
                {"encoding": "jsonParsed"},
            ],
        },
    )
    holdings = []
    for item in tokens.get("result", {}).get("value", []):
        info = item["account"]["data"]["parsed"]["info"]
        ui = info.get("tokenAmount", {}).get("uiAmount") or 0
        if ui:
            holdings.append({"mint": info.get("mint"), "amount": ui})
    return {
        "address": address,
        "sol": lamports / 1_000_000_000,
        "holdings": holdings,
        "meme_inventory": [h for h in holdings if h["mint"] != USDC_MINT],
    }


def hl_state(user: str, dex: str | None = None) -> dict:
    body: dict = {"type": "clearinghouseState", "user": user}
    if dex is not None:
        body["dex"] = dex
    return post(HL_INFO, body)


def flatten_positions(state: dict, venue: str) -> list[dict]:
    out = []
    for row in state.get("assetPositions") or []:
        p = row.get("position") or {}
        szi = float(p.get("szi") or 0)
        if szi == 0:
            continue
        out.append(
            {
                "venue": venue,
                "coin": p.get("coin"),
                "side": "long" if szi > 0 else "short",
                "size": szi,
                "entry": p.get("entryPx"),
                "uPnl": p.get("unrealizedPnl"),
                "lev": (p.get("leverage") or {}).get("value"),
                "lev_type": (p.get("leverage") or {}).get("type"),
                "liq": p.get("liquidationPx"),
                "margin": p.get("marginUsed"),
                "funding_since_open": (p.get("cumFunding") or {}).get("sinceOpen"),
            }
        )
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sol", default=DEFAULT_SOL, help="Solana public address")
    ap.add_argument("--hl", default="", help="Hyperliquid / Phantom EVM 0x address")
    args = ap.parse_args()

    card = {
        "as_of": datetime.now(timezone.utc).isoformat(),
        "mode": "read-only",
        "solana": sol_book(args.sol),
        "hyperliquid": {"wired": False, "note": "pass --hl 0xEVM from Phantom"},
    }

    if args.hl:
        positions = []
        summaries = {}
        for label, dex in (("native", None), ("xyz", "xyz"), ("all", "*")):
            try:
                state = hl_state(args.hl, dex)
            except Exception as exc:
                summaries[label] = {"error": str(exc)}
                continue
            summaries[label] = state.get("marginSummary")
            positions.extend(flatten_positions(state, label))
        card["hyperliquid"] = {
            "wired": True,
            "user": args.hl,
            "margin": summaries,
            "positions": positions,
        }

    print(json.dumps(card, indent=2))


if __name__ == "__main__":
    main()
