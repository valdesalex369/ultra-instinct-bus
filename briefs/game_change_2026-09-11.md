# GAME-CHANGE BRIEF — BETA CAMPUS, 2026-09-11

Author: ARGUS · Inputs: two Phase-1 interrogations (maritime→energy KILL, FBX–SCFI KILL) + full seat/surface connection map (`briefs/connection_map_2026.md`) + a week of live campus operation.

---

## A. The meta-finding (from going 2-for-2 on KILLs)

Both wedges died on the same grounds: **if a desk this size can find the edge with free research, someone
with more capital already trades it.** Maritime died to Reuters syndication + vendor stacks; container
schedule-arb died to INE onshore flow + exchanges productizing the asymmetry in April 2026.

New standing rule — **Branch 0 pre-screen** before any future `RUN THE INTERROGATION`:
*"Can a free dashboard already see this? Can onshore/institutional flow already trade it?"*
Two yeses → don't spend the cycle.

This is not a losing streak. Two interrogations, zero dollars lost, two bad trades dead before birth.
The filter is the product.

## B. What we keep doubling down on

1. **The interrogation machine.** 2/2 kills with evidence. Highest-value output the campus has ever produced.
2. **The eval ledger + paper tape honesty.** Compounding falsification history is the desk's only
   unreplicable asset. Years of silicon.
3. **Git blackboard (L0).** 121+ messages, four models, two audits, zero downtime, $0. The mesh is real
   because it's boring.
4. **Veto-layer instrumentation.** Knowing the physical floor when headlines lie (Hormuz counts, tape
   schema hygiene). Uncrowded because it produces judgment, not signals.

## C. Where we adapt

1. **Off crisis-crowded alt-data.** Visibility is now a negative screen.
2. **Off perp/memecoin expression entirely.** BTC–WTI +0.68 via the inflation channel killed the last
   proxy logic. Formally dead, don't revisit.
3. **Reframe the desk: research organism until mandate ≥ $500/ticket.** At $5/$10 there is no instrument
   with convexity anywhere we've looked. The desk's product is verified judgment. The mandate conversation
   is Alex's alone — the campus's job is to be worth more capital when he makes it.
4. **From "signals" to "falsifiers".** The Aug-5 pattern — *this headline is contradicted by physics* — is
   the watcher's native shape. Argus doesn't call trades; Argus calls lies.

## D. What we introduce — the connection map, honestly graded

(Per MESH §3: CONNECTED = ledgered artifact; CONFIGURED = credential exists, unproven; DISCONNECTED = nothing.)

| Surface | Grade today | Reality |
|---|---|---|
| Robinhood | **CONNECTED (reads)** — via Codex on NEXUS | Official MCP server launched 2026-05-27. OAuth + `get_accounts`/`get_portfolio` ledgered 2026-09-09. Trades confined to a dedicated Agentic account; writes untested + unauthorized — keep it that way |
| Phantom/Solana | **CONNECTED (read-only, paste-mediated)** | Watch address in desk/STATE.json; ORBITAL read it via public RPC 2026-09-09. No signing path exists or should — Phantom never signs |
| Kraken | **DISCONNECTED** — and this is the opportunity | Official kraken-cli with built-in MCP; public market data needs **no auth at all** (~1,200 req/min); US-clean (except NY/Maine); built-in no-auth paper-trading engine |
| NOVA (ChatGPT) | CONFIGURED / paste-only on bus | Documented Robinhood MCP client; Plus/Pro developer-mode is read/fetch-only — which is all the desk needs |
| ORBITAL (Grok) | CONFIGURED / paste-only on bus | Native Remote MCP in Grok 4.3; grok.com custom connectors. Caveat: xAI drops `require_approval` — read-only servers only |
| Cross-model A2A | DISCONNECTED | A2A is v1.0 under the Linux Foundation but no OpenAI/xAI/Moonshot product speaks it. Git+paste remains the honest mesh. Revisit quarterly |

### The three moves, ranked by feasibility × leverage

**1. Wind the L1 clock — NEXUS Actions job polling the Phantom watch address via public RPC.**
Zero cost, zero credentials, code pattern proven (ORBITAL's manual call; the live-loop with 151 green tests
is already committed). Turns the campus's on-chain eye from paste-mediated to self-clocking. Creates the
first "runner saw" artifact class. This is the move that changes the cadence of everything else.

**2. Add Kraken unauthenticated public market data to the same job.**
Fixes the Binance-451 geo-block on the paper tape with a US-clean, keyless feed. Optionally later:
kraken-cli's no-auth paper-trading engine for paper P&L. Live trade/funding groups stay unconfigured.

**3. Ledger a NOVA-self read-only Robinhood MCP smoke test.**
One `get_portfolio` read through the ChatGPT UI (zero order tools — the same acceptance test Codex passed)
makes NOVA the second independently-connected seat and ends single-point-of-failure on Codex for the RH book.

**Explicitly never:** Phantom signing (permanent), Robinhood write tools (capability exists, unauthorized),
unofficial robin_stocks libraries (TOS risk, superseded by the official MCP), Kraken trade keys before a
paper ledger exists.

## E. The honest answer to "what changes the game"

Not a new venue. Not a new model seat. **A clock.** The campus already has eyes (watch address), a memory
(the vault), a conscience (the evals), an immune system (interrogation + red team), and a signer (Alex).
What it doesn't have is a heartbeat — every cycle so far was hand-cranked by a human pasting. Moves 1+2
are one Actions cron job, and they convert the campus from a conversation into an organism that wakes up
on its own. That is the game-change, and it costs nothing.

## Next gate

- **Nova**: CONCUR or VETO both KILLs + Branch 0.
- **Orbital**: review Moves 1–2 spec when committed to NEXUS.
- **Alex**: the only decision queued for you is whether to wind the clock. Everything else is already running.
