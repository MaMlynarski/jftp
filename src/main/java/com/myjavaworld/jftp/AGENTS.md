# JFTP application guidance

This package contains desktop startup (`JFTPApplication`), the main window (`JFTP`), session/pane coordination (`FTPSession`, `SessionPanel`, `LocalPane`, `RemotePane`), connection profiles, preferences, favorites, menus, and dialogs.

## Project-specific behavior boundaries

- `FTPSession` coordinates application behavior, but FTP client and listing parser implementations are external. Do not infer protocol-level behavior from this package alone.
- Connection profiles persist FTP client and parser implementation class names. Preserve compatibility with those names when changing reflection or profile handling.
- Preferences and favorites use Java serialization below `${user.home}/.jftp/data`. Preserve existing data or provide an explicit, fixture-tested migration.
- `JFTPApplication` is the desktop entry point. `JFTPApplet` is a separate legacy applet path; do not remove or redefine its support status as incidental cleanup.
- Session work uses the project's custom Swing worker. Preserve background execution, EDT callbacks, cancellation, and busy-state cleanup unless a change is deliberate and tested.

## Tests and documentation triggers

- Before changing session, pane, preference, favorite, or startup behavior, define the user-visible outcome and add or update tests before production changes.
- Open `docs/architecture-and-ui.md` when changing application startup, session composition, panes, menus, or dialogs.
- Open `docs/preferences-and-user-data.md` when changing connection profiles, favorites, preferences, or persistence.
- Open `docs/current-state-overview.md` when the cross-package ownership/data flow is unclear.
- Update the triggered guide when architecture or observable behavior changes. Use a real desktop check for UI/runtime changes when the application and desktop automation are available.
