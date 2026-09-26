# Falsification

TEMRAL invites technically qualified reviewers to try to falsify the bounded published claims.

A reviewer should reject the claim for an experiment if the treatment fails the predeclared acceptance contract or if the measured reduction does not satisfy the stated threshold.

Recommended procedure:
1. Select a supported model and representative workload.
2. Freeze control request, treatment request, provider/model identity, cache policy, retry policy, and success criteria before execution.
3. Prefer a provider account controlled by the reviewer.
4. Record provider-reported input/output tokens, cache usage, request count, result, and request identifiers.
5. Require treatment to satisfy the predeclared acceptance contract.
6. Reconcile provider/account telemetry where available.
7. Publish positive or negative results without requiring TEMRAL approval.

The original packet protocol is at `evidence/2026-09-24/05_FALSIFICATION_PROTOCOL.md`.
