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
Use task-delivery.md under team_root/workflows for handoff: return changed files,
baseline identities, tests/results and risks to the parent. Do not update shared
task status yourself or invent missing business decisions to finish a task.
