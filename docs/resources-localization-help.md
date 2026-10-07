# Resources, localization, and help (current state)

This document describes source and resource layout as inspected in the repository. Bundle selection, HelpSet loading, and packaging were not runtime-verified.

## Resource lookup

Most UI classes obtain text from `ResourceBundle` instances through the project helper `com.myjavaworld.util.ResourceLoader`. Base English/default bundles are under `src/main/resources/com/myjavaworld/`. For the application UI, the main set is `src/main/resources/com/myjavaworld/jftp/*.properties`; shared GUI bundles are under `src/main/resources/com/myjavaworld/gui/`; common labels and messages are under `src/main/resources/com/myjavaworld/util/CommonResources.properties`.

Localized resource roots found in the repository include `src/main/resources_de/` and `src/main/resources_zh_TW/`. They mirror many of the `jftp`, `gui`, and `util` bundle names with language/locale suffixes, for example `JFTP_de.properties` and `JFTP_zh_TW.properties`. `JFTPApplication` sets the process default locale from the saved preference before creating `JFTP`, and the applet's static initializer does likewise. `LocalePrefsPanel` is the settings UI for locale selection.

Bundle keys are coupled to Java call sites. Adding, renaming, or deleting keys should be checked against all locale bundles; some locale-specific files may not contain every key present in the default bundle. The existence of bundle files alone does not prove every locale selection works.

## UI text and visual assets

Bundle naming generally follows the Java class name: for example, `LocalPane` loads `com.myjavaworld.jftp.LocalPane`, and `PreferencesDlg` loads its corresponding bundle. Menus, dialogs, status widgets, table models, and preference panels each have their own bundle. Icons and images are loaded by `JFTPUtil` from the image resources. `JFTPConstants` contains product identity/version strings, while user-facing labels/messages are predominantly bundle-based.

When changing resources, preserve base bundle names and locale suffix conventions. Verify keys used by Java sources and the help metadata, and retain expected icon resource paths.

## JavaHelp help system

Help content is in `src/main/help/helpset/`. The HelpSet descriptor is `helpSet.xml`, with associated map, table-of-contents, index, and glossary XML files. HTML pages are grouped by subject areas such as `connect`, `userInterface`, `security`, `transfer`, `local`, `remote`, and `sessions`; screenshots and license/credits pages are also present.

`JFTPHelp2` is a lazy singleton. It calls JavaHelp `HelpSet.findHelpSet` for `helpset/helpSet.xml`, constructs a `HelpSet`, creates a broker with the ID `main window`, and provides methods that bind help buttons and keys to help IDs. `PreferencesDlg` binds the `preferences` help ID; other dialogs and menus also call these helpers. Help ID definitions and target pages are in the help-set map/content files, so ID changes need coordinated updates.

The loader catches `HelpSetException` when creating the HelpSet but then uses the HelpSet to create a broker. The source does not establish how a missing or malformed HelpSet behaves beyond that point; verify this path if help loading is refactored.

## Build/package boundary to verify later

This audit did not inspect the build configuration or run a packaged application. A later packaging review should confirm that `src/main/help/helpset/` is included at the classpath location expected by `JFTPHelp2`, all base and localized `.properties` files are copied, and image resources remain available through the paths used by `JFTPUtil`. The JavaHelp `javax.help` API also requires a compatible dependency/runtime packaging arrangement; its actual configured version is documented separately in the dependency inventory.

## Relevant source/resource locations

- `src/main/java/com/myjavaworld/jftp/JFTPApplication.java` — desktop locale initialization.
- `src/main/java/com/myjavaworld/jftp/JFTPApplet.java` — applet locale initialization.
- `src/main/java/com/myjavaworld/jftp/JFTPHelp2.java` — HelpSet and HelpBroker integration.
- `src/main/java/com/myjavaworld/jftp/LocalePrefsPanel.java` — locale preference UI.
- `src/main/java/com/myjavaworld/jftp/JFTPUtil.java` — image/resource helpers.
- `src/main/resources/com/myjavaworld/jftp/`, `src/main/resources/com/myjavaworld/gui/`, and `src/main/resources/com/myjavaworld/util/` — default bundles.
- `src/main/resources_de/` and `src/main/resources_zh_TW/` — localized bundle trees.
- `src/main/help/helpset/` — JavaHelp metadata, content, and screenshots.
