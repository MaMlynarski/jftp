# Repository Guidelines

## Project

This is a **{{PROJECT_TYPE}}** for **{{PROJECT_CONTEXT_OR_GOAL}}**.

This repository contains **{{PROJECT_SUMMARY}}**. Its current scope is **{{PRODUCT_SCOPE}}**; preserve that scope during maintenance and modernization.

All user-facing chat should be in **{{CHAT_LANGUAGE}}**. Repository documentation should be in **{{REPOSITORY_DOCUMENTATION_LANGUAGE}}**. Preserve the application's existing UI locales unless a change is explicitly requested.

**Key docs** (open only when the trigger applies):

- `{{REQUIREMENTS_DOC_PATH}}` — {{REQUIREMENTS_DOC_TRIGGER}}
- `{{ARCHITECTURE_OR_ADR_PATH}}` — {{ARCHITECTURE_DOC_TRIGGER}}
- `{{DATA_OR_SECURITY_DOC_PATH}}` — {{DATA_SECURITY_DOC_TRIGGER}}
- `{{OTHER_DOC_PATH_OR_REMOVE_LINE}}` — {{OTHER_DOC_TRIGGER_OR_REMOVE_LINE}}

## Repository Layout

List only nonstandard or easy-to-miss project areas. Do not list conventional language/framework folders.

```text
{{NONSTANDARD_PATH_1}}  {{WHY_AGENTS_MUST_KNOW}}
{{NONSTANDARD_PATH_2}}  {{WHY_AGENTS_MUST_KNOW}}
```

## Agent Workflow

### When implementing new or refactoring functionality

1. Read the relevant requirements and subsystem documentation for the affected behavior.
2. Define expected observable behavior before changing code. For undocumented legacy behavior, characterize current behavior and distinguish it from intended behavior.

### TDD Rules

For every feature and bug fix:

1. Start from the specification or agreed behavior, not from an assumption about the implementation.
2. Write or extend behavior-focused tests **before** production code.
3. Run the new tests and confirm they fail for the expected reason.
4. Implement the minimum code needed to make them pass.
5. Run the focused tests and the full verification suite relevant to the change.
6. Refactor only while the behavior tests stay green.
7. Manually validate the running desktop application (see Manual QA below). Automated tests can pass while the actual window flow is broken; a task affecting runtime behavior is not complete until the real app has been exercised.

If the area has no suitable test infrastructure, add the minimum needed as part of the authorized implementation task; do not silently skip behavioral tests. A compile/bootstrap failure is not a behavioral test failure—record it separately.

### Manual QA (required after every task that affects the running app)

Use **{{DESKTOP_AUTOMATION_TOOL}}** (for example, available computer-use tooling or a Computer Commander MCP) to operate the real application like a user. Do not prescribe browser-only Playwright for native desktop windows.

1. Start the app using `{{VERIFIED_START_COMMAND}}` with isolated user data where persistence is involved.
2. Capture screenshots of changed screens when the environment permits.
3. Exercise the affected flow through success, completion, cancellation, and relevant failure paths.
4. Verify visible state, persisted results, dialogs, status/progress, responsiveness, localization, and relevant application/service logs.
5. Compare with `{{DESIGN_REFERENCE_OR_REMOVE_LINE}}` if a project design reference exists.
6. Report the steps and outcomes. If the app cannot start or desktop control is unavailable, record the blocker and obtain human verification before declaring runtime work complete.

Headless tests do not prove GUI behavior. Do not fabricate screenshots or claim a manual check passed when it did not run.

### Verification (required before every commit)

Verify the scope relevant to the change. Runtime changes require successful startup and desktop Manual QA when the environment supports them.

**Test Strategy:**

| Type | Boundary | Owner |
|---|---|---|
| Unit | {{UNIT_TEST_BOUNDARY}} | {{UNIT_TEST_OWNER}} |
| Integration | Actual application/domain with controlled external boundaries: {{INTEGRATION_TEST_BOUNDARY}} | {{INTEGRATION_TEST_OWNER}} |
| Desktop end-to-end | Real running application and {{REAL_LOCAL_SERVICES_OR_DEVICES}}; do not mock the changed user workflow | {{E2E_TEST_OWNER}} |

**Commands:** `{{VERIFICATION_COMMANDS}}`

**Configuration:** `{{CONFIGURATION_DOC_OR_ENV_REFERENCE}}`

Tests passing is not proof that the app works. Complete Manual QA for runtime changes when possible and report blocked checks honestly.

### Commit Rules

- Commit only after relevant verification passes and the changed scope is in a working, reviewable state.
- Keep commits focused: one logical change per commit.
- Format: `{{COMMIT_AREA_PREFIX}}: short summary` (for example, `Backend:` or `UI:`).
- Do **not** push unless the user explicitly asks.

### Completion Criteria

A task is complete only when:

- Implementation matches the relevant requirements and architecture decisions.
- Behavior-focused tests were written first and pass honestly.
- Relevant verification completed without unexplained failures or warnings.
- The real desktop app was exercised for runtime changes, or the blocker and required human check are reported.
- Documentation and the repository are consistent and reviewable.
- The commit is focused; no remote push occurred without explicit authorization.
