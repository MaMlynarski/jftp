# Shared GUI components (current state)

This guide describes `src/main/java/com/myjavaworld/gui/` from source inspection. It is not a visual or runtime verification of the UI.

The package provides a collection of Swing extensions and helpers used throughout JFTP. Most `M*` controls are thin subclasses of standard Swing components. They keep the application on a project-specific component vocabulary and add a few behaviors such as mnemonic parsing, default renderers, popup placement, input masking, and text-document constraints. Some additions are behavior-bearing; replacing these classes with stock Swing controls wholesale could change user-visible behavior.

## Windows, busy state, and progress

- `MFrame` extends `JFrame`, installs a content pane with configurable insets, and owns an `MGlassPane`. Its `setBusy(boolean)` changes the cursor and shows/hides the glass pane.
- `MDialog` extends `JDialog`, sets `DO_NOTHING_ON_CLOSE`, installs an Escape-key action, and defaults to hiding the dialog on Escape or window close. Its `escape()` method is overridable.
- `MInternalFrame` extends `JInternalFrame`, enables the standard internal-frame controls, and adds a busy glass pane. When the busy pane receives a mouse press, its specialized inner pane moves the internal frame to front and selects it before consuming the event.
- `MDesktopPane` adds cascade and horizontal/vertical tile operations over visible, non-iconified internal frames.
- `MGlassPane` consumes mouse and key events and exposes normal and wait cursors. `SessionPanel` and `FTPSession` use this busy-state pattern around session work; the main frame also provides `setBusy` for callers.
- `ProgressDialog` wraps a `JProgressBar`, message label, and disabled-by-default Cancel button. It exposes progress, bounds, indeterminate state, and cancellation-listener APIs. The dialog itself does not implement cancellation logic.
- `SplashWindow` centers an icon in a small window when shown. Its documentation mentions blocking for a display time, but the inspected implementation of `setVisible` only positions and displays it. JFTP's splash-window construction is commented out in `JFTPApplication`.

The event-blocking behavior while busy and progress/cancel lifecycle have not been exercised at runtime.

## Common controls and text editing

The package contains Swing subclasses for buttons, check boxes, radio buttons, labels, combo boxes, lists, menu items, menus, radio menu items, popup menus, scroll panes, tables, and trees. The simple wrappers mostly forward standard constructors. Many expose string-based mnemonic setters because UI text and mnemonic positions are read as strings from resource bundles; mnemonic decoration is skipped by selected overloads on macOS. `MComboBox` also provides helpers to repopulate items from an array or `Vector`.

`MMenu` and `MPopupMenu` override `add(Action)` to create an `MMenuItem` and remove its icon. `MPopupMenu.show` estimates popup size and moves it left/up when it would cross the screen's right or lower edge. Its positioning uses the primary toolkit screen dimensions; multi-monitor placement was not tested.

Text components share `MTextComponent`, which defines a common editing contract: case mode, maximum length, clipboard operations, selection, undo/redo, and capability checks. `MTextField`, `MTextArea`, `MPasswordField`, and `MLabelTextField` implement this interface with different behavior:

- `MPlainDocument` limits inserted text to a maximum length and can normalize inserted characters to upper or lower case.
- `SingleLineDocument` truncates inserted or pasted input at the first carriage return or line feed.
- `MTextField` uses `SingleLineDocument`, adds an `UndoManager` with a default limit of one edit, selects all on focus gain, clears selection on focus loss, and opens the shared edit popup on platform popup triggers.
- `IntegerField` uses a specialized single-line document to reject non-integer edits (while allowing a lone minus sign as an intermediate value); `getValue()` parses the current text.
- `MTextArea` uses `MPlainDocument` and the same style of context edit popup and one-edit undo manager.
- `MPasswordField` uses `SingleLineDocument`, reports cut/copy as unavailable, and leaves undo/redo unsupported. Its `canPaste()` still checks the system clipboard.
- `MLabelTextField` is configured as transparent and non-editable, while retaining the shared text API.
- `EditPopupMenu` supplies text editing commands and checks their enabled state through the `MTextComponent` contract.

These document and clipboard behaviors are part of the UI contract. The clipboard implementation uses AWT's system clipboard, whose availability can vary in headless environments; no headless behavior was tested.

## Tables, renderers, and icons

`MTable` sets `MTableHeaderRenderer` as the default header renderer, computes row height from the current table font, and customizes popup-trigger handling. A context click on a row preserves that row if it was already selected, otherwise selects it; a click on empty table space clears selection. `LocalPane` and `RemotePane` use this behavior in their file tables.

Shared renderer classes include:

- `MTableCellRenderer` and `MDefaultRenderer` for general text values, with selection colors and padding.
- `MTableHeaderRenderer` for centered headers, UIManager header colors/borders, and optional icons. Local and remote panes use sort-direction icons in these renderers.
- `DateCellRenderer` for locale-formatted date/time values and `NumericCellRenderer` for right-aligned locale-formatted numbers.
- `ImageCellRenderer`, which can render text and an icon for list, table, or tree cells.
- `IndentIcon`, which adds depth-based horizontal spacing for left-to-right directory-combo rendering.

`JFTP` and the pane classes register renderers by model value type, so model column classes and renderer selection are coupled. `ImageCellRenderer` and table renderers read some UI defaults statically at class initialization; changing look and feel or theme application order may affect resulting colors. That visual effect is an inference from the implementation and needs runtime verification.

## Look and feel themes

The package defines Metal themes based on `DefaultMetalTheme`:

- `DefaultTheme` supplies Dialog fonts and baseline theme behavior.
- `GreenMetalTheme`, `SandstoneTheme`, and `HighContrastTheme` override primary/secondary colors.
- `DefaultLargeTheme`, `GreenMetalLargeTheme`, `SandstoneLargeTheme`, and `HighContrastLargeTheme` override font sizes/styles to provide large-text variants.

`JFTP` holds a display-name-to-theme-class map, and `UIPrefsPanel` is the user-facing theme preference surface. Theme class names therefore form a string-based integration point: a renamed or removed theme class requires updating the map and considering saved preference values.

## Utility classes

- `GUIUtil` provides screen centering, look-and-feel checks, platform-specific help/delete key choices, JOptionPane wrappers, and simple HTML formatting for messages. It uses `Toolkit.getMenuShortcutKeyMask()` and older modifier-mask constants, which should be checked against the selected modern Java baseline.
- `IDTreeNode` adds an integer ID to a tree node; `PreferencesDlg` uses it to map selected tree sections to CardLayout names.
- `LicenseAgreementDlg` renders a license URL and records agreement through its dialog API.
- `MOptionPane` overrides maximum characters per line to a fixed value.
- `DateCellRenderer`, `NumericCellRenderer`, `ImageCellRenderer`, `MDefaultRenderer`, `MTableCellRenderer`, and `MTableHeaderRenderer` are shared by application panes and dialogs.

## Coupling points and modernization notes

1. **Resource strings and mnemonics:** UI components expose setters that accept mnemonic characters and indexes as strings. Their callers and the `.properties` bundles must move together if the API changes. Check all default and localized bundles when changing these setters or keys.
2. **Theme names and serialized preferences:** Theme selection is stored as a string and looked up through the map in `JFTP`. Preserve aliases or migrate saved values if names/class paths change.
3. **Busy state and worker callbacks:** `MGlassPane`, `MFrame`, `MInternalFrame`, and `SessionPanel` share the notion of busy state. Session operations use the project's custom `SwingWorker`, not `javax.swing.SwingWorker`.
4. **Raw Swing model APIs:** The wrappers and older callers use raw `Vector`, `ListModel`, `ComboBoxModel`, and table models. Generic type improvements should preserve existing model/rendering behavior.
5. **Swing event thread assumptions:** The custom `SwingWorker` runs `construct()` on a new `Thread`, then posts `finished()` with `SwingUtilities.invokeLater`. It does not itself capture or propagate exceptions from `construct()`; uncaught failures can skip the completion callback because scheduling occurs after the `try/finally`. This is source-derived, not runtime-tested. Preserve or intentionally change this lifecycle only with characterization coverage.
6. **Legacy UI surface:** `MDesktopPane` and `MInternalFrame` supply MDI helpers, while the main `JFTP` shell uses a tabbed pane. Their presence in the package does not establish that they are part of the current primary workflow.

## Source map

- Window and status components: `MFrame.java`, `MDialog.java`, `MInternalFrame.java`, `MDesktopPane.java`, `MGlassPane.java`, `ProgressDialog.java`, `SplashWindow.java`.
- Controls and editing: `MButton.java`, `MCheckBox.java`, `MComboBox.java`, `MLabel.java`, `MList.java`, `MMenu.java`, `MMenuItem.java`, `MOptionPane.java`, `MPopupMenu.java`, `MRadioButton.java`, `MRadioButtonMenuItem.java`, `MScrollPane.java`, `MTree.java`, `MTextComponent.java`, `MTextField.java`, `MTextArea.java`, `MPasswordField.java`, `MLabelTextField.java`, `MPlainDocument.java`, `SingleLineDocument.java`, `IntegerField.java`, `EditPopupMenu.java`.
- Tables and rendering: `MTable.java`, `MDefaultRenderer.java`, `MTableCellRenderer.java`, `MTableHeaderRenderer.java`, `DateCellRenderer.java`, `NumericCellRenderer.java`, `ImageCellRenderer.java`, `IndentIcon.java`.
- Themes: `DefaultTheme.java`, `DefaultLargeTheme.java`, `GreenMetalTheme.java`, `GreenMetalLargeTheme.java`, `SandstoneTheme.java`, `SandstoneLargeTheme.java`, `HighContrastTheme.java`, `HighContrastLargeTheme.java`.
- Utilities and help/license dialogs: `GUIUtil.java`, `IDTreeNode.java`, `LicenseAgreementDlg.java`.
