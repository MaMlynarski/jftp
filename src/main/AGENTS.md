# Instructions for application source and assets

This source tree has several project-specific resource roots in addition to Java source. Apply these rules when changing code, bundles, images, or help content.

## Nonstandard resource layout

- German and Traditional Chinese bundles are kept in separate roots: `src/main/resources_de/` and `src/main/resources_zh_TW/`. They are configured as Maven resources alongside the default `src/main/resources/` tree.
- Images are loaded from `src/main/images/`, separate from the standard resource directory.
- JavaHelp metadata and pages are under `src/main/help/helpset/`; `JFTPHelp2` expects the HelpSet at the packaged `helpset/helpSet.xml` path.
- Distribution scripts and the assembly descriptor are under `src/main/scripts/` and `src/main/assembly/` and must remain consistent with packaged JAR/resource paths.

## Change rules

- When changing a UI string, keep the base bundle key aligned with Java call sites and inspect corresponding localized bundles. Record any translation gap rather than silently dropping coverage.
- When changing help IDs, update the HelpSet map and linked content. When changing images or resource paths, check the loading code and packaged artifact.
- Update `docs/resources-localization-help.md` when resource lookup, locale coverage, HelpSet integration, or image usage changes. Update `docs/build-and-dependencies.md` when Maven resource or packaging configuration changes.
- Preserve existing translations, help pages, and image assets unless the requested change explicitly covers their removal.
