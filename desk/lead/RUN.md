# Runner that does not die

The bus is files. Something has to open them.

## Who does what

| Agent | Prompt file | Job |
|---|---|---|
| orbital (Grok) | PROMPT_FOR_ORBITAL.md | LEAD. Writes messages. RH place only after alex |
| chatgpt / Nova | PROMPT_FOR_CHATGPT.md | Verifier. CONCUR or VETO. Never places |
| Codex | PROMPT_FOR_CODEX.md | Cook. Writes real files on Nexus + this bus |

## Minimum alive loop

1. Alex opens Grok with PROMPT_FOR_ORBITAL.md already in the thread (or says "check the bus").
2. Alex pastes PROMPT_FOR_CHATGPT.md into a ChatGPT thread pointed at this repo.
3. Alex pastes PROMPT_FOR_CODEX.md into Codex/Cursor pointed at this repo or Nexus.
4. Optional: Grok Automation hourly 06:00-16:00 America/New_York writes a desk card into messages/.

No fourth repo. If the cron is missing, the humans are the cron.
