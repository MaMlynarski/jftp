# JFTP Repomix packs

Generated on 2026-10-08 with Repomix 1.18.1 from the current working copy at
revision `c3182280a6c74049b9f926e53c7b381ecdc74f8c`. The working copy was dirty,
so these packs reflect the files present at generation time, including any
uncommitted changes in the selected scope.

## Artifacts

- `jftp-source-full.xml` — full selected source and resource text: 359 files,
  266,874 estimated tokens, 1,021,359 characters.
- `jftp-source-compressed.xml` — Repomix structural compression of the same
  359 files: 182,440 estimated tokens, 700,996 characters. This is a 31.6%
  reduction in Repomix's token estimate.

Both outputs are valid XML and contain the same number of file entries. The
Repomix security scan reported no suspicious files. That scan is a screening
check, not a guarantee that an artifact is safe to publish.

## Which pack to use

Start with the compact [Repo Map](../jftp-repomap.md) for file and symbol
navigation. Its sidecars are in `Artefact/jftp-repomap/`. Load the compressed
pack for a broad view across the application; structural compression can omit
method logic and signature details, so verify behavior in the full pack or
original source. The full pack retains the selected source text.

The session-analysis helper is also kept under `Artefact/`; these supporting
files are not part of the default source context.

## Local Context7 source search

The repository also has a local Context7-compatible retrieval service backed by
SQLite FTS5. The index covers the checkout's UTF-8 source/configuration and
authored Markdown docs, with docs provenance. Generated maps/packs and the
tracked `mpc.json` are excluded. The index was built at revision
`9e8489140eded27672977ca8b50a1fd2c53320fe` (553 files, 3,003 chunks); 41
non-UTF-8 files were reported as skipped. This lexical index does not use a
downloaded model.

The index database and isolated `ctx7` 0.5.13 CLI/config live under
`%LOCALAPPDATA%\Codex\jftp-context7`, outside the checkout. To refresh the
index after source changes, run `Artefact/context7/index-jftp-context7.ps1`.
That repo-specific helper calls the Python backend shipped with the legacy-codebase
skill and supplies this repository's database path and exclusions.
Start the loopback-only service with
`Artefact/context7/start-jftp-context7.ps1`, then search with:

```powershell
.\docs\RepoMix\Artefact\context7\query-jftp-context7.ps1 -Query "FTP transfer cancellation"
```

Use `-Command library` to resolve `/local/jftp`, or `-Command docs` for source
snippets. Exact-symbol lookups are also served by `rg` and the Repo Map; use
these before broader natural-language retrieval. Treat retrieved snippets as
navigation evidence, then verify behavior in current source. The helper always
targets `127.0.0.1` and returns JSON; it never needs Context7 login or a hosted
endpoint. The local HTTP service is unauthenticated, so it binds only to
loopback. This local CLI service is separate from the hosted Context7 MCP used
for external library documentation.

The isolated CLI is `ctx7` 0.5.13. To reinstall it, run
`npm install --prefix "$env:LOCALAPPDATA\Codex\jftp-context7\client" --no-audit --no-fund ctx7@0.5.13`.

## Automatic refresh

The installed Git hooks refresh the local index after a commit, merge, branch
checkout, or history rewrite. They run the same index script and print changed
and deleted file counts. To enable the repo-local hooks in another clone, run
`git config --local core.hooksPath .githooks` after initializing the index.
The agent instructions also tell agents to refresh once after a batch of
indexed source/docs edits, before the next local search or handoff.

The indexer already updates chunks incrementally: it hashes the included
corpus, then only rebuilds chunks/vectors for changed files and removes deleted
files in one transaction. It has no `--files` partial-index option, and Git
revision/freshness validation still requires a full inventory/hash pass. Thus
one invocation avoids reprocessing unchanged file content, but does not avoid
scanning the whole indexed corpus. A Git revision change requires an index
refresh even when the commit did not alter an indexed file.

## Scope

Included Java sources, default/German/Traditional Chinese `.properties`
resources, assembly XML, launch scripts, `pom.xml`, `.classpath`, and `.project`.
Excluded local `.agents` and `.claude` skill copies, generated maps and
artifacts, help content, images, tests, and any other files outside those include
patterns.

Reproduce from the repository root with:

```powershell
$include = 'src/main/java/**/*.java,src/main/resources/**/*.properties,src/main/resources_de/**/*.properties,src/main/resources_zh_TW/**/*.properties,src/main/assembly/**/*.xml,src/main/scripts/**,pom.xml,.classpath,.project'
$exclude = 'docs/RepoMix/**,docs/repo-maps/**,docs/analysis/**,.agents/**,.claude/**,src/main/images/**,src/main/help/**,src/test/**'
npx --yes repomix@1.18.1 . --include $include --ignore $exclude --style xml --parsable-style --output docs/RepoMix/jftp-source-full.xml
npx --yes repomix@1.18.1 . --include $include --ignore $exclude --style xml --parsable-style --compress --output docs/RepoMix/jftp-source-compressed.xml
```
