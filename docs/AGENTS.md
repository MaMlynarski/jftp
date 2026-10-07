# Documentation guidance

All repository documentation is written in English. Keep descriptions source-grounded and distinguish observed implementation, inferred behavior, verified results, open risks, and proposed decisions.

Open and update documentation by trigger:

- `docs/current-state-overview.md` — when broad ownership, startup, or repository boundaries need orientation.
- `docs/build-and-dependencies.md` — before changing Java compatibility, Maven, dependency resolution, launch scripts, or packaging.
- `docs/architecture-and-ui.md` — when startup, sessions, panes, menus, dialogs, or UI workflows change.
- `docs/preferences-and-user-data.md` — when settings, favorites, profiles, or serialized data change.
- `docs/resources-localization-help.md` — when bundles, translations, images, JavaHelp, or resource packaging change.
- `docs/ftp-transfers-and-zip.md` — when connection, file operations, transfers, actions, or ZIP behavior change.
- `docs/security-and-ssl.md` — when TLS, trust decisions, certificate stores, or extraction security changes.
- `docs/gui-components.md` — when custom Swing component or worker contracts change.
- `docs/utilities-and-events.md` — when shared helpers, events, or file monitoring change.
- `docs/jftp-repomap.md` — for generated source-symbol navigation; regenerate after significant source-structure changes, and do not use as a behavior specification.

Update `docs/README.md` when adding, renaming, or removing a guide. Do not claim tests, builds, packaging, or manual QA passed unless they actually ran.
