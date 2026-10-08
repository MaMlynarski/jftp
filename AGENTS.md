# Repository Guidelines

## Project and scope

JFTP is a legacy Java Swing FTP/FTPS application being modernized as a Codex + GitHub Copilot course exercise. Preserve existing functionality and saved user data. Adding SFTP, removing legacy entry points, or changing visible trust policies requires an explicit scope decision.

Use Polish for user-facing chat and English for repository documentation. Preserve the application's existing UI locales.

Follow the phase authorized by the current user request. Documentation/planning work does not authorize test implementation, startup repairs, or the larger refactor.

## Project-specific boundaries

- FTPAPI supplies the protocol client and listing parser through configurable class names. Its provenance and redistribution rights must be established before replacement or packaging; an absent tracked JAR does not prove the dependency is unavailable.
- The `com.myjavaworld.gui`, `util`, and `zip` packages are in-repository support code. The custom `SwingWorker` is not the JDK worker; verify callback, completion, and cancellation behavior before replacing it.
- `src/main/images` and `src/main/help` are additional classpath resource roots. German and Traditional Chinese bundles live in sibling resource trees; preserve lookup paths and locale suffixes. Consult the distribution documentation before moving them.
- Preferences and favorites use legacy serialization; certificate stores use configurable paths. Changing field types, serial UIDs, credentials, or store formats requires synthetic compatibility fixtures and a deliberate migration policy.

## Documentation triggers

Load the relevant page when its trigger applies; do not load the entire documentation set by default.

| When you need to... | Open |
|---|---|
| Choose the next modernization slice or check prerequisites and exit gates | [modernization-plan.md](docs/modernization-plan.md) |
| Configure a clone, publish modernization work, or bring in changes from the original author | [git-workflow.md](docs/git-workflow.md) |
| Find an unfamiliar subsystem or a documentation topic | [README.md](docs/README.md) |
| Change entry points, session ownership, cross-package calls, or threading | [architecture.md](docs/architecture.md) |
| Repair compilation, resolve artifacts, choose versions, or change Maven configuration | [build-and-dependencies.md](docs/build-and-dependencies.md) |
| Define observable connection, transfer, command, or saved-settings behavior | [application-workflows.md](docs/application-workflows.md) |
| Change dialogs, validation, selection, sorting, filters, or browser models | [ui-and-browser-details.md](docs/ui-and-browser-details.md) |
| Write characterization tests or choose fixtures and test boundaries | [regression-test-design.md](docs/regression-test-design.md) |
| Change shared Swing helpers, filesystem utilities, events, or archives | [support-libraries.md](docs/support-libraries.md) |
| Change certificate trust, hostname checks, keystores, credentials, or serialization | [tls-and-persistence.md](docs/tls-and-persistence.md) |
| Evaluate protocol/TLS direction or a replacement FTP library | [security-modernization-options.md](docs/security-modernization-options.md) |
| Change resource roots, translations, help, launchers, or archive layout | [resources-and-distribution.md](docs/resources-and-distribution.md) |
| Assess what the original analysis covered and what still needs runtime proof | [analysis-method.md](docs/analysis-method.md) and [analysis/verification.md](docs/analysis/verification.md) |

## Source navigation packs

- Start with [the Repo Map](docs/jftp-repomap.md): a compact index of source files and captured declarations (classes, enums, methods, and signatures/parameters), without method bodies. Its raw map, inventory, and metadata are in `docs/RepoMix/Artefact/jftp-repomap/`.
- Load [the compressed Repomix pack](docs/RepoMix/jftp-source-compressed.xml) when a broad cross-file overview helps. Compression can omit implementation details; use [the full selected-source pack](docs/RepoMix/jftp-source-full.xml) or original files to verify behavior. See [the pack README](docs/RepoMix/README.md). Keep helper scripts and supporting artifacts under `docs/RepoMix/Artefact/` out of default context.
- For natural-language, cross-file searches in the local source index, use the local Context7-compatible CLI documented in [the RepoMix README](docs/RepoMix/README.md). It searches this checkout and returns source paths and line ranges; verify results in original files. Start the local service if needed with `docs/RepoMix/Artefact/context7/start-jftp-context7.ps1`, then query with `docs/RepoMix/Artefact/context7/query-jftp-context7.ps1 -Query "..."`. This is a local CLI endpoint, separate from the hosted Context7 MCP used for external library documentation.
- After a batch of edits to indexed code or docs, run `docs/RepoMix/Artefact/context7/index-jftp-context7.ps1` once before the next local Context7 query or handoff. This repo-specific helper calls `.agents/skills/legacy-codebase-workflows/scripts/context7_backend.py` with the correct index path, docs root, and exclusions. Git hooks also refresh after commits, merges, branch checkouts, and history rewrites. Avoid indexing after every individual file edit.

## TDD and modernization workflow

1. Define expected observable behavior from the relevant documentation and acceptance criteria. For undocumented legacy behavior, characterize it first; distinguish intended contracts from known defects.
2. Write or extend behavioral tests before production changes. Assert user-visible state, transferred bytes, filesystem results, and persisted compatibility rather than private fields or implementation choices.
3. Run the tests and record failure for the expected reason. If legacy compilation prevents execution, make only the narrow bootstrap changes needed to run them; a compiler failure is not a behavioral red test.
4. Implement the minimum fix, run the same tests, and then verify the affected scope. If tests fail after a code change, investigate the changed application first; never weaken assertions or skip failures to obtain green results.
5. Refactor only with a passing characterization checkpoint. Keep deliberate security/correctness fixes and their fail-first cases separate from behavior-preserving refactors; named pending defects must remain visible.
6. Finish runtime changes with desktop Manual QA. If suitable test infrastructure is missing, add it within the authorized implementation task and report any execution blocker explicitly.

Keep the four regression suites as the shared baseline: startup/settings/favorites, browser operations, transfers/archives, and FTPS trust decisions. Establish minimal startup and a passing baseline before broad dependency or Java upgrades. Use granular checkpoints to isolate failures.

## Verification and desktop Manual QA

| Layer | Required boundary |
|---|---|
| Unit | Deterministic behavior; doubles only at irrelevant external boundaries |
| Integration | Actual JFTP session/actions and protocol client against controlled loopback FTP/FTPS fixtures |
| Desktop end-to-end | Real running Swing app and local server; no mocked transfers, certificate decisions, or persisted state |

Use isolated temporary homes, files, favorites, and keystores with synthetic credentials/certificates. Never run tests against a developer's real profile or customer files.

After every task affecting the running app:

1. Start the app using the verified launcher/build procedure for the current phase, with isolated state and a graphical desktop. Headless checks do not prove GUI behavior.
2. Drive the real window with available computer-use tooling or a Computer Commander MCP. If desktop access/tooling is unavailable, record the blocked check and obtain human verification before declaring runtime work complete.
3. Capture each changed screen and exercise the affected flow through completion, cancellation, and relevant failure paths. For transfer changes, verify destination bytes and paths; for packaging changes, launch the extracted distribution outside the IDE.
4. Check session routing, dialogs, status/progress, responsiveness, existing localized text, and application/server logs. Preserve the existing interface unless a change is authorized.
5. Fix observed regressions and report the steps, environment, outcomes, and screenshot/log locations. Automated tests alone are insufficient evidence that the application works.

Before committing, run checks relevant to the changed scope and investigate failures or new warnings. Runtime changes require successful startup, applicable tests, and Manual QA. Documentation-only changes require content, link, and consistency checks; they do not require starting the legacy app.

## Documentation, commits, and completion

- Update affected documentation and repository instructions in the same logical change when actual behavior, structure, dependencies, commands, or verification practices change. Keep exact versions and environment observations in the appropriate documentation, not here. Preserve `docs/analysis/` baseline manifests and coverage ledgers as historical evidence.
- Keep execution state in the shared tracker, not Markdown status lists. When delegating, give disjoint ownership; delegates return evidence and changes, and the coordinator verifies and commits them.
- Commit only verified, focused changes. Use `Area: short summary`, such as `Docs:`, `Build:`, `Tests:`, or `FTP:`; explain significant decisions in the body. Stage explicit paths and preserve unrelated work. Do not push unless explicitly requested.
- Publish modernization work to the personal fork through `origin`. Keep the original author's repository as fetch-only `upstream`; do not push there. Review upstream changes before integrating them.
- A task is complete when it meets the agreed behavior, passes relevant verification honestly, includes Manual QA for runtime changes, has aligned documentation, and leaves a consistent, reviewable commit. Report remaining blockers and pending defect cases explicitly; never present planned or unexecuted checks as passing.
