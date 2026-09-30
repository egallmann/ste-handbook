---
work_id: work-architecture-as-model-condition
edition: handbook
title: "Can Architecture Change What a Model Is Likely to Do?"
status: argument-complete
maturity: L3
diagrams: false
last_reviewed: "2026-09-29"
content_type: conceptual-essay
standalone: true
authority: explanatory
extends:
  - ../00-problem/00-02-the-problem-of-lossy-reasoning.md
  - ../00-problem/00-04-architecture-as-a-first-class-artifact.md
  - ../00-problem/00-08-the-ste-thesis.md
  - ../03-artifacts/03-01-architecture-decision-records.md
  - ../03-artifacts/03-03-invariants.md
  - ../06-governance/06-03-authority-and-decision-rights.md
  - ../08-runtime/08-05-context-assembly-and-mvc.md
  - ../10-ai-interface/10-01-agents.md
---

# Can Architecture Change What a Model Is Likely to Do?

*Normative Propositions, machine reasoning, and why I stopped asking prompts to carry the architecture*

People who know me well would probably describe me as highly risk-averse. That posture shows up in how I approach architecture. I think in failure modes. I notice authority leakage, identity drift, second sources of truth, and apparently harmless shortcuts that become hard to explain later.

Despite that, I increasingly say something that sounds like a contradiction: I do not actually care very much what implementation the model comes up with, so long as it lands inside the shape of outcomes the architecture says are acceptable.

How can someone who is risk-averse, skeptical of treating AI output as authority, and habitually focused on failure modes be willing to give up control over something as consequential as “the answer”?

Because “the answer” is often the wrong thing for architecture to control.

Many engineering problems have multiple valid implementations. Some will be familiar. Some will not. Some may be better than what I would have prescribed in advance. Working with coding models has reinforced that point. The model sometimes surfaces approaches I likely would not have found if the architecture had prescribed the implementation too tightly. That does not mean I grant model output authority merely because it is plausible. It means I am more careful about where architectural control belongs.

I do not need control over the answer. I need control over what counts as an acceptable answer.

Bounded freedom is not unconstrained freedom. A capable coding model can still produce an implementation that is clean, tested, internally coherent, and architecturally wrong. The obvious remedy is to tell it more. In my case, that remedy worked well enough to expose a different problem: I had started using the prompt as a temporary architecture repository.

Consider a fairly ordinary request:

> Add support for updating an existing architectural entity.

There is enough there for a capable model to begin. Give it the ADR-Kit repository and it can inspect the authoring surface, follow existing types and conventions, trace tests, identify likely extension points, and produce a reasonable implementation plan.

There are also several reasonable ways for it to get the architecture wrong. An update might modify persisted state directly. It might construct a replacement entity. It might preserve the UUID of the thing being updated, or decide that a materially changed object deserves a new one. It might use an alias as an identity shortcut because aliases are readily available in the source. If identity information looks incomplete, it might repair it. Once construction succeeds, it might persist the result because persisting successful work is a perfectly ordinary thing for an API to do.

None of those choices requires a bad model, and several are ordinary software-design choices. The problem is not that the model chose an implementation I personally would not have preferred. The problem is that some of those choices fall outside the architectural acceptability envelope ADR-Kit has actually accepted.

So I can make the prompt better:

> Add support for updating an existing architectural entity. Preserve its established UUID identity. Do not derive canonical identity from an alias, path, prose, hash, ordering, or source location. Construction must produce a detached candidate; it must not persist the result, reserve an alias, perform governance promotion, or imply repository admission. Return the constructed candidate through the authoring boundary and leave those later authorities to their owners.

That is a much stronger instruction, and it reveals what has happened. The model did not become better at programming. I moved more of the architecture into the condition from which it would reason.

What began bothering me was what happened as the prompt became responsible for more than the work. Give the model a role. Add the constraints. Explain which decisions are authoritative. Tell it which identifiers may change and which may not. Add the responsibility boundaries. Include the test expectations. Preserve the wording that worked last time because nobody is quite certain which sentence was load-bearing. Eventually the prompt stops looking like a request about engineering and starts looking like a temporary engineering specification assembled for one inference event.

I would much rather talk to the model about the work.

There is some irony here because ADR-Kit had already confronted a version of the same problem.

In March 2026, `ADR-L-0005` accepted an **ADR-to-Prompt Translation** architecture. Its diagnosis was reasonable: manually translating architecture into prompts was inconsistent, incomplete, time-consuming, error-prone, and difficult to scale. The proposed answer was a deterministic translator that would parse machine-readable ADRs and generate implementation prompts containing the relevant invariants, component specifications, testing requirements, and validation criteria. The ADR described the translator as a kind of code generator for AI instructions.

I still agree with the problem it identified.

What changed was my understanding of where the difficult part actually was. `ADR-L-0005` answered the problem by automating the translation of architecture into prompts. Later ADR-Kit work made the underlying semantic problem more visible: before generating a better prompt, the system first needed a more precise representation of the architectural meaning being translated.

ADR-Kit itself also demonstrated the deeper shaping pattern before it had a first-class object for it. I did not sit down and decide that ADR-Kit needed a Rust semantic core. The March foundation was structured around machine-readable ADRs, Python and Pydantic models, parsers, validators, and machine-oriented generation concepts. When the semantic-core boundary later became explicit, the architecture did not initially say “write the semantic core in Rust.” The early semantic-core contract allowed the implementation to be native, portable, or interpreted. What it constrained were the semantic properties that mattered: one semantic implementation authority; host parity so Python and Node consumed the same semantic artifact; no host-specific recreation of the domain rules; a portable semantic boundary; and domain meaning remaining owned by ADRs and canonical schemas rather than by host-language interpretation.

Rust was not the architecture's starting answer. The architecture constrained the shape of a correct answer before it selected the technology.

I did not pick Rust first and then bend the architecture around it. The architecture kept closing outcomes I was unwilling to accept—semantic divergence, duplicated authority, incompatible cross-host behavior. As those constraints accumulated, implementation options became more or less fit for the remaining shape. Rust/WASM eventually fit that shape well enough that it became the implementation we selected, and later architecture promoted that embodiment into the governed design. Leaving the language open was not a failure to govern; it was refusing to spend architectural authority on a choice that had not yet become material.

ADR-Kit had demonstrated the pattern before I had a clean semantic primitive for it. The architecture could already shape an implementation by accumulating boundaries through decisions, invariants, contracts, and responsibility lines. Those local boundaries were still distributed. The missing thing was not the architectural behavior. The missing thing was a first-class ADR-local semantic object capable of saying what a decision requires here. Normative Propositions were not the invention of that shaping behavior. They gave that shaping force an address.

Over the following months ADR-Kit became much more demanding about architectural meaning. Entities acquired stable UUIDv7 identity. Relationships became explicit semantic objects. Authority, provenance, contract qualification, historical interpretation, normalized representation, consumer extension, and materialization all became things the system had to represent rather than ideas a downstream consumer could be expected to recover casually from prose.

The more explicit that representation became, the more a nearby gap stood out. An ADR could tell me what we had decided. An invariant could tell me something that must remain true more broadly. An implementation could show me one particular embodiment. What I kept needing in between was a durable answer to a narrower question:

**What does this decision require here?**

That answer is not necessarily a system-wide invariant. It may apply only within the semantic boundary established by one ADR. It is also not arbitrary implementation advice. If violating it would make otherwise good code architecturally wrong regardless of which engineer, language, model, or implementation technique produced the code, the meaning is more durable than the task that happened to expose it.

Once I started looking for that shape, I found it everywhere in ADR-Kit. `ADR-L-0029`, for example, governs semantic authoring construction and candidate authority. It makes construction distinct from persistence and promotion. Successful construction produces detached candidate state. A valid caller-supplied UUIDv7 is preserved; an update preserves UUID identity; identity is not derived from aliases, prose, paths, hashes, ordering, source location, or composition position. Compact input may remove ceremony, but it cannot authorize ADR-Kit to invent semantically material intent. Those statements shape implementation directly without describing the implementation.

At the time that ADR was accepted, the authoring representation still lacked a native first-class place for that ADR-local normative consequence. `ADR-L-0028` had already locked the semantic model: Normative Proposition and Invariant were peer types; normative force was separate from authority, effectivity, scope, applicability, and conformance; and an NP's authority and lifecycle remained with its declaring ADR. But the repository was still on authoring v1.5, so the ADR deliberately represented that design using the decisions and invariants the supported schema could actually validate.

The semantic model came first.

The representation followed.

Authoring v1.6 then gave it a first-class home: the **Normative Proposition**.

The name is less interesting than the problem that forced it.

If the architecture already knows what an implementation must preserve, perhaps the prompt should not have to reconstruct or restate that meaning every time a model works on the system. And if that meaning can be represented explicitly and introduced into the model's working context when it applies, a harder question follows.

**Can the architecture itself change what the model is likely to do?**

---

## The Model Still Only Gets Tokens

If architecture only defines the acceptable shape, how can that shape influence what a probabilistic model produces?

Before giving Normative Propositions too much credit, there is an obvious problem with the premise.

The language model never sees the architecture in the way I do. When I read `ADR-L-0029`, I can distinguish a decision from its rationale. I know that the ADR is an accepted architecture artifact rather than an implementation comment. I can recognize the relationship between identity establishment and admission, or between construction and persistence, without assuming those concerns belong to the same authority.

The model does not receive any of that through a privileged architectural channel.

At an ordinary LLM inference boundary, the material available to the model is serialized into context. The task, system instructions, source code, tool results, retrieved documents, examples, and whatever architectural material we include become text that is encoded into tokens. Those tokens are processed through transformer layers whose learned parameters and attention mechanisms produce context-dependent representations. From that state the model produces conditional distributions over subsequent tokens and generates a result. Changing the supplied context can therefore change the distribution over what the model produces. This essay does not measure how large that effect is for Normative Propositions.

Reasoning models can do substantially more useful work inside that process than the old description of an LLM as sophisticated autocomplete suggests. They can decompose problems, compare candidate approaches, inspect evidence, invoke tools, revise plans, test assumptions, and recover relationships that were never stated verbatim. None of that creates a known symbolic architecture channel. They still reason from the condition they were given.

There is no `ARCHITECTURAL AUTHORITY` input beside the token stream. `MUST` does not flip a compliance bit. A UUID does not force the model to respect identity continuity. Tokenization does not understand NP structure, and supplying a proposition does not guarantee that the model will use it.

So if a Normative Proposition eventually becomes context like everything else, what have we gained?

For a while I would have answered: a better prompt.

I no longer think that explanation is precise enough.

Return to the authoring update. Suppose a model finds this idea somewhere in an ADR:

> Update preserves the UUID.

That looks straightforward, but the sentence alone leaves several things for the consumer to reconstruct. Is it descriptive or normative? Is preservation mandatory, recommended, or merely the behavior of the current implementation? Which architectural decision owns the statement? Does it apply to create as well as update? Does it mean aliases are immutable too? Why does the architecture care about preserving the UUID? If another statement appears to conflict with it, which one governs?

A good model can reason through those questions. So can a good engineer. The more useful question is why either of them should be required to rediscover answers the architecture has already decided.

I think of that work as **semantic reconstruction**: inference spent recovering architectural authority, meaning, scope, responsibility, and constraint from artifacts that only imply them. Semantic reconstruction cannot disappear. Engineering always requires interpretation. No useful architecture should attempt to precompute every conclusion an engineer or model might need. But some of the reconstruction we routinely ask models to perform is unnecessary.

If the architecture already knows that update must preserve canonical identity, then deciding whether that sentence is normative should not be a fresh inference problem. If the architecture already knows that construction is not persistence, a coding model should not have to infer the responsibility boundary from the current repository layout. If the accepted reason for the rule is that canonical identity must remain independent of presentation and source-location properties, that rationale need not be reverse-engineered from the code that happened to embody it last time.

ADR-Kit is not changing how the transformer works. It is changing how much architectural classification and meaning remains unresolved when inference begins. The model may still reason over, interpret, or misinterpret the supplied semantics.

The model still gets tokens.

What changed is how much architectural classification and meaning it has to infer from scratch.

---

## What the ADR Needed to Carry

ADR-Kit already had invariants. Why was another semantic type necessary?

`ADR-L-0029` makes the boundary fairly visible. One of its accepted invariants says, in part, that update **MUST preserve UUID identity**. Another says construction **MUST NOT** be treated as persistence, repository admission, governance promotion, alias reservation, or implementation-conformance authority. Another prohibits compact authoring input from inventing semantically material architectural intent. Those statements are useful because they express truths the architecture refuses to let an implementation erase.

But the invariant model and the decision model answer different questions. An invariant asks what must remain true across the governed architecture. An ADR records an architectural choice and its authority. There is still a useful local question between those structures and the eventual code: given this decision, what does it require, prohibit, recommend, discourage, or permit **within its own scope**?

That was the shape I needed the semantic model to preserve. One useful way to locate the responsibilities, and not a universal parent-child chain, looks like this:

```text
Invariant
    broad truth that must remain true

        ↓

ADR
    accepted architectural decision / declaring authority

        ↓

Normative Proposition
    ADR-scoped local normative consequence

        ↓

Implementation
    one valid embodiment
```

This is not a mandatory hierarchy. An invariant and an NP are peer semantic types; NP authority remains with the ADR that declares it. `ADR-L-0028` makes that boundary explicit.

Authoring v1.6 gives the proposition first-class fields for stable identity, alias identity, statement, closed normative force (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`), scope, and optional rationale, with authority remaining on the containing ADR. Logical, physical-system, and physical-component models all expose the collection.

There is a historical wrinkle I do not want to smooth over. `ADR-L-0029` was authored under schema v1.5. It therefore could not carry a first-class `normative_propositions` collection, and I do not want to reconstruct history for convenience. The concrete identity obligation already existed in the forms that schema could validate. One accepted representation is `INV-0114`, an invariant—not a hidden or retroactive NP:

```yaml
invariants:
  - alias_id: INV-0114
    alias_name: canonical-identity-is-explicit-and-stable
    statement: >
      Valid supplied UUIDv7 identity MUST be preserved, update MUST preserve
      UUID identity, and ADR-Kit MUST NOT silently replace supplied identity
      or derive canonical identity from presentation or source-location
      properties; create MAY mint UUIDv7 without implying admission.
    rationale: >
      Canonical identity is independent of aliases, prose, paths, hashes,
      ordering, and composition position.
```

That is the historical representation I actually had. `INV-0114` is an invariant, not a first-class NP, and I do not want to rewrite it into one after the fact. `ADR-L-0029` was nevertheless already pointing toward the later form. `DEC-0194` (`preserve-normative-proposition-construction-boundaries`) explicitly preserved Normative Proposition as a peer semantic type to Invariant for future construction. It required explicit proposition content and exactly one normative force, and it prohibited tooling from inferring propositions, materiality, applicability, competence, or effectivity from prose. The ADR carried the obligation in the forms v1.5 could validate while also preserving the future Normative Proposition boundary. The meaning came first. Authoring v1.6 gave that meaning a first-class place to live.

Once that representation exists, another problem appears: not every architectural statement deserves to become an NP. A statement should become a Normative Proposition only when it carries durable ADR-local meaning whose violation would materially change what the declaring ADR considers acceptable. A useful test is subtraction. Remove the candidate proposition. If the acceptable implementation envelope does not materially change, the statement probably does not belong as an NP. If removing it leaves open an outcome the ADR intends to reject, the proposition may be carrying material normative intent. That judgment is semantic, not schema validation. Without it, every preference becomes an NP and the mechanism degenerates into architectural verbosity.

The question is not whether a proposition mentions a technology. The question is whether violating it changes architectural acceptability. Because the shaping effect is compositional, authoring discipline favors one dominant normative proposition per NP. Permissions or exceptions may qualify that meaning, but a single NP should not become a miniature specification packing several unrelated obligations.

---

## A `MUST` Is Not Authority

Making normative meaning explicit immediately exposed several category errors that prose had allowed me to blur.

Start with `MUST`. It is tempting to treat normative force as the important part of a Normative Proposition. A proposition saying that update `MUST` preserve UUID identity sounds much stronger than one saying it `SHOULD`. But force is only one dimension.

A `MUST` written in an obsolete ADR is not made current by typography. A `MUST` from an ADR that does not govern the work is not applicable merely because the proposition was retrieved. A proposition included in a normalized model is not thereby effective. An applicable proposition does not prove that the resulting implementation conforms to it.

ADR-Kit's normative design therefore keeps several questions separate:

```text
represented?
    ↓
authoritative and effective?
    ↓
in scope?
    ↓
applicable here?
    ↓
conformant?
```

`ADR-L-0028` explicitly separates normative force, authority, effectivity, scope, applicability, and conformance, and explicitly rejects the idea that successful representation or materialization can manufacture the later forms of authority. That separation matters more than the force vocabulary.

If an NP says that update `MUST` preserve UUID identity, `MUST` describes the deontic strength of the proposition **if the proposition governs**. The declaring ADR supplies authority. The ADR's state and governing rules determine effectivity. The proposition's scope bounds where it can matter. Applicability asks whether it governs the task actually in front of us. Conformance asks whether the resulting implementation satisfies it. Those are not synonyms.

A schema could have flattened them into something simpler. That would have made the representation easier to explain and much easier to misuse. The machine representation forced those separations into the open.

---

## Shaping the Reasoning Space

Now return to the original task:

> Add support for updating an existing architectural entity.

Without any further architectural context, several implementation branches remain plausible:

```text
update entity
    ├── mutate persisted source directly
    ├── construct a replacement entity
    ├── preserve the existing UUID
    ├── mint a replacement UUID
    ├── derive identity from an alias
    ├── repair missing identity
    ├── return a detached candidate
    └── persist automatically after success
```

A capable model can reject some branches by reading the repository carefully. Existing types, tests, naming conventions, and nearby implementations all supply useful evidence. But those are indirect signals. The accepted architecture is more precise.

`ADR-L-0029` says successful construction produces detached candidate state. Construction does not absorb persistence or governance promotion. Update preserves UUID identity. Create may establish UUIDv7 identity when appropriate without implying admission. Identity is not derived from aliases, prose, paths, hashes, ordering, source location, or composition position.

No single proposition describes the implementation I want. That would miss the point. The shaping effect comes from multiple applicable propositions acting together. One closes replacement identity. One closes deriving identity from aliases or source-location properties. One closes persistence or admission as a side effect of construction. One closes invention of missing material intent. Those are different architectural dimensions.

Expressed in the later NP form, the relevant accepted semantics would look approximately like this:

```yaml
normative_propositions:
  - statement: "Update MUST preserve UUID identity."
    normative_force: MUST
    scope: authoring-update

  - statement: "Canonical identity MUST NOT be derived from aliases or source-location properties."
    normative_force: MUST NOT
    scope: canonical-identity

  - statement: "Construction MUST NOT imply persistence, admission, or governance promotion."
    normative_force: MUST NOT
    scope: authoring-construction

  - statement: "Compact input MUST NOT authorize ADR-Kit to invent semantically material intent."
    normative_force: MUST NOT
    scope: compact-authoring-input
```

That set is an illustrative later projection of accepted `ADR-L-0029` semantics into the v1.6 NP form—not a claim that the historical ADR already contained these first-class objects.

The NP is individually addressable; the shaping effect is compositional. Each proposition closes a class of outcomes the architecture has already decided is unacceptable. The applicable set establishes the combined architectural conditions the implementation must account for. Their intersection defines the acceptable envelope:

```text
preserve canonical identity
          ∩
do not derive identity from aliases
          ∩
construction remains detached
          ∩
do not invent missing material intent
          ↓
architecturally acceptable envelope
          ↓
implementation remains open
```

This is not entirely hypothetical for ADR-Kit. The semantic core evolved through the same pattern before NPs were first-class. Retrospectively, the shaping forces already present in the architecture looked less like a prescription and more like an envelope:

```text
prescriptive architecture

"Implement the semantic core in Rust/WASM."
                ↓
         one prescribed answer


shaping architecture

one semantic authority
        ∩
cross-host parity
        ∩
shared implementation artifact
        ∩
portable execution boundary
        ∩
deterministic cross-host behavior
        ↓
  acceptable solution region
        ↓
  Rust/WASM is one fitting answer
```

That diagram is a retrospective illustration of forces already present in decisions, contracts, and responsibility boundaries—not a claim that these exact propositions historically existed as first-class NPs. The architecture did not initially specify `semantic core = Rust/WASM`. It constrained the properties any acceptable semantic core had to satisfy. Rust/WASM later occupied that acceptable region well enough to be selected. Once that embodiment was promoted, later architecture could legitimately make the technology itself normative. An open dimension may later become governed when evidence and system pressure make the choice architecturally material.

I did not pick the answer and then encode it as architecture. I constrained the outcomes I was unwilling to accept, let implementation pressure expose a fitting answer, and only then promoted that answer when it became worth governing.

Return to the update task and the same pattern holds: several previously plausible outcomes are no longer inside the acceptable region. Together, the applicable propositions describe the shape an acceptable implementation must fit inside. The architecture leaves class structure, decomposition, data structures, internal APIs, and algorithms open unless another governing decision closes them.

At this point, I do not care very much which implementation the model chooses. I care that the result stays inside the architectural shape we have already accepted. The model remains free to search within that region, including approaches I did not anticipate. I am not relinquishing control over semantic outcomes. I am deliberately relinquishing control over choices the architecture does not care about.

That is the sense in which I mean **shaping**. Shaping means changing the architectural condition and narrowing the set of architecturally acceptable candidate implementations. The propositions do not tell us which path the model takes internally. They establish what any acceptable result has to account for. By introducing those boundaries into the inference condition, we expect them to influence which candidate implementations the model is likely to produce. That expectation remains probabilistic. It does not claim that ADR-Kit can inspect, enumerate, or deterministically bound a model's internal reasoning process.

Nothing about this guarantees that the model will obey the architecture. It can misunderstand the supplied context, fail to use it, or violate a proposition despite having seen it. What changed is the conditional problem presented to the model. One condition says “update an entity.” The other supplies identity continuity, construction authority, and persistence boundaries as explicit meaning. That is a smaller architecturally acceptable solution space without being a scripted implementation.

---

## The Prompt Can Become an Address

This brought me back to the original problem from a different direction. The detailed prompt was not wrong:

> Preserve UUID identity. Do not infer identity from aliases. Return a detached candidate. Do not persist. Do not reserve aliases. Do not treat successful construction as admission.

But if those instructions are already durable architectural meaning, repeatedly hand-authoring them into prompts is an odd system boundary. `ADR-L-0005` had already tried to automate that restatement. I still see that answer as directionally right. The harder problem is determining which architectural meaning is authoritative and applicable before any prose is produced for the model.

That changes the job of the prompt. Instead of this:

```text
Implement update construction.

Preserve established UUID identity.
Never derive canonical identity from alias or path.
Construction must return a detached candidate.
Do not persist the result.
Do not reserve an alias.
Do not perform governance promotion.
...
```

I want to be able to work much closer to this:

```text
Implement update construction governed by ADR-L-0029.

Use the applicable normative architecture for the operation.
Preserve the existing public contract.
Review the result against the same governing propositions.
```

That shorter form is a direction of travel, not a claim that ADR-Kit already completes the end-to-end resolution. Something else has to resolve the ADR identifier to architectural authority, distinguish effective architecture from merely historical architecture, identify candidate propositions, determine which apply, preserve enough authority and rationale to interpret them, and serialize the resulting context for the model.

The prompt became shorter because the system became more responsible.

That is a systems problem, not a wording trick.

I do not want every engineer, IDE integration, agent framework, or model adapter to become independently excellent at reconstructing the architecture. I want the architecture to become better at producing the context those consumers need.

---

## Applicability Is the Hard Part

Once propositions become addressable, another apparently simple solution presents itself: retrieve all of them. That would recreate the problem at a different layer.

An NP existing does not mean it governs the current task. Being stored beneath a relevant ADR does not automatically make it applicable. Being reachable through a semantic graph does not make it applicable. Being present in a normalized or materialized representation does not make it applicable either. `ADR-L-0028` is explicit about this: normalized inclusion must not be treated as applicability, and representation, interpretation, or materialization does not manufacture applicability authority.

That leaves a harder operational question. Suppose I ask the model to modify update construction. The identity proposition is an obvious candidate. The detached-construction boundary is probably another. A proposition governing creation-only identity minting may matter because the implementation shares code with create. A proposition governing unrelated documentation projection almost certainly does not.

Where exactly is that boundary?

Too little context and the model is again forced to reconstruct an architectural obligation that should have been supplied. Too much context and we create a different failure: irrelevant normative material competes for attention, apparently contradictory statements arrive without enough locality to reconcile them, and the task context becomes a dump of everything the architecture knows rather than a projection of what the task requires. An enormous context window does not make indiscriminate context good architecture.

The direction I currently find most credible is to resolve the **minimal applicable closure**: the smallest authority-correct set of propositions and broader invariants that together establish the architectural acceptability envelope for the task.

I do not consider that problem closed. Scope is authored. Applicability is contextual. A robust resolver may need architectural relationships, task intent, authority and effectivity, source state, and potentially evidence that only exists when the work begins. Some of that may belong naturally in ADR-Kit; some may belong to whatever later system owns task-relative context resolution. That boundary should remain unresolved until the authority is clear.

The existence of NPs does not solve context assembly. It makes the missing context-assembly problem much easier to state precisely.

---

## The Same Architecture Can Come Back for Review

There is another consequence of keeping the normative meaning outside the prompt: it survives the generation event.

Suppose an implementing model receives the update task and the applicable architectural propositions. It produces a candidate change that preserves UUID identity, returns a detached construction result, and avoids persistence. The fact that those propositions were supplied during generation does not establish conformance. The model may have misunderstood one, satisfied the wording while violating the rationale, received an incomplete applicable set, or simply introduced a defect.

I do not want the implementing model's confidence to close that question. The durable object is still the architecture. A later review can re-resolve the governing architectural authority—not merely reuse the exact generation context packet—and ask a different model, or a deterministic mechanism where one exists, to examine the actual result against those propositions.

```text
ADR + applicable NPs + goal
            ↓
     implementation inference
            ↓
         candidate


ADR + applicable NPs + goal + candidate
            ↓
        fresh review
            ↓
 proposition-relative evidence
```

The reviewer does not need the generator's hidden reasoning. It needs the artifact and the same architectural authority. A second model does not automatically create independence; generation and review can still share a model-family blind spot.

Each proposition should remain individually reviewable, but the implementation may also need to satisfy them in combination. Preserving UUID identity while accidentally persisting the candidate still does not land inside the acceptable envelope. Review can ask whether the candidate preserved the existing UUID, whether any path silently derived canonical identity from an alias or source location, and whether construction remained detached from persistence and admission.

Some of those questions can and should become deterministic. If a schema, test, or static check can prove the requirement exactly, probabilistic review is unnecessary. Normative semantic review is useful where the architecture cares about something that has not been completely encoded in executable checks, or where encoding every meaningful architectural judgment deterministically would be disproportionate.

The model can help evaluate the evidence. It does not become the architecture authority by doing so.

---

## What I Have Actually Observed

There is a temptation at this point to claim that first-class NPs make models more architecturally conformant. I do not have the experiment that establishes that. I have not compared a statistically useful set of implementation tasks supplied with first-class NPs against the same tasks supplied with equally clear unstructured prose. I do not know the effect size. I do not know whether the closed `MUST`/`SHOULD` vocabulary itself produces any measurable benefit independent of the clarity, locality, and structure around it. Those are empirical questions.

What I have observed so far is architectural and workflow-level. The repository history gives me direct evidence for the architectural evolution and the shaping model—including semantic-core constraints preceding the later Rust/WASM promotion—but not for model-behavior uplift.

That still changed practice before measuring anything about model output. It changed the authoring question: whether a statement is a durable local architectural obligation, a broader invariant, rationale, or transient implementation guidance. It changed review: a reviewer can ask which proposition governs a particular choice and seek evidence against that proposition. It changed how I see prompt construction: a large architecture-heavy prompt may be evidence that upstream semantic representation or context resolution is doing too little. And it exposed more gaps. First-class propositions are only useful if their relationships survive normalization. Retrieval is not applicability. Applicability is not conformance. A proposition can be represented perfectly and still never reach the model that needed it. Generation and review can share the same architecture and still share the same model-family blind spot.

The mechanism is implemented. The architectural effect is observable. The model-behavior effect size is not yet measured.

I regard those remaining gaps as useful failures of simplification. The new semantic primitive did not make the problem disappear. It made the remaining problem easier to see.

---

## Can Architecture Change What a Model Is Likely to Do?

I think it can. That answer is narrower than it first sounds. Architecture cannot reach into a language model and directly control its hidden reasoning. ADR-Kit does not alter model weights. A Normative Proposition does not become enforcement because its force says `MUST`. The model can receive perfectly represented architecture and still produce the wrong result.

What the architecture can change is the condition from which that inference begins. We already rely on that fact whenever we use system instructions, examples, retrieval, source code, tool results, or carefully written prompts. All of them change the information available to the model and therefore can change the distribution over what it produces. Normative Propositions move one class of that information upstream.

Instead of asking each prompt to reconstruct what the architecture requires, the ADR can carry the requirement as governed semantic state. Instead of asking the model to determine from surrounding prose whether a statement is normative and how strongly it binds, those dimensions can be represented before inference. Instead of allowing implementation precedent to masquerade as authority, the proposition remains attached to the decision that actually owns it. A later system can then decide which of those propositions apply to a task and project the relevant subset into the model's context.

```text
architectural decision
        ↓
ADR-scoped normative propositions
        ↓
authority + effectivity
        ↓
task-relative applicability
        ↓
bounded architectural context
        ↓
LLM inference
        ↓
candidate implementation
        ↓
independent review against the same architecture
```

The durable part of that loop is not inside the model. It is the architecture. The model may change, the prompt may change, and the implementation strategy may change; a new model may find an approach I never considered. The proposition continues to say what the decision means locally until the architecture changes it.

That is the boundary I wanted. My risk posture did not become looser. I became more precise about where the risk actually was. Instead of controlling every implementation choice, the architecture controls the boundaries that materially affect identity, authority, semantics, and acceptability. Applicable propositions collectively close the outcomes the ADR has already rejected while leaving the remaining implementation space open to engineering reasoning.

ADR-Kit itself taught me that architecture need not begin with the final answer. The semantic core did not begin as “Rust.” It began as a set of properties the architecture refused to compromise. Rust/WASM came later. I do not need the architecture to know the final implementation in advance. I need it to know what the final implementation is not allowed to violate.

Six months ago, ADR-Kit described a deterministic translator that would turn architecture into better prompts. I still think that was directionally correct.

The deeper change was realizing that the prompt was not the thing I most needed to improve.

I was trying to stop making the prompt remember what the architecture should have remembered itself.

## Relationship to the handbook

This essay is a **conceptual essay** in [Part 13: Architectural Essays and Deep Dives](13-00-essays-and-deep-dives-overview.md). It is explanatory. It does not define STE contracts, and it is not research evidence.

It argues that Normative Propositions give ADR-local architectural meaning a durable shape so models and reviewers can reason from governed requirements rather than reconstructing them from prompts. ADR-Kit is the running case, including its earlier demonstration that architecture can constrain semantic properties before selecting a technology embodiment. The essay does not establish Normative Propositions as handbook doctrine, and it does not claim measured conformance uplift.

Detailed doctrine for the obligation it motivates lives in the core handbook:

- Lossy reconstruction and intent: [The problem of lossy reasoning](../00-problem/00-02-the-problem-of-lossy-reasoning.md), [Architecture as a first-class artifact](../00-problem/00-04-architecture-as-a-first-class-artifact.md), [The STE thesis](../00-problem/00-08-the-ste-thesis.md)
- Decisions and durable intent: [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md)
- Broad architectural truths: [Invariants](../03-artifacts/03-03-invariants.md)
- Authority ceilings: [Authority and decision rights](../06-governance/06-03-authority-and-decision-rights.md)
- Task-scoped context: [Context assembly and MVC](../08-runtime/08-05-context-assembly-and-mvc.md)
- Machine participants: [Agents](../10-ai-interface/10-01-agents.md)

Normative semantics for Normative Propositions remain in **ste-spec** and the ADR corpora that embody them, including ADR-Kit. Research claims and methods remain in [Part 14](../14-research/14-00-research-overview.md).

**Previous:** [Privacy Has a Composition Problem](13-04-privacy-has-a-composition-problem.md)
**Up:** [Architectural Essays and Deep Dives overview](13-00-essays-and-deep-dives-overview.md)
