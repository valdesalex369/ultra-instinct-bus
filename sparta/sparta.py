"""SPARTA — the local campus heartbeat. Small, disciplined, always on.

Rungs:
  python sparta.py hello    -> hello world: identity + environment check + first local heartbeat
  python sparta.py beat     -> one cycle: solana watch + kraken tape (+optional read-only portfolio)
  python sparta.py loop     -> beat every N minutes (default 60)

What this file can NEVER do: place orders, withdraw, sign Solana transactions,
or store secrets. Kraken private access is READ-ONLY (Balance) and only if
KRAKEN_KEY / KRAKEN_SECRET env vars exist. Repos are public: no keys in files.

Bus I/O: works on a LOCAL git clone of ultra-instinct-bus. Set its path in
sparta/config.json ("bus_repo"). Outbox: drop *_{seat}_{seq}.json files into
sparta/outbox/ and the next beat commits+pushes them — that is the ChatGPT line.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
CFG_PATH = HERE / "config.json"
STATE_PATH = HERE / "state.json"
HIST_PATH = HERE / "history.jsonl"
OUTBOX = HERE / "outbox"
UA = {"User-Agent": "SPARTA/1.0"}
SOL_RPC = "https://api.mainnet-beta.solana.com"
KRAKEN_PUBLIC = "https://api.kraken.com/0/public"
KRAKEN_PRIVATE = "https://api.kraken.com"
SPL_TOKEN_PROGRAM = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"

DEFAULTS = {
    "bus_repo": "",  # e.g. C:/Users/alex/ultra-instinct-bus  (local clone)
    "watch_address": "FvUwXJ9T34oock3kv6CThyq1wNjA4Kf4uxPB534YyQBw",
    "push": False,   # set true once hello-world is green and you trust the loop
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def cfg() -> dict:
    c = dict(DEFAULTS)
    if CFG_PATH.exists():
        c.update(json.loads(CFG_PATH.read_text()))
    return c


def get(url: str, timeout: int = 20) -> dict:
    with urlopen(Request(url, headers=UA), timeout=timeout) as res:
        return json.loads(res.read().decode())


def sol_rpc(method: str, params: list) -> dict:
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = Request(SOL_RPC, data=body, headers={**UA, "Content-Type": "application/json"})
    with urlopen(req, timeout=25) as res:
        return json.loads(res.read().decode())


# ---------- senses (all read-only, all keyless unless noted) ----------

def solana_watch(address: str) -> dict:
    """Wallet + SPL token accounts = the pump.fun portfolio. Public chain data."""
    bal = sol_rpc("getBalance", [address])
    lamports = (bal.get("result") or {}).get("value")
    toks = sol_rpc(
        "getTokenAccountsByOwner",
        [address, {"programId": SPL_TOKEN_PROGRAM}, {"encoding": "jsonParsed"}],
    )
    holdings = []
    for acc in (toks.get("result") or {}).get("value") or []:
        info = (((acc.get("account") or {}).get("data") or {}).get("parsed") or {}).get("info") or {}
        amt = (info.get("tokenAmount") or {})
        if float(amt.get("uiAmount") or 0) > 0:
            holdings.append({"mint": info.get("mint"), "uiAmount": amt.get("uiAmount")})
    return {
        "address": address,
        "sol": round((lamports or 0) / 1_000_000_000, 6),
        "tokens": holdings,
        "mode": "watch-only",
        "signing": "never",
    }


def kraken_tape() -> list[dict]:
    body = get(KRAKEN_PUBLIC + "/Ticker?pair=XBTUSD,ETHUSD,SOLUSD")
    result = body.get("result") or {}
    alias = {"XXBTZUSD": "BTC", "XETHZUSD": "ETH", "SOLUSD": "SOL"}
    out = []
    for key, sym in alias.items():
        row = result.get(key)
        if row:
            out.append({"symbol": sym, "price": float(row["c"][0]), "source": "Kraken"})
    return out


def kraken_portfolio() -> dict:
    """READ-ONLY Balance. Key must be created with query-only permissions.
    Never logs secrets. If no env keys: reports DISCONNECTED, does nothing."""
    key, secret = os.environ.get("KRAKEN_KEY"), os.environ.get("KRAKEN_SECRET")
    if not key or not secret:
        return {"status": "DISCONNECTED", "hint": "set KRAKEN_KEY/KRAKEN_SECRET (read-only key)"}
    path = "/0/private/Balance"
    nonce = str(int(time.time() * 1000))
    data = {"nonce": nonce}
    post = urllib.parse.urlencode(data)
    sha = hashlib.sha256((nonce + post).encode()).digest()
    sig = hmac.new(base64.b64decode(secret), path.encode() + sha, hashlib.sha512)
    req = Request(
        KRAKEN_PRIVATE + path,
        data=post.encode(),
        headers={"API-Key": key, "API-Sign": base64.b64encode(sig.digest()).decode(), **UA},
    )
    with urlopen(req, timeout=20) as res:
        body = json.loads(res.read().decode())
    if body.get("error"):
        return {"status": "ERROR", "error": body["error"]}
    balances = {k: v for k, v in (body.get("result") or {}).items() if float(v) > 0}
    return {"status": "CONNECTED", "balances": balances, "permissions_used": "read-only Balance"}


# ---------- bus ----------

def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()[:200]}")
    return r.stdout.strip()


def bus_commit(config: dict, files: list[Path], message: str) -> str:
    repo = Path(config["bus_repo"])
    if not config["bus_repo"] or not repo.exists():
        return "bus: no local clone configured (set bus_repo in sparta/config.json)"
    git(repo, "pull", "--rebase", "origin", "main")
    for f in files:
        sub = "sparta" if f == STATE_PATH else "messages"
        name = "latest.json" if f == STATE_PATH else f.name
        dest = repo / sub / f.name if f.is_relative_to(repo) else repo / sub / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not f.is_relative_to(repo):
            dest.write_text(f.read_text())
        git(repo, "add", str(dest.relative_to(repo)))
    if not git(repo, "status", "--porcelain"):
        return "bus: no change"
    git(repo, "commit", "-m", message)
    if config.get("push"):
        git(repo, "push", "origin", "main")
        return "bus: committed+pushed"
    return "bus: committed locally (push=false)"


# ---------- rungs ----------

def hello() -> None:
    print("SPARTA online. Campus seat: local runner. Signer: Alex. Orders: never.")
    print(f"python: {sys.version.split()[0]}")
    c = cfg()
    print(f"bus_repo: {c['bus_repo'] or '(not set — bus writes disabled)'}")
    print(f"watch: {c['watch_address']}")
    print(f"kraken portfolio: {'env keys present' if os.environ.get('KRAKEN_KEY') else 'DISCONNECTED (fine for hello)'}")
    STATE_PATH.write_text(json.dumps({"hello": now(), "python": sys.version}, indent=2))
    print(f"state written: {STATE_PATH}")
    print("Next: python sparta.py beat   (add --offline to skip network)")


def beat(offline: bool = False) -> dict:
    c = cfg()
    errors, watch, tape, portfolio = [], None, [], {"status": "SKIPPED"}
    if not offline:
        try:
            watch = solana_watch(c["watch_address"])
        except (HTTPError, URLError, TimeoutError, ValueError, KeyError, TypeError) as e:
            errors.append(f"solana: {type(e).__name__}")
        try:
            tape = kraken_tape()
        except (HTTPError, URLError, TimeoutError, ValueError, KeyError, TypeError) as e:
            errors.append(f"kraken-public: {type(e).__name__}")
        try:
            portfolio = kraken_portfolio()
        except (HTTPError, URLError, TimeoutError, ValueError, KeyError, TypeError) as e:
            portfolio = {"status": "ERROR", "error": type(e).__name__}
            errors.append(f"kraken-private: {type(e).__name__}")
    payload = {
        "at": now(), "beat": "sparta", "watch": watch,
        "tape": tape, "krakenPortfolio": portfolio,
        "liveOrders": False, "errors": errors,
    }
    STATE_PATH.write_text(json.dumps(payload, indent=2) + "\n")
    with HIST_PATH.open("a") as fh:
        fh.write(json.dumps(payload, separators=(",", ":")) + "\n")
    # outbox: the ChatGPT line. Drop a message JSON here; the beat mails it.
    mailed = []
    OUTBOX.mkdir(exist_ok=True)
    for f in sorted(OUTBOX.glob("*.json")):
        json.loads(f.read_text())  # validate; malformed JSON raises and stops mailing
        mailed.append(f)
    bus_result = "bus: skipped (offline)" if offline else None
    if not offline:
        try:
            files = [STATE_PATH] + mailed
            bus_result = bus_commit(c, files, f"sparta beat {payload['at'][:16]}")
            for f in mailed:
                (HERE / "sent").mkdir(exist_ok=True)
                f.rename(HERE / "sent" / f.name)
        except (RuntimeError, ValueError) as e:
            bus_result = f"bus: {type(e).__name__} {str(e)[:160]}"
    payload["bus"] = bus_result
    print(json.dumps(payload, indent=2)[:3000])
    return payload


def loop(minutes: int) -> None:
    print(f"SPARTA loop: beat every {minutes} min. Ctrl+C to stop. Orders: never.")
    while True:
        try:
            beat()
        except Exception as e:  # the loop must never die silently
            print(f"[{now()}] beat failed: {type(e).__name__} {e}")
        time.sleep(minutes * 60)


if __name__ == "__main__":
    args = sys.argv[1:]
    cmd = args[0] if args else "hello"
    if cmd == "hello":
        hello()
    elif cmd == "beat":
        beat(offline="--offline" in args)
    elif cmd == "loop":
        mins = int(args[args.index("--minutes") + 1]) if "--minutes" in args else 60
        loop(mins)
    else:
        print("usage: sparta.py [hello|beat|loop] [--offline] [--minutes N]")
