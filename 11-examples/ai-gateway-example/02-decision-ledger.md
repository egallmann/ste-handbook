---
title: "Example step 2 — Decision ledger (AI Gateway)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 2 — Decision ledger

## Purpose

Show how STE **bounds** the work of a **logical ADR**. The **decision ledger** turns the snapshot into **explicit questions**, each with **alternatives** and **trace links** back to requirement items. This is a major governance move: the organization decides **which decisions must be resolved** before logical architecture is treated as settled.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Illustrative excerpt

```yaml
# Simplified decision ledger
type: decision_ledger
ledger_id: LEDGER-0003
source_requirements_snapshot: REQ-0001
target_logical_adr: ADR-L-AIGW-001

required_decisions:
  - ledger_decision_id: LDEC-0001
    question: What architecture pattern should the AI gateway use?
    alternatives: [serverless, containerized, hybrid]
    related_snapshot_items: [RQINV-0001, RQNFR-0001]

  - ledger_decision_id: LDEC-0002
    question: How should provider failover be implemented?
    alternatives:
      - circuit breaker pattern
      - retry with exponential backoff
      - health check based routing
    related_snapshot_items: [RQCAP-0002, RQNFR-0002]

  - ledger_decision_id: LDEC-0003
    question: Where should API keys be stored?
    alternatives: [AWS Secrets Manager, HashiCorp Vault, environment variables]
    related_snapshot_items: [RQINV-0002]

constraints:
  snapshot_items: [RQINV-0001, RQINV-0002, RQNFR-0001, RQCONST-0001]
```

## What to read from it

- Each row is a **question** the logical layer must answer, with **alternatives** still on the table.
- **Related snapshot items** make **traceability** explicit: reviewers can see **why** a decision belongs in scope.
- The ledger names the **target logical ADR** that will receive resolutions.

### Invent versus resolve (central STE idea)

The **logical ADR does not invent** a fresh shopping list of decisions that bypass governance. It **resolves** the **ledger’s** `required_decisions`: for each ledger row, the logical ADR (or linked decision records) should record **which alternative was chosen** and **why**, within the **constraints** the ledger carries forward.

If someone “just writes a logical ADR” without a ledger, teams often smuggle new scope or skip alternatives review. The ledger pattern keeps **decision governance** visible: **what must be answered** is known before the logical text claims closure.

---

**Previous:** [Step 1](./01-requirements-snapshot.md) · **Next:** [Step 3 — Logical ADR](./03-logical-adr.md) · **Diagram:** [Intent to design](./diagrams/intent-to-design.md)
