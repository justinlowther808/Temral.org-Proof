# Independent Falsification Protocol

TEMRAL invites technically qualified reviewers to try to falsify the published bounded claims.

Recommended independent procedure:
1. Select a supported model and one representative workload with a deterministic or predeclared acceptance contract.
2. Freeze the control request, treatment request, provider/model identity, cache policy, retry policy, and success criteria before execution.
3. Run the control and treatment through the provider account controlled by the reviewer when practical.
4. Record provider-reported input/output tokens, cache usage, request count, response result, and request identifiers.
5. Require the treatment to satisfy the predeclared acceptance contract.
6. Reconcile provider/account telemetry where the provider exposes it.
7. Publish positive or negative results without requiring TEMRAL approval.

A reviewer should reject the claim for that experiment if the treatment fails the predeclared acceptance contract or if the measured reduction does not satisfy the stated threshold.
