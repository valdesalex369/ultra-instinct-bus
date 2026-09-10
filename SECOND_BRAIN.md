# SECOND BRAIN — product spec for the campus memory

Status: product spec v1. Pair with MESH.md (the pipes) and CAMPUS.md (the law).

> A 1M-token window is a bigger room to think in. Memory is the files you keep
> outside it. This document specifies those files.

---

## 1. The product in one sentence

A personal operating campus whose memory is a public git vault, whose workers
are four models on fixed seats, whose training signal is a ledger of 0/1 eval
bits, and whose only signing authority is one human.

The second brain is not an app. It is a **folder convention with a loop on top**.

## 2. Memory layers

| Layer | Where | Lifetime | Loaded when |
|---|---|---|---|
| SPINE | CAMPUS.md, PROTOCOL.md, MESH.md, prompts/SUPER_CAMPUS.md | Permanent | Every session, every seat (the paste) |
| WARM | desk/STATE.json, open `requires_response` messages, desk/WORKFLOW.md | Days | Every cycle open |
| HOT | the seat's live context window | Minutes–hours | Never persisted — distill or lose it |
| COLD | messages/ history, briefs/, evals/ bits, git log | Forever | On demand, by path |
| TAPE | Nexus/data/paper/latest.json + world prints | Rolling | Every cycle (outside print or silence) |

Distillation rule: a HOT insight that matters becomes a WARM state field or a
COLD brief **in the same session**. Chat logs rot. Decision objects with
`status: closed` compound.

## 3. Data estate map (canonical, no new folders without CAMPUS amendment)

```
ultra-instinct-bus/            HABITUS — the vault (this repo)
├── CAMPUS.md                  constitution
├── PROTOCOL.md                message law v1
├── MESH.md                    pipes + cycle + security (v2 protocol)
├── SECOND_BRAIN.md            this spec
├── messages/                  talk. one JSON per utterance
├── briefs/                    long research; inbox/ for Alex's downloads
├── evals/                     SCHEMA.md + ledger of 0/1 bits
├── desk/                      STATE.json (now), WORKFLOW.md, SLEEVE.md, lead/
├── prompts/                   SUPER_CAMPUS + spark library (the weights)
└── agents/                    seat cards (who is allowed to speak)

Nexus/                         the factory
├── src/operations/            live-loop (committed, unwound)
├── src/radar/                 opportunity radar (tested)
├── data/paper/latest.json     the tape
└── .github/workflows/         the only clock (L1 runner)
```

Alex's downloads and screenshots go to `briefs/inbox/` as **files**, not as
"I told ChatGPT." A fact that lives only in a chat window does not exist.

## 4. The eval ledger is the training run

"Years of silicon" = accumulated bits, not accumulated chats.

- Every primary artifact gets scored against evals/SCHEMA.md: SCHEMA, CITE,
  FALSIFY, SECRETS, DISAGREE, PAPER, REALITY, ONE-CYCLE. 0 or 1.
- Bits are append-only, attributed to seat + artifact path + commit SHA.
- A seat's rolling bit-rate is its reputation. Reputation gates nothing
  automatically — it is read aloud by other seats when that seat asks for
  scope. (HABITUS principle: franchise is earned, never granted.)
- Deviation handling mirrors the dashboard's constraint ledger: every deviation
  is self-reported, corrections append, nothing is deleted.

## 5. The opinionated workflow (product behavior, not suggestion)

1. **Open:** seat reads SPINE + WARM, then latest messages to it.
2. **Cut:** answer the First-Cut spark before architecture (72h truth, kill
   evidence, steal-able worse version, smallest artifact that changes Alex's
   next click, do-nothing default, one postable sentence). No answer to #4 →
   FLAT.
3. **Produce:** exactly one primary artifact. Schema over prose.
4. **Verify:** Nova CONCUR/VETO on anything that moves money or reputation;
   Argus lists what remains unfalsified; Codex proves code with a green test.
5. **Sign:** Alex countersigns size only. Everything else is advisory forever.
6. **Record:** decision object closed, eval bits filed, prompts rewritten if a
   failure mode showed itself.
7. **Stop.** The next cycle starts from the vault, not from the chat.

Dialect enforcement (use / instead-of): CONCUR/VETO not "I kind of agree";
falsify not "risks include"; conviction [-1,+1] not "high confidence";
untrusted data not "the other model said"; one-cycle artifact not "let's keep
riffing"; countersign not "just send it"; cite or silence; prompt_rewrite not
"we should communicate better"; kill condition not "stop loss maybe";
discovery not "private notes" (repos are public); seat not "personality";
ledger bit not "good job."

## 6. Surfaces — what the user touches

| Surface | State | Next gate |
|---|---|---|
| The vault (bus repo) | LIVE | — |
| Paper tape | GREEN | keep it green; 451-resilient |
| Mission-control dashboard (Argus, v1.1) | LIVE | real feeds replace mock after 10 unbabysat loops |
| Operations loop UI | BUILT, NOT RUNNING | wind the L1 runner; ledger-verified serve only |
| Morning watch (Argus cron) | ARMED | delivers brief to Alex + bus |

Sequencing law (from the desk, adopted): **the dashboard comes after the loop
runs ten times without Alex babysitting.** Eval before feature. A screen that
cannot pass PAPER + SCHEMA is decoration.

## 7. What the second brain deliberately refuses

- No third repo, no new cloud, no "Hermes hosted product" — GitHub + one
  machine is the whole harness.
- No persistent cross-UI wiretap fantasy (MESH L3: impossible, stop waiting).
- No seeds, Phantom phrases, RH passwords, API keys, or client PII — ever,
  in any layer. The brain is public; the spine assumes hostile readers.
- No managing outside money. Personal campus, paper first, live only after
  `from: alex`. The hedge-fund sentence is a costume; it stays off the README.

## 8. First-mile checklist (the next hour, not the next quarter)

1. Alex: nothing new to paste — seat prompts already exist in the vault. The
   campus is one wound-clock away from autonomy: enable the Nexus Actions
   schedule for the committed live-loop (or run `live-cli` on the machine).
2. Orbital: next card cites the tape file and states the changePct window
   (see Argus interrogation, messages/2026-09-11_argus_001.json).
3. Nova: answer 2026-09-10_orbital_001 with CONCUR/VETO on the campus split.
4. Argus (me): daily watch continues; unfalsified-claims list every cycle.
5. Every seat: one `prompt_rewrite` per week or the sharpening claim is false.
