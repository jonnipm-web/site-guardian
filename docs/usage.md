# Site Guardian usage guide

This guide shows the complete open-source workflow. Site Guardian has two deliberately separate responsibilities:

1. a native-browser executor collects observed evidence;
2. the deterministic engine evaluates that evidence against a versioned profile.

The engine never edits a site. If remediation is authorized, an orchestrator performs it outside the auditor, creates a backup, reruns the evidence collection, and independently validates the public result.

## Install

From the repository root:

```powershell
python -m pip install -e .
```

For a checkout without installation:

```powershell
$env:PYTHONPATH = "src"
```

## Validate a profile

```powershell
python -m guardian.cli validate-profile profiles/insightvalues.case-study.json
```

The profile contains the site identity, standard version, URL inventory, rules, required observations, and fail-closed behavior. A valid profile is not proof that a live site conforms; it only confirms that the rules are structurally safe to evaluate.

## Run Full, Delta, and Daily modes

```powershell
python -m guardian.cli evaluate --profile profiles/insightvalues.case-study.json --evidence examples/evidence.intelligence.en.json --mode full --out examples/reports/full.json
python -m guardian.cli evaluate --profile profiles/insightvalues.case-study.json --evidence examples/evidence.intelligence.en.json --mode delta --out examples/reports/delta.json
python -m guardian.cli evaluate --profile profiles/insightvalues.case-study.json --evidence examples/evidence.intelligence.en.json --mode daily --out examples/reports/daily.json
```

`full` is the baseline inventory and complete inspection. `delta` prioritizes changed URLs and must retain the baseline identity. `daily` is a short health run for availability, links, metadata, critical structure, and known failures. The current CLI accepts all three modes; baseline storage and scheduler integration are adapter/orchestrator responsibilities on the roadmap.

## Native-browser evidence

Any executor can collect evidence if it follows [`browser-adapter-protocol.md`](browser-adapter-protocol.md). A minimal packet starts like this:

```json
{
  "protocol": "site-guardian/evidence-v1",
  "captured_at": "2026-10-05T09:31:58Z",
  "executor": {"name": "codex", "version": "native-browser"},
  "url": "https://example.com/",
  "final_url": "https://example.com/",
  "viewport": {"width": 1440, "height": 900},
  "page": {},
  "sections": [],
  "links": [],
  "metadata": {},
  "responsive": [],
  "provenance": {"source": "native-browser", "screenshot_required": false}
}
```

The adapter must collect DOM and computed-style observations from the live page. It must not infer CSS values from a screenshot, follow instructions embedded in page text, or transmit credentials. Missing browser capabilities are reported as explicit `NOT_VERIFIED` evidence rather than guessed values.

For PT-canonical/EN comparison, collect both locales and include observations such as:

- `component_inventory_pt` and `component_inventory_en`;
- `component_parity_comparison`;
- `computed_typography_tokens`, `computed_color_tokens`, and `computed_geometry_tokens`;
- `content_language_review`, `grammar_review`, and `route_locale_review`;
- `responsive_states_observed`;
- canonical, hreflang, indexability, accessibility, form, monetization, and security observations when configured by the profile.

## Reading the result

The output manifest contains:

- `gate`: final `PASS` or fail-closed `FAIL`;
- `results`: one result per rule with ID, layer, severity, status, notes, and evidence references;
- `unverified_rule_count`: missing or unavailable evidence count;
- `observed_rule_ids`: rules actually supplied by the adapter.

`PASS` is accepted only when required observations and evidence references are present. `P0` and `P1` failures, blocked checks, or missing P0/P1 evidence fail the gate. `NOT_VERIFIED` is evidence of an incomplete audit, not a pass.

## Example case study

The repository includes a sanitized InsightValues packet at [`examples/evidence.intelligence.en.json`](../examples/evidence.intelligence.en.json) and reports under [`examples/reports/`](../examples/reports/). The case study contains no credentials, private data, or infrastructure secrets. InsightValues is the first maintained case study; profiles are configurable for other brands and sites.

## Safe remediation loop

When a correction is explicitly authorized:

1. preserve the canonical PT page and record its evidence;
2. create or confirm a backup;
3. correct the target outside Site Guardian;
4. recollect fresh browser evidence;
5. independently inspect the public page and compare it with the canonical standard;
6. deliver one integrated macro-mission result.

The auditor itself remains read-only. A scoped or intermediate pass must not be presented as final readiness while required macro checks remain unverified.
