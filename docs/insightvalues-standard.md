# InsightValues Site Standard — v0.2.0 reconstructed from live evidence

This is the first reconstructed standard for the InsightValues case study. The PT-BR public site is the canonical reference. The EN site is conformant only when it preserves the PT structure, page family, component order, CTA intent, SEO role, and product truth, changing language rather than design. It does not replace that pattern with a generic blog template or invented design tokens. Values not collected from the live browser remain `NOT_VERIFIED`.

## The three governing pillars

### 1. Automation

The Guardian discovers URLs, opens the live page in the executor's native browser, collects DOM/accessibility/metadata/computed-style evidence, runs deterministic checks, and emits a versioned manifest. Screenshots are optional evidence only; they are not the audit mechanism.

### 2. Monetização

The public site is a commercial institutional ecosystem with an editorial intelligence hub as one section. Institutional/product pages must remain conversion-oriented and product-truthful. SEO, AdSense eligibility, structured content, and early-access/contact paths are audited as configurable commercial controls; monetization must not turn institutional pages into blog archives.

### 3. Segurança

Auditing is read-only. No auditor rule may edit WordPress, submit a form, change SEO, or publish content. Corrections require an independent backup, explicit owner authorization, a correction log, and public revalidation. P0/P1 evidence gaps remain fail-closed.

## Canonical-language rule

PT-BR is the source of truth for the site's public pattern. For every PT/EN pair, the Guardian must compare:

- page family and purpose;
- header/navigation and locale switcher;
- section order and section count;
- heading hierarchy within the page-family template;
- cards, labels, badges, forms, CTAs, and their destinations;
- product status and commercial claims;
- footer/legal/navigation blocks;
- SEO title, description, canonical, hreflang, indexability, and structured data.

Translation differences are expected. Structural differences are `FAIL` or `REVIEW_REQUIRED` according to severity. A page that follows an EN-only blog/archive pattern when its PT counterpart is institutional is not conformant.

## Observed global shell

Observed on the inspected PT and EN routes, with PT treated as canonical:

- GeneratePress-style public shell with a dark header and footer.
- Masthead identity is a link named `InsightValues` to the locale home.
- PT primary navigation exposes Início, IVE, Ecossistema, Inteligência, Quem Somos, Contato, and the Português/English switcher.
- EN primary navigation exposes Home, Intelligence, InsightValues Ecosystem, IVE, About, Contact, and the Português/English switcher.
- The Ecosystem menu exposes Overview, Core, IVE, Quant, and Impact.
- Footer exposes Privacy Policy, Terms of Use, Cookie Policy, Comments Policy, About, and Contact.
- Footer identity text is `Intelligence → Decision → Execution. IVE is the intelligence and execution engine of the InsightValues ecosystem.`
- Copyright text observed: `© 2026 InsightValues`.
- Locale links are route-paired per page; the actual destination must be collected rather than guessed.

## PT/EN parity finding from current evidence

The current `/inteligencia/` and `/en/intelligence/` pages are not structurally identical. PT exposes the canonical `O que publicamos` card taxonomy (`Intelligence Briefs`, `Flagship Articles`, `Technical Guides`, `Research`) before the publications list; the inspected EN page exposes a different `Latest articles` presentation and different article set/order. Their navigation labels and footer navigation also differ beyond translation. Therefore EN Intelligence is currently `NOT CONFORMANT` with the PT canonical pattern pending correction or an explicitly approved template exception.

## Observed page families

### Institutional / ecosystem pages

Home, About, Contact, Ecosystem, and IVE are structured as institutional/product pages. Their observed pattern is:

`eyebrow or status → page proposition → explanatory sections → product/truth status → controlled CTA → shared footer`.

They are not article archives. They may contain detailed technical evidence, product states, early-access CTAs, and forms, but their page purpose is institutional/product communication.

Observed examples:

- `/en/` begins with `InsightValues` and the proposition `Intelligence → Decision → Execution`, followed by Problem, Engine, Featured Implementation, Ecosystem, Evidence, Research & Building in Public, Explore, and Early Access.
- `/en/about/` uses ABOUT, PURPOSE, WHAT WE BUILD, IVE, HOW WE WORK, BUILDING IN PUBLIC, FOUNDER, and EXPLORE.
- `/en/contact/` uses CONTACT, `Talk to InsightValues`, explanatory institutional copy, and the contact form.
- `/en/ecosystem/` uses EARLY ACCESS, `InsightValues Ecosystem`, product architecture, Core, IVE, Quant, Impact, Foundation, and Access the Ecosystem.
- `/en/ive-2/` uses availability status, product proposition, Five Stages, Human Gate, implementation status, reference implementation, and ecosystem access.

### Editorial intelligence hub

`/en/intelligence/` is the editorial/research hub. Its observed pattern is:

`INSIGHTVALUES → Intelligence → What is Intelligence → Publications → categorized article entries → shared footer`.

Article pages and article indexes may use editorial/archive patterns. That pattern must not be copied onto Home, About, Contact, Ecosystem, or IVE.

## Heading rule reconstructed from evidence

Heading level is page-family/template evidence, not a blanket repair target. The inspected institutional routes Home, About, and Contact expose their first content heading as H2; Ecosystem and IVE expose their page proposition as H1; Intelligence exposes `Intelligence` as H2. The correct rule is therefore: preserve the approved template's hierarchy and investigate outliers against the canonical family before editing. Do not normalize all pages to H1 or all pages to H2 from an accessibility summary alone.

## Not yet verified

Computed font family, font sizes, weights, line heights, exact colors, contrast ratios, spacing, max-widths, breakpoints, focus styling, canonical/hreflang headers, indexability directives, server response headers, form behavior, link status across the full inventory, AdSense placement/eligibility, structured data, and all responsive states remain `NOT_VERIFIED` until collected through the browser adapter.

## Rules

The executable rule IDs live in `profiles/insightvalues.case-study.json`. New rules must preserve the three pillars, distinguish institutional from editorial page families, and never promote an observed inconsistency into a correction without independent template-level evidence.
