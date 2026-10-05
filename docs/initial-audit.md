# Initial native-browser audit — 2026-10-05

## Scope

Read-only inspection of five high-value EN routes plus the EN Intelligence page in the currently available Chrome native-browser surface:

`/en/`, `/en/intelligence/`, `/en/ecosystem/`, `/en/ive-2/`, `/en/about/`, `/en/contact/`.

The WordPress XML sitemap URLs were attempted but were blocked by the browser client. Therefore this is an initial structural sample, not a claim of complete EN coverage.

## Persistent observations

1. The shared primary navigation and legal footer are exposed on all inspected routes.
2. PT/EN switch links are exposed on all inspected routes, but PT route patterns vary and were not matched against hreflang/canonical metadata.
3. Page-title heading levels were inconsistent in the accessibility tree: some inspected pages exposed H1 and others exposed H2. The initial H2 -> H1 interpretation was incorrect because it did not first establish the site's canonical page pattern. Those three changes were reverted; no new structural interpretation is being applied in this run.
4. The Intelligence page contains a mixed-locale article destination under the EN listing. It may be intentional; the locale policy must decide whether that route is acceptable.

## Remediation completed

An UpdraftPlus local database-and-files backup completed successfully before the original edits. The incorrect H2 -> H1 changes on `/en/`, `/en/about/`, and `/en/contact/` were reverted to H2 and each route was reopened in the native browser after publication. No new page design, copy, CSS, form, navigation, or SEO change was applied. See `examples/reports/correction-log-2026-10-05.json`.

## What Claude can fix later

Use the report findings as a checklist, but validate each item in DOM/CSS/head evidence before editing. Do not fix from the accessibility summary alone. For each correction, create a backup, apply the change outside Site Guardian, rerun the relevant URL set, and compare the manifest.

## 2026-10-05 — EN Intelligence remediation

The PT route `/inteligencia/` was used as the canonical reference and kept read-only. The EN route `/en/intelligence/` was rebuilt to match its observed page pattern: the same lead/content hierarchy, four category cards, Publications section, ten publication entries, shared shell, and no inherited right sidebar or duplicate automatic title.

An UpdraftPlus database-and-files backup completed successfully before the EN changes. The public EN page was reopened and revalidated through the native browser accessibility/DOM surface after saving. Result: `PASS_CONTROLADO` for the EN Intelligence scope. PT was not edited or saved.

This does not close site-wide SEO head, canonical/hreflang, responsive, AdSense, computed-CSS, or complete-URL-inventory gates; those remain explicitly `NOT_VERIFIED` and are recorded in `examples/reports/en-intelligence-correction-2026-10-05.json`.

