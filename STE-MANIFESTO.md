# STE Manifesto

System of Thought Engineering (STE) treats software architecture as an explicit engineering artifact: a structured body of intent that can be compiled, compared, and tested like other critical system descriptions.

Informal architecture fails in predictable ways. Rationale thins as it moves across people, tools, and time. Diagrams diverge from code. Decisions hide inside pull requests and chat logs. The result is lossy reasoning: the organization cannot reliably say what it decided, why it decided it, or whether the running system still matches those decisions.

STE responds by separating intent from implementation while binding them with traceability. Intent is authored and refined as durable records—not as a one-time narrative. A canonical architecture model (Architecture IR) makes structure machine-addressable. Deterministic checks, where appropriate, turn evidence into assessments that can be repeated, reviewed, and audited. The control loop closes when assessments drive explicit decisions and controlled change rather than silent drift.

This handbook explains that discipline. It does not replace normative contracts: **`ste-spec`** defines what STE systems mean and must do. **`adr-architecture-kit`**, **`ste-kernel`**, and **`ste-runtime`** (and related tooling) implement or consume those contracts. The manifesto states a thesis—governed, inspectable architecture—not a guarantee about any single deployment.

STE is engineering: decisions under constraints, evidence where claims matter, and governance that keeps the model honest as the system evolves.
