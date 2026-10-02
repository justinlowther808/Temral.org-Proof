# Independent Reviewer Start Here

This is the shortest path for a technically qualified reviewer who wants to test a bounded TEMRAL result without relying on TEMRAL's internal implementation.

## Independence rules

A serious replication should keep the reviewer in control of the evidence that matters most:

- reviewer-selected workload;
- reviewer-controlled provider account when practical;
- reviewer-controlled provider credentials;
- predeclared provider and exact model;
- predeclared acceptance criterion;
- predeclared cache and retry policy;
- predeclared call and dollar ceilings;
- provider-reported usage and request identifiers;
- the final publication decision.

TEMRAL does not require a positive result, editorial approval, or prepublication review.

## Before any treatment result exists

Freeze a review record containing:

1. review date and timezone;
2. provider and exact model;
3. workload SHA-256 or other cryptographic commitment;
4. control-request commitment;
5. required-output or semantic acceptance contract;
6. cache policy;
7. retry policy;
8. maximum provider calls;
9. maximum provider spend;
10. telemetry fields that must be preserved;
11. disclosure and custody plan.

Use [`REPLICATION_RECORD_TEMPLATE.json`](REPLICATION_RECORD_TEMPLATE.json) as a starting point.

Do not change the frozen acceptance or measurement rules after seeing a treatment result. If anything material changes, classify the run as `PROTOCOL_DEVIATION` and state what changed.

## Recommended execution order

1. Run the control/baseline first.
2. Confirm the baseline satisfies the predeclared stability rule.
3. Run the TEMRAL treatment under the same provider/model boundary.
4. Preserve provider-reported input/output tokens, cache usage, request count, request identifiers, and account-level telemetry where available.
5. Evaluate the treatment against the frozen acceptance contract.
6. Reconcile account/provider telemetry where available.
7. Classify the result.

## Result classes

### GREEN

Use `GREEN` only when all predeclared acceptance and measurement conditions pass, the provider-reported reduction satisfies the frozen threshold, and no material protocol deviation occurred.

### RED

Use `RED` when the treatment fails the frozen acceptance contract or the measured reduction fails the frozen threshold.

### INCONCLUSIVE

Use `INCONCLUSIVE` when the experiment cannot answer the question cleanly, for example because baseline stability failed, required telemetry was unavailable, a provider incident interfered, or the evidence is insufficient to classify the result.

### PROTOCOL_DEVIATION

Use `PROTOCOL_DEVIATION` when a material frozen condition changed after treatment began or the run no longer matches the declared protocol.

## Credential and custody boundary

A reviewer should not give TEMRAL an account password or unrelated account access. Prefer narrowly scoped or temporary provider credentials when supported, and revoke them after the experiment.

Public evidence does not need to contain raw credentials, private prompts, private treatment payloads, route credentials, or internal implementation material. Publish cryptographic commitments when raw material should remain private.

## Minimum publication record

A useful public result should state:

- provider and exact model;
- date/time window;
- workload commitment;
- acceptance contract;
- cache/retry/call/spend policy;
- control provider telemetry;
- treatment provider telemetry;
- output-acceptance result;
- telemetry reconciliation result;
- final classification;
- every protocol deviation or unresolved limitation.

Supporting screenshots, exported provider telemetry, request identifiers, signed statements, or reviewer-held raw records can be attached when appropriate.

## Publish a replication report

After the run, use the [structured replication report form](https://github.com/justinlowther808/Temral.org-Proof/issues/new?template=replication-report.yml) to publish `GREEN`, `RED`, `INCONCLUSIVE`, or `PROTOCOL_DEVIATION` directly in the public repository. Do not paste credentials or other private material into the issue.

## Existing public material

- [`CLAIMS.md`](CLAIMS.md) — current bounded claims.
- [`SCOPE_AND_LIMITS.md`](SCOPE_AND_LIMITS.md) — explicit non-claims.
- [`FALSIFICATION.md`](FALSIFICATION.md) — how to reject a result.
- [`REPLICATION_PROTOCOL.md`](REPLICATION_PROTOCOL.md) — compact external protocol.
- [`PROVENANCE.md`](PROVENANCE.md) — evidence custody.
- [`CORRECTIONS.md`](CORRECTIONS.md) — corrections and withdrawals.

The private optimization mechanism is outside the public evidence boundary. The experiment should succeed or fail on observable behavior, provider telemetry, the frozen acceptance contract, and preserved evidence.
