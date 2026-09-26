#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "evidence" / "2026-09-24"
PACKET = ROOT / "releases" / "TEMRAL_VERIFICATION_PACKET_2026-09-24.zip"

def green(label: str) -> None:
    print(f"[GREEN] {label}")

def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    green(label)

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def verify_published_hashes() -> None:
    sums = EVIDENCE / "SHA256SUMS.txt"
    rows = []
    for line in sums.read_text(encoding="utf-8").splitlines():
        digest, name = line.split(None, 1)
        rows.append((digest, name.strip()))
    for expected, name in rows:
        path = EVIDENCE / name
        require(path.is_file(), f"published file present: {name}")
        require(sha256(path) == expected, f"published SHA-256 matches: {name}")

def verify_zip() -> None:
    require(PACKET.is_file(), "verification ZIP present")
    with zipfile.ZipFile(PACKET) as zf:
        names = {Path(n).name: n for n in zf.namelist() if not n.endswith("/")}
        expected_files = [
            "00_READ_ME_FIRST.md",
            "01_LIVE_PAIR_REPORT.md",
            "02_PROVIDER_TELEMETRY_RECONCILIATION.md",
            "03_CROSS_PROVIDER_REPLICATION.md",
            "04_SCOPE_AND_LIMITS.md",
            "05_FALSIFICATION_PROTOCOL.md",
            "SHA256SUMS.txt",
            "manifest.json",
        ]
        for name in expected_files:
            require(name in names, f"ZIP contains: {name}")
            require(
                zf.read(names[name]) == (EVIDENCE / name).read_bytes(),
                f"ZIP byte-match: {name}",
            )

def verify_claims() -> None:
    manifest = load_json(EVIDENCE / "manifest.json")
    latest = load_json(EVIDENCE / "public-proof-latest.json")
    ledger = load_json(ROOT / "claims.json")

    require(
        manifest["schema"] == "temral.public-verification-packet.v1",
        "manifest schema",
    )
    f = manifest["flagship"]
    calc = (
        Decimal(1)
        - Decimal(f["treatment_input_tokens"]) / Decimal(f["control_input_tokens"])
    ) * Decimal(100)
    calc5 = calc.quantize(Decimal("0.00001"), rounding=ROUND_HALF_UP)
    require(calc5 == Decimal("99.38766"), "flagship reduction arithmetic")

    pe = latest["publishedEvidence"]
    lf = pe["flagship"]
    require(lf["controlInputTokens"] == 365320, "flagship control tokens")
    require(lf["treatmentInputTokens"] == 2237, "flagship treatment tokens")
    require(lf["exactOutputPreserved"] is True, "flagship exact output preservation")
    require(
        lf["cacheTokens"] == 0 and lf["retryCount"] == 0,
        "flagship zero-cache / zero-retry",
    )

    tel = lf["providerTelemetry"]
    require(tel["exactMinuteRequests"] == 2, "provider bucket request count")
    require(
        tel["exactMinuteInputTokens"] == 365320 + 2237,
        "provider bucket input total",
    )
    require(
        tel["exactMinuteOutputTokens"] == 166 + 166,
        "provider bucket output total",
    )
    require(tel["exactMinuteCachedTokens"] == 0, "provider bucket zero cache")
    require(tel["exactPairCostClaimed"] is False, "no exact pair-dollar claim")

    rep = pe["replication"]
    require(rep["fullMatchedPairGreenCount"] == 6, "six full matched replication pairs")
    require(
        rep["exactOutputPreservedAcrossAllPairs"] is True,
        "replication exact-output preservation",
    )
    require(rep["oracleExactAcrossAllPairs"] is True, "replication oracle exact")
    require(
        Decimal(str(rep["minimumTokenReductionPercent"])) == Decimal("99.33"),
        "replication token-reduction floor",
    )
    require(
        Decimal(str(rep["minimumRequestBodyReductionPercent"])) == Decimal("99.3"),
        "replication body-reduction floor",
    )
    require(
        rep["retryCount"] == 0 and rep["missingLanes"] == 0,
        "replication zero retry / zero missing lanes",
    )
    require(rep["universalClaimed"] is False, "universal performance not claimed")

    ids = {row["claim_id"] for row in ledger["claims"]}
    require(
        ids == {"C001", "C002", "C003", "C004", "C005", "C006"},
        "claim ledger IDs",
    )
    for rel in ledger["evidence_index"].values():
        require((ROOT / rel).is_file(), f"claim evidence present: {rel}")

def main() -> int:
    try:
        verify_published_hashes()
        verify_zip()
        verify_claims()
    except Exception as exc:
        print(f"[RED] {exc}", file=sys.stderr)
        return 1
    print("\nPUBLIC PACKET INTEGRITY: GREEN")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
