---
title: "HSCA Methodology"
status: draft
maturity: L2
diagrams: true
last_reviewed: "2026-08-02"
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

Neither direction alone is enough. AI-only validation still hallucinates structure. Human-only validation still smuggles in memory. **Full HSCA requires both checks** before a substrate-closed `Q` or golden context can be locked. `Q_fixture` requires a later, separate benchmark adjudication.

Through that bidirectional loop, the study may derive a substrate-closed `Q`: a complete answer whose material claims are supported by the permitted authoritative substrate at a named evidence boundary. `Q` remains distinct from `Q_fixture`. A later benchmark or fitness workflow may promote a closed `Q` to `Q_fixture` only through its own explicit adjudication and authority process.

HSCA is not answer authority by itself. It is experimental evidence that makes memory confounds visible before they infect benchmarks.

The target protocol is bidirectionally cooperative. The current evidence boundary supports live sealed collection, durable claim-level closure, and bounded substrate-closed `Q` promotion. B1Q1 and B1Q2 have completed that closure protocol for their named evidence boundaries. This does not establish that all questions or batches are closed. `Q_fixture`, rubric or gold benchmark adjudication, and research fitness remain absent. Collection provenance must not be read as completeness or correctness, and a closed `Q` must not be read beyond its declared boundary or authority ceiling.

## The Model

### Two roles in the MVC program

HSCA serves two distinct jobs. They share vocabulary but run at different times:

| Role | When | Question |
|------|------|----------|
| **Upstream — golden context** | Before substrate-closed `Q`, and before any later `Q_fixture` adjudication | Does this representation actually encode what a good answer requires, or did memory fill the gaps? |
| **Downstream — interpretation guard** | After a reasoner or benchmark run | Did this result fail because of the model, or because substrate, assembly, or memory confounded the condition? |

Upstream HSCA is how fixture authoring earns defensible `Q`. Downstream HSCA stops post-hoc scores from being read as model evidence when the golden context was never validated.

Both roles need the same gap vocabulary. Only upstream currently has the strongest claim on the cooperative human-plus-AI substrate check.

### Observation modes and stream boundaries

HSCA distinguishes the observation condition from the participant type. Each sealed answer records one explicit mode:

| Observation mode | Meaning |
|------------------|---------|
| `human_memory_only` | A human answers without substrate access. The answer records recall as an observation; it does not grant recalled material substrate authority. |
| `human_evidence_assisted` | A human answers with access only to the declared permitted substrate. The answer remains observational until its claims are mapped and adjudicated. |
| `ai_original_substrate` | An AI answers from the declared permitted substrate under the original collection ordering and isolation controls. |
| `ai_repaired_substrate` | An AI produces a new append-only observation after a defect in the original AI input version, boundary, or execution condition is corrected. It links to, but never replaces, the original observation. |

Each human and AI observation stream has its own immutable observation boundary. That boundary identifies the question, permitted evidence, substrate snapshot, execution condition, and sealed answer without exposing the other stream before both independent observations are complete. The later closure-review boundary may include both streams and their mappings; it does not retroactively change either observation condition.

A repaired AI observation may be used in closure only with its repair lineage and changed execution condition made explicit. It cannot inherit or assert the chronology of an original AI observation, including an original AI-before-human ordering that the repaired execution did not satisfy. The original and repaired observations remain separately addressable research artifacts.

### Cooperative validation loop (target)

The core loop is bidirectional review, not classification by intuition:

```text
task + permitted substrate
  → AI blinded answer sealed before human exposure (A_obs)
  → human blinded answer (H_obs) under sealed collection controls
  → independently decompose both answers into exact claim spans
  → independently map each claim to permitted substrate
  → normalize semantically related claims without discarding qualifiers
  → AI validates human mappings; human validates AI mappings
  → adjudicate every claim and preserve unsupported or incorrect claims
  → derive required answer elements independently from substrate
  → construct a candidate authoritative answer from supported claims
  → map every candidate-answer sentence back to adjudicated claims
  → validate correctness, completeness, authority, and reproducibility
  → reciprocal AI review approves the candidate and closure package hashes
  → human reviews the same package and locks the final candidate and package hashes
  → mechanically validate and promote the bounded answer to Q
  → revise context or packet (not only rewrite answer prose)
  → repeat when any material gap or rejection remains
```

Sealed collection uses AI-before-human ordering; reciprocal review later remains bidirectional.

Blinding matters because a participant who has already seen model scores, gold strings, or rubric outcomes can unconsciously supply the missing substrate from memory.

This loop is the **north-star protocol**. It is realized for closed questions at their named evidence boundaries (currently B1Q1 and B1Q2 via apparatus-integrated closure). It is not yet a general or scaled closure capability, and it does not grant `Q_fixture`, benchmark adjudication, or research-fitness authority.

### Closure records and review projection

The canonical closure evidence is an append-only record set, not a mutable table. It preserves:

- the two unchanged sealed answers;
- exact claim spans and hashes for each answer;
- normalization relations between semantically related claims;
- claim-to-substrate mappings;
- reciprocal reviewer judgments;
- adjudicated claim status;
- independently derived required answer elements;
- candidate-answer versions and sentence-level traceability;
- validation results, reviewer approvals, and closure lineage.

A claim matrix is the primary human review projection over those records:

| Claim ID | Normalized claim | Relation | Human claim | Human status | AI claim | AI status | Authoritative source | Authority class | Manifest status | Locator | Authoritative verbiage | Adjudication | Evidence confidence |
|----------|------------------|----------|-------------|--------------|----------|-----------|----------------------|-----------------|-----------------|---------|-------------------------|--------------|---------------------|

Exact wording need not match for two claims to be related. Normalization must record whether claims are equivalent, overlap, subsume one another, conflict, or remain unrelated. It must preserve modality, scope, conditions, exceptions, and authority qualifiers. A normalized claim is an alignment object, not a replacement for either original claim.

Status values are `supported`, `qualified`, `unsupported`, `incorrect`, `incomplete`, `not_applicable`, and `unresolved`. Unsupported and incorrect claims remain part of the record. Their preserved existence does not block closure after valid adjudication, provided they are excluded from the final answer or corrected there. Shared agreement does not convert an unsupported claim into a supported one.

The matrix cannot establish completeness by itself because both answers may omit the same required proposition. A separate completeness ledger derives required answer elements from authoritative substrate independently of either answer:

| Required answer element | Authoritative source and verbiage | Human coverage | AI coverage | Final-answer coverage | Status |
|-------------------------|-----------------------------------|----------------|-------------|-----------------------|--------|

### Source discovery and claim authority

Derived discovery surfaces may accelerate traversal without becoming claim authority. A source-locator registry can resolve entity identity, repository, path, source hash, provenance class, and graph snapshot. An owning ADR or artifact manifest can establish membership, lifecycle status, supersession, and declared ownership. Neither surface substitutes for the resolved source artifact.

The required traversal is:

```text
source-locator registry
  → owning artifact manifest
  → resolved authoritative artifact
  → exact supporting or contradicting verbiage
  → claim mapping and reviewer judgment
```

Every supported or qualified mapping records artifact identity, authority class, manifest status, snapshot or version, source hash where available, precise locator, short exact verbiage, mapping rationale, and evidence confidence. Reviewers must verify that the cited language entails the claim at its stated scope. Discovery metadata may prove where an artifact came from; it does not prove the claim the artifact is cited to support.

### Adjudication and answer construction

Adjudication and authoritative-answer construction are separate artifacts. Adjudication decides which propositions are supported, qualified, unsupported, incorrect, incomplete, not applicable, or unresolved. Construction assembles the smallest complete answer warranted by the adjudicated claim set and the independent completeness ledger.

Every sentence in the candidate authoritative answer must trace to one or more adjudicated claims and their source mappings. The candidate answer is then decomposed and mapped again. Human and AI reviewers approve support, correctness, completeness, and authority boundaries against the identical candidate-answer hash. Rejection creates a new immutable closure round; it does not overwrite prior reasoning.

The reciprocal AI review precedes the final human lock. That lock binds the exact candidate-answer hash and the already reviewed closure-package hash. Once the lock exists, promotion is a deterministic validation and publication operation: it performs no further semantic interpretation and invokes no semantic model. Any semantic change requires a new append-only candidate round, reciprocal review, and human lock.

### Validation profile

Closure reports separate dimensions rather than blending them into one compensatory score:

- observation-claim coverage;
- required-answer-element coverage;
- evidentiary sufficiency;
- claim-to-source mapping confidence;
- authority validity;
- citation reproducibility;
- normalization validity;
- final-answer sentence traceability;
- reciprocal-review completion.

If a headline completeness confidence is required, it is the minimum of the required dimensions, not their average. A numeric value never overrides a hard blocker. Unclassified material claims, absent required elements, unverifiable citations, invalid authority, unresolved contamination, incomplete reciprocal review, unapproved answer hashes, or unsupported claims carried into the final answer block closure regardless of other scores.

### `Q` and `Q_fixture` prerequisites

No question should be promoted to substrate-closed `Q` until full HSCA completes for that task at the active evidence boundary. No task fixture should claim a benchmark known outcome (`Q_fixture`) until `Q` exists and a separate benchmark adjudication grants that authority.

| Prerequisite | Why |
|--------------|-----|
| Blinded `H_obs` | Human answer recorded without pre-exposure to scores or gold |
| Blinded `A_obs` | AI answer recorded under the same permitted-evidence boundary |
| AI validates human | Memory-only human claims are surfaced before lock-in |
| Human validates AI | AI inference beyond substrate is surfaced before lock-in |
| `D_cls` from comparison | Gaps are structural outputs, not unchecked judgment |
| Representation revision | Packet or context updated when substrate is missing or unassembled |
| Explicit `B_gap` or `U_d` | Authority missing and unresolved cases stay visible instead of forcing closure |
| Complete claim matrix | Every material human and AI claim remains visible and classified |
| Independent completeness ledger | Shared omissions cannot pass as a complete answer |
| Revalidated candidate answer | Every final sentence traces to adjudicated authoritative claims |
| Reciprocal review and final human lock | AI review and human approval bind the same bounded answer and closure package without rewriting sealed observations |

Until these are satisfied, the MVC program may run apparatus validation, instrument calibration, and collection-readiness tests. Local discrimination under a fixed reasoner may be reported as instrument sensitivity only. It must not be treated as research fitness, and it must not treat local mechanical scores, source discovery, reviewer consensus, or author judgment as `Q` or `Q_fixture`.

Promotion to `Q` additionally requires:

- valid sealed-answer identities and hashes;
- an immutable, replayable evidence boundary;
- complete claim decomposition for both answers;
- reviewed normalization relations;
- classification of every material claim;
- reproducible evidence for every supported or qualified claim;
- preserved unsupported and incorrect claims;
- registry resolution, owning-manifest checks, source-hash verification, and supersession checks where those surfaces exist;
- independent enumeration and coverage of required answer elements;
- sentence-level traceability for the final answer;
- final-answer revalidation;
- reciprocal AI review followed by a final human lock over the same answer and closure-package hashes;
- no unresolved material authority, provenance, contamination, snapshot, or completeness blocker;
- an explicit authority ceiling that denies automatic `Q_fixture`, benchmark, fitness, publication, architecture, runtime, or production authority.

The working dependency is conservative: no validated apparatus, no defensible `Q`; no defensible `Q`, no eligible input to `Q_fixture` adjudication; no adjudicated `Q_fixture`, no benchmark authority; no benchmark authority, no research fitness authority.

### Current capability boundary

Handbook status uses durable capability classes, not dated run inventories:

| Capability class | Status | Meaning |
|------------------|--------|---------|
| Live sealed paired collection | Present | Independent AI-before-human sealing, append-only locks, isolation, contamination accounting; observational only. |
| Apparatus-integrated semantic review | Present for closed questions | Independent mappings, normalization, adjudication, completeness, candidate traceability, reciprocal review, and final human lock are durably recorded for B1Q1 and B1Q2. Other questions remain open until they complete the same protocol. |
| Mechanical closure and `Q` promotion contracts | Present with live records | Deterministic gates, bounded promotion, replay, and repository-admitted evidence exist. B1Q1 and B1Q2 have immutable substrate-closed `Q` records. |
| Benchmark adjudication to `Q_fixture` | Absent | No rubric/gold adjudication path; no research fitness authority. |

Live sealed collection establishes provenance and ordering. It does not establish substrate completeness or answer correctness. Synthetic review establishes wiring and fail-closed behavior. It does not complete live reciprocal review or grant `Q_fixture`.

### Collection apparatus readiness boundary

HSCA requires a validated collection apparatus before live observations can become research evidence. This is analogous to laboratory instrumentation validation: before an experiment can use observations, the collection instrument must be shown to record the right metadata, preserve traceability, reject invalid inputs, and keep synthetic tests out of research evidence.

The methodology requires four apparatus states, independent of any project-specific gate name or implementation plan:

1. **Apparatus implementation.** The collection system has record shapes, producer paths, isolation controls, recorder-only storage, and validation entry points.
2. **Apparatus validation.** Synthetic or local-test artifacts validate collection mechanics without creating research evidence.
3. **Failure-mode validation.** The apparatus demonstrates fail-closed behavior, provenance checks, replayability, leakage detection, quarantine behavior, exclusion semantics, and traceability.
4. **Apparatus readiness.** The validated apparatus is frozen or otherwise controlled so live evidence collection can begin under a known configuration.

Only after apparatus readiness is established should live HSCA evidence collection begin. Subsequent GA, MVC, RSS, representation-ceiling, substrate-quality, human-performance, and AI-performance studies may consume evidence collected through that apparatus. Apparatus validation does not validate those later studies. It validates only the instrument they depend on.

Apparatus validation is distinct from evidence collection, evidence adjudication, benchmark authority, rubric authority, publication evidence, experimental conclusions, and methodology claims. It does not validate HSCA hypotheses, validate MVC, validate production RSS, materialize MVC-M, invoke kernel admission, introduce authoritative `Q`, implement full GA, establish benchmark authority, establish rubric authority, create publication evidence, or support experimental conclusions.

Synthetic local-test outputs are engineering validation artifacts only. They are not MVC experiment evidence, HSCA evidence, representation-ceiling evidence, benchmark answer authority, rubric authority, publication evidence, adjudication inputs, substrate-quality evidence, human-performance evidence, AI-performance evidence, or research conclusions. Their contribution is confidence that collection machinery can fail closed and preserve traceability before live HSCA evidence is collected.

The broader conceptual instrument is described in [MVC experimental apparatus](experimental-apparatus.md). HSCA supplies the substrate-completeness and memory-confound side of that instrument; it does not make apparatus validation into research validation.

**Operator workflow today:**

1. Prepare a sealed question bank and immutable question identities.
2. Import and lock independent substrate-grounded AI answers before human exposure.
3. Present one participant surface at a time and lock the human memory-only answer verbatim.
4. Validate collection ordering, isolation, hashes, deviations, contamination fields, and paired-answer completeness.
5. Regenerate the durable generation-scoped report.
6. Interpret collection counts as readiness and provenance evidence, not answer authority.
7. Use the operator closure protocol for independent decomposition, mapping, normalization, completeness audit, candidate construction, traceability validation, and reciprocal review.
8. After reciprocal review and explicit human approval bind the same candidate and package hashes, record the final lock, promote the bounded `Q` mechanically, and admit the exact promotion dependency closure as tracked research evidence.

### Implemented closure capabilities and remaining boundary

Live paired observation collection and apparatus-integrated closure are shipped. The realization includes:

1. **Durable closure records** — Exact claims, independent mapper outputs, normalization relations, evidence mappings, reciprocal judgments, completeness requirements, candidate-answer rounds, clause traceability, validation dimensions, approvals, and blockers are append-only records.
2. **Apparatus-owned writers** — Semantic workers return bounded proposals; deterministic writers bind identities, hashes, evidence metadata, lifecycle state, and immutable phase commits.
3. **Process-graph validation** — Question, run, snapshot, lock, source, claim, relation, adjudication, candidate, approval, and predecessor identities are verified across the closure lifecycle.
4. **Durable reporting and replay** — Closure state and human review surfaces are projections from immutable records. Mechanical replay does not silently reproduce or replace semantic judgments.
5. **Atomic Q promotion** — A bounded substrate-closed `Q` is written only when the mechanical gate and both reviewer approvals reference the same answer and package hashes and every material blocker is resolved.
6. **Repository admission** — After promotion, the exact immutable `Q`, promotion commit, closure dependency graph, selected observations, question identity, and snapshot lineage are admitted as tracked evidence through a hash-bound manifest. Unpromoted live collection remains ignored and isolated.
7. **Closure after-action review and Q lineage** — Append-only AAR records may evaluate apparatus cost, failures, and schema pressure without changing the closed evidence. Later answers supersede, coexist with, or withdraw earlier `Q` records through explicit relationships rather than mutation.

The remaining boundary is separate **fixture adjudication**: promotion from `Q` to `Q_fixture` requires its own benchmark-authority process. HSCA closure alone does not grant fitness use. The equations below remain methodological notation; their operational records are governed by the apparatus contracts rather than duplicated here.

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

Weak structural connectivity should not be collapsed into substrate missingness by default. A weak or absent relationship may mean the relationship does not exist, has not been observed, has not been represented, has not been adjudicated, sits outside current substrate scope, or lacks sufficient supporting evidence. HSCA records those possibilities as observational evidence about completeness and reasoning requirements. It does not turn any one observation into answer authority.

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

**Golden-context and known outcome.** HSCA is how a question earns a substrate-closed `Q`. The bidirectional cooperative loop above is the authoring path; the equation is the compact form:

```text
Q(task, generation, substrate_snapshot) =
  cooperative_review(
    task,
    draft context or packet,
    H_obs,
    A_obs,
    validate_AI_checks_human(H_obs, substrate),
    validate_human_checks_AI(A_obs, substrate),
    D_cls
  )
  until every material claim is adjudicated,
        every required answer element is covered,
        every final sentence is traceable,
        and both reviewers approve the same answer hash
```

`Q` is blocked while material gaps, missing authority, incomplete provenance, contamination, or reciprocal-review failures remain. Explicit unresolved gaps remain valid HSCA outcomes, but material unresolved gaps block `Q` rather than being forced closed. A gold answer string stored without this review is unchecked author judgment. `Q_fixture` remains a separate downstream adjudication.

**Link to reasoner evaluation.** After any later `Q_fixture` adjudication, HSCA reports still guard interpretation of reasoner results:

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
- If `C_sub` or `C_mem` counts are high for a task used in fitness comparison, **do not close `Q` or promote `Q_fixture`** for that task until upstream review completes.
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
- **Target:** bidirectional cooperative validation, claim adjudication, independent completeness checking, and reciprocal approval before bounded `Q` closure.
- **Closed per question:** substrate-closed `Q` is available only for a question whose claim-level review, completeness validation, reciprocal approval, and promotion gates have completed. `Q_fixture`, rubric/gold authority, and research fitness remain blocked until their separate downstream adjudication also completes.
- HSCA serves upstream fixture authoring and downstream reasoner interpretation; do not collapse the two roles.
- Human memory does not become architecture authority unless captured through accepted artifacts. AI citations do not become answer authority without adjudication.
- Publications must not treat synthetic/local-test HSCA outputs as MVC experiment evidence. Harness documentation should distinguish synthetic mechanism tests, local instrument calibration, live collection, and completed cooperative review.

## Relationship to STE system

HSCA supports [Evidence](../../../../03-artifacts/03-05-evidence.md) and [Traceability](../../../../03-artifacts/03-06-traceability.md) by making completeness and disagreement inspectable. It does not replace ADRs, invariants, Architecture IR, benchmark adjudication, or Kernel admission.

Operational harness behavior lives in the owning research apparatus outside handbook prose. The handbook records method and boundaries; it does not duplicate command-level harness documentation.

Related MVC methodology pages:

- [MVC methodology](mvc-methodology.md) — research unit, evidence boundary, interpretation rules
- [Benchmark methodology](benchmark-methodology.md) — discrimination instrument and task controls
- [MVC experimental apparatus](experimental-apparatus.md) — conceptual apparatus capability and non-claim boundaries
- [Context preflight methodology](context-preflight-methodology.md) — what context was assembled before evaluation
- [MVC candidate equation variables](candidate-equation-variables.md) — shared `Q`, `R_q`, `C_v` notation

## Summary

- HSCA stops latent human memory, unchecked AI inference, normalization loss, and shared omission from contaminating golden context.
- **Upstream:** earn substrate-closed `Q` only after claim-level evidence review, independent completeness checking, answer revalidation, and reciprocal approval. **Downstream:** separately adjudicate any `Q_fixture` and guard reasoner interpretation when gaps remain.
- A final human Q lock follows reciprocal AI review and ends semantic work for that round; deterministic validation and publication alone may follow it.
- **Full HSCA is complete for B1Q1 and B1Q2 at their declared evidence boundaries; it is not complete for the remaining question set.**
- **Shipped — live:** sealed question identity, independent substrate-grounded AI prelock, human memory-only capture, strict ordering, paired answer locks, deviation and contamination accounting, and durable collection reporting.
- **Shipped — apparatus-integrated closure:** independent claim mapping, qualified source traversal, normalization, completeness audit, candidate-answer review, matrix and traceability validation, reciprocal approval, deterministic locking and promotion, repository admission, replay, and bounded substrate-closed `Q` records.
- **Not shipped — downstream authority:** separate real `Q_fixture` promotion, benchmark or rubric authority, and research fitness-use authority.
- A zero gap count is meaningful only within a completed closure record and its named evidence boundary; an absent closure record is missing evidence, not zero gaps.
- Gap labels are outputs of substrate comparison. Synthetic scenarios validate mechanisms; live closed-question records supply research-apparatus evidence within their declared authority ceilings.
- Future substrate-arm studies may measure answerability under controlled decay and AI-generated question banks.
- HSCA reports completeness and gaps as evidence, not benchmark or architecture authority.

Read next: [MVC methodology](mvc-methodology.md) shows how HSCA fits into the broader MVC research unit and interpretation rules.
