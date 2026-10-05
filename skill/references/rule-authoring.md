# Rule authoring

Each rule has a stable ID, layer, severity, evidence requirement, comparator, and remediation note. A rule must distinguish:

- `PASS`: required evidence was observed and satisfied the comparator.
- `WARN`: evidence exists but is incomplete, outside tolerance, or needs human review without blocking release.
- `FAIL`: required evidence contradicts the standard.
- `NOT_VERIFIED`: the adapter did not expose required evidence; this is not a pass.
- `BLOCKED`: collection could not safely continue.

Use P0 for catastrophic trust/security or dangerous public defects, P1 for release-blocking structural or authorization defects, P2 for important quality defects, and P3 for polish or advisory issues. P0/P1 are fail-closed.

Never encode a guessed color, font, spacing, or product status. Put unknown values in `observed: null` and explain the missing evidence.

