# Application architecture and UI (current state)

This document records the application and Swing UI structure as found in the repository audit. It describes the code paths; the behavior has not been verified by running the application.

## Startup and application shell

The desktop entry point is `com.myjavaworld.jftp.JFTPApplication.main`. Construction of `JFTPApplication` applies macOS menu properties and registers an `OSXAdapter` on macOS, selects the saved locale and look and feel, constructs the main `JFTP` window, shows it, and opens a new session. Locale and look-and-feel setup failures are silently ignored. See `src/main/java/com/myjavaworld/jftp/JFTPApplication.java` and `JFTP.java`.

`JFTP` extends the project wrapper `MFrame` and is the top-level application coordinator. It builds a menu bar from `FTPMenu`, `LocalSystemMenu`, `RemoteSystemMenu`, `TransferModeMenu`, `ToolsMenu`, and `HelpMenu`; creates `JFTPToolBar`; and hosts session components in a tabbed pane. Most window-level commands resolve the selected tab through `getCurrentSession()` and then call the selected `FTPSession`. A new session creates a fresh `FTPSession` tab. Session titles are changed to the saved favorite/site name, or the host name when the name is blank, after connection-state changes.

The main window also handles preference and favorite entry points, file filtering and selection commands, remote/local properties dialogs, certificate-manager launch, and transfer-mode selection. A number of menu and toolbar commands are delegated to classes in `src/main/java/com/myjavaworld/jftp/actions/` (outside this UI audit's scope).

`JFTPApplet` is a second launch path: it displays a launch button and creates an applet-mode `JFTP` window when pressed. Its class directly extends `JApplet`. The applet path is present in source; it was not exercised. `JFTPConstants` identifies the product as JFTP 5.0.1, build 20120623.

## Session composition and UI data flow

`FTPSession` extends `SessionPanel`, which is a `JRootPane` with a glass pane and a session title. Each session creates:

- `LocalPane`, a local filesystem browser with root and working-directory selectors, a sortable table, selection/status display, context menus, and drag-and-drop wiring.
- `RemotePane`, a remote listing browser with a working-directory selector, sortable table, selection/status display, context menus, and drag-and-drop wiring.
- `StatusWindow` and `StatusBar`, placed with the panes in nested split panes.

The session initializes the local working directory from preferences, falling back to the platform's default directory if that value is missing or not a directory. Pane selection changes cause the session/application toolbar state to update. Directory navigation and refresh requests route from each pane to the session; the session obtains/updates pane data. FTP connection and protocol details are intentionally not described here.

Session background operations use `com.myjavaworld.gui.SwingWorker`, a project-defined worker abstraction that runs `construct()` on a new thread and schedules `finished()` on Swing's event-dispatch thread. `SessionPanel.setBusy` shows or hides `MGlassPane`, whose listeners consume mouse and keyboard events while visible. The source structure implies this is intended to prevent UI interaction during selected operations; actual coverage and responsiveness were not runtime-verified.

The window has standard file-transfer, local-file, remote-file, tools, transfer mode, and help menus. Local and remote pane tables register keyboard actions for Enter and Delete, and use table models and renderers to represent files, dates, sizes, and sort direction. The menu classes update command enabled state based on current session state and selection. See `LocalPane.java`, `RemotePane.java`, `LocalFileTableModel.java`, `RemoteFileTableModel.java`, `LocalSystemMenu.java`, `RemoteSystemMenu.java`, and `JFTPToolBar.java`.

## Shared Swing components

`src/main/java/com/myjavaworld/gui/` contains custom subclasses and helpers used across the app. These include window/dialog wrappers (`MFrame`, `MDialog`, `MInternalFrame`), buttons, labels, menus, tables, lists, trees, text fields, document classes, renderers, `GUIUtil`, and the busy glass pane/worker. The package also defines Metal look-and-feel themes: default, green, sandstone, high contrast, and large-font variants. `JFTP` maps display names to theme class names; theme application is managed in the UI preferences code.

Several UI components are legacy implementations rather than adapters around newer framework APIs. In particular, the custom `SwingWorker` predates `javax.swing.SwingWorker`; modernization should characterize worker lifecycle, cancellation, error handling, and EDT callbacks before replacing it.

## Shutdown and window behavior

When the main window closes, `JFTP.exit()` closes each session, saves window bounds to the preferences object, attempts to save preferences, disposes the frame, and calls `System.exit(0)` in desktop mode. Applet mode skips `System.exit`. When no stored window bounds exist, the frame uses most of the screen and is maximized on window open. The source also starts `AutoUpdater` on window open when the saved setting enables update checks.

## Modernization observations

- `JApplet` in `JFTPApplet` is not available in modern Java releases. The standalone desktop entry point is separate, so applet removal or replacement should be treated as an explicit scope decision.
- `JFTPHelp2` depends on JavaHelp classes in `javax.help`; library version, compatibility, and packaging should be verified during build modernization.
- `GUIUtil` calls `Toolkit.getMenuShortcutKeyMask()` and uses older input modifier masks. These APIs should be checked for deprecation/removal against the selected Java baseline.
- The code uses raw collections and explicit wrapper constructors in multiple UI classes. Those are modernization candidates, but changes should be behavior-preserving.
- This document is source-derived. No build, test, or GUI launch was run as part of this audit.
