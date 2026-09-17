# Requirements-review workflow

## Independent entry and completion

Read project-context.md for shared setup, role selection and delegation. Input is
the original requirement source, project rules and any existing item/Q&A records.
This workflow can start or resume without a development plan. It ends with a
versioned confirmed-baseline handoff; no detailed design, implementation plan or
code is part of its completion. Development is a separately requested workflow.

## Objective and scope

A supplied requirement document starts understanding, business decomposition and
item-level question/answer clarification, not immediate implementation. Review is
continuous checking plus a final baseline gate, not repeated full-report generation.
Identify interpretation differences, missing behavior,
contradictions, unreasonable constraints and feasibility risks. Produce materials
the user can hand to human product planners/designers for revision. AI suggestions
are proposals, never silently accepted business rules. Do not promise zero ambiguity;
make interpretations and decisions explicit and traceable.

The orchestrator reads this workflow and delegates bounded review assignments.
Resolve and include the project's development_roles and implementation scope using
project-context.md. Backend-only and client-only selections preserve all three review
dimensions. Treat genuinely required changes to an unselected end as a scope
question, not as a missing agent; external interfaces need explicit contracts.
Until the gate below passes, allowed work is reading project/source material and
writing review documents. Do not start detailed architecture, implementation task
planning, production changes or executable tests. Feasibility analysis is not
permission to implement a prototype. No automatic messages to human collaborators.

## Understanding and clarification cycle

Accept a full-project document or document set; the human author need not split it
into features first. For that intake, use a project-level task ID and review the
complete submitted scope before downstream work. Product owns business
decomposition; planner owns technical task decomposition during development's
document phase, after agent design review.

1. Identify the source document(s), versions and related business rules. Record
   exact content identity: Git commit plus file hash for local content, or a versioned
   snapshot/hash for supplied text. A filename or modification date alone is not
   sufficient. Preserve originals; never replace the author's document with AI prose.
   Save a source snapshot in the target project's round directory when needed.
2. Product reads the entire relevant source, restates the goal, scope, actors,
   main flow, rules and exceptions. For full-project inputs, produce the business
   decomposition below before feasibility and acceptance reviews. Those reviews
   use both the source and decomposition, including cross-module behavior.
   Assign stable requirement IDs and cite source
   sections. Distinguish explicit source statements, inferred interpretations,
   proposed additions and unresolved decisions. Provide examples of differing
   interpretations and their user-visible consequences.
3. Product attaches gaps, conflicting rules, unreasonable behavior and scope concerns
   to the affected requirement IDs; keep project-wide/cross-module issues separately
   linked rather than forcing them under one item. Each issue has a stable ID,
   source reference, category, impact, blocking status,
   concrete decision/question, proposed options and tradeoffs. Explain evidence;
   do not label a requirement unreasonable merely because it is difficult to build.
4. Architect reviews technical feasibility against the actual project: conflicting
   interfaces/state ownership, dependencies, compatibility, data constraints,
   performance/reliability expectations and implementation risks. Give evidence,
   alternatives and unresolved prerequisites. Do not produce a detailed design yet.
5. QA reviews whether every requirement has observable acceptance criteria and
   adequate normal, boundary and failure examples. Propose Given/When/Then criteria,
   trace them to requirement IDs and flag missing decisions. This is document-only
   review, not execution or proof that the feature works.
6. Orchestrator reconciles reviews without silently resolving disagreements. Present
   questions grouped by requirement, with original text, interpretation and options
   so the user can reply inline/by ID or forward a concise handoff to human authors.
   Follow project-context.md's document-first human review: finish independent
   analysis across the submitted scope and consolidate questions in review.md,
   without stopping at each question for a chat reply. Mark unassessable dependent
   sections explicitly, then deliver the package for human replies. Unresolved blocking questions mean
   NEEDS_REVISION (clarification needed, not necessarily an original-file edit).
   No downstream design/development while the initial gate is pending.
7. On answers or source updates, follow the item and change rules below. Reuse
   valid answers and review evidence, update only affected content, and retain
   stable IDs/history. Before the final gate, product checks overall consistency
   and coverage; architect and QA provide current feasibility/acceptance verdicts,
   incorporating affected checks and explicitly carried-forward valid evidence.

### Requirement items and answers

Use decomposition.md (or the project's equivalent) as the current item index.
Each item includes source/version references, understanding, acceptance criteria,
dependencies, linked question IDs, and clarification state: OPEN (questions remain),
CLARIFIED (blocking questions resolved), REOPENED (new conflicting evidence), or
RETIRED (removed/superseded with history). These are not implementation permissions.
Never reuse retired IDs; for split/merged items record successor/predecessor links.

Keep questions and replies in review.md. If issues.md or item sections already hold
the canonical register, review.md links them as the human entry without duplicating
mutable questions. Record the actual answer/message reference, affected IDs, agreed meaning,
whether it supplements/corrects the source, and resolution evidence. A clear explicit
user decision may resolve a question without editing the original; an ambiguous
reply or AI-proposed answer stays open. Do not require repeated confirmation of
the same decision. Item answers do not themselves approve the whole baseline.
Close a question only after checking that the answer resolves it and propagating
its implications to related items/criteria; record remaining implications as issues.
Keep prior answers when superseded and cite the replacing decision.

### Source updates and incremental review

Read the new source, identify its exact content and compare it with the previous
source AND recorded decisions. Reconcile all relevant content to detect additions,
changes and deletions; do not use textual similarity alone as proof of unchanged
meaning. Update the item index and source references, not a fresh ID set.

| Change | Required action |
| --- | --- |
| Wording/layout only, meaning unchanged | Record source mapping and equivalence evidence; keep answers and review results |
| Previously confirmed answer incorporated into source | Verify exact semantic agreement; link that decision, no repeat question |
| New requirement | Add stable ID, clarify and check dependencies/cross-item effects |
| Changed or deleted requirement | Preserve old version/ID, mark affected items for review or retirement; identify dependent design/tasks/tests; an unconfirmed deletion is not authorized scope reduction |
| New source conflicts with an earlier answer | Show both sources and ask which applies unless an explicit user decision already resolves this exact conflict; newer timestamp alone does not decide |
| Major scope change or uncertain impact | Broaden to whole-baseline assessment where necessary, explaining why; retain history and unaffected valid evidence |

Product establishes semantic impact; architect and QA recheck affected feasibility
and acceptance implications. Show a concise change list with source identities,
affected IDs, carried-forward decisions/evidence and reopened questions in the
existing understanding/handoff records. Include cross-module dependencies, shared
rules and acceptance changes; do not limit impact to edited paragraphs.
For nonsemantic updates, carry prior approval forward only with a recorded old-to-new
baseline mapping and verified unchanged behavior, scope and criteria. Missing
comparison evidence requires review, not an assumed carry-forward.
Semantic changes require affected review and explicit updated-baseline confirmation
before dependent downstream work. Unaffected authorized work can continue when
independence is established; do not restart the entire project automatically.

### Business decomposition within review

Product records the project goal, actors, scope and non-goals, then organizes
business modules -> user scenarios -> verifiable requirements. For each requirement,
record a stable ID, source section, owning business module, observable behavior,
business dependencies, acceptance criteria (or a linked open issue) and whether it
is explicit, inferred, proposed or unresolved. These are business groupings, not
prescribed services, classes, interfaces or backend/client implementation tasks.

Map every substantive source requirement to these IDs, including cross-module
flows, shared rules, nonfunctional constraints and external dependencies. Mark
unmapped or ambiguous source content as issues; never silently omit it. Reference
shared rules rather than copying conflicting versions into each module. Proposed
priorities, milestones, exclusions or MVP reductions require user confirmation;
decomposition alone does not approve scope changes or new business decisions.

Keep the breakdown as a compact table for small inputs. For large projects, link
module detail files under the same round's modules/ directory only when useful.
Do not create implementation plans or start design/development for a clear module
while the complete initial project baseline is still awaiting review/confirmation.
Later changes follow the existing affected-approval rules below.

Human revision rounds have no automatic three-round limit. The development
fix/review limit applies only after implementation. Waiting for human revision is
an expected workflow state, not a reason to fabricate decisions or keep polling.

## Review artifacts

All files are under the target project, by default
`docs/tasks/<task-id>/requirements/round-<n>/`. Existing project conventions may
override the location. Product, architect and QA return response-only review content;
the orchestrator writes these documents (QA has an empty allowed_paths assignment
in this phase). Do not read templates/ to generate the package.

| File | Contents |
| --- | --- |
| `understanding.md` | Source identity, requirement IDs, restated understanding, inferred vs explicit behavior, proposed supplements |
| `decomposition.md` | Stable requirement-item index, business modules/scenarios, understanding, criteria, dependencies, question links, clarification states and source coverage; small inputs may use a linked section in understanding.md |
| `review.md` | Human review entry: artifact versions, questions grouped by requirement plus cross-item issues, impacts/options, reply fields, resolutions and whole-baseline approval; links an existing issues.md register when applicable |
| `feasibility.md` | Architect assessment, project evidence, constraints, alternatives and remaining risks |
| `acceptance.md` | QA's requirement-to-acceptance mapping and missing conditions; proposed criteria clearly labeled |
| `handoff.md` | Self-contained summary for human planners/designers: what to clarify/change, why, choices, and what to return |
| `gate.md` | Exact baseline, issue dispositions, product/architect/QA verdicts, user confirmation evidence and orchestrator decision |

Use the user's language (Chinese by default) in handoff materials. Preserve old
rounds so human decisions and rejected proposals are not lost. Link the latest
round and workflow status from the task's status.md. Do not infer a human's response.
Rounds are versioned checkpoints, not a requirement to regenerate the full package
for each reply. Append Q&A within the active round with history; create a new round
for a revised source or a new formal baseline review. Reference unchanged prior
artifacts by exact version rather than copying them. Never overwrite a frozen or
approved checkpoint; subsequent decisions belong to the next checkpoint.

## Review completion gate and handoff

Track states: IN_REVIEW, NEEDS_REVISION, AWAITING_CONFIRMATION, READY_FOR_DESIGN.
Use BLOCKED for unavailable evidence/capabilities preventing assessment. A review
stage can finish successfully while the overall development task is still waiting.

The orchestrator may record READY_FOR_DESIGN only when all conditions hold:

- The complete current baseline comprises the exact original-source version(s),
  confirmed supplemental/corrective decisions, and reviewed decomposition/acceptance
  criteria. Identify all components and their versions for downstream agents; an
  unchanged original file does not mean the baseline is unchanged if decisions changed.
- Product finds no unresolved blocking ambiguity, contradiction or missing rule.
- Product checks cross-item consistency and completeness; individually clarified
  items alone do not prove that the overall requirements are coherent.
- For full-project intake, business decomposition covers the entire submitted scope,
  including shared rules and cross-module acceptance; exclusions have explicit user
  agreement. The reviewed decomposition and accepted criteria are part of the exact
  baseline above. Per-module verdicts cannot replace the project-wide gate.
- Architect's feasibility assessment passes with no unresolved technical blockers.
- QA's acceptance-readiness review passes; success/failure can be objectively checked.
- All review disagreements are resolved. Any nonblocking residual risk is documented
  and explicitly accepted by the user; an accepted scope change updates the baseline.
- The user explicitly confirms this reviewed version as the agreed requirements.
  Record the actual message/decision reference; silence,
  elapsed time, a revised upload, or the original request to develop is not approval
  of AI-proposed additions. Reuse existing explicit approval for the same baseline.
- The orchestrator verifies these conditions and records its readiness verdict.

Once both human confirmation and workflow readiness pass, record READY_FOR_DESIGN,
finish this review workflow and STOP. Return exact gate/handoff links and explain
how to explicitly start development. Do not turn baseline approval or an earlier
combined review/build request into automatic design or implementation.
READY_FOR_DESIGN remains the compatibility state meaning the baseline is eligible
for development intake, not that development has started.
Legacy READY_FOR_DEVELOPMENT requirement records mean READY_FOR_DESIGN only; they
cannot bypass design and contract checks. A human request
to proceed does not turn an unresolved technical blocker into a passing assessment.

Any subsequent requirement/acceptance change invalidates the affected approval and
readiness evidence: pause dependent implementation, review the change, obtain the
updated baseline confirmation and a handoff before explicit development resumption.
Unaffected authorized work can continue
when its independence is established. Implementation details within the agreed
requirements do not require repeated product approval.

The final handoff.md (or equivalent project entry) must be self-contained across
sessions: reference the exact original source versions/hashes or snapshots,
understanding/decomposition with stable IDs, confirmed Q&A decisions/corrections,
acceptance criteria, scope/exclusions/dependencies, accepted residual risks,
issue dispositions, three-role verdicts and actual user confirmation in gate.md.
Distinguish these records from a draft "questions for human authors" handoff.
Keep a versioned manifest or equivalent gate references; do not require replaying
chat to reconstruct accepted rules. Preserve decision content and its provenance
in project records, not only an inaccessible message ID. Link existing artifacts
instead of creating another full specification or rewriting the author's original.
