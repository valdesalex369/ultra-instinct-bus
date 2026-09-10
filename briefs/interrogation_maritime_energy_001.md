# INTERROGATION REPORT — Maritime→Energy Wedge (Hormuz transits → Brent)

- **Cycle**: quant-agent-swarm Phase 1 (INTERROGATE), first pass
- **Date**: 2026-09-11
- **Author**: argus (Kimi) · red-team: independent verifier (report: `briefs/redteam_maritime_energy.md`)
- **Trigger**: "say the word" → canonical desk trigger **`RUN THE INTERROGATION`** (any seat may fire Phase 1 on any named wedge)
- **Subject**: Hypothesis A — AIS/PortWatch transit anomalies at the Strait of Hormuz → Brent/WTI and retail-reachable wrappers
- **Capital policy in force** (desk/STATE.json): max_ticket_usd 5, max_day_usd 10, powder_floor_usd 5, capital level 0 (paper)

---

## VERDICT: KILL — as a trading wedge. Retain as a monitoring/veto layer. Promote Hypothesis B (FBX–SCFI) to the next interrogation.

The red team pre-committed 8 falsifiers; **6 are already TRIGGERED by documented September 2026 evidence**
(K1 wire syndication, K2 free dashboard replication, K3 EIA data disavowal, K4 >50% dark-fleet share,
K5 instrument minimums vs capital policy, K6 broken crypto-perp correlation). Any one of K1, K3, or K5 is
independently sufficient. The decisive finding: **the "secret" physical signal is front-page wire copy** —
Reuters syndicates Kpler's daily Hormuz counts (US News, CBS, CNBC, JPost, Gulf News), Kpler tweets them
free, and four free dashboards already wrap PortWatch chokepoint6 + Brent + war-risk composites. The
headline-vs-physical gap this thesis existed to exploit has closed: the physical data *is* the headline.

Campus honesty rules apply: when the evidence kills the idea, the report says KILL. The scout layer
survives as an instrument of the campus (veto input, not alpha), and one adjacent hypothesis survives
interrogation better than this one did.

---

## Current tape (as of 2026-09-10/11, cited to live sources)

| Fact | Value | Source |
|---|---|---|
| Brent front month | $106.88 (Sep 10), +5.6% d/d, +20.2% past month | tradingeconomics.com 2026-09-10 |
| Hormuz transits (PortWatch, last published Sep 6) | 6 vessels vs ~85/day baseline = 7% of pre-crisis | straits.live 2026-09-10 |
| gCaptain preliminary crossings | 7 on Sep 9, below 10-day avg of 14 | straits.live news feed |
| War-risk insurance | ~40× pre-crisis; 6 P&I clubs withdrawn | straits.live 2026-09-10 |
| Kinetic state | First tanker sunk in direct combat (M/T Kylo, Sep 6); ~40 ships/day under US escort | hormuzstraitmonitor.com |
| Iran posture | "Completely closed" declared Sep 7; restricted zone announced | hormuzstraitmonitor.com |
| Crisis Pressure composite | 94/100 (extreme), rising | straits.live |

---

## Resolved decision tree (8 branches)

### 1. Edge Identification — KILLED (commoditized)
The intended inefficiency was the headline-vs-physical gap (canonical case Aug 5: WTI −8.2% on a "draft
deal" headline vs Kpler's 5 tankers/24h). Red-team finding: that gap no longer exists. Reuters prints the
Kpler daily count within ~24h; CNBC computes the same derived statistics; Manifold settles markets directly
on PortWatch chokepoint6. When the retail-facing press computes your signal, **you are the crowd**.
CargoMetrics — the canonical AIS→alpha fund, decade head start, institutional capital — exited trading to
sell data (TradeWinds 2022). The firm with the best version of this edge concluded the *signal* was worth
less than the *feed*.

### 2. Data Sources — KILLED in-regime
- PortWatch: free but weekly Tuesday refresh + ~5-day lag + revisions.
- AISstream: no SLA, no replay, September-2026 bandwidth caps with message drops — untested, and it fails
  exactly when needed: 62–79% of crisis transits AIS-dark; GNSS jamming displaced 970–1,650 vessels/day.
- **The EIA itself cautions Hormuz AIS data has been "especially unreliable since end-February 2026"**
  (July 2026 STEO). When the authoritative user disavows the input in-regime, the "physical ground truth"
  premise inverts — the free count is a biased lower bound, and dark-transit volume was large enough to
  cause premature price unwinds. A signal that mis-measures the thing it claims to measure, in the wrong
  direction for the trade, is worse than no signal.

### 3. Decay Estimation — INSTANT
Brent reprices on anticipation, in minutes (Apr 9: −15% in one session on a ceasefire headline; Jul 27:
−11.3%; Sep 10: +5.9% *while* strikes were reported — the market trades the news cycle, not the ship count).
The free data stack is the slowest layer of an instantly-decaying signal.

### 4. Capacity Limits — NON-BINDING
Irrelevant at desk scale. (Only branch that passes.)

### 5. Regime Dependency — SEVERE, and the regime destroyed the wedge
Eight months into the crisis, every component (transit counts, war-risk multiples, stranded vessels, P&I
withdrawals) is daily public copy. Brent ~$107 with 6 transits/day is a market that has *fully absorbed* the
physical picture. Academic support doesn't transfer: predictability dies at 6-month horizons (Bakshi);
confined to 2001–2007 (Oomen). In 2026 the literature gap is evidence the effect doesn't survive costs.

### 6. Execution Reality — KILLED (arithmetic)
MCL margin ~$550–1,500 vs a $5 ticket. XLE call spread ~$100–150/unit. USO ~$150/share. $5 buys no
convexity anywhere in the energy complex. Crypto-perp proxy is broken twice: Binance 451-blocks the venue,
and BTC–WTI correlation is **+0.68 via the inflation/Fed channel** (BTC–Nasdaq 85% during oil spikes) —
"supply shock → long crypto" is directionally *wrong*. The correct expression (short BTC into oil spikes)
is a macro rates trade wearing an AIS costume.

### 7. Risk Scenarios — mapped (for the surviving monitor)
Dark-fleet misread (count recovery = shadow normalisation, Jun 2026: 94% non-IMO-lane); feed failure during
events; contested state-actor vs vendor claims (US "20–30 tankers/night" vs Kpler 7) where a free stack has
zero adjudicating power; correlation-to-1 in broad risk-off.

### 8. Stop-Loss Discipline — kill switches (fired and standing)
**Fired** (K1–K6 per red-team table): wire syndication; dashboard replication; EIA disavowal; dark share
>50%; instrument minimums; inverted crypto correlation.
**Standing, for the monitoring layer and any future revival**:
1. Any proposed ticket > $5 or day total > $10 → hard block (mandate)
2. PortWatch + AISstream both unavailable > 72h → posture NO-SIGNAL
3. Transits ≥ 80% of baseline for 7 consecutive days → regime over → archive
4. Statistical honesty: effective n≈5–6 (one war), ≥6 tuning knobs — any t-stat, regression coefficient,
   or Sharpe attached to this wedge is an automatic eval FAIL (SCHEMA/CITE)

---

## What survives (the viable core)

1. **Monitoring/veto layer, not alpha.** Knowing the true transit floor when a "deal" headline hits
   (Aug-5 pattern) is a conviction input that prevents being shaken out of sized-elsewhere positions.
   Research tool. Must never be represented as a tradeable signal.
2. **Peacetime nowcasting.** IMF-validated AIS/port-call nowcasts vs official statistics (r>0.8, WP 25/93,
   26/099) work in normal regimes where AIS isn't jammed and wires aren't watching. Slower, quieter,
   uncrowded. File for post-crisis.
3. **Hypothesis B (FBX–SCFI publication-schedule arb) survives relatively intact.** It rests on a schedule
   asymmetry (daily FBX vs Friday SCFI), not a data-superiority claim; nobody syndicates FBX-vs-SCFI
   divergence. Mandatory before any build: in-house β regression (Freightos free CSV + SCFI history) and a
   CME FBX 2026 liquidity check (open question OQ1). This is the **next interrogation candidate**.
4. **The one conditional tradeable pattern**: headline-fade has a real mechanism (physical normalisation
   takes days–weeks; algos reprice in ms). If the mandate ever permits ≥$500/ticket, defined-risk fades of
   diplomatic-headline spikes against still-collapsed counts — pre-registered, n accumulated from 2 — is
   the single defensible pattern. Not before.

## Risk budget

| Bucket | Allocation |
|---|---|
| Live capital to this wedge | **$0** — permanent at current mandate; revival requires ≥$500/ticket conversation |
| Compute/attention | ≤1 watch cycle/day (straits.live JSON + Tuesday PortWatch print) as a veto input only |
| Eval budget | Headline-fade observations may be logged as `eval` messages (not signals) to build n |

---

## Trigger word, canonized

**`RUN THE INTERROGATION`** — fires Phase 1 on a named wedge, any seat. Output must be this format:
verdict PASS / CONDITIONAL / KILL, resolved 8-branch tree, risk budget, kill switches defined **before**
any code. The word Alex asked for now exists in the dialect.

## Next gate

- **Nova (ChatGPT)**: CONCUR or VETO the KILL.
- **Orbital (Grok)**: if CONCUR — schedule the lightweight Hormuz monitor (veto input only); queue
  Hypothesis B for `RUN THE INTERROGATION` with the β-regression and CME-liquidity prerequisites.
- **Alex**: nothing to sign. No capital was requested and none is. The interrogation did its job: it
  killed a bad trade before it existed, kept the useful instrument, and named the next candidate.

*Core philosophy holds: every dollar of risk capital must survive an interrogation. This one didn't.
That is the system working, not failing.*
