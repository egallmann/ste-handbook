---
title: "MVC Candidate Equation Variables"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# MVC Candidate Equation Variables

## The Problem

MVC research needs candidate equations, but an equation is not useful unless its variables are visible. If variables remain implicit, a study can accidentally measure representation volume, retrieval convenience, configuration drift, or scoring sensitivity while claiming to measure viable context.

## The Reframe

Candidate equation variables are research notation. They identify what the MVC research program can observe, derive, or still cannot measure. They do not define STE contracts, MVC production fields, benchmark authority, or Kernel admission.

## The Model

The current candidate equation shape is:

```text
Q_task,persona =
  f(representational substrate,
    substrate affordances,
    assembly configuration,
    representation structural quality,
    viable-context sufficiency,
    candidate context structure,
    controls,
    reasoner or participant condition,
    interaction terms)
```

`Q` means reasoning quality for a task and persona. It is a future target variable until answer correctness, answer completeness, source fidelity, hallucination, confidence, and repeated-run stability have suitable evaluation authority.

### Observed Variables

Observed variables are directly represented in the research substrate or evidence package:

| Variable | Meaning |
|----------|---------|
| `E` | candidate entities |
| `R` | candidate relationships |
| `P` | provenance completeness or classification |
| `F` | freshness |
| `A` | admission result, where admission is in scope |
| `I` | invariant compliance |
| `T` | topology metrics |
| `N` | negative space |
| `B` | budgets |
| `O` | operational graph metrics |
| `L` | source locator coverage |
| `M` | attribution or embodiment coverage |
| `X` | projection level or compression metadata |
| `U` | attributed implementation entities |
| `J` | enforced invariant links |
| `G_b` | blast-radius graph over dependency and attribution edges |
| `R_m` | repository manifest coverage |
| `F_m` | operational file manifest coverage and freshness |
| `A_d` | assembly definition |
| `A_g` | assembly algorithm and version bound to the assembly definition |
| `S_b` | representational substrate |
| `S_af` | substrate affordance set |
| `A_s` | admissible assembly configuration space |
| `A_c` | selected or evolved assembly configuration |
| `A_p` | prohibited assembly mechanisms |
| `C_id` | configuration identity |
| `C_hash` | configuration fingerprint or hash |
| `C_fix` | fixed configuration field set |
| `C_var` | varied configuration field set |
| `C_eq` | configuration equivalence or non-equivalence class |
| `C_drift` | configuration drift |
| `B_g` | evidence boundary or generation |
| `E_hash` | experiment fingerprint |
| `P_id` | candidate context artifact identity |
| `P_hash` | candidate context artifact hash |
| `P_m` | candidate context artifact metrics |
| `P_h` | context health |
| `I_h` | instrument health |
| `Q_local` | local mechanical score |
| `D_local` | local task discrimination status |
| `R_q` | representational structural quality proxy |
| `C_v` | viable-context sufficiency proxy |

These variables may be renamed or namespaced in later publications. The current notation is a research aid, not a schema.

### Derived Variables

Derived variables are computed from observed variables under a declared method:

| Variable | Meaning |
|----------|---------|
| `D` | context-domain composition |
| `G` | graph-domain composition |
| `S` | selector composition |
| `V` | persona policy composition |
| `C` | structural context completeness proxy |
| `W` | operational workspace coverage proxy |
| `C_m` | manifest-derived discovery completeness proxy |
| `C_p` | candidate-context-derived completeness proxy |

Derived variables must cite the method used to compute them. A derived proxy is not a ground-truth measurement unless the study has separate validation authority.

### Future Variables

Future variables name target measurements the current research program wants but should not pretend to have:

| Variable | Meaning |
|----------|---------|
| `Q` | reasoning quality |
| `K` | answer correctness |
| `L_answer` | answer completeness |
| `Y` | source fidelity |
| `H` | hallucination or unsupported-claim rate |
| `Z` | stability or consistency across repeated runs |

These variables require additional evaluation authority, such as rubric adjudication, answer authority, claim-to-evidence mapping, repeated-run protocol, or hosted validation where the study requires it.

### Interaction Terms

MVC candidate equations should preserve interaction terms until evidence supports simplification. Examples include:

| Interaction | Why It Matters |
|-------------|----------------|
| `S_b * A_c` | The same representational substrate (`S_b`) can look better or worse depending on which assembly configuration was selected or evolved for it (`A_c`). Substrate quality and assembly choice must be analyzed together. |
| `S_af * A_c` | Substrate affordances (`S_af`) only affect outcomes when the selected assembly configuration (`A_c`) can actually use them. A rich affordance set with a configuration that ignores it is not a fair test of the substrate. |
| `A_s * R_q` | The admissible assembly configuration space (`A_s`) can cap how much representational structural quality (`R_q`) the study can observe. A substrate may look weak because the search never reached a legitimate configuration. |
| `C_var * R_q` | Varied configuration fields (`C_var`) can change measured representational structural quality (`R_q`) without any change in the underlying representation. Configuration movement can masquerade as representation improvement. |
| `C_drift * Q` | Configuration drift (`C_drift`) can mimic or erase an apparent reasoning-quality (`Q`) effect. If the assembly changed between runs, the study may be measuring instability, not representation. |
| `R_q * C_v` | Representational structural quality (`R_q`) matters through viable-context sufficiency (`C_v`). Strong structure that still fails the task is not sufficient context; sufficiency is where structural quality becomes reasoning-relevant. |
| `A_d * D` | Assembly definition (`A_d`) and context-domain composition (`D`) are coupled. Change what assembly means and you change which domains can appear in the assembled context. |
| `A_g * D` | Assembly algorithm and version (`A_g`) can change which domain structure is assembled (`D`), even when the declared assembly definition stays the same. |
| `V * D` | Persona policy composition (`V`) changes which context domains matter (`D`) for the same task. The consumer shapes what counts as relevant structure. |
| `L * R` | Source locator coverage (`L`) and candidate relationship preservation (`R`) interact. Relationships without locators, or locators without preserved edges, both degrade traceability and reasoning fidelity. |
| `M * D` | Attribution or embodiment coverage (`M`) only helps when the domains that carry embodiment are actually assembled (`D`). Discovery without assembly produces coverage metrics, not usable context. |
| `G_b * R` | Blast-radius graph quality (`G_b`) depends on whether dependency and attribution relationships (`R`) survive into the candidate context. Impact reasoning fails when the graph is present in principle but severed in assembly. |

The research program should estimate interaction effects where the design and sample size permit. Additive weights are hypotheses to test, not assumptions to inherit.

## The Implications

- MVC research should publish variable inventories before publishing equation claims.
- Candidate equations should separate representation quality, assembly quality, and reasoner behavior.
- Missing answer authority should remain visible in the notation.
- Configuration variables are first-order controls, not implementation details.
- Future findings should identify which variables were observed, which were derived, and which remained unmeasured.

## Relationship to STE system

This page applies the general [candidate theories, hypotheses, and equations](../../../14-03-candidate-theories-hypotheses-and-equations.md) doctrine to the MVC research program. It connects to [MVC methodology](mvc-methodology.md), [Evolution methodology](evolution-methodology.md), and [MVC reproducibility model](../03-experiment-design/mvc-reproducibility-model.md).

## Summary

- Candidate equation variables belong in the handbook as research notation.
- The notation is not a contract, benchmark, or production MVC schema.
- Current MVC research has observed and derived variables, but not full reasoning-quality authority.
- Interaction terms are central to the representation-ceiling hypothesis.
