# Desktop application workflow

Use this workflow when the primary product is a native desktop application. Start from `assets/AGENTS.desktop.template.md`.

## Discover project-specific facts

Confirm the product's user-facing purpose, languages, runtime/toolchain, verified start procedure, real test commands, available desktop automation, and nonstandard module/resource/data boundaries. Identify durable behavior and saved-data constraints that every agent must respect. Keep exact versions, environment observations, setup procedures, and unverified runtime claims in project documentation.

Build documentation triggers from pages that actually exist. Link a guide only when a task involving the described subsystem should cause an agent to read it. Do not invent a PRD, ADR, design reference, test fixture, or launcher. Mention only repository layout exceptions, such as separately packaged assets, plugins, templates, or runtime data.

## Copy and adapt

1. Copy the desktop template byte-for-byte to the repository root as `AGENTS.md`.
2. Edit only the copy. Fill in project/language placeholders, real documentation triggers, verified test boundaries and commands, and the verified application start procedure.
3. Keep the behavior-first TDD, startup, desktop Manual QA, verification, commit, and completion gates. Replace the example desktop automation with a tool actually available for the project; do not require a specific MCP if it is unavailable.
4. For a nested `AGENTS.md`, first copy the same template byte-for-byte into the folder, then reduce it to durable instructions every agent in that folder needs. Put specialized task scenarios in docs or skills, not as conditional rules in a nested file.

## Desktop Manual QA expectations

Use available computer-use or desktop automation to operate the real application, such as a computer-use tool or a Computer Commander MCP. Browser-only Playwright is not suitable for native windows unless the application is actually browser-hosted. Run with isolated settings/data when persistence is involved. After automated checks, start the app with the verified procedure, exercise the changed flow through success and relevant cancellation/failure cases, inspect visible state and logs, and capture changed screens when practical.

Headless tests do not prove that a GUI works. If the app cannot start or desktop control is unavailable, record the exact blocker and require human verification before describing runtime work as complete. Do not fabricate screenshots or report unrun manual checks as passed.
