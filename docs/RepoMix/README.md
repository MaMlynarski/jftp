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
