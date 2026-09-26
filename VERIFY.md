# Verify the Public Packet

Requirements:
- Python 3.10+
- no provider key
- no TEMRAL credential
- no network access
- standard library only

Run:

```bash
python verify.py
```

Expected final line:

```text
PUBLIC PACKET INTEGRITY: GREEN
```

The verifier checks:
- SHA-256 hashes from the published packet;
- flagship reduction arithmetic;
- provider telemetry totals;
- machine-readable flagship and replication facts;
- six-pair replication count;
- the explicit universal-performance boundary.

A green result verifies internal consistency and integrity of the public packet. It does not independently reproduce TEMRAL's private implementation.
