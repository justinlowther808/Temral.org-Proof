# Published Claims

The machine-readable source of this ledger is [claims.json](claims.json).

## C001 — Flagship matched pair

OpenAI GPT-5.6 Sol:
- control input tokens: **365,320**
- treatment input tokens: **2,237**
- provider-reported input-token reduction: **99.38766%**
- exact required output preserved
- cached input tokens: 0
- treatment retries: 0

Evidence: `01_LIVE_PAIR_REPORT.md`, `manifest.json`, and `public-proof-latest.json`.

## C002 — Provider telemetry reconciliation

OpenAI organization usage telemetry for the exact one-minute bucket beginning `2026-09-22T19:50:00Z` reported **2 requests, 367,557 input tokens, 332 output tokens, and 0 cached input tokens**.

Those values match the expected combined control+treatment usage.

This is provider/account telemetry reconciliation, not an external third-party reproduction.

## C003 — Cross-provider replication

Six additional full matched pairs:
- OpenAI GPT-5.6 Terra: 3
- Anthropic Claude Sonnet 5: 3

Published result: **6 / 6 green**, exact required output preserved across all six, independent oracle satisfied across all six, retry count 0.

## C004 — Replication reduction floor

Across the six Terra/Sonnet pairs:
- minimum token reduction: **99.33%**
- minimum request-body reduction: **99.30%**

## C005 — Current public proof count

The flagship plus replication set totals **seven matched TEMRAL proof pairs across three models and two providers**.

Repeatability admission checks are not counted as additional TEMRAL proof pairs.

## C006 — Scope boundary

Universal performance is **not claimed**. See [SCOPE_AND_LIMITS.md](SCOPE_AND_LIMITS.md).
