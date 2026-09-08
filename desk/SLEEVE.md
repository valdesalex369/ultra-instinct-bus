# Powder sleeve

No fiat ACH required.

## What Agentic can hold as powder

- USD cash on the brokerage book (already $5 after the SOL trim). This is the spendable powder I can fire.
- SOL remainder is the hold, not the clip.
- USDC: only if the pair is live on this account. If the pair is missing, USD cash is the USDC-equivalent. Do not invent a stablecoin transfer.

## Recycle rule

1. Clip spends powder (USD or USDC).
2. Closed winner recycles into SOL.
3. Closed loser stays in USD/USDC. Do not revenge-buy SOL.
4. SOL share of the agent book after recycle stays ≤ 40% unless Alex says hold heavy.
5. Inbound: Alex can deposit SOL or USDC into the Agentic crypto account. Giant cannot pull from Coinbase or Phantom.

## Portal / self R&D while idle

Work lives in this repo (`desk/`, `PROTOCOL.md`) and Nexus (`src/`, `docs/`). No Grok cron.
