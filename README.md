# Site Guardian

Browser-native site and brand design-system compliance auditing for any public website.

Site Guardian is an open-source, portfolio-ready reference implementation created and maintained by **InsightValues**. InsightValues is the first case study; the engine is deliberately neutral so another team can provide its own brand/site standard.

## What it does

The Guardian audits a live page as:

`URL → page → section → component → element → property → rule`

It uses a browser-native evidence adapter to collect DOM structure, computed CSS, links, metadata, responsive states, and interaction observations. Screenshots may be attached as optional evidence, but are never the audit mechanism.

The architecture has three pillars:

- **Automation** — deterministic discovery, browser evidence collection, delta detection, daily health checks, and machine-readable manifests.
- **Monetization** — open-source core with configurable profiles, hosted/team execution, policy packs, and commercial reporting extensions kept outside the read-only core.
- **Security** — read-only by design, no credentials in profiles or reports, fail-closed P0/P1 gates, independent verification, and corrections kept outside the auditor.

## Modes

- `full` — inventory and inspect the configured URL scope, locales, breakpoints, and rules.
- `delta` — compare a fresh evidence set with a baseline and inspect changed surfaces first.
- `daily` — fast health checks for availability, links, metadata, critical structure, and previously failing rules.

## Quick start

```powershell
python -m pip install -e .
python -m guardian.cli validate-profile profiles/insightvalues.case-study.json
python -m guardian.cli evaluate --profile profiles/insightvalues.case-study.json --evidence examples/evidence.intelligence.en.json --out examples/reports/sample-report.json
```

Without installing, set `PYTHONPATH=src` (PowerShell: `$env:PYTHONPATH = "src"`) before invoking `python -m guardian.cli`.

## Example executions

Validate a brand/site profile before running an audit:

```powershell
python -m guardian.cli validate-profile profiles/insightvalues.case-study.json
```

Evaluate a native-browser evidence packet and write a machine-readable manifest:

```powershell
python -m guardian.cli evaluate `
  --profile profiles/insightvalues.case-study.json `
  --evidence examples/evidence.intelligence.en.json `
  --mode full `
  --out examples/reports/local-full-audit.json
```

Run the same evidence packet as a delta or daily health check:

```powershell
python -m guardian.cli evaluate --profile profiles/insightvalues.case-study.json --evidence examples/evidence.intelligence.en.json --mode delta --out examples/reports/local-delta-audit.json
python -m guardian.cli evaluate --profile profiles/insightvalues.case-study.json --evidence examples/evidence.intelligence.en.json --mode daily --out examples/reports/local-daily-health.json
```

The command prints the final gate and the number of unverified rules. A P0/P1 failure or missing required evidence keeps the result fail-closed. See [`docs/usage.md`](docs/usage.md) for the complete workflow, evidence contract, adapter examples, and interpretation guidance.

The live browser adapter is intentionally not coupled to one vendor. ChatGPT, Claude, Codex, Playwright, or another native-browser host can implement the same protocol in `docs/browser-adapter-protocol.md`.

## Current case-study status

The initial evidence was collected read-only from the live EN Intelligence page in a native Chrome browser on 2026-10-05. It confirms the visible navigation/content/footer topology and PT/EN links. Exact computed font families, weights, colors, spacing, and responsive measurements were not available from the current browser surface and therefore remain `NOT_VERIFIED` in the profile and report. No site changes were made.

See:

- `docs/insightvalues-standard.md` — evidence-bounded standard.
- `examples/reports/initial-insightvalues-en-audit.json` — first manifest, with explicit scope limits.
- `docs/architecture.md` — components and trust boundaries.
- `docs/browser-adapter-protocol.md` — cross-executor protocol.
- `docs/usage.md` — installation, execution modes, native-browser adapter examples, and report interpretation.

## Safety boundary

The auditor never edits a website, submits forms, logs in, uploads files, or applies a fix. A correction workflow must create a backup, apply changes outside this repository, rerun the auditor, and independently verify the resulting evidence.

## Macro-mission delivery rule

Site Guardian missions are delivered as one autonomous macro mission. Inventory, PT-canonical/EN parity, content and grammar, visual/computed CSS, components, responsive behavior, links, SEO, accessibility, forms, product truth, monetization/AdSense, security, backup, remediation, public QA, and non-regression are not separate completion options. When correction is authorized, the orchestrator coordinates the correction outside the read-only auditor and reruns the complete audit before delivery. A scoped pass or partial gate is never presented as ready; unresolved required evidence produces a single macro `BLOCKED` or fail-closed result.

## License

Apache-2.0. See `LICENSE`.

