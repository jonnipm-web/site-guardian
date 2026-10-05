"""Small deterministic manifest engine; browser collection is intentionally external."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

FAIL_CLOSED = {"P0", "P1"}

def load(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def validate_profile(profile: dict) -> list[str]:
    errors = []
    for key in ("schema_version", "profile_id", "site", "standard", "inventory", "rules"):
        if key not in profile: errors.append(f"missing:{key}")
    for rule in profile.get("rules", []):
        for key in ("id", "layer", "severity", "status_when_unavailable"):
            if key not in rule: errors.append(f"rule:{rule.get('id','?')}:missing:{key}")
        if rule.get("status_when_unavailable") != "NOT_VERIFIED": errors.append(f"rule:{rule.get('id','?')}:must-not-default-pass")
    return errors

def evaluate(profile: dict, evidence: dict, mode: str = "full") -> dict:
    results = []
    observed_ids = set(evidence.get("rule_results", {}))
    for rule in profile.get("rules", []):
        outcome = evidence.get("rule_results", {}).get(rule["id"])
        if outcome not in {"PASS", "WARN", "FAIL", "NOT_VERIFIED", "BLOCKED"}:
            outcome = "NOT_VERIFIED"
        refs = evidence.get("evidence_refs", {}).get(rule["id"], [])
        missing = [key for key in rule.get("required_evidence", []) if not evidence.get("observations", {}).get(key)]
        if outcome == "PASS" and (not refs or missing):
            outcome = "NOT_VERIFIED"
        note = evidence.get("notes", {}).get(rule["id"], "No executable result supplied by adapter.")
        if missing:
            note = f"PASS rejected: missing required browser evidence: {', '.join(missing)}. {note}"
        results.append({"rule_id": rule["id"], "layer": rule["layer"], "severity": rule["severity"], "status": outcome, "evidence_refs": refs, "notes": note})
    gate = "FAIL" if any(r["status"] in {"FAIL", "BLOCKED", "NOT_VERIFIED"} and r["severity"] in FAIL_CLOSED for r in results) else "PASS"
    return {"manifest": "site-guardian/manifest-v1", "generated_at": datetime.now(timezone.utc).isoformat(), "mode": mode, "profile_id": profile["profile_id"], "standard": profile["standard"], "source": evidence.get("source", "native-browser"), "scope": evidence.get("scope", {}), "gate": gate, "results": results, "unverified_rule_count": sum(r["status"] == "NOT_VERIFIED" for r in results), "observed_rule_ids": sorted(observed_ids)}
