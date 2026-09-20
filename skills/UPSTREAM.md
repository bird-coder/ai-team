# Vendored skill sources

The implementation-simplicity section in `ai-team-developer-handoff/SKILL.md`
derives from ponytail; `ponytail-review/SKILL.md` is an unmodified copy. Sources:
https://github.com/DietrichGebert/ponytail at commit
`e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156`, installed on 2026-09-20.
Upstream paths: `skills/ponytail/SKILL.md`, `skills/ponytail-review/SKILL.md`.
The developer-handoff and ponytail-review directories retain the upstream MIT notice.
No plugin or hooks installed. The standalone ponytail skill was removed after its
adapted guidance was merged into the existing developer-handoff skill.

Local guidance changes: authorized implementation only, without a separate skill
or activation mode; no global switches, code-first/three-line output, reduced
test policy or unilateral scope reductions. Keep the reuse ladder, caller analysis
and safety boundaries. Team gates, framework contracts, full test acceptance and
normal handoff are explicit. The MIT notice is unchanged.

Reviewer-specific integration of ponytail-review remains in agents/reviewer.toml.
Review upstream changes against these approval/test/scope boundaries before
intentionally updating; do not overwrite the shared handoff with a fresh install.
