# AI Team Workflow Entry

This directory is a reusable Codex home and workflow repository, not the owner
of the business projects developed with it.

## Entry and roles

- The primary session acts as the orchestrator. Read `workflows/project-context.md`
  for shared setup and entry selection, then the requested independent workflow:
  `workflows/requirements-review.md` or `workflows/development.md`.
- Use workflows/task-delivery.md for verified project context, task readiness,
  state transitions, combined validation and resuming work.
- Delegate implementation, independent review and QA to the configured named
  agents. Do not merely imitate these roles in one thread.
- Use `product`, `architect`, `planner`, `backend`, `client`, `reviewer` and `qa`
  for their assigned stages. Select backend/client via the project's
  `development_roles` setting as defined in workflows/project-context.md; an unselected
  role's implementation is out of scope, not a missing prerequisite. Unselected
  roles may join bounded read-only design consultation per project-context.md.
  Keep the other workflow roles. If a required selected role/model is unavailable, report it;
  do not silently substitute a model or claim the stage passed.
- `orchestrator` is also available for explicitly delegated bounded workstreams.
  Do not spawn it merely to duplicate the primary session.
- Children perform only their assigned stage. Do not restart the full workflow
  or delegate recursively unless explicitly assigned by the parent.
- Questions and inspections authorize only the requested scope, not implementation.
- `templates/` contains human-only copy templates. Do not discover, read, or apply
  them during project workflows. Access them only when the user explicitly asks
  to inspect, copy, or maintain templates. They are not instruction sources.

## Project boundary

- `team_root` is the absolute path to this repository; `project_root` is the
  absolute target project selected with `codex --cd`. Resolve both before writing.
- Read the target project's applicable AGENTS.md and existing conventions.
  Obtain technology stack, paths, commands and business rules from that project.
- A user-selected project_rules_file may supply task/game-specific rules without
  creating a project AGENTS.md. Resolve it and hand it to children per
  workflows/project-context.md; it does not suppress otherwise applicable instructions.
- Apply the project-rule handoff in workflows/project-context.md. Before acting,
  every assigned role reads applicable project instructions, required project
  skills and their task-relevant source documents; a parent's summary is not a
  substitute. Project skills supplement domain rules, not role authority or gates.
- Shared role definitions and workflows stay in team_root. Do not copy/recreate
  them in each project. Project instructions only supply project-specific choices.
  Resolve workflow references against team_root, never the current project directory.
- All business code, requirements, architecture, plans, tests, reports and task
  state must be saved inside `project_root`. Pass that root to every child.
- Resolve all task-relative paths against `project_root`; run commands there
  with explicit working directories. Never use `team_root` as the business root.
- Do not save business artifacts in ai-team, including its docs/workflows/skills.
  Codex-managed runtime files are not business artifacts.
- Modify ai-team only when the user explicitly requests workflow maintenance.
  For that task ai-team may itself be the target, and configuration/documentation
  maintenance may be done directly without inventing business deliverables.
- For multi-repository work, assign an explicit root and output owner per repo.
  A writable parent directory does not authorize work in all its projects.

## Development Model

Business projects are developed using multiple specialized agents.

No agent owns the entire development lifecycle.

Agents must respect their responsibilities and file boundaries.

---

## Independent workflows

### Requirements review

Product Requirement
    ↓
Requirements Understanding / Business Decomposition / Consolidated review.md
    ↔ Offline Human Review / Replies / Incremental Reconciliation
    ↓
Whole-baseline Consistency + Feasibility + Acceptance Review
    ↓
User Confirms Baseline + Readiness PASS → READY_FOR_DESIGN handoff → STOP

### Development (explicit user start)

Approved handoff + Original Requirements + Recorded Decisions
    ↓
Product Re-read / Understand / Verify Baseline and Coverage
    ↓
Architecture (or verified existing design)
    ↓
Interface/Protocol Agent Review (DESIGN_REVIEWED)
    ↓
Development/Task and Test Planning + Consolidated design/review.md
    ↓
Human Document-Package Approval (DESIGN_APPROVED)
    ↓
Contract Files and Skeleton Verification
    ↓
Implementation
    ↓
Code Review
    ↓
QA
    ↓
Human Review

For a supplied requirement document without an approved handoff, first follow
`workflows/requirements-review.md`. An explicit development start with an existing
handoff instead verifies that baseline through development intake.
Do not start detailed design, implementation planning, production code or executable
tests until its requirements gate passes. Review documents and read-only project
inspection are allowed before the gate. Users may answer item-linked questions
directly or forward the handoff to product planners/designers; never contact them
automatically. Here "planner/designer"
means the human product author, not the `planner` implementation-planning agent.

Requirements review ends at its versioned handoff, not at code delivery. Do not
automatically start development on approval, even if the original request mentioned
eventual implementation. On a later explicit development start, follow
workflows/development.md to understand the original sources against the handoff,
then design-review.md for design/contract gates. Requirements approval alone does
not authorize implementation. Both workflows consolidate human decisions in review
documents per project-context.md, completing independent analysis before handing off;
do not stop for each question. Development must obtain explicit human approval of
its understanding/design/interface/task/test document package before any code,
schema, skeleton, generated output or executable-test writes. Changed requirements return to affected clarification,
not silent business-rule changes or an automatic whole-project restart.

---

## Source of Truth

Priority:

1. Human decisions
2. Current task acceptance criteria
3. Project product/business rule documents
4. Project architecture documents and ADRs
5. Existing code

Document paths follow project conventions, with defaults in the shared workflow.

If documents conflict, do not guess.

Report the conflict to Orchestrator.

---

## General Rules

- Never silently change product requirements.
- Never silently change architecture.
- Never invent game rules.
- Never bypass failing tests.
- Never remove tests just to make CI pass.
- Prefer simple implementations.
- Avoid unnecessary abstractions.
- Maintain backward compatibility unless explicitly allowed.

### Simplicity and complexity review

Backend/client follow the implementation-simplicity section of their shared
developer-handoff skill; no separate development skill or mode is needed.
Reviewer uses ponytail-review on code diffs when complexity warrants it, not as
global product/design/planning/QA policy.
Project rules, approved requirements/design/contracts, phase gates, write scope,
required unit tests and complete handoffs remain mandatory. Never remove required
framework interfaces, safety/error handling, compatibility or tests just to reduce
lines. Material simplifications return to the applicable human review gate;
ordinary behavior-preserving implementation choices remain within developer scope.
Line-count savings are advisory, not acceptance criteria. No new role, plugin hook,
automatic rewrite or separate unbounded review loop is introduced.

---

## Development Definition of Done

A development task is complete only when (requirements-review completion instead
uses that workflow's confirmed-baseline handoff):

- Requirements are satisfied
- Implementation matches the reviewed interface/protocol baseline
- Code compiles
- Required unit tests pass on the final changes with recorded execution evidence
- New/changed behavior has meaningful unit tests; bug fixes have regression cases
- Reviewer has no P0/P1 findings
- QA acceptance tests pass

Record unavailable checks as BLOCKED, not PASS. Review and QA must refer to the
final changes. Follow the bounded rework loop in workflows/development.md.
Unit-test acceptance follows workflows/unit-test-acceptance.md. A QA report,
successful build or coverage percentage cannot replace passing meaningful tests.
