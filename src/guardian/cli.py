from __future__ import annotations
import argparse, json
from .engine import load, validate_profile, evaluate

def main():
    parser = argparse.ArgumentParser(prog="site-guardian")
    sub = parser.add_subparsers(dest="command", required=True)
    v = sub.add_parser("validate-profile"); v.add_argument("profile")
    e = sub.add_parser("evaluate"); e.add_argument("--profile", required=True); e.add_argument("--evidence", required=True); e.add_argument("--out", required=True); e.add_argument("--mode", default="full", choices=["full", "delta", "daily"])
    args = parser.parse_args()
    if args.command == "validate-profile":
        errors = validate_profile(load(args.profile)); print(json.dumps({"valid": not errors, "errors": errors}, indent=2)); raise SystemExit(1 if errors else 0)
    result = evaluate(load(args.profile), load(args.evidence), args.mode)
    with open(args.out, "w", encoding="utf-8") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps({"gate": result["gate"], "unverified_rule_count": result["unverified_rule_count"], "out": args.out}, indent=2))

if __name__ == "__main__": main()
