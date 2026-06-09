---
title: "HSCA Methodology"
status: draft
maturity: L2
diagrams: true
last_reviewed: "2026-06-09"
---

# HSCA Methodology

## The Problem

Golden context and known outcomes (`Q`) for MVC experiments are easy to contaminate.

A human building or reviewing a task fixture can answer from **latent memory**: knowledge that feels authoritative but is not present in the substrate under test. That is the same failure family the representation-ceiling thesis calls **lossy reasoning** — rationale decay, context loss, assumption loss, and drift compressing recoverable structure back into habit and recall.

Without a guard, fixture authoring becomes: question → plausible answer → lock fixture, while missing substrate is never surfaced. Fitness comparisons and reasoner evaluation then run against a golden context that was never validated against what the representation actually encodes.

## The Reframe

Human-Assisted Substrate Completeness Analysis (HSCA) exists to stop memory from silently becoming context.

It is a **cooperative** protocol, not a human-versus-AI contest and not a taxonomy drill. Cooperation runs in **both directions**:

1. **Human → substrate** — A blinded human answers from permitted evidence only. An AI reviewer checks whether each substantive claim is **present in the substrate**, cites the source when it is, and calls out gaps when it is not.
2. **Human → AI** — The same human reviews the AI answer against permitted evidence. The human rejects unsupported AI claims, confirms sourced claims, and records where the AI inferred beyond substrate.

Neither direction alone is enough. AI-only validation still hallucinates structure. Human-only validation still smuggles in memory. **Full HSCA requires both checks** before a known outcome (`Q_fixture`) or golden context can be locked.

Through that bidirectional loop, the study derives a defensible `Q_fixture` and a defensible golden context: a representation that actually carries what a good answer requires, with both human and AI answers audited against substrate.

HSCA is not answer authority by itself. It is experimental evidence that makes memory confounds visible before they infect benchmarks.

The target protocol is bidirectionally cooperative. The current evidence boundary supports collection and reporting readiness only. **Full HSCA is not implemented.** `Q_fixture`, rubric authority, and meaningful fitness comparison must wait until both validation directions exist in apparatus.

## The Model

### Two roles in the MVC program

HSCA serves two distinct jobs. They share vocabulary but run at different times:

| Role | When | Question |
|------|------|----------|
| **Upstream — golden context** | Before a task fixture or known outcome (`Q_fixture`) is locked | Does this representation actually encode what a good answer requires, or did memory fill the gaps? |
| **Downstream — interpretation guard** | After a reasoner or benchmark run | Did this result fail because of the model, or because substrate, assembly, or memory confounded the condition? |

Upstream HSCA is how fixture authoring earns defensible `Q`. Downstream HSCA stops post-hoc scores from being read as model evidence when the golden context was never validated.

Both roles need the same gap vocabulary. Only upstream currently has the strongest claim on the cooperative human-plus-AI substrate check.

### Cooperative validation loop (target)

The core loop is bidirectional review, not classification by intuition:

```text
task + permitted substrate
  → human blinded answer (H_obs)
  → AI blinded answer (A_obs)
  → AI validates human: each H_obs claim present in substrate? cite or gap
  → human validates AI: each A_obs claim present in substrate? confirm or reject
  → gap record (D_cls) for unsupported claims in either direction
  → revise context or packet (not only rewrite answer prose)
  → repeat until both answers are substrate-sourced or gaps are explicit
```

Blinding matters because a participant who has already seen model scores, gold strings, or rubric outcomes can unconsciously supply the missing substrate from memory.

This loop is the **north-star protocol**. It is not implemented in the benchmark harness yet.

### `Q_fixture` prerequisite

No task fixture should claim a known outcome (`Q_fixture`) until full HSCA completes for that task at the active evidence boundary.

| Prerequisite | Why |
|--------------|-----|
| Blinded `H_obs` | Human answer recorded without pre-exposure to scores or gold |
| Blinded `A_obs` | AI answer recorded under the same permitted-evidence boundary |
| AI validates human | Memory-only human claims are surfaced before lock-in |
| Human validates AI | AI inference beyond substrate is surfaced before lock-in |
| `D_cls` from comparison | Gaps are structural outputs, not unchecked judgment |
| Representation revision | Packet or context updated when substrate is missing or unassembled |
| Explicit `B_gap` or `U_d` | Authority missing and unresolved cases stay visible instead of forcing closure |

Until these are satisfied, the MVC program may run instrument checks, pilot discrimination, and collection-readiness tests. It must not treat local mechanical scores or author judgment as `Q`.

### Current capability boundary

The operational harness outside this handbook currently supports the following HSCA capabilities:

| Capability | Status | Notes |
|------------|--------|-------|
| Blinded human observation capture | **Shipped** | The collection workflow writes append-only `H_obs` records with `memory_origin`, `evidence_sources`, blinding flag, fingerprints, and `authority_effect: observational_only`. |
| Disagreement record schema | **Shipped** | The disagreement record shape defines `D_cls`, `D_adj`, and observational-only boundary. |
| Completeness report aggregation | **Shipped** | The reporting workflow counts existing `classification` values into `C_sub`, `C_asm`, `C_mem`, `C_rep`, and collection readiness fields. |
| Synthetic fixture validation | **Shipped** | Synthetic fixtures exercise record shape, unresolved preservation, and report math. |
| Validator integration | **Shipped** | The validation layer checks HSCA manifest policy, record shape, generation/fingerprint alignment, and report fields. |
| AI validates human claims against substrate | **Not shipped** | No automated review step compares each claim in `H_obs` to packet/substrate content and emits sourced citations or gap findings. |
| Human validates AI claims against substrate | **Not shipped** | No protocol step records human confirm/reject of each substantive `A_obs` claim against permitted evidence. |
| Automated `classify()` | **Not shipped** | `D_cls` is stored on disagreement records; it is not derived automatically from bidirectional substrate inspection in code today. |
| Cooperative review driver | **Not shipped** | No first-class workflow runs the full iterate-until-both-sides-sourced loop or locks `Q_fixture`. |
| Dedicated HSCA `A_obs` path | **Not shipped** | Reasoner run records serve a different role; there is no first-class blinded `A_obs` paired to the HSCA cooperative step. |

**Operator workflow today:**

1. Participant answers blinded; operator records `H_obs` via the collection helper.
2. A separate step authors or updates a disagreement record with `D_cls` (manual or out-of-band review today).
3. The HSCA reporting step aggregates counts into a generation-scoped report.
4. Interpretation uses those counts as evidence signals, not as answer authority.

Synthetic fixtures prove steps 2–3 can run. They do not prove step 1 plus an automated step 2 on real tasks.

### Target protocol (to build)

The next harness tranche should implement **full HSCA** — bidirectional cooperative validation — not more collection plumbing alone:

1. **Blinded `A_obs`** — Record an AI answer under the same permitted-evidence boundary as `H_obs`, without exposing scores or gold to either side prematurely.
2. **AI validates human** — For each substantive claim in `H_obs`, verify presence in permitted substrate. Emit present, absent, or cite `type:id`.
3. **Human validates AI** — For each substantive claim in `A_obs`, the human confirms or rejects against permitted substrate and records rationale. Unsupported AI inference becomes a first-class gap, not silent acceptance.
4. **Gap write** — Produce `D_cls` from both comparisons plus `M_org` and `E_src`, not from either participant's unchecked judgment.
5. **Revision hook** — When gaps are substrate-missing or present-not-assembled, require packet/context revision before fixture lock-in.
6. **Fixture lock** — Record `Q_fixture` only when **both** `H_obs` and `A_obs` are substrate-sourced, gaps are explicit, or `B_gap` blocks progress.

Until those steps exist, the handbook equations below describe **target notation**. Reports already implement the aggregation half.

### Gap labels

Gap labels name what the cooperative check found — not what a participant guessed:

- substrate missingness — required information is not encoded in authoritative substrate,
- substrate present but not assembled — encoded information did not reach the assembled condition,
- assembly failure — assembly mechanism failed under declared rules,
- ambiguous task or authority gap — no authority surface resolves the requirement,
- human memory only — observation cites knowledge not present in permitted substrate,
- human stale memory — recalled knowledge conflicts with substrate or evidence,
- AI reasoning error — substrate and assembly appear sufficient; disagreement tracks to reasoner behavior,
- unresolved evidence — the cooperative check cannot close the case under current authority.

In the target protocol, these labels are **outputs of substrate comparison**. In the current harness, they are **allowed values on disagreement records** awaiting automated derivation.

### Memory confound and lossy reasoning

HSCA exists because fixture authors and study participants share the same decay modes the thesis names:

- **Rationale decay** — the answer sounds right but supporting structure was never encoded.
- **Context loss** — conditions that bound the original decision are recalled as unconditional fact.
- **Assumption loss** — binding limits are obeyed but no longer articulable from substrate.
- **Drift** — embodied state and recorded intent diverge; memory bridges the gap invisibly.

`memory_origin` and `evidence_sources` on `H_obs` exist to separate **what was read from permitted evidence** from **what was reconstructed from recall**. That separation is the first guard. The AI substrate check is the second: even a sincere human can be wrong if recall filled in missing structure.

### Live collection fields

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

**Disagreement attribution.** Gap classification compares task requirements to substrate and assembly state, using blinded observations as probes:

```text
D_cls(task, candidate, generation) =
  classify(
    task requirements,
    substrate encoding,
    assembled condition,
    permitted evidence,
    human observation record (H_obs),
    AI observation record (A_obs),
    blinding verification (B_ver),
    memory origin (M_org),
    structured evidence sources (E_src),
    task fingerprint (T_fp),
    evidence boundary (G_b)
  )
```

`D_cls` is a structural gap label, not a correctness score and not a vote by the participant. Adjudication result (`D_adj`) may be recorded separately and must not silently promote observations into benchmark or architecture authority.

**Harness note:** Current reporting aggregates whatever `classification` is already on disagreement records. The `classify(...)` function in the equation is **target behavior**, not current automation.

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

**Golden-context and known outcome.** HSCA is how a task fixture earns its `Q`. The bidirectional cooperative loop above is the authoring path; the equation is the compact form:

```text
Q_fixture(task, generation) =
  cooperative_review(
    task,
    draft context or packet,
    H_obs,
    A_obs,
    validate_AI_checks_human(H_obs, substrate),
    validate_human_checks_AI(A_obs, substrate),
    D_cls
  )
  until H_obs and A_obs claims are substrate-sourced
     OR gaps are explicit and unresolved (U_d)
     OR authority is missing (B_gap)
```

`Q_fixture` is blocked until both validation directions complete. A gold answer string stored without that review is not a known outcome; it is unchecked author judgment.

**Link to reasoner evaluation.** After fixture lock-in, HSCA reports still guard interpretation of reasoner results:

```text
Interpret(Q_local or Q_reasoner) requires
  C_sub, C_asm, C_mem, C_rep, U_d, B_gap
```

If memory-only or missing-substrate signals are high, a surprising reasoner score may be a fixture problem, not a representation-ceiling result.

### Future substrate-arm studies

The same cooperative protocol can later support experiments on **human answerability under controlled decay**, not only fixture authoring. Example arms:

- memory alone — no substrate access beyond the task prompt,
- Nygard-style prose ADRs with synthetic rationale decay applied,
- STE structured ADRs and Architecture IR surfaces,
- code graph or operational graph alone,
- full STE substrate with assembly variants.

An AI-generated question bank supplies tasks; HSCA supplies the cooperative check that separates what was answered from memory from what the substrate actually encoded. That program is future work.

Each arm holds the question bank and evaluation protocol constant while changing only the substrate condition. The dependent signal is not "did the human win" but **how much of the answer came from substrate versus memory**, and whether decayed substrates predictably increase memory-only classifications.

### Interpretation rules

Use HSCA evidence conservatively:

- If `H_obs` cites knowledge with no matching `evidence_sources` entry in permitted substrate, treat it as a **memory-only signal** until the cooperative check closes or refutes it.
- If `C_sub` or `C_mem` counts are high for a task used in fitness comparison, **do not lock `Q_fixture`** for that task until upstream review completes.
- If reasoner scores move but HSCA shows assembly or substrate gaps, investigate **fixture and packet quality** before interpreting representation effects.
- If `U_d` or `B_gap` is non-zero, preserve the uncertainty in publications. Unresolved and authority-missing are valid outcomes, not defects to hide.
- A positive reasoner result does not override a negative HSCA completeness signal. They measure different things.

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

- HSCA protects golden context from latent human memory — the main confound in fixture authoring and in designer/researcher self-evaluation.
- **Target:** bidirectional cooperative validation — AI checks the human, the human checks the AI — before `Q_fixture` lock-in.
- **Today:** full HSCA is not implemented. Only blinded `H_obs` capture and count-only reports are shipped.
- **Blocked until full HSCA:** defensible `Q_fixture`, rubric/gold authority, and fitness comparisons that require known outcomes.
- HSCA serves upstream fixture authoring and downstream reasoner interpretation; do not collapse the two roles.
- Human memory does not become architecture authority unless captured through accepted artifacts. AI citations do not become answer authority without adjudication.
- Publications must say whether HSCA claims rest on synthetic fixtures, live collection only, or completed cooperative review.

## Relationship to STE system

HSCA supports [Evidence](../../../../03-artifacts/03-05-evidence.md) and [Traceability](../../../../03-artifacts/03-06-traceability.md) by making completeness and disagreement inspectable. It does not replace ADRs, invariants, Architecture IR, benchmark adjudication, or Kernel admission.

Operational harness behavior lives in the MVC benchmark suite repository path referenced by [Benchmark methodology](benchmark-methodology.md). The handbook records method and boundaries; it does not duplicate command-level harness documentation.

Related MVC methodology pages:

- [MVC methodology](mvc-methodology.md) — research unit, evidence boundary, interpretation rules
- [Benchmark methodology](benchmark-methodology.md) — discrimination instrument and task controls
- [Context preflight methodology](context-preflight-methodology.md) — what context was assembled before evaluation
- [MVC candidate equation variables](candidate-equation-variables.md) — shared `Q`, `R_q`, `C_v` notation

## Summary

- HSCA stops latent human memory and unchecked AI inference from contaminating golden context and `Q_fixture`.
- **Upstream:** earn `Q_fixture` only after bidirectional cooperative review. **Downstream:** guard reasoner interpretation when gaps remain.
- **Full HSCA is not implemented** at the current evidence boundary.
- **Shipped:** blinded `H_obs`, disagreement schema, count-only reports, synthetic validation.
- **Not shipped:** AI validates human, human validates AI, automated `classify()`, cooperative loop driver, `Q_fixture` lock.
- Gap labels are target outputs of substrate comparison; today they are authored on disagreement records.
- Future substrate-arm studies may measure answerability under controlled decay and AI-generated question banks.
- HSCA reports completeness and gaps as evidence, not benchmark or architecture authority.
