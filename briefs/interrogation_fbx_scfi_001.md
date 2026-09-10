# INTERROGATION REPORT #2 — Hypothesis B: FBX–SCFI Publication-Schedule Arb

- **Cycle**: quant-agent-swarm Phase 1 (INTERROGATE), second trigger
- **Date**: 2026-09-11 · **Author**: argus (Kimi) · evidence: explore lane (`briefs/hypb_evidence.md`)
- **Subject**: FBX (daily, 14:00 UTC) leads SCFI (weekly, Friday) → trade the lag via SCFI-linked instruments or container-equity proxies
- **Capital policy**: max_ticket_usd 5, max_day_usd 10, capital level 0 (paper)

---

## VERDICT: KILL — on crowding and access, not on mechanism.

The mechanism is **confirmed live**: week of Sep 4, SCFI printed +2.3% (3,590) while FBX Global fell 2% and
daily FBX01 dropped 10% into Sep 9 — the daily/weekly sign disagreement the thesis needs is happening right
now. But the thesis dies two branches later: **the asymmetry is already consumed daily by onshore flow we
cannot access, and every retail-reachable proxy is disqualified.** The exchanges productized the exact
speed asymmetry themselves in April 2026 (ICE NYFI daily futures, Euronext XSI-C daily futures).

Second wedge, second KILL. Pattern noted in the advisory: **visibility is now a negative screen.**

---

## Resolved decision tree (8 branches)

### 1. Edge Identification — MECHANISM REAL, EDGE NOT OURS
Schedule asymmetry exists and is exploitable — by INE EC futures flow (~$1bn+/day turnover, 44–61k lots OI),
which front-runs SCFI/SCFIS prints as standard practice. EC2610 sat at a ~35% discount to spot before the
Aug 2026 decline, "fully priced in" per trade press. The edge is consumed by 60k+ lots of onshore flow
before any offshore participant sees the Friday print.

### 2. Data Sources — PASS (the only clean branch)
FBX free charts + CSV on request; SCFI public Friday print; both verifiable. Data was never the problem.

### 3. Decay — CONSUMED PRE-PUBLICATION
The lead time (daily vs weekly) is arbed intraday by INE flow; what remains by Friday's print is fully
priced. Decay isn't the issue — pre-consumption is.

### 4. Capacity — N/A (killed upstream)

### 5. Regime — AMPLITUDE CONFIRMED, IRRELEVANT
SCFI +156% since the Iran conflict; record Shanghai congestion (139 vessels, 1.7M TEU); FBX01 swung
$2,617→$7,068→$2,418 in 2026. Big regime, wrong seat.

### 6. Execution Reality — KILLED (three independent disqualifications)
- **INE EC futures**: the real venue — QFII-only, inaccessible to US retail.
- **CME FBX futures**: ghost market. Linerlytica: "CoFIF has liquidity while CFFA doesn't." No volume
  milestone ever published. OQ1 resolved *against*.
- **Equity proxies**: ZIM is a Hapag-Lloyd merger-arb instrument ($35 cash deal, Q4 2026 close, price
  capped by deal spread, Q1 2026 net loss while rates rose) — disqualified. BOAT's top holdings are
  tankers (FRO/INSW/STNG; ZIM 1.81%) — its +61% YTD is Hypothesis A's P&L, not B's. Disqualified.
- And again the mandate: even if a proxy existed, $5/$10 buys no expression.

### 7. Risk Scenarios — the venue flood
ICE (NYSHEX/NYFI daily futures) and Euronext (Xeneta XSI-C daily futures) launched the same week of April
2026 — exchanges productized the daily-vs-weekly asymmetry. When the exchange builds the product, the
arbitrage is the product.

### 8. Stop-Loss Discipline — kill switches (fired and standing)
**Fired**: (B1) onshore flow consumes the lead daily; (B2) CME venue is a ghost; (B3) both retail proxies
disqualified; (B4) exchanges productized the asymmetry.
**Standing revival triggers** (all must hold): direct CME/ICE bulletin shows usable FBX/NYFI open interest;
a US-listed pure container-freight proxy exists; mandate ≥ $500/ticket; in-house β regression (OQ6, never
published anywhere — consistent with the edge being exploited onshore and never written up) shows residual
lead after INE consumption.

---

## What this interrogation proves (the meta-finding)

Two wedges interrogated, two KILLs, both on the same grounds: **if a desk this size can find the edge with
free research, someone with more capital already trades it.** This is not failure — this is the filter
working. The wedge portfolio is now honestly empty, which is the correct state for capital level 0.

The campus's actual products, in order of demonstrated value:
1. **Interrogation** (2/2 kills, zero dollars lost)
2. **Verification/monitoring** (veto-layer instrumentation, unfalsified-claim hygiene)
3. **The eval ledger** (compounding judgment history)

The next wedge brought to `RUN THE INTERROGATION` must pass a new pre-screen, Branch 0:
**"Can a free dashboard already see this, and can onshore/institutional flow already trade it?"**
If either is yes → don't spend the cycle.

## Next gate

- **Nova**: CONCUR or VETO the second KILL and the Branch-0 pre-screen.
- **Orbital**: no new wedge queued. Standing work is the connection map (see game_change brief).
- **Alex**: $0 requested. Again. The meter is running on judgment, not P&L.
