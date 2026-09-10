# BETA CAMPUS — Real Connection-Surface Map (September 2026)

Seats: ARGUS (Kimi/Moonshot, GitHub MCP + browser + search), NOVA (ChatGPT/OpenAI), ORBITAL (Grok/xAI), NEXUS (GitHub repo + Actions runner, Codex). Desk accounts: Robinhood, Phantom (Solana, watch address public in desk/STATE.json), Kraken (possible venue), GitHub public repos.

Honesty grades per MESH.md §3: **DISCONNECTED** = no credential; **CONFIGURED** = credential exists, nothing proven; **CONNECTED** = last successful real call with timestamp/artifact.

---

## 1. Robinhood (brokerage)

| Field | Value |
|---|---|
| Surface | Official Robinhood MCP servers (Trading + Banking), launched 2026-05-27, hosted at `https://agent.robinhood.com/mcp/trading`, OAuth login in-client. Documented clients incl. ChatGPT, Codex/Codex CLI, Claude Code/Desktop, Cursor, Grok. |
| What works today | Bus-ledgered: Alex completed OAuth 2026-09-09T15:05Z (`2026-09-09_chatgpt_002`); smoke test 2026-09-09T15:10Z — `get_accounts` returned 2 active brokerage accounts + 1 Agentic account; `get_portfolio` on the Agentic account returned structured portfolio/cash/buying-power fields. Zero write tools invoked. (`2026-09-09_chatgpt_003`) |
| Auth model | OAuth via Robinhood's own login flow; agent never handles the password. Trades allowed only inside a dedicated, separately funded **Agentic account**; all other accounts are read-only to the agent. Equities only at launch; options "later in beta." |
| Read vs write | Reads: LIVE_CONFIRMED (ledgered). Writes (order review/place): capability exists but UNTESTED and NOT AUTHORIZED; autonomy is "review before action" by default — keep it off. |
| Cost | Free (feature of a RH account in good standing). |
| Honesty grade | **CONNECTED (reads only)**. Writes: DISCONNECTED by policy. |
| Sources | gamut.so/mcp/payments-finance/robinhood (2026-06-24); truthifi.com/providermcps/robinhood-mcp (2026-06-18); vorplabs.com/agent-tools/robinhood-cli (2026-07-20); bus messages/2026-09-09_chatgpt_001..003. Note: a 2026-05-25 roundup (aifinhub.io) still claims "no official API/MCP" — stale, published 2 days before launch. The older **Crypto Trading API** (Ed25519 keys) still exists: robinhood.com/us/en/support/articles/crypto-api/. Unofficial libraries (robin_stocks etc.) remain TOS-risky. |

## 2. Kraken (possible venue)

| Field | Value |
|---|---|
| Surface | (a) Public REST + WebSocket v2 market data — no auth needed. (b) Private REST/WS/FIX with API keys. (c) **Official `krakenfx/kraken-cli`** — open-source Rust binary, 134 commands, built-in MCP server over stdio (`kraken mcp`), shipped ~2026-03; works with Claude Code, Codex, Cursor, Gemini CLI, Copilot, Goose. |
| What works today | Nothing configured on this desk. Public market data is reachable by anyone (e.g. from the NEXUS runner) with zero signup. |
| Auth model | API key + HMAC-SHA512; keys scope-able (read / trade / withdraw split; withdraw excluded by design on trade-only keys); IP whitelisting. kraken-cli MCP groups: `market` (no auth), `account` (read-only), `trade`/`funding`/`earn` (gated by `acknowledged=true` unless `--allow-dangerous`). |
| Read vs write | Public data: read, unauthenticated. Private: read/trade/withdraw separable per key. Paper-trading engine built into kraken-cli (`futures-paper`, `paper` groups need no auth). |
| Cost | Free data/API; Kraken Pro 0.25% maker / 0.40% taker entry tier. |
| Geo | US: every state **except New York and Maine**; US users can't access futures. 190+ countries, full EEA under MiCA. |
| Rate limits | Public ~1,200 req/min (burst ~20/s); private ~600 req/min. |
| Honesty grade | **DISCONNECTED** (no key, no campus artifact). Public market data: available but unused. |
| Sources | github.com/krakenfx/kraken-cli; awesomeagents.ai/news/kraken-cli-ai-agents-crypto-trading-mcp/ (2026-04-08); blog.cremonix.com/kraken-api-rate-limits-2026 (2026-04-10); buybitcoinsmart.com/exchanges/kraken (2026-08-23); coinbureau.com/review/gemini-vs-kraken (2026-09-03). |

## 3. Phantom / Solana (watch-only — no keys, no seeds, ever)

| Field | Value |
|---|---|
| Surface | (a) Public RPC `api.mainnet-beta.solana.com` (free, ~5-15 RPS). (b) Helius free tier (1M credits/mo, 10 RPS) + webhooks; **official Helius MCP server** (`helius-mcp` npm) + skills incl. Phantom dApp skill. (c) Solana web3.js `getBalance`/`getSignaturesForAddress`/`accountSubscribe`. (d) Off-the-shelf watcher bots (Telegram alerts, public-address only). |
| What works today | Bus-ledgered: ORBITAL read the watch address via public RPC 2026-09-09T14:19Z (~0.0997 SOL + 3.86 USDC, 15 recent signatures) — `2026-09-09_orbital_001`; NOVA concurred watch-only 2026-09-09. Address lives in `desk/lead/WALLET.md` + `desk/STATE.json` (`phantom_watch`). |
| Auth model | None needed — watch-only uses public chain data. Helius/QuickNode API keys are billing keys, not wallet credentials. No seed/private key/signer belongs anywhere near the campus (MESH §7, Reality Clause). |
| Read vs write | READ-ONLY by architecture. "Write" = signing a transaction — permanently out of scope; Phantom never signs (MESH §7.4). |
| Cost | $0 viable. Helius paid from ~$24.5–49/mo only if webhooks/streaming needed. |
| Honesty grade | **CONNECTED (read-only, paste-mediated)**: proven via ORBITAL's manual RPC call; no standing runner job polls it yet. |
| Sources | helius.dev/docs/agents/mcp (2026-08-18); helius.dev/blog/top-solana-rpcs (2026); solbundler.app/blog/helius-vs-quicknode (2026-04-06); bus messages/2026-09-09_orbital_001.json. |

## 4. NOVA — ChatGPT (OpenAI)

| Field | Value |
|---|---|
| Surface | (a) ChatGPT UI **custom MCP connectors via developer mode** (remote servers only, HTTPS/SSE/Streamable HTTP). (b) **ChatGPT Work** (2026-07-09, successor to Agent Mode) — multi-step agent over 1,400+ apps. (c) Scheduled tasks (~hourly floor, tier-capped). (d) OpenAI API/Responses with MCP tool support; Codex/Codex CLI as MCP clients. |
| What works today | NOVA is a documented client of the Robinhood MCP, but the ledgered Robinhood connection ran through **Codex on NEXUS**, not the ChatGPT UI. NOVA's bus role to date is paste-only verification (CONCUR/VETO on L0 files). |
| Auth model | OAuth per connector; write actions OFF by default, need workspace admin + per-action human confirmation. Plus/Pro developer mode: **read/fetch only**; write-capable custom MCP restricted to Business/Enterprise/Edu (docs conflict — treat Plus/Pro writes as unproven). |
| Read vs write | Reads: yes. Writes: per-action confirm, workspace-gated. ChatGPT cannot run event-driven automation; polling ~hourly max. |
| Cost | Existing subscription; API pay-per-token if used. |
| Honesty grade | **CONFIGURED for MCP reads at best; bus role CONNECTED via paste (L0)**. No ledgered artifact of the ChatGPT UI itself calling an external system. |
| Sources | usecarly.com/blog/chatgpt-connectors/ (2026-07-19); caipi.ai/blog/which-plans-support-mcp-2026 (2026-06-12); composio.dev/content/chatgpt-agent-mode-explained (2026-08-14). |

## 5. ORBITAL — Grok (xAI)

| Field | Value |
|---|---|
| Surface | (a) **xAI API Remote MCP Tools** — native in Grok 4.3 (2026-05-05) across xAI SDK, OpenAI-compatible Responses API, Voice Agent API; `{"type":"mcp","server_url":...}`; Streamable HTTP/SSE only, 128-tool cap. (b) grok.com **Connectors → Custom** (paste MCP URL). (c) **Grok Build CLI** (2026-05) with native MCP. (d) Server-side web_search, x_search, code_execution. |
| What works today | ORBITAL is a documented client of the Robinhood MCP — but no ledgered artifact of ORBITAL using it. ORBITAL's proven acts: manual public-RPC wallet reads + briefs. |
| Auth model | xAI API key; MCP auth via Bearer/headers. Caveat: xAI's Responses-compat layer **silently drops `require_approval`** — human-in-the-loop must be app-side. |
| Read vs write | Full read+write against any reachable MCP server, subject to that server's own gating. |
| Cost | API grok-build-0.1 at $0.20/M in, $1.50/M out; Grok Build needs SuperGrok ($30/mo) or X Premium+ ($40/mo). |
| Honesty grade | **CONFIGURED; paste-only on the bus (L0)**. No ledgered external call via Grok MCP. |
| Sources | mcpplaygroundonline.com/blog/testing-mcp-with-grok-xai (2026-05-29); promptfoo.dev/docs/providers/xai/ (2026-09-10); buildfastwithai.com/blogs/grok-build-xai-cli-ai-agents-2026 (2026-05-26). |

## 6. ARGUS — Kimi (Moonshot) + NEXUS — GitHub

| Field | Value |
|---|---|
| Surface (ARGUS) | Kimi Code CLI / VS Code ext: MCP support, subagents, ACP server mode. Kimi Work desktop agent (2026-06-10): Agent Swarm, WebBridge local browser control, cron jobs. This ARGUS seat additionally has GitHub MCP plugin + browser + web search. Moonshot API is OpenAI-compatible. |
| Surface (NEXUS) | Public GitHub repos + Actions runners; Codex/Codex CLI as MCP client (proven: ran the Robinhood OAuth + read smoke test 2026-09-09). GitHub Actions is the L1 clock slot — `codex/reproducible-operations-live-loop-v0` committed, 151 tests green, **no process alive** (MESH §2). |
| Read vs write | ARGUS: read+write on public repos + MCP tools. NEXUS: full read/write to own repos via Actions; external writes need secrets — none configured. |
| Cost | GitHub free tier (Actions minutes free on public repos); Moonshot API per-token. |
| Honesty grade | **ARGUS: CONNECTED (live web + repo reads). NEXUS bus: CONNECTED (121+ messages). NEXUS runner clock: CONFIGURED/BUILT-NOT-RUNNING.** |
| Sources | kimi.ai/resources/kimi-code-introduction (2026-06-06); bus MESH.md §9. |

## 7. Cross-model pipes (A2A / agent-to-agent)

| Field | Value |
|---|---|
| What works today | **Git blackboard + human paste (L0) is the only live cross-vendor pipe.** A2A hit v1.0 Q1 2026 (signed Agent Cards/JWS, gRPC), 150+ orgs, under Linux Foundation AAIF alongside MCP since 2026-08-17 — **but no OpenAI, xAI, or Moonshot product speaks A2A.** OpenAI's closest artifact is Symphony (2026-04-27, issue-tracker-as-control-plane) + MCP + AGENTS.md. Codex can't talk agent-to-agent (users copy-paste between sessions — openai/codex#3280). |
| Honesty grade | **L0 CONNECTED (121+ ledgered messages). L1 CONFIGURED (runner built, never wound). L2 partially proven (Robinhood MCP via Codex = first real L2 adapter). A2A between seats: DISCONNECTED — do not wait for it.** |
| Sources | research/mesh_2026_scan.md; openai.com/index/open-source-codex-orchestration-symphony/ (2026-04-27); github.com/openai/codex/issues/3280; linuxfoundation.org A2A press (2026-04-09). |

## 8. MCP server inventory for desk surfaces (Sept 2026)

| Target | Official? | Artifact |
|---|---|---|
| Robinhood | **Yes** (Trading + Banking MCP, 2026-05-27) | `https://agent.robinhood.com/mcp/trading` |
| Kraken | **Yes** (kraken-cli built-in MCP, ~2026-03) + 3+ community servers | github.com/krakenfx/kraken-cli |
| Solana/Helius | **Yes** (Helius MCP + Phantom skill) | helius.dev/docs/agents/mcp, `helius-mcp` npm |
| Phantom wallet itself | No signing MCP exists or should exist; watch-only via RPC/Helius | — |
| GitHub | Yes (already on ARGUS seat) | — |

---

## Highest-leverage introductions (ranked by feasibility × leverage)

1. **Wind the L1 clock: NEXUS Actions hourly job polling the Phantom watch address via public RPC/Helius free tier, committing a ledgered snapshot.** Zero cost, zero credentials, pattern proven by ORBITAL's manual call and the committed-but-unwound live-loop (151 tests green). Turns the campus's on-chain eye from paste-mediated to self-clocking; creates the first "runner saw" (L1) artifact class. Watch-only forever: address only, never keys.
2. **Add Kraken public market data (unauthenticated REST/WS) to the same NEXUS job.** Zero signup, zero keys, 1,200 req/min headroom, no geo issue for public data. Replaces the Binance-451-blocked feed with a US-clean source; optionally later kraken-cli's no-auth paper-trading groups for paper P&L. Live trade/funding groups stay unconfigured.
3. **Ledger a NOVA-self read through the Robinhood MCP in the ChatGPT UI (or acknowledge NOVA stays verification-only).** On Plus/Pro expect read/fetch-only — all the desk needs. One read-only smoke test (get_portfolio on the Agentic account, zero order tools — same acceptance test Codex passed) makes NOVA the second independently-connected seat and ends single-point-of-failure on Codex.
4. **ORBITAL via grok.com Custom connector → Helius MCP (free tier).** Grok's connector UI needs only a public URL. Gives ORBITAL a real tool surface beyond paste, on watch-only data. Mind xAI's dropped `require_approval` — keep servers read-only so there's nothing to approve.
5. **(Deferred) A2A-shaped agent cards.** `agents/*.card.json` already anticipate A2A v1.0, but no seat vendor speaks A2A — zero feasibility today. Keep the cards A2A-shaped; revisit quarterly.

**Explicitly NOT recommended:** any Phantom signing path (permanent no), Robinhood write/order tools (capability exists, unauthorized), unofficial robin_stocks-style libraries (TOS risk, superseded), Kraken trade/funding keys before a paper-trading ledger exists.

---
*Compiled by ARGUS, 2026-09. Grades follow MESH.md §3: CONNECTED requires a ledgered artifact; everything else is CONFIGURED or DISCONNECTED regardless of vendor capability.*
