# Shared project context and delegation

Both independent workflows read this document before acting. It contains shared
project/role/path rules, not an instruction to start either workflow.

## Workflow selection

Accept an explicit request for requirements review or development; users may also
write `workflow: requirements-review` or `workflow: development` in their prompt.
These are ai-team instruction conventions, not CLI flags or config keys.
A raw requirement or a combined "review then build" request without an approved
handoff starts requirements-review only. At its completion, return the handoff and
stop; the user must explicitly start development after reviewing the result.
An explicit development request with missing/invalid evidence reports the required
review inputs and does not silently approve them or start implementation.
For an ambiguous request, inspect referenced status and ask before crossing a
workflow boundary. A resume request stays in the recorded workflow.
Record workflow identity separately from phase/gate and implementation-unit states.

## Document-first human review

In either workflow, collect human decisions in the phase's review.md (or a linked
existing issue register) rather than stopping to ask each question in chat. Finish
all safely independent analysis and document work in the current scope; mark
dependent sections/tasks provisional or blocked and state the missing decision.
Never fill a gap with an assumed answer or execute work requiring that decision.
If the source is incomplete, explicitly list what could not be assessed; a review
package is not a claim that every possible question has been discovered.

The orchestrator owns the consolidated review entry. Include the exact artifact
versions under review, scope, stable question IDs, source/requirement links,
impact, options/recommendation, blocking status, a human reply field and resolution
evidence. Link existing issue details instead of keeping duplicate mutable ledgers.
Collect role disagreements as well as questions for the user. Continue accepting
unsolicited answers while working, but do not require an interactive Q&A sequence.
At the document checkpoint, save the package and return its paths and remaining
decisions, then end the turn for offline human review; do not poll or wait on chat.
An unavailable source/root/permission may prevent even safe document work: report
that limitation immediately instead of inventing a package or writing elsewhere.

On explicit resume, read human replies from the review entry or supplied messages,
preserve decision content/provenance and revalidate affected documents. Answers to
individual questions are not approval of the whole package. Record explicit human
approval against the complete current version and scope, only after blocking issues
and required agent checks pass. New questions go into the next review checkpoint.
Requirements approval ends its workflow; development document approval releases
code work in the already-started development workflow. Project-specific approvals
may satisfy the same checkpoint when they cover the exact package, scope and version;
they cannot omit required evidence. Material changes reopen affected approvals.

## Initialize

The primary session coordinates. Establish `team_root`, `project_root`, scope,
project instructions, existing changes and required checks before delegation.
Read the project rather than assuming Go, Cocos, Redis or a directory layout.
Resolve all shared workflow documents from team_root/workflows. Never look for
copies in project_root or duplicate the team's orchestration there. Record the
team source version (commit and relevant file hashes when uncommitted) in task
status so later sessions can identify changes to the shared workflow. Preserve
the project's local configuration and do not modify global role files to select
developers for a particular project.
Choose a stable task ID and use the project's task directory, or default to
`docs/tasks/<task-id>/`. Do not create artifacts for read-only questions/reviews
unless requested.

Follow task-delivery.md in this directory for context verification and task records.
Keep records proportional to task size without bypassing required gates.

Resolve project development roles below before checking role availability.
Select the configured named custom agents using the runtime's role selection,
not merely a role name in a prompt. If the runtime cannot select the required
role/model, report the limitation before the dependent stage. Loading a TOML
file is not proof of an actual model invocation.

## Project rules and business skills

Keep project policy in the target project's applicable AGENTS.md or an explicitly
selected project_rules_file, business skills
in the project, and business/design/protocol facts in their existing documents.
Do not copy them into team_root or hardcode project-specific skill names in shared
roles/configuration. Projects need not have skills to use this workflow.

The user may specify `project_rules_file: docs/<game>/project-rules.md` in the
task prompt (or explicitly name an equivalent rules entry in natural language).
This is an ai-team task convention, not a CLI flag, config.toml key or automatic
AGENTS.md replacement. A project AGENTS.md is not required. Resolve the selected
file to an absolute path inside project_root, including symlinks; outside-project
sources require explicit scope authorization. Read it fully before selecting
development roles or delegating. Project-relative paths declared in this entry
resolve against project_root, not the entry's containing directory. This does not
change relative-link rules inside separate skills/documents.

Record the selected entry, content identity and game/module scope in task status
and pass them to children. Do not discover other games' project-rules.md files as
additional instructions. Still obey applicable AGENTS.md and read applicable shared
component rules when shared code is involved; report conflicts rather than assuming
the selected file overrides all other instructions. If the explicitly selected
file is missing, unreadable or ambiguous, report the problem and stop dependent
work; never silently fall back to another entry or generate a replacement.
Without a selected entry, use applicable AGENTS.md and the existing evidence-based
convention discovery. Do not create either file or read team_root/templates/ to
initialize a business task. Resume the recorded selection for the same task;
switching entries requires explicit user direction and affected-rule revalidation.

At intake, identify applicable project instructions, task-matching available skills
and explicit project skill/document references. Read each selected SKILL.md fully
and follow its document routing before the relevant stage, including requirements
review. Use project-relative input paths against project_root; resolve relative
links inside a skill against that skill's directory unless it explicitly declares
another base. Verify targets rather than guessing from a familiar project name.
An explicitly referenced legacy skill path may be read as an instruction source;
do not claim this proves automatic discovery. Do not silently enable a disabled
skill, install/migrate skills or change project configuration to finish intake.

For every delegation, pass exact applicable instruction/skill paths, required
document paths, source identities and why they apply to that assignment in
project_rules below. Each child reads those sources before acting and returns
the references it actually used plus any conflicts or missing inputs. Discovery,
enablement or a parent summary is not evidence that the child read the content.
Do not load every business module's documents into every child. Complete-project
requirements review must still cover the full submitted scope.

Apply only skill steps allowed by the assigned role, phase and write scope.
An implement/test/update-docs checklist cannot authorize production work during
requirements review, direct writes by read-only roles, protocol edits outside
the contract-change process, or delegation by a child. Assign permitted document
updates to one writer; read-only roles return proposed content to the parent.
Project test commands supplement, rather than replace, shared unit-test acceptance.
Project rules may specify an existing procedure/templates for a stage. Assign its
applicable work to the existing roles, reuse its versioned outputs, and keep the active
workflow's gates and write boundaries. A project's approval is an input to the
corresponding gate, not permission to skip later stages. Explicitly supplied project
templates are distinct from the human-only templates under team_root.
Reading counterpart protocol/integration rules does not enable an unselected
client/backend role or authorize changes in another project.

Report conflicting requirements, existing docs, code and skill instructions with
their sources. Do not edit business rules to remove a disagreement or treat an
AI proposal as approved. Route business decisions to requirements review and
interface changes to design review. Missing required sources or unresolved rule
conflicts block dependent work; independent authorized work may continue. Apply
the existing approval/recovery rules when referenced rules change.

## Project development roles

Read `development_roles` from the selected project_rules_file when specified;
if it omits the setting, use the target project's applicable AGENTS.md. Resolve
conflicting applicable instructions before planning, not by silent precedence. This is
an ai-team instruction convention, not a Codex config.toml key or a runtime loader
setting. Accept exactly one of these nonempty lists:

```text
development_roles: [backend]
development_roles: [client]
development_roles: [backend, client]
```

The primary orchestrator and product, architect, planner, reviewer and QA stages
remain in place in all three modes. Only implementation ownership changes.
Do not spawn, require, or wait for the unselected development role. Its TOML file
may be absent without affecting that project's workflow. Merely loading an agent
definition does not require invoking it.

If the setting is absent, infer backend/client needs from project contents and
the task, record the resolved selection and evidence in task status, and proceed
when clear. Do not assume both are required. If unclear, finish independent
requirements review and ask for the intended implementation scope before planning.
Empty/unknown/conflicting selections require correction, not silently enabling
all roles. Explicit user changes to the selection override the project default.

Pass the resolved selection and implementation scope to all stage owners.
Planner creates tasks only for selected developers; independent review and QA
evaluate the selected scope without requiring an unselected developer's output.
Record the other implementation branch as NOT_APPLICABLE with its scope reason,
not FAIL, BLOCKED or a fabricated PASS. Product/feasibility/acceptance reviews still
cover every requirement within the agreed scope, even for a single-end project.

If requirements genuinely need changes to an unselected end, report the scope
mismatch during requirements review. Have the user choose a scope adjustment or
enable that role; do not drop requirements or assign the other end's implementation
to the selected developer automatically. An existing external API/client may be a
dependency: document its contract and verification boundary. Mock-based checks do
not prove real cross-project integration. Missing actual test prerequisites can
still block a required check; absence of an unselected role alone cannot.

If a selected developer's file/model is unavailable, report the configuration
problem. This is different from intentionally selecting only backend or client.
Check availability for roles required by the active phase; a missing developer
does not block requirements review, but must be resolved before its development work.

## Delegation contract

Every assignment includes:

```text
workflow: requirements-review or development (the parent lifecycle, not a child workflow to restart)
role: configured custom agent name
development_roles: resolved backend/client selection for this project
team_root: absolute workflow repository path
project_root: absolute target project path
project_rules_file: resolved selected rules-entry path and scope, or explicit none
task_id: stable identifier
goal: bounded objective
inputs: requirements, design, files, existing changes and review scope
project_rules: applicable instruction/skill/document paths, source identities and task relevance; explicit none when no additional rules apply
gate: current phase, approved baseline identities, permitted work (design/contract/implementation)
protected_paths: canonical interfaces/protocol sources excluded from ordinary implementation writes
allowed_paths: project-relative write scope; empty for read-only roles
output_paths: exact project-relative destinations, including response-only proposals
constraints: project conventions, ownership and architectural constraints
acceptance_criteria: observable success conditions
verification: commands and explicit working directories
```

Resolve outputs inside the assigned project, including symlink destinations.
Paths escaping it require explicit scope assignment. Preserve unrelated changes.
Give concurrent writers disjoint file ownership; finalize shared interfaces first.
Respect the runtime's concurrency limit. Children do only the assigned stage.
