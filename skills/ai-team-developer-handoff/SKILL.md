---
name: ai-team-developer-handoff
description: Apply the shared project-path and result-handoff contract for backend or client assignments in ai-team. Use when those developers begin an assigned task, not for general project orchestration.
---

# Developer Project Contract

The parent supplies the absolute team_root together with the assignment.
The role's own phase gates, permissions and specialist rules remain in force.
Read this shared contract before acting; it does not replace those role rules.

Require project_root, allowed_paths, output_paths and acceptance criteria from
the parent. Resolve task paths and command working directories against project_root.
Write only assigned project files, never business artifacts in team_root.
Do only this assignment; do not restart the workflow or delegate independently.
Use task-delivery.md under team_root/workflows for phase-appropriate handoff:
consultation returns response-only findings, source/baseline identities and evidence
limitations; contract/implementation work returns changed files, baseline identities,
applicable checks/results and risks. Consultation requires no writes or test execution.
Do not update shared task status yourself or invent missing business decisions.

## Implementation simplicity

For authorized contract/implementation work only; this section does not permit
code writes during read-only consultation or expand the assignment's scope.

- Understand the approved requirement, design, affected code and actual callers
  before editing. Fix root causes within scope; report needed scope expansion.
- Prefer existing project helpers/framework patterns, then suitable standard-library,
  native-platform or installed-dependency capabilities; otherwise implement the
  smallest clear solution meeting the contract. Do not add speculative functionality,
  abstractions or dependencies. Prefer clarity over compressed one-liners.
- A single implementation does not make a required framework interface, test seam
  or approved extension point unnecessary. Preserve business behavior, protocols,
  lifecycle, compatibility, validation, error handling, security, accessibility and
  required observability. Material alternatives go to the existing human review
  gate, not a reduced feature shipped first; tradeoffs must meet accepted constraints.
- For contract setup, supply design-review.md's schema/generation/build evidence;
  do not claim acceptance of unfinished business behavior. For implementation,
  apply team_root/workflows/unit-test-acceptance.md in full with project test tools.
  Rerun affected normal/boundary/error/regression checks after simplification; do not
  substitute a smoke test for required coverage or optimize for deleted-line counts.
- Return the complete handoff above, including test evidence and risks. No extra
  skill invocation, persistent mode or mandatory ponytail-review self-check is needed.

Simplicity guidance derives from DietrichGebert/ponytail; source and adaptation
details are recorded in ../UPSTREAM.md, with the MIT notice in LICENSE.
