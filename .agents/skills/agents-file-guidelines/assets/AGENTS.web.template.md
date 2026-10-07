# Repository Guidelines

## Project

This is a **{{PROJECT_TYPE}}** for **{{PROJECT_CONTEXT_OR_GOAL}}**.

This repository contains **{{PROJECT_SUMMARY}}**. Its current scope is **{{PRODUCT_SCOPE}}**; preserve that scope during maintenance and modernization.

All user-facing chat should be in **{{CHAT_LANGUAGE}}**. Repository documentation should be in **{{REPOSITORY_DOCUMENTATION_LANGUAGE}}**. Preserve the application's existing UI locales unless a change is explicitly requested.

**Key docs** (open only when the trigger applies):

- `{{REQUIREMENTS_DOC_PATH}}` — {{REQUIREMENTS_DOC_TRIGGER}}
- `{{ARCHITECTURE_OR_ADR_PATH}}` — {{ARCHITECTURE_DOC_TRIGGER}}
- `{{DESIGN_OR_API_DOC_PATH}}` — {{DESIGN_DOC_TRIGGER}}
- `{{OTHER_DOC_PATH_OR_REMOVE_LINE}}` — {{OTHER_DOC_TRIGGER_OR_REMOVE_LINE}}

## Repository Layout

List only nonstandard or easy-to-miss project areas. Do not list conventional language/framework folders.

```text
{{NONSTANDARD_PATH_1}}  {{WHY_AGENTS_MUST_KNOW}}
{{NONSTANDARD_PATH_2}}  {{WHY_AGENTS_MUST_KNOW}}
```

## Agent Workflow

### When implementing new or refactoring functionality

1. Read the relevant requirements, architecture, and design documentation for the affected behavior.
2. Define expected observable behavior before changing code. For undocumented legacy behavior, characterize current behavior and distinguish it from intended behavior.

### TDD Rules

For every feature and bug fix:

1. Start from the specification or agreed behavior, not from an assumption about the implementation.
2. Write or extend behavior-focused tests **before** production code.
3. Run the new tests and confirm they fail for the expected reason.
4. Implement the minimum code needed to make them pass.
5. Run the focused tests and the full verification suite relevant to the change.
6. Refactor only while the behavior tests stay green.
7. Manually validate the running web application (see Manual QA below). Automated tests can pass while the real user flow is broken; a task affecting runtime behavior is not complete until the real app has been exercised.

If the area has no suitable test infrastructure, add the minimum needed as part of the authorized implementation task; do not silently skip behavioral tests. A compile/bootstrap failure is not a behavioral test failure—record it separately.

### Manual QA (required after every task that affects the running app)

Use **{{WEB_E2E_TOOL}}** (normally Playwright CLI when supported) to exercise the real running application like a user:

1. Start the app using `{{VERIFIED_START_COMMAND}}` and open the affected route/page.
2. Capture screenshots of changed screens when the environment permits.
3. Exercise the affected end-to-end flow, including success and relevant cancellation/failure paths.
4. Verify navigation, displayed/persisted data, localization, and relevant browser/server logs.
5. Compare the result with `{{DESIGN_REFERENCE_OR_REMOVE_LINE}}` when the project has an established visual reference.
6. Report the steps and outcomes. Fix observed regressions before committing; if the app/tooling is unavailable, record the blocker and do not claim manual QA passed.

### Verification (required before every commit)

Verify the scope relevant to the change. Runtime changes require a successful startup check and Manual QA when the environment supports them.

**Test Strategy:**

| Type | Boundary | Owner |
|---|---|---|
| Unit | {{UNIT_TEST_BOUNDARY}} | {{UNIT_TEST_OWNER}} |
| Integration | {{INTEGRATION_TEST_BOUNDARY}} | {{INTEGRATION_TEST_OWNER}} |
| End-to-end | Real application flow; {{E2E_TEST_BOUNDARY}} | {{E2E_TEST_OWNER}} |

**Commands:** `{{VERIFICATION_COMMANDS}}`

**Configuration:** `{{CONFIGURATION_DOC_OR_ENV_REFERENCE}}`

Tests passing is not proof that the app works. Always complete Manual QA for runtime changes when possible and report any blocked steps honestly.

### Commit Rules

- Commit only after relevant verification passes and the changed scope is in a working, reviewable state.
- Keep commits focused: one logical change per commit.
- Format: `{{COMMIT_AREA_PREFIX}}: short summary` (for example, `Backend:` or `Frontend:`).
- Do **not** push unless the user explicitly asks.

### Completion Criteria

A task is complete only when:

- Implementation matches the relevant requirements and architecture decisions.
- Behavior-focused tests were written first and pass honestly.
- Relevant verification completed without unexplained failures or warnings.
- The running app was manually exercised for runtime changes, or the blocker and required human check are reported.
- Documentation and the repository are consistent and reviewable.
- The commit is focused; no remote push occurred without explicit authorization.
