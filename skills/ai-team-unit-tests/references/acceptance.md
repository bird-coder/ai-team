# Unit tests as a code acceptance gate

## Scope and responsibility

Passing meaningful unit tests is mandatory for accepting behavior-changing code.
It is not a substitute for independent review or required integration/acceptance
checks. Apply this rule only within the authorized development phase; requirements
review may propose cases but must not write executable tests before its gate passes.
Business implementation/tests require READY_FOR_IMPLEMENTATION from design-review.md.
Contract materialization may run its specifically approved schema/generation/build
checks earlier; this is not feature acceptance.

- Architect identifies testable boundaries, controllable dependencies and state
  ownership. Do not introduce abstractions solely to satisfy a mock library.
- Planner maps changed requirements/behaviors to unit cases, developer ownership,
  actual test locations, and commands with working directories.
- The selected backend/client developer implements and runs unit tests alongside
  production changes. Do not postpone this responsibility to QA.
- Reviewer checks assertions, edge cases and whether tests could detect incorrect
  behavior. Required missing tests or vacuous assertions fail code acceptance.
- QA verifies acceptance coverage and execution evidence. It may add independent
  tests, but cannot approve behavior-changing code with missing/failing unit tests.
- Orchestrator records the gate result and returns failures to the implementation
  owner using the development workflow's bounded rework loop.

## What tests must demonstrate

Use existing project tools and conventions. Cover normal behavior, relevant
boundaries, invalid input and error paths, plus state transitions, idempotency,
timeouts/cancellation or concurrency when affected by the change. Assertions must
derive from approved requirements/interface contracts, not copy implementation
logic as the expected result. Assert observable results, state or meaningful effects;
"does not crash" and mocks merely agreeing with one another are not sufficient.

For bug fixes, add a focused regression case. Demonstrate that it detects the old
failure when safely practical; record evidence or why that could not be demonstrated.
Never revert the user's working tree to run a negative check.

Keep unit tests deterministic and isolated: control clock/randomness as needed,
avoid real networks/databases and timing sleeps, and mock only external boundaries.
For client projects, test state, transformations, message handling and controllers
using the appropriate unit runner; Go commands are not a universal requirement.
Integration/UI tests supplement unit tests where unit tests cannot establish behavior.

An unselected backend/client branch is NOT_APPLICABLE and has no required test suite.
An external counterpart can be represented by a documented contract/test double;
that does not prove real integration. A selected implementation must not claim
NOT_APPLICABLE merely because no test infrastructure exists yet: establish a minimal
project-appropriate runner, or report the actual blocking prerequisite.

## Acceptance evidence

Save evidence in the target project's existing test report location or
`docs/tasks/<task-id>/unit-tests.md`:

- Changed requirement/behavior IDs and corresponding test files/cases.
- Exact commands, working directories, runner/version where relevant, and scope.
- Actual results, including executed test counts when available, failures/skips,
  and coverage if supported by the project.
- The tested code identity (commit plus relevant working-file hashes or equivalent
  exact snapshot), and any later changes that require rerunning affected checks.

Run focused unit tests during implementation and the project's required unit suite
before handoff. Honor existing coverage thresholds. Do not invent a universal
percentage; coverage alone does not prove useful assertions. Zero discovered tests,
skipped required cases or a green build do not establish a unit-test PASS.

Gate results:

- PASS: all required unit cases are present, meaningful and passing on final code;
  reviewer has checked their adequacy and execution evidence is available.
- FAIL: required tests are absent/ineffective or executed checks fail. Fix code or
  tests according to the agreed behavior, never weaken expectations to hide a bug.
- BLOCKED: required checks cannot run due to actual tooling/environment/permission
  prerequisites. State what is unverified and needed; do not accept the code as passed.
- NOT_APPLICABLE: documentation-only or other changes without executable behavior,
  with a concrete justification reviewed by reviewer. This is not a PASS claim and
  cannot be used to excuse untested new/changed business logic.

Unrelated pre-existing failures must be separated and reported with evidence;
they do not become passing checks. Do not delete, disable, loosen or repeatedly
rerun flaky tests merely to obtain green output. Required unresolved failures prevent
code acceptance; unaffected investigation may continue.
