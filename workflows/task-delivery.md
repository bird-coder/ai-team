# Task readiness, execution and recovery

This workflow complements requirements-review.md, design-review.md and
unit-test-acceptance.md. It defines handoff and delivery records, not extra roles
or a second orchestrator. The primary orchestrator owns task status. All records
belong to project_root; never load human-only templates/ as instructions.

## Verified context

Record the selected workflow, its phase and exact upstream handoff separately.
Requirements review ends at its confirmed-baseline handoff, not at the code DoD
below. Development intake follows development.md and reads source requirements
alongside that handoff; keep separate status sections or linked task records when
both workflows use the same task ID. Only the orchestrator writes shared status.

Before planning, inspect the actual source, applicable project instructions,
dependency manifests, build/test scripts and CI relevant to the change. Confirm
referenced paths and distinguish declared commands from commands actually run.
Identify stale instructions and conflicts; do not silently rewrite project policy.
Resolve factual mistakes from evidence and surface unresolved policy decisions.

Record only necessary findings and source references in task status (or existing
project context records), including generated files, external dependencies and
test-environment caveats. Do not generate another full repository description.
Recheck affected facts when files/tools change. Workflow/model sources stay shared
in ai-team; the target project contains only local facts, decisions and deliverables.

## Handoff readiness

Planner gives each implementation unit a stable ID, a selected developer owner,
dependencies, scope, actual allowed/protected paths, requirement/contract references,
acceptance criteria and unit-test cases/commands. A unit should produce an observable
piece of behavior where practical; contract setup can be a separate prerequisite.
Developers must not need to infer missing business or interface decisions from chat.

Before dispatch, the orchestrator checks the plan with reviewer (read-only):

- Every in-scope requirement/acceptance criterion maps to at least one task and
  planned verification. No task introduces unapproved behavior.
- Each dependency exists; the graph is acyclic and no task depends on an unselected
  backend/client branch. External prerequisites have owners and evidence.
- Required requirement/design/contract gates match current versions. Document-phase
  plan review uses DESIGN_REVIEWED; it does not dispatch code. A contract setup task
  needs DESIGN_APPROVED including human document-package approval; business tasks
  need READY_FOR_IMPLEMENTATION.
- Shared writes have one owner; parallel units do not claim overlapping files.
- Task inputs include the exact relevant source documents, not copies of the
  entire conversation or independently rewritten requirements.
- Applicable project instructions, skills and business-document references from
  project-context.md's project_rules handoff are available and current. Resolve missing
  required sources and rule conflicts before dispatching dependent work.

Record the outcome in plan.md/status.md. This agent readiness check contributes to
the document-package human review; it does not substitute for that approval.
Missing decisions are consolidated in the phase's human review entry and routed to their source owner and
the appropriate gate. Planning defects return to planner; bound automatic plan
repair/review attempts to three per baseline and surface unresolved issues.
Independent ready tasks may proceed while another task has a local blocker.

## Work-item state

Track each unit in the existing tracker or a compact table in status.md; do not
invent synchronization with external trackers. Only orchestrator updates the shared
status from child evidence so concurrent children cannot overwrite one another.

| State | Required condition |
| --- | --- |
| PLANNED | Scope, owner and dependencies identified |
| READY | Applicable gates and handoff readiness pass; prerequisites satisfied |
| IN_PROGRESS | Assigned owner is performing the unit |
| IN_REVIEW | Owner supplies file list, baseline, tests/results and open risks |
| IN_QA | Independent review has no unresolved P0/P1; phase-applicable checks below pass, including required implementation unit tests |
| DONE | Required QA/checks pass on current deliverables and reports are saved |
| BLOCKED | Specific unmet prerequisite recorded, with previous state and next action |
| NOT_APPLICABLE | Explicitly out of agreed scope, with reason; not a fake pass |

Contract setup uses design-review.md's schema/generation/build evidence rather
than pretending the unfinished feature passes business tests. Docs-only units use
the justified applicability rules in unit-test-acceptance.md. Fixes return to
IN_PROGRESS and invalidate affected downstream evidence; do not reset retry counts
to escape the bounded rework rule. DONE is reopened only when its evidence is
invalidated, not merely because a new session starts.

## Integration and closure

Triage review findings against the actual source and requirement before assigning
fixes. Preserve each finding's disposition and evidence: confirmed fix, pre-existing
out-of-scope issue, refuted with reason, or decision needed. A disputed P0/P1 stays
unresolved until reviewer reassesses the evidence; the implementer cannot dismiss
it unilaterally. Repeated substantive findings should trigger inspection of their
upstream requirement/design cause within the existing rework limit.

Individual DONE items do not prove that the whole feature works. At a feature or
milestone boundary, run project-required combined regression/integration checks
against the assembled final changes. Reviewer checks cross-task contract consistency;
QA verifies overall acceptance and reports mocks/external dependencies honestly.
Do not require a nonexistent opposite-end implementation for a single-end project.

Check child handoffs for the project-rule sources actually used. Reviewer checks
required business/protocol documentation updates and consistency with final changes;
QA checks applicable project test evidence alongside shared unit-test acceptance.
Do not accept discovery or a checked-off skill checklist as execution evidence.

Keep traceability as references in the plan: requirement -> contract -> unit ->
unit/acceptance tests -> result. If an accepted requirement has no result, the
feature is not complete. The final handoff lists artifacts, final versions, verified
commands, deferred work and risks. Merge/deployment still require their own authority.

Record a short retrospective in status.md only for actual repeated failures,
surprising constraints or useful follow-up work. Do not automatically edit ai-team
or impose new project policies from one task's lesson; shared changes need an
explicit maintenance request. No additional human retrospective approval is required.

## Resume and changes

Read status and referenced current gates before resuming. Restore the
recorded workflow first. A completed requirements review waits for explicit
development start; a review-only resume does not create a development plan.
Read a plan only when it exists for development; its absence is normal in review.
Restore the task's recorded project_rules_file and scope (if any) before interpreting project
rules; do not switch games based on the current directory or a newly found file.
Restore the next ready unit and existing retry counts; recheck changed context and evidence. Check
changes to referenced project instructions, skills and business documents as well:
re-read affected sources and revalidate dependent decisions/checks, not all unrelated
work. Resolve
live writers before redispatching a task to avoid duplicate edits. Preserve unrelated
working-tree changes and report old results as stale when final code differs.

Route business changes to the requirement source, cross-component decisions to
architecture/contracts, and local task refinements to the plan. Update downstream
references and affected checks after approval; never patch a task to contradict its
source. For a large scope change, first summarize the affected units, completed work,
external dependencies and options before replanning. Retain stable IDs/history and
unaffected completed work; never silently discard implementation or decisions.
The requirement baseline includes source documents AND recorded user decisions.
Reconcile changed sources/answers per requirements-review.md, retaining stable
requirement IDs. Pause and revalidate affected dependent work, not all unrelated
tasks; item-level clarification never substitutes for the baseline gate.

For small tasks these records can be compact sections in existing files. Document
size may shrink; the active workflow's gates do not disappear. Requirements review
requires baseline confirmation; development additionally requires contract review,
independent code review and meaningful unit-test acceptance.
