# TEMRAL Public Proof

[![Verify public proof](https://github.com/justinlowther808/Temral.org-Proof/actions/workflows/verify-public-proof.yml/badge.svg)](https://github.com/justinlowther808/Temral.org-Proof/actions/workflows/verify-public-proof.yml)

This repository is the public, zero-history evidence mirror for TEMRAL's bounded verification results.

**Canonical proof:** https://temral.org/proof

**Machine-readable proof:** https://temral.org/proof/latest.json

**Public verifier:** https://temral.org/verify

**Media & technical review:** https://temral.org/media

## Published result

TEMRAL currently publishes **seven green matched proof pairs across three models and two providers**:

- one heavyweight OpenAI GPT-5.6 Sol matched pair;
- three OpenAI GPT-5.6 Terra matched retrieval pairs;
- three Anthropic Claude Sonnet 5 matched retrieval pairs.

The flagship Sol pair measured **365,320 control input tokens vs 2,237 treatment input tokens**, a **99.38766% provider-reported input-token reduction**, while preserving the exact required output.

The six Terra/Sonnet replication pairs were **6 / 6 green**, preserved the exact required output across all six, and had a **99.33% minimum token reduction** across the published replication set.

OpenAI organization usage telemetry also reconciled the flagship pair's exact one-minute usage bucket: **2 requests, 367,557 input tokens, 332 output tokens, 0 cached input tokens**.

## Verify locally

Run:

```bash
python verify.py
```

No provider key. No TEMRAL credential. No network. Standard library only.

A green verifier result means the public evidence package is internally consistent with the published manifest, arithmetic, and checksums. It is **not** a substitute for an independent reproduction of TEMRAL's private mechanism.

## Start here

1. [CLAIMS.md](CLAIMS.md) — exactly what is claimed.
2. [SCOPE_AND_LIMITS.md](SCOPE_AND_LIMITS.md) — exactly what is not claimed.
3. [VERIFY.md](VERIFY.md) — verify the packet locally.
4. [FALSIFICATION.md](FALSIFICATION.md) — how to try to prove a result wrong.
5. [REPLICATION_PROTOCOL.md](REPLICATION_PROTOCOL.md) — protocol for an external test.
6. [PROVENANCE.md](PROVENANCE.md) — public artifact custody.
7. [CORRECTIONS.md](CORRECTIONS.md) — how corrections and withdrawals are handled.

The original public packet is preserved under [evidence/2026-09-24/](evidence/2026-09-24/) and as the downloadable archive under [releases/](releases/).

## Security and disclosure boundary

This repository does **not** publish private implementation mechanics, provider credentials, customer prompt content, private treatment payloads, route credentials, or internal custody material.

Security concerns: root@temral.org

## Challenge it

TEMRAL welcomes technically grounded attempts to falsify the bounded claims. Use the **Evidence challenge** issue form or run an independent experiment under the published replication protocol.

A negative result is useful evidence too.

---

TEMRAL: https://temral.org
