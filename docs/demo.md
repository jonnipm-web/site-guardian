# Two-minute demo

This walkthrough uses the sanitized InsightValues evidence packet included in the repository. It does not access a live site and does not contain credentials.

## Run locally

```powershell
python -m pip install -e .
python -m guardian.cli validate-profile profiles/insightvalues.case-study.json
python -m guardian.cli evaluate `
  --profile profiles/insightvalues.case-study.json `
  --evidence examples/evidence.intelligence.en.json `
  --mode full `
  --out examples/reports/local-full-audit.json
```

## What to inspect

- the profile defines the standard and required evidence;
- the evidence packet records what the browser observed;
- the engine emits a machine-readable manifest;
- unavailable evidence remains `NOT_VERIFIED`;
- the auditor does not edit the target site.

For a real browser integration, implement the protocol in [`browser-adapter-protocol.md`](browser-adapter-protocol.md) and keep collection separate from correction.
