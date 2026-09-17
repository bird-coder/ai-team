# Design and contract gate

## Entry and ownership

Enter only in an explicitly started development workflow after its intake has
verified READY_FOR_DESIGN for the current requirements baseline. The
orchestrator coordinates; architect authors design content read-only, selected
developers inspect feasibility read-only, reviewer independently reviews design,
and QA reviews testability without executing business tests. The parent persists
their outputs inside the target project. No extra roles or per-project workflow
copies are needed. A single-end project reviews the external counterpart's contract
without requiring an unselected developer or inventing its implementation.

## Required design

Use existing designs where adequate, identify their versions and document what is
unchanged. Routine fixes may use a brief no-contract-change assessment, reviewed
by reviewer, instead of new architecture. Never skip the contract check entirely.

Describe only applicable items, with reasons for omissions:

- Modules, classes or Go types: responsibilities, owned state, dependencies,
  construction/cleanup and public methods. Do not enumerate every private helper.
- Interfaces: signatures, input/output types, preconditions, errors, side effects,
  ownership and concurrency/cancellation semantics. Prefer existing abstractions.
- State/data: transitions, invariants, persistence, transactions and migration
  compatibility where relevant. Include test seams without speculative frameworks.
- Client/server protocol: canonical schema location and owner, message identifiers,
  direction, fields/types/units/defaults/presence, validation, responses/errors,
  sequence, retries/idempotency, ordering and reconnect behavior where applicable.
- Compatibility: old/new peers, version negotiation or evolution rules, stable field
  numbering when applicable, generator/tool versions and regeneration commands.
- Traceability: requirement ID -> interface/message/type -> planned test behavior.
- Risks: permissions/trust boundaries, resource limits, failure handling, observable
  diagnostics and rollout/rollback implications where the feature changes them.

A protocol must have one canonical source (for example the project's protobuf or
OpenAPI files). Examples/docs must agree with that source; do not maintain competing
handwritten schemas or manually patch generated output.

## Design review and contract materialization

1. Architect proposes the design; selected developers flag implementation problems,
   reviewer checks correctness/compatibility and QA checks observable acceptance.
2. Resolve agent-fixable findings and collect human decisions without interrupting
   independent document work. When technical design checks pass, record DESIGN_REVIEWED
   with requirement
   and design identities, reviewer verdict, QA testability verdict, scope, contract
   owner, protected paths and generation/validation commands.
   Reviewer must have no unresolved P0/P1 findings and QA no unresolved testability
   blockers. Bound automatic design-revision attempts to three per baseline; report
   persistent disagreements instead of looping. Human requirement revision rounds
   remain separate and are not limited by this automatic retry count.
3. Planner writes the development plan against that agent-reviewed baseline, including
   tasks, owners, dependencies, implementation guidance, coverage and unit-test plan.
   Reviewer checks plan readiness per task-delivery.md. Consolidate the complete
   document package for human review as specified below. No code is authorized yet.
4. Only after human package approval and DESIGN_APPROVED, assign one selected
   developer to materialize agreed interface declarations, protocol sources and
   necessary skeletons in owned paths. Separate this task from business logic.
   Generated outputs must follow the project's generation procedure.
5. Reviewer verifies that materialized contracts match the approved design; run
   applicable schema/generation/compilation checks. A skeleton need not pretend to
   pass feature acceptance or contain fake success implementations. Do not add
   reachable panic/TODO behavior to an existing working application as scaffolding.
6. Orchestrator records READY_FOR_IMPLEMENTATION only when materialized contracts
   and checks pass (or existing unchanged contracts are verified with evidence).
   Dependent business implementation can now proceed in parallel with disjoint
   ownership. No developer may silently edit protected contract paths in those tasks.

## Human document-package gate

Human review is required for every development document package, not only projects
opting into it. Follow project-context.md's consolidated review convention. The
package includes product's development understanding, architecture, interface/protocol
design, development/task plan and test/acceptance plan. Existing documents or concise
linked sections may satisfy these outputs; do not create duplicate specifications.
Before technical checks pass, safe independent draft sections may be prepared, but
must be marked provisional and must not invent unresolved interfaces or business rules.

Use design/review.md as the human entry: list exact artifacts/versions, agent review
results, all known questions and reply fields, dependencies, unassessable gaps and
the package-level approval field. NEEDS_REVISION means decisions or revisions remain;
AWAITING_CONFIRMATION means checks pass and the complete package awaits approval.
Save and return this entry even when no questions remain. End the turn for review.
Keep agent design and plan-readiness verdicts separate from human approval.

Record DESIGN_APPROVED in design/gate.md only after DESIGN_REVIEWED, plan-readiness
checks and explicit human approval of the complete current package all pass. Include
requirement, understanding, architecture, contract and plan identities plus actual
approval content/provenance and scope. Earlier requests to develop, requirement
approval, answered questions, or agent PASS alone are not package approval.
Legacy DESIGN_APPROVED records lacking this evidence need the human checkpoint
before any new code work; do not discard existing code or valid verification.
Approval may explicitly request continuing development in the same reply.

Before this gate, writes are limited to documents/state: no production code,
executable tests, canonical protocol/schema edits, generated output, or code skeletons.
Read-only inspection and non-mutating existing checks are allowed. Documented API
proposals are design drafts, not a second canonical schema. Human review does not
replace independent technical checks or approve unresolved blocking issues.

## Contract changes during development

Record a change request before modifying approved signatures, type responsibilities
or wire contracts: reason, affected requirement, callers/peers, compatibility,
migration/regeneration and tests. Architect assesses it, reviewer reviews it and
QA updates test implications. Material changes to the approved design, contracts,
scope or task/test plan require renewed human review of affected package versions;
collect decisions in the review entry rather than repeatedly interrupting chat.

Pause dependent work while the request is unresolved; independent authorized work
can continue. After approval, update the design and canonical sources as one owned
task, regenerate and validate, record the new baseline, update dependent assignments
and rerun affected tests. Requirement changes also reopen the requirements gate.
Do not change the schema merely to make a failing implementation/test pass. Internal
private implementation choices that preserve the contract do not require this loop.

## Records and recovery

Use project conventions, defaulting to `docs/tasks/<task-id>/design/` for
`contracts.md`, `review.md`, `gate.md` and versioned `changes/<change-id>.md`.
Architecture may live in the existing architecture directory; reference it rather
than duplicate it. Protocol/interface source stays in the project's actual source
directories. Gate records include exact source identities, evidence and unresolved
issues. Previous design rounds and decisions must remain traceable.

On resume, compare current requirement/design/contract/code identities with recorded
gates and assignments. Revalidate affected gates/checks when changed; never reuse
stale approval or overwrite unrelated user edits. Do not restart completed valid
phases simply because the session changed. Record final requirement-to-interface-
task-to-test links in the task plan/status for handoff.
