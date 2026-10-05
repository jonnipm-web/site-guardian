# Architecture

```text
Native browser host
  └─ Browser Evidence Adapter (untrusted observations)
       ├─ URL inventory
       ├─ DOM / computed CSS / metadata / links
       ├─ responsive-state observations
       └─ optional semantic evidence packets
              ↓
        Deterministic rule engine
              ↓
        Minimal AI semantic reviewer (optional)
              ↓
        Signed-by-provenance manifest + gate
```

The adapter is the only component allowed to talk to a live browser. The rule engine is pure evaluation over evidence. The AI reviewer cannot change evidence, downgrade a P0/P1 failure, or authorize a correction. A correction system is intentionally out of scope and must re-run the auditor after backup and change approval.

## Three pillars

Automation is the collection/evaluation pipeline. Monetization is a boundary around hosted runs, team history, policy packs, and reporting; the core remains usable locally. Security is read-only collection, secret-free configuration, least privilege, provenance, and fail-closed release gates.

