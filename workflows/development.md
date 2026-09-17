# Development workflow

## Independent entry

Start only when the user explicitly requests development after an approved
requirements handoff. Read project-context.md for shared initialization, project
rules, role selection and delegation, then task-delivery.md for execution records.
This workflow consumes requirements-review outputs; it does not automatically rerun
that workflow. READY_FOR_DESIGN is baseline eligibility, not a development-start command.

## Requirements understanding and intake verification

The user supplies the review gate/handoff (or an equivalent versioned project
record), project rules and optional existing designs. Resolve exact references;
do not depend on the previous session's conversation or infer the latest approved
version from filenames.

1. Read the original requirement sources alongside the approved understanding,
   stable business decomposition, recorded answers/corrections, acceptance criteria,
   scope/exclusions, accepted risks and product/architect/QA verdicts. Verify source
   identities and actual user confirmation; summaries alone are insufficient.
2. Product is required at intake: read the original in-scope sources against the
   handoff, confirmed decisions and acceptance criteria; return business understanding,
   coverage and mismatches for the parent to persist. Reuse valid review decisions,
   not a second requirements specification or a full automatic re-review.
   Architect re-reads the full in-scope source and approved interpretation before
   design; planner subsequently cross-checks the same sources against the approved
   design before technical decomposition. Give implementation/review/QA children
   the original sections and decisions relevant to their tasks, not only a task summary.
3. Record a concise intake result in development status: baseline references,
   understood goals/behavior/boundaries, key constraints/dependencies and any mismatches.
   Do not create a competing requirements document or repeat answered questions.
   Reuse approval for the exact baseline, or documented nonsemantic equivalence
   per requirements-review.md; never claim an unread source was verified.
4. Missing source/decision evidence blocks dependent work. Changed behavior, new
   requirements or inconsistencies return affected IDs and concrete questions to
   requirements-review; no silent reinterpretation. Preserve independent authorized
   work and the existing development plan. User-directed clarification runs as a
   separate review lifecycle; after its handoff, resume development only on explicit
   user request and revalidate affected designs/tasks/checks.
5. A valid intake proceeds to design or resumes a verified existing design/contract
   stage. Existing design files alone are not approval. Product's intake assessment
   does not replace baseline confirmation. Consolidate questions under the shared
   document-first review convention; continue independent analysis, not dependent design.

Development task IDs may differ from the review task ID; link the exact upstream
gate and its source manifest. For the same task ID, preserve both workflow records
as separate status sections rather than overwriting the completed review result.

## Stages and artifact ownership

1. Complete the intake verification above against the approved requirements handoff.
2. After READY_FOR_DESIGN, follow design-review.md in this workflow directory for
   interfaces, type responsibilities and protocol design; obtain DESIGN_REVIEWED
   (agent review only, permission to plan documents, not permission to write code).
3. Planner writes the assigned plan, task ownership and dependencies after design
   review. Assemble the document package and obtain explicit human approval per
   design-review.md before DESIGN_APPROVED. Only then materialize and verify
   contracts, followed by READY_FOR_IMPLEMENTATION.
   Planner does not redesign the product or change production code. Include unit-test cases, ownership and
   acceptance commands per workflows/unit-test-acceptance.md under team_root.
   Check plan readiness and source-to-task coverage per task-delivery.md before
   dispatch; resolve missing decisions at their source rather than inside code.
4. Only the selected backend/client developers implement in-scope tasks and tests.
   A backend-only or client-only project proceeds directly to review and QA after
   its selected implementation and unit tests complete; there is no empty second
   branch or test suite for an unselected developer to await.
5. Reviewer independently reviews the actual change scope, including new files.
   Supply a baseline and changed files to distinguish pre-existing user changes.
6. QA independently checks acceptance on the final implementation. It may add
   assigned tests and reports, but returns production fixes to the implementation owner.
7. Orchestrator records results and evidence for human review. Development completion
   does not imply human approval or authorize merge/deployment.
   Verify the combined feature at task-delivery.md's closure step; individual task
   passes do not replace integration and overall requirement coverage.

Product, architect and reviewer are read-only. They return complete content and
the assigned destination. Orchestrator saves those results in the target project
before downstream stages depend on them. It may write documentation/task state,
but normally delegates production code.

Use existing document conventions first. Defaults for new artifacts:

| Artifact | Project-relative path | Writer |
| --- | --- | --- |
| Approved requirements handoff | Exact upstream review gate/handoff path | Read-only input; see requirements-review.md |
| Supplied requirements | `docs/product/source/` (recommended intake location) | Human author; preserve originals |
| Development understanding | Section in `docs/tasks/<task-id>/status.md`, linking upstream requirements | Orchestrator from product output |
| Architecture | `docs/architecture/<task-id>.md` | Orchestrator from architect output |
| Interfaces/protocol design | `docs/tasks/<task-id>/design/contracts.md` | Orchestrator from architect output |
| Development/task and test plan | `docs/tasks/<task-id>/plan.md` | Planner |
| Human document review | `docs/tasks/<task-id>/design/review.md` | Orchestrator consolidates role findings and human replies |
| Code review | `docs/tasks/<task-id>/review.md` | Orchestrator from reviewer output; distinct from human document review |
| QA | `docs/tasks/<task-id>/qa.md` | QA |
| Status/handoff | `docs/tasks/<task-id>/status.md` | Orchestrator |

Do not duplicate existing documents merely to match defaults. Status records
stage, role/model when observable, artifact paths, commands/results, rework count
and blockers. Never report inferred model identity as observed runtime evidence.

## Verification and rework

Apply team_root/workflows/unit-test-acceptance.md as the code acceptance contract.
The developer owns unit tests; reviewer examines their quality and QA checks the
execution evidence against acceptance criteria. This applies equally to client-only,
backend-only and dual-end projects, using each project's own test tools.

- P0/P1 review findings or QA FAIL return to the implementation owner.
- After fixes, repeat affected review and acceptance checks. QA-added tests are
  changes too; have their additions reviewed before final PASS.
- Allow up to three automatic rework cycles total across review and QA per task.
  If failures persist, stop dependent work and report unresolved findings.
- Missing tooling, credentials, services or permissions means BLOCKED for that
  check. Record the command/error and next step. Never count it as PASS or endlessly
  retry infrastructure failures as code fixes.
- Run focused checks plus all project-required delivery checks. Later edits that
  invalidate evidence require rechecking; never complete from stale passes.
- Report remaining P2/P3 findings and risks.

Escalate unresolved product decisions and material architecture/business rule/
infrastructure/compatibility changes when not already authorized. Do not repeatedly
ask permission for decisions the user already authorized.
