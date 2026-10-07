# Web application workflow

Use this workflow when the primary product is accessed through a browser. Start from `assets/AGENTS.web.template.md`.

## Discover project-specific facts

Confirm the application purpose and scope, preferred chat/documentation languages, real acceptance/design/architecture documents, test commands, launch procedure, and nonstandard repository layout. Find durable integration boundaries and constraints that every project agent must honor. Keep framework/library versions in dependency documentation rather than agent guidance.

Build a documentation-trigger table from documents that actually exist. A trigger should say what task involving a workflow, UI area, schema, or architecture decision should cause an agent to open the page. If no spec/ADR/design system exists, do not invent it; remove unused entries from the adapted file.

## Copy and adapt

1. Copy the web template byte-for-byte to the repository root as `AGENTS.md`.
2. Edit only the copy. Fill project, language, commands, test boundaries, real documentation triggers, and any verified special configuration. Keep the TDD, real-app QA, verification, commit, and completion gates unless the user explicitly changes them.
3. Describe only exceptional layout and non-obvious constraints. Do not reproduce a generic `src/`, `app/`, or package tree.
4. For a nested `AGENTS.md`, copy the same template byte-for-byte into that folder first. Then retain only always-on instructions for any work in that subtree. Root-level TDD/commit procedures should not be repeated unless a local rule modifies them for every task in the subtree.

## Web manual QA expectations

The template uses Playwright CLI as the default browser automation example. Replace it when the repository has a different supported browser tool, and do not claim a browser test is available until confirmed. Exercise the real running application; end-to-end tests should not mock the main product flow. Capture changed screens where practical, check relevant navigation/data/console or server errors, preserve existing localization, and compare with a design reference only if the project has one.

Automated tests and application startup remain separate checks. State which was actually run. If no suitable test infrastructure exists, the adapted guidance should require adding it within an authorized implementation task rather than silently skipping behavioral coverage.
