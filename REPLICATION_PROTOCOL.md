# External Replication Protocol

For a reviewer-ready walkthrough and machine-readable freeze/result template, start with:
- [`REVIEWER_START_HERE.md`](REVIEWER_START_HERE.md)
- [`REPLICATION_RECORD_TEMPLATE.json`](REPLICATION_RECORD_TEMPLATE.json)

Before any treatment result exists, freeze:
- provider and exact model;
- workload or workload hash;
- control request or cryptographic commitment;
- acceptance criterion;
- reduction threshold;
- cache policy;
- retry policy;
- maximum provider calls;
- maximum dollars;
- required provider/account telemetry;
- disclosure/custody plan.

Recommended sequence:
1. Run baseline repeatability first.
2. Admit treatment only if the frozen baseline meets the predeclared stability rule.
3. Prefer reviewer-controlled provider credentials and account telemetry.
4. Preserve request/result identifiers or cryptographic commitments.
5. Reconcile provider/account telemetry where available.
6. Publish `GREEN`, `RED`, `INCONCLUSIVE`, or `PROTOCOL_DEVIATION`.

Classification contract:
- `GREEN`: frozen acceptance and reduction conditions pass with no material protocol deviation.
- `RED`: the treatment fails the frozen acceptance contract or frozen reduction threshold.
- `INCONCLUSIVE`: the experiment cannot answer the question cleanly because required evidence or baseline stability is insufficient.
- `PROTOCOL_DEVIATION`: a material frozen condition changed after treatment began or the run no longer matches the declared protocol.

TEMRAL does not require a positive result, editorial approval, or prepublication review.

Private credentials, prompts, treatment payloads, route credentials, and internal implementation material do not need to be published. Use cryptographic commitments when raw material should remain private.
