# Shared Swing component guidance

This package includes custom Swing controls, documents, renderers, themes, busy glass panes, and a project-specific `SwingWorker`. Several wrappers add behavior beyond their Swing superclass, including mnemonics, text limits, popup placement, focus/selection, and close handling.

- Preserve EDT rules and characterize worker construction, completion callbacks, error propagation, cancellation, and busy-state cleanup before replacing the custom worker.
- Preserve keyboard/focus behavior, selection, popup triggers, localization mnemonics, and theme names/class mappings.
- Clipboard, display, and multi-monitor behavior may depend on a graphical environment; report when such checks cannot run.
- Use automated behavior tests first, then exercise visible changes in the real desktop app with available computer-use/desktop MCP tooling. Do not use browser-only Playwright for Swing UI.
- Open `docs/gui-components.md` for custom component contracts and `docs/architecture-and-ui.md` for how the app uses them. Update the relevant guide when a contract changes.
