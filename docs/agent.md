# Site Guardian Agent

The Site Guardian Agent is the execution role built on top of the `site-guardian` skill and a selected browser adapter.

## Agent contract

- Load exactly one profile and standard version for a run.
- Build an auditable inventory before claiming coverage.
- Collect browser-native evidence; screenshots are optional context only.
- Run deterministic rules before any AI judgment.
- Send only minimal, relevant evidence to semantic review.
- Preserve provenance and never let the semantic reviewer rewrite observations.
- Fail closed for any unverified P0/P1 rule.
- Produce PASS, WARN, FAIL, NOT_VERIFIED, or BLOCKED per rule.
- Never modify the audited site or treat a report from another executor as proof.

## AI review budget

The agent should invoke AI only for ambiguity that cannot be expressed as a deterministic comparator: editorial meaning, product-truth interpretation, route-pair intent, or whether a visible component is semantically equivalent to an approved pattern. It should pass a bounded evidence packet, rule ID, and question, then store the judgment separately from raw browser evidence.

## Autonomous macro mission

The agent must treat the requested outcome as one macro mission. It may use deterministic checks, semantic review, authorized remediation orchestration, backup, full rerun, public-browser QA, and non-regression validation as separate internal phases, but it must return one final delivery status only after all required phases are closed. `CONFORMANT_SCOPED`, `PASS_CONTROLADO`, or a partial gate is not a completion state when required checks remain unverified. Missing evidence blocks the macro mission rather than being silently deferred.

## Executor independence

ChatGPT, Claude, Codex, and other hosts may collect evidence differently, but each must emit `site-guardian/evidence-v1`. A receiving agent must verify the manifest against its own profile and reject missing provenance or unsupported PASS claims.

