---
title: "HSCA Methodology"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# HSCA Methodology

## The Problem

When a reasoner fails, the cause is often ambiguous. The needed information may not exist in the substrate, may exist but fail to assemble, may be ambiguous, may be remembered by a human outside the substrate, or may be absent from any authority surface.

Without a protocol for classifying these cases, a benchmark can confuse reasoner failure, substrate failure, assembly failure, memory drift, and authority gaps.

## The Reframe

Human-Assisted Substrate Completeness Analysis (HSCA) is a measurement protocol for evidence completeness. It records human and AI observations so disagreements can be classified without making either side authoritative.

HSCA is not a human-versus-AI benchmark. It is not an authority mechanism. It is not a source of truth.

## The Model

HSCA classifies where a disagreement appears to originate:

- substrate missingness,
- substrate present but not assembled,
- assembly failure,
- ambiguous task or authority gap,
- human memory only,
- human stale memory,
- AI reasoning error,
- unresolved evidence.

The live collection protocol should record:

- pseudonymous participant identity,
- blinding verification,
- task generation or scenario generation,
- task or scenario fingerprint,
- experiment fingerprint,
- response duration,
- confidence,
- memory origin,
- structured evidence sources,
- rationale,
- observational-only authority status.

Blinding matters because participants who know the expected outcome can unconsciously supply missing context. Participants should not see AI answers, scores, gold answers, rubric outcomes, or disagreement classifications before answering.

HSCA reports completeness signals rather than correctness scores:

- substrate completeness,
- assembly completeness,
- memory drift,
- representation gaps,
- unmatched observations,
- benchmark authority gaps,
- unresolved disagreements.

### Candidate equations

HSCA uses its own candidate equation layer. These are research notation and report structures, not answer-correctness authority. They complement the main reasoning-quality equation in [MVC candidate equation variables](candidate-equation-variables.md); they do not replace it.

**Disagreement attribution.** HSCA classifies where a disagreement appears to originate from blinded observations and permitted evidence:

```text
D_cls(task, candidate, generation) =
  classify(
    human observation record (H_obs),
    AI observation record (A_obs),
    permitted evidence,
    blinding verification (B_ver),
    memory origin (M_org),
    structured evidence sources (E_src),
    task fingerprint (T_fp),
    evidence boundary (G_b)
  )
```

`D_cls` is a disagreement classification, not a correctness score. Adjudication result (`D_adj`) may be recorded separately and must not silently promote observations into benchmark or architecture authority.

**Completeness reports.** Classifications aggregate into count-only report families. Each family is a derived proxy, not ground-truth measurement:

```text
C_sub = Σ substrate_missing
      + Σ substrate_ambiguous
      + Σ substrate_present_not_assembled
      + Σ authority_gap
      + Σ unresolved   # substrate-completeness bucket only

C_asm = Σ available_information
      + Σ assembled_information
      + Σ omitted_information
      + Σ assembly_gap

C_mem = Σ stale_memory
      + Σ contradicted_memory
      + Σ memory_only
      + Σ validated_memory

C_rep = Σ encoded_and_used
      + Σ encoded_not_used
      + Σ available_not_encoded
      + Σ memory_only
      + Σ authority_missing
```

**Collection readiness counts** track whether live observation is available without scoring participants:

```text
H_count = |H_obs|
A_count = |A_obs|
U_h     = unmatched human observations
U_a     = unmatched AI observations
B_gap   = benchmark authority gaps
U_d     = unresolved disagreements
```

**Golden-context iteration.** Before reasoning-quality (`Q`) or fitness comparisons are meaningful, a task fixture may require iterative representation review. HSCA supplies the named failure vocabulary for that loop:

```text
Fixture_confidence(task, generation) =
  iterate(
    task,
    draft context or packet,
    H_obs,
    D_cls
  )
  until substrate completeness (C_sub) and assembly completeness (C_asm)
        stabilize toward encoded-and-assembled
     OR benchmark authority gap (B_gap) requires an explicit governance act
```

This loop judges whether the representation encodes what a good answer requires. It is not the same as storing a gold answer string.

**Link to reasoning quality.** HSCA does not estimate reasoning quality (`Q`) directly. It decomposes confounds that would otherwise be read as model success or failure:

```text
Interpret(Q_local or Q) requires
  C_sub, C_asm, C_mem, C_rep, U_d, B_gap
```

If substrate or assembly gaps are high, a nondiscriminating or surprising reasoning outcome may be a fixture or instrumentation problem rather than evidence about the representation-ceiling thesis.

### Interaction terms

Preserve these interaction terms until evidence supports collapsing them:

| Interaction | Why It Matters |
|-------------|----------------|
| `B_ver * H_obs` | Blinding verification (`B_ver`) conditions whether a human observation record (`H_obs`) is admissible for completeness analysis. Unblinded observations may circularly supply missing context. |
| `M_org * C_mem` | Memory origin (`M_org`) shapes how memory drift counts (`C_mem`) should be read. Recalled knowledge and direct observation are different failure modes. |
| `C_sub * Q` | Substrate completeness (`C_sub`) must be known before reasoning quality (`Q`) is interpreted. Missing substrate can masquerade as weak reasoning. |
| `C_asm * Q` | Assembly completeness (`C_asm`) separates present-but-not-assembled substrate from reasoner failure when interpreting `Q`. |
| `C_rep * R_q` | Representation gap counts (`C_rep`) interact with representational structural quality (`R_q`). Encoded-but-unused structure is a different gap than never-encoded structure. |
| `U_d * D_adj` | Unresolved disagreements (`U_d`) must stay visible even when adjudication result (`D_adj`) exists. Automatic resolution would hide inspectable uncertainty. |
| `B_gap * Fixture_confidence` | Benchmark authority gaps (`B_gap`) block golden-context lock-in until an explicit rubric, gold, or governance surface exists. |

### HSCA variable inventory

| Variable | Meaning |
|----------|---------|
| `H_obs` | human observation record |
| `A_obs` | AI observation record |
| `D_cls` | disagreement classification |
| `D_adj` | adjudication result |
| `B_ver` | blinding verification status |
| `M_org` | memory origin |
| `E_src` | structured evidence sources |
| `T_fp` | task fingerprint |
| `G_b` | evidence boundary or bank generation |
| `C_sub` | substrate completeness report |
| `C_asm` | assembly completeness report |
| `C_mem` | memory drift report |
| `C_rep` | representation gap report |
| `H_count` | human observation count |
| `A_count` | AI observation count |
| `U_h` | unmatched human observations |
| `U_a` | unmatched AI observations |
| `B_gap` | benchmark authority gap count |
| `U_d` | unresolved disagreement count |

Shared symbols such as reasoning quality (`Q`), representational structural quality (`R_q`), and viable-context sufficiency (`C_v`) are defined in [MVC candidate equation variables](candidate-equation-variables.md).

## The Implications

- HSCA can explain why a study failed to discriminate.
- HSCA can identify missing substrate before blaming a reasoner.
- HSCA can surface where authority is absent.
- Human review generates evidence; human memory does not become architecture authority unless captured through accepted artifacts.
- AI review generates evidence; AI output does not become answer authority without adjudication.
- Synthetic HSCA fixtures can validate mechanics, but they do not prove that live human observations will classify gaps consistently.
- HSCA candidate equations classify completeness and disagreement; they do not authorize fitness weights or answer correctness by themselves.
- Golden-context iteration may use HSCA classifications before a task fixture is locked for MVC-D fitness comparison.

## Relationship to STE system

HSCA supports [Evidence](../../../../03-artifacts/03-05-evidence.md) and [Traceability](../../../../03-artifacts/03-06-traceability.md) by making completeness and disagreement inspectable. It does not replace ADRs, invariants, Architecture IR, benchmark adjudication, or Kernel admission.

## Summary

- HSCA is a completeness-analysis protocol.
- Human and AI observations are evidence only.
- Blinding protects the observation boundary.
- Disagreements should be classified, not silently resolved.
- HSCA reports completeness and gap classifications, not authority.
- HSCA has candidate equations for attribution, report aggregation, golden-context iteration, and interpretation guards on reasoning quality.
