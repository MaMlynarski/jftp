# User action guidance

Action classes connect menus, toolbars, dialogs, and keyboard commands to the selected session. Preserve selection requirements, enabled state, confirmation prompts, destination naming, and pane refresh behavior.

- Trace an action to the `FTPSession` method it invokes before editing it. Keep transfer and filesystem rules in the session/domain layer rather than duplicating them in UI wrappers.
- Test outcomes such as names, paths, file bytes, prompts, and refresh state; avoid tests that only assert internal calls.
- For UI-affecting changes, run the relevant action in the desktop app using available computer-use/desktop MCP tooling. Playwright is not appropriate for this Swing client.
- Open `docs/ftp-transfers-and-zip.md` when changing connection, file-operation, transfer, or archive actions. Open `docs/architecture-and-ui.md` when changing menu/toolbar wiring or session selection behavior.
- Update the relevant guide when the user-visible action flow changes.
