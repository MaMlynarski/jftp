# First-use review: legacy codebase workflow and native mapper

Reviewed: 2026-10-07  
Repository revision: `c3182280a6c74049b9f926e53c7b381ecdc74f8c`  
Scope: first-run check of the repo-map workflow and availability of the `legacy-repo-map` Rust executable. No application code or skill files were changed during this review.

## Summary

- The repo-map workflow could not be executed in this checkout because Python is not available in the current Windows environment. The recommended inventory-only mode still requires a Python interpreter, even though it has no third-party package requirement.
- The Rust executable and the `legacy-tools` bundle are not included in the installed skill or this repository. No Rust source crate or Cargo manifest is included either. `cargo` and `rustc` are also unavailable in the environment.
- Consequently, no map from this skill was generated and the Rust executable could not be run. The output directory created for the inventory-only attempt remained empty.
- [The existing JFTP map](../jftp-repomap.md) is an Aider 0.86.2 map dated 2026-10-06. It is useful prior navigation material, but it does not demonstrate that this skill's Python or Rust implementation works.
- The skill documentation says CI builds and tests platform-specific artifacts, but also says the build helper does not publish or upload them. A supported, discoverable download path is not established by the installed skill.

## Checks and observed results

| Check | Result | Evidence |
|---|---|---|
| Locate Python, Rust, and packaged commands | `python`, `python3`, `py`, `pip`, `uv`, `cargo`, `rustc`, `rustup`, `legacy-tools`, and `legacy-repo-map` were not available through `Get-Command`. | Windows PowerShell check on this checkout. |
| Run inventory-only | Failed before the script started: `The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program.` | Attempted `python <skill>/scripts/repo_map.py <repo> --output-dir <temp> --inventory-only`. |
| Run native mapper | Failed before the program started: `The term 'legacy-repo-map' is not recognized as the name of a cmdlet, function, script file, or operable program.` | Attempted `legacy-repo-map <repo> --output-dir <temp> --budget 1024`. |
| Run standalone fallback | Failed before the program started: `The term 'legacy-tools' is not recognized as the name of a cmdlet, function, script file, or operable program.` | Attempted `legacy-tools map <repo> --output-dir <temp> --inventory-only`. |
| Search the checkout and skill for native artifacts | No matching executable, Rust source, `Cargo.toml`, or `Cargo.lock` was found. | Searched tracked and hidden project paths for `legacy-repo-map`, `legacy-tools`, `*.exe`, `*.rs`, `Cargo.toml`, and `Cargo.lock`; separately searched the installed skill directory. |
| Check inventory output | No files were produced. | The output directory was empty after all three launch attempts. |
| Verify existing map provenance | Existing map reports Aider 0.86.2, 576 scanned files, and a 6,000-token budget. | `docs/jftp-repomap.md:3-7`. |

The missing-command messages are environment/setup failures, not failures in the mapper's parsing or ranking behavior. No claim is made here about runtime correctness, map coverage, or Rust/Python parity on this checkout.

## Skill documentation evidence

- The workflow says to start large repositories with `--inventory-only`, which requires only Python's standard library: [`references/repo-map.md:9-12`](../../.agents/skills/legacy-codebase-workflows/references/repo-map.md).
- The supported source implementation still requires Python 3.12–3.14; the standalone and native modes require their respective packaged executable: [`references/setup.md:5-11`](../../.agents/skills/legacy-codebase-workflows/references/setup.md).
- The setup guide explicitly says that no binaries are stored in the skill or repository and points to toolbox build artifacts only “when its maintainers publish them”: [`references/setup.md:73`](../../.agents/skills/legacy-codebase-workflows/references/setup.md).
- Building requires a separate toolbox source checkout containing `src/legacy-repo-map/` and `scripts/build-legacy-tools.py`; the Rust target requires Cargo 1.82+ and a C compiler: [`references/setup.md:87-93`](../../.agents/skills/legacy-codebase-workflows/references/setup.md).
- The build helper creates checksums and smoke-test results but does not publish or upload artifacts: [`references/setup.md:95`](../../.agents/skills/legacy-codebase-workflows/references/setup.md).
- The native tooling reference labels Rust experimental, records a Python grammar difference, and links to CI that it says builds/tests Linux x86-64, macOS arm64, and Windows x86-64: [`references/native-tooling.md:64-68`](../../.agents/skills/legacy-codebase-workflows/references/native-tooling.md).
- The skill says to use the installed Python entrypoint and keep generated artifacts outside the source repository: [`SKILL.md:21-27`](../../.agents/skills/legacy-codebase-workflows/SKILL.md).

The referenced GitHub Actions page could not be fetched during this review (`Cache miss`). Its current artifact retention, download permissions, and whether the workflow uploads assets therefore remain unverified. The local setup documentation's statement that the build helper itself does not upload artifacts is verified by reading the installed documentation.

## Friction and possible documentation defects

1. **“Bundled map” can sound like a bundled executable.** In `SKILL.md:17`, “The bundled map runs locally” may be read as saying the executable ships in the skill. The setup guide says the opposite. Consider “The skill's Python map implementation runs locally without an LLM endpoint.”
2. **Inventory-only can sound independently runnable.** “Needs only Python's standard library” correctly describes Python dependencies, but does not make the command runnable without Python. Add a short prerequisite/preflight statement before the first-run command.
3. **Windows first-run instructions are incomplete.** Most examples are Bash and use POSIX virtualenv paths. The setup guide mentions a Windows interpreter path, but does not provide a complete PowerShell path for environment creation, package installation, inventory-only, and map generation. This matters especially where Python is absent from `PATH`.
4. **The no-Python/no-binary state has no direct recovery path.** The skill package does not identify a stable versioned release URL or an install command that selects a platform artifact. The build instructions require obtaining the separate toolbox source repository first.
5. **CI build versus distribution is unclear.** The native reference links to one CI run, while setup says the helper does not upload artifacts and directs users to build artifacts “when maintainers publish them.” Clarify whether the CI workflow uploads downloadable artifacts, whether those expire, and where stable release archives live. The external run was not accessible in this review, so do not treat it as evidence of a usable download route.
6. **“Device versions” need a concrete support matrix.** Native artifacts are platform/architecture-specific and have host runtime prerequisites. Publish a matrix with exact supported targets and prerequisites; do not imply that one executable works across Windows, macOS, and Linux.

## Rust and binary distribution recommendation

The user's proposal to build binaries in CI is a good way to avoid requiring Rust toolchains on every skill consumer's machine. The skill should not carry an unqualified executable as if it were portable. A safer distribution design would be:

1. Keep the Rust implementation optional/experimental until its documented language differences and coverage gaps are resolved.
2. Build each explicitly supported OS/architecture target in CI from a tagged toolbox source revision.
3. Publish versioned archives with `SHA256SUMS`, `BUILD-INFO.json`, and required license notices; provide a stable index or release page from which an installer can select a matching target.
4. Have the skill's setup instructions verify the archive checksum and executable version before use, and clearly describe host runtime requirements.
5. Keep the Python implementation or reference bundle as the correctness fallback. Do not silently compile Rust locally when the user only installed the skill; local compilation requires a separate source checkout, Cargo, and a C compiler.

This is a recommendation, not a claim that such a release pipeline already exists.

## Follow-up verification to close this review

1. On a machine with Python 3.12–3.14, create an isolated tool environment and install the pinned `requirements-map.txt` packages without using the JFTP application's environment.
2. Run inventory-only to a directory outside this checkout; inspect the bounded summary, skipped files, revision, and working-copy fingerprint.
3. Select a JFTP module from the inventory, generate a scoped map, and confirm `map.meta.json` reports `complete` with expected coverage.
4. Obtain a matching Windows x86-64 Rust release artifact if a supported publication exists; verify its checksum and notices, run its help/version command, and map the same module. Otherwise, obtain the separately maintained toolbox source and follow its documented Rust build procedure in an isolated output directory.
5. Compare Python and Rust map output for Java and record any expected metadata or output differences. Keep the Rust program marked experimental unless parity and the documented grammar gaps are addressed.

Do not count this follow-up as completed until those commands actually run and their output is inspected.
