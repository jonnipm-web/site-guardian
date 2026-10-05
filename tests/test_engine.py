import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from guardian.engine import evaluate, load, validate_profile

ROOT = Path(__file__).parents[1]

def test_profile_is_valid():
    assert validate_profile(load(ROOT / "profiles/insightvalues.case-study.json")) == []

def test_unavailable_evidence_never_becomes_fail_open_pass():
    profile = load(ROOT / "profiles/insightvalues.case-study.json")
    result = evaluate(profile, {"source": "native-browser", "rule_results": {}})
    assert result["unverified_rule_count"] == len(profile["rules"])
    assert result["gate"] == "FAIL"

def test_p1_failure_fails_gate():
    profile = load(ROOT / "profiles/insightvalues.case-study.json")
    result = evaluate(profile, {"rule_results": {"IVSG-INV-001": "FAIL"}})
    assert result["gate"] == "FAIL"

def test_visual_pass_without_computed_browser_evidence_is_rejected():
    profile = load(ROOT / "profiles/insightvalues.case-study.json")
    evidence = {
        "rule_results": {"IVSG-VISUAL-001": "PASS"},
        "evidence_refs": {"IVSG-VISUAL-001": ["fake-screenshot-only"]},
        "observations": {"visual_reference_comparison": True}
    }
    result = evaluate(profile, evidence)
    visual = next(item for item in result["results"] if item["rule_id"] == "IVSG-VISUAL-001")
    assert visual["status"] == "NOT_VERIFIED"
    assert result["gate"] == "FAIL"

def test_visual_pass_requires_all_browser_tokens_and_geometry():
    profile = load(ROOT / "profiles/insightvalues.case-study.json")
    evidence = {
        "rule_results": {"IVSG-VISUAL-001": "PASS"},
        "evidence_refs": {"IVSG-VISUAL-001": ["pt-en-computed-style-1"]},
        "observations": {
            "computed_theme_tokens": True,
            "computed_typography_tokens": True,
            "computed_color_tokens": True,
            "computed_geometry_tokens": True,
            "visual_reference_comparison": True
        }
    }
    result = evaluate(profile, evidence)
    visual = next(item for item in result["results"] if item["rule_id"] == "IVSG-VISUAL-001")
    assert visual["status"] == "PASS"
