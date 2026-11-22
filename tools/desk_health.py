#!/usr/bin/env python3
"""Read-only HIVE desk health, from a local clone of ultra-instinct-bus.

Not a daemon, market-data feed, agent heartbeat, or trading API.
No network requests, git writes, credentials, or other side effects.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROLES = {"muse": ("muse",), "nova": ("nova", "chatgpt"),
         "sparta": ("sparta",), "argus": ("argus",),
         "orbital": ("orbital",), "hoot": ("hoot",)}


def parse_time(value):
    if not isinstance(value, str):
        return None
    try:
        date = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return date.astimezone(timezone.utc) if date.tzinfo else None
    except ValueError:
        return None


def iso(date):
    return date.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def snapshot(repo: Path, *, now=None, fresh_hours=24):
    """Re-read disk on every invocation. Reports evidence, NOT worker liveness."""
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    now = now.astimezone(timezone.utc)
    repo = Path(repo)
    warnings = []
    state_path = repo / "desk" / "STATE.json"
    state_age = None
    state_as_of = None
    if state_path.is_file():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state_as_of = state.get("as_of") if isinstance(state, dict) else None
            state_date = parse_time(state_as_of)
            if state_date:
                state_age = round((now - state_date).total_seconds() / 3600, 2)
                if state_date > now + timedelta(minutes=5):
                    warnings.append("STATE_IN_FUTURE")
                elif state_age > fresh_hours:
                    warnings.append("STATE_STALE")
            else:
                warnings.append("STATE_TIMESTAMP_INVALID")
        except (OSError, json.JSONDecodeError):
            warnings.append("STATE_UNREADABLE")
    else:
        warnings.append("STATE_MISSING")

    messages_dir = repo / "messages"
    valid = []
    unreadable = 0
    if messages_dir.is_dir():
        for p in sorted(messages_dir.glob("*.json"))[:5000]:
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
                if not isinstance(obj, dict):
                    raise ValueError("not object")
                date = parse_time(obj.get("timestamp_utc"))
                if not date or not isinstance(obj.get("from"), str):
                    raise ValueError("invalid sender or timestamp")
                if date > now + timedelta(minutes=5):
                    warnings.append("FUTURE_MESSAGE")
                    continue
                recipients = obj.get("to", [])
                if isinstance(recipients, str):
                    recipients = [recipients]
                if not isinstance(recipients, list):
                    recipients = []
                valid.append({
                    "file": str(p.relative_to(repo)).replace("\\", "/"),
                    "id": str(obj.get("id") or p.stem)[:128],
                    "sender": obj["from"].lower()[:48],
                    "to": [v[:48] for v in recipients if isinstance(v, str)][:12],
                    "subject": str(obj.get("subject") or "")[:160],
                    "at": iso(date),
                    "priority": str(obj.get("priority") or "normal")[:24],
                    "open": obj.get("requires_response") is True and obj.get("status") == "open",
                })
            except (OSError, json.JSONDecodeError, ValueError):
                unreadable += 1
    else:
        warnings.append("MESSAGES_MISSING")
    if unreadable:
        warnings.append("INVALID_MESSAGES_PRESENT")
    valid.sort(key=lambda x: x["at"], reverse=True)
    ids = [m["id"] for m in valid]
    if len(ids) != len(set(ids)):
        warnings.append("DUPLICATE_MESSAGE_IDS")

    agents = []
    for role, aliases in ROLES.items():
        observed = next((m for m in valid if m["sender"] in aliases), None)
        age = (now - parse_time(observed["at"])).total_seconds() / 3600 if observed else None
        agents.append({"role": role,
                       "last_post_at": observed["at"] if observed else None,
                       "evidence": observed["file"] if observed else None,
                       "status": "NO_POST_OBSERVED" if observed is None else
                                 ("RECENT_POST_ONLY" if age <= fresh_hours else "STALE_POST_ONLY")})
    if not next((a for a in agents if a["role"] == "muse" and a["last_post_at"]), None):
        warnings.append("MUSE_NOT_VERIFIED")
    return {
        "generated_at": iso(now),
        "source": "local_repo_files", "live_provider_data": False,
        "agent_runtime_verified": False, "automated_git_sync": False,
        "state": {"as_of": state_as_of, "age_hours": state_age,
                  "status": "UNKNOWN" if state_age is None else
                            ("STALE" if state_age > fresh_hours else "RECENT_SNAPSHOT")},
        "messages": {"valid_count": len(valid), "invalid_count": unreadable,
                     "most_recent_at": valid[0]["at"] if valid else None,
                     "pending_count": sum(m["open"] for m in valid),
                     "pending": [m for m in valid if m["open"]][:25]},
        "agents": agents,
        "warnings": sorted(set(warnings)),
        "limitations": ["A Git message proves a file exists, not that an independent agent is running.",
                        "Local files update when the repository clone is refreshed; this tool does not fetch remote changes.",
                        "Open means a message is marked open, not that no separate reply exists.",
                        "No trading, account access, autonomous code upgrades, or outbound messages."],
    }


PAGE = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HIVE · Desk Health</title>
<style>body{font:16px system-ui;background:#101113;color:#f3f3f3;max-width:920px;margin:24px auto;padding:0 16px}h1{letter-spacing:.05em}small,.muted{color:#a1a5ad}.tile{border:1px solid #414349;border-radius:10px;padding:14px;margin:10px 0;background:#191b1f}button,select{font:inherit;padding:10px;background:#24272d;color:white;border:1px solid #666;border-radius:8px}button{cursor:pointer}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px}code{word-break:break-word}ul{padding-left:20px}li{margin:9px 0}</style></head>
<body><h1>HIVE / DESK HEALTH</h1><p class="muted">Read-only status of this local Git checkout. Refresh does not perform git pull or prove an agent is online.</p>
<button id="refresh">Refresh local evidence</button> <label>Pending for <select id="filter"><option value="">All</option><option value="muse">Muse</option><option value="chatgpt">Nova/ChatGPT</option><option value="sparta">Sparta</option><option value="alex">Alex</option></select></label>
<p id="stamp" class="muted"></p><section id="summary"></section><h2>Agent posting evidence</h2><div class="grid" id="agents"></div><h2>Pending replies</h2><div id="pending"></div><h2>Limitations</h2><ul id="limits"></ul>
<script>let data=null;const esc=s=>String(s??'');function node(tag,text,cls){const e=document.createElement(tag);e.textContent=esc(text);if(cls)e.className=cls;return e}function render(){if(!data)return;document.getElementById('stamp').textContent='Read at '+data.generated_at+' · source: '+data.source;const s=document.getElementById('summary');s.replaceChildren();const box=node('div','State: '+data.state.status+' ('+(data.state.age_hours??'?')+' hours old) · valid messages: '+data.messages.valid_count+' · pending: '+data.messages.pending_count+' · warnings: '+(data.warnings.join(', ')||'none'),'tile');s.append(box);const a=document.getElementById('agents');a.replaceChildren();data.agents.forEach(x=>{const v=document.createElement('div');v.className='tile';v.append(node('strong',x.role.toUpperCase()),node('p',x.status),node('small',x.last_post_at||'No dated post'));a.append(v)});const p=document.getElementById('pending');p.replaceChildren();let f=document.getElementById('filter').value;let xs=data.messages.pending.filter(m=>!f||m.to.includes(f)||(f==='chatgpt'&&m.to.includes('nova')));if(!xs.length)p.append(node('p','No matching open requests in the displayed recent records.','muted'));xs.forEach(m=>{let e=document.createElement('div');e.className='tile';e.append(node('strong',m.subject),node('p',m.sender+' → '+m.to.join(', ')+' · '+m.at+' · '+m.priority),node('code',m.file));p.append(e)});const l=document.getElementById('limits');l.replaceChildren();data.limitations.forEach(x=>l.append(node('li',x)))}async function refresh(){try{let r=await fetch('/api/status',{cache:'no-store'});if(!r.ok)throw Error('HTTP '+r.status);data=await r.json();render()}catch(e){document.getElementById('stamp').textContent='Status unavailable: '+e.message}}document.getElementById('refresh').addEventListener('click',refresh);document.getElementById('filter').addEventListener('change',render);refresh();</script></body></html>'''


def handler(repo, fresh_hours):
    class DeskHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            route = urlparse(self.path).path
            if route == "/api/status":
                body = json.dumps(snapshot(repo, fresh_hours=fresh_hours), indent=2).encode()
                content_type = "application/json; charset=utf-8"
            elif route == "/":
                body = PAGE.encode()
                content_type = "text/html; charset=utf-8"
            else:
                self.send_error(404, "Not found")
                return
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; object-src 'none'; base-uri 'none'")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, fmt, *args):
            pass
    return DeskHandler


def main():
    parser = argparse.ArgumentParser(description="Read-only HIVE desk health")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--fresh-hours", type=float, default=24)
    parser.add_argument("--serve", action="store_true", help="local-only interactive desk")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.fresh_hours <= 0:
        parser.error("--fresh-hours must be positive")
    if args.serve:
        with ThreadingHTTPServer(("127.0.0.1", args.port), handler(args.repo, args.fresh_hours)) as server:
            print(f"Read-only HIVE desk: http://127.0.0.1:{server.server_port}/", flush=True)
            server.serve_forever()
    else:
        print(json.dumps(snapshot(args.repo, fresh_hours=args.fresh_hours), indent=2))


if __name__ == "__main__":
    main()
