# JFTP project documentation

This documentation records the repository's current state as inspected on 2026-10-06, before application modernization. It is based on a static review; no build or application launch was performed for this snapshot.

## Current-state guides

- [Project overview](current-state-overview.md) — purpose, high-level architecture, repository layout, and known boundaries.
- [Repo Map](jftp-repomap.md) — compact generated index of source files and declarations; start here for navigation.
- [RepoMix packs and local Context7 search](RepoMix/README.md) — full and structurally compressed snapshots, plus local source retrieval setup.
- [Build and dependencies](build-and-dependencies.md) — Maven configuration, dependency and plugin versions, launch entry point, packaging, and build risks.
- [Architecture and UI](architecture-and-ui.md) — startup, windows, session composition, menus, panes, and shared Swing components.
- [Shared GUI components](gui-components.md) — custom Swing controls, renderers, themes, busy-state handling, and worker lifecycle.
- [Utilities and events](utilities-and-events.md) — support utilities, progress/status events, and file-change monitoring.
- [Preferences and user data](preferences-and-user-data.md) — preference and favorites persistence and migration-sensitive behavior.
- [Resources, localization, and help](resources-localization-help.md) — resource bundles, images, locale variants, and JavaHelp content.
- [FTP transfers and ZIP](ftp-transfers-and-zip.md) — connection and transfer orchestration, actions, and archive workflows.
- [Security and SSL](security-and-ssl.md) — certificate, trust, key store, and TLS behavior, with security-sensitive observations.

## How to read these documents

These pages describe behavior and structure found in the current source tree. They are not a modernization specification. Items marked as risks or unverified need confirmation during later build and behavior checks. Dependency versions and configuration are reported as declared in the repository, not as proof that artifacts remain available or that the project currently builds.

During modernization, update the affected current-state page when code, dependencies, persistence, startup, packaging, or user-visible behavior changes. Once a page describes the migrated state rather than the original snapshot, update its introduction and this index accordingly. Keep behavior changes, compatibility decisions, and unresolved questions explicit.
