# Current-state overview

## Purpose

JFTP is a Java desktop FTP client with a Swing interface. Its documented user-facing areas include managing connection sessions, browsing local and remote files, transferring files, using favorites, and configuring connection and interface preferences. The repository also contains SSL-related UI and code, ZIP upload/download workflows, JavaHelp content, and localized interface resources.

This page records the repository before modernization. It is based on static inspection and the project README; actual compilation, packaging, and interactive behavior have not been verified in this documentation pass.

## Application shape

The desktop launch class is `com.myjavaworld.jftp.JFTPApplication`. It creates the main window and opens a session. `JFTP` is the top-level window and coordinates menus, toolbar, and session tabs. A session combines local and remote panes and delegates connection, browsing, and transfer work to `FTPSession`. Many menu and toolbar commands are implemented as actions under `com.myjavaworld.jftp.actions`.

The interface is Swing-based and uses project-specific components in `com.myjavaworld.gui`, including a custom `SwingWorker` implementation and common frame/dialog behavior. `JFTPApplet` remains as a separate legacy launch path.

The FTP client and parser APIs are referenced through `com.myjavaworld.ftp.*` types supplied by the declared `com.myjavaworld:ftpapi` dependency; their implementation is not present in this repository's Java source tree. Protocol behavior therefore depends on that external library as well as the application's orchestration code.

## Repository map

| Area | Contents |
|---|---|
| `pom.xml` | Maven project, dependencies, plugins, repositories, and packaging configuration. |
| `src/main/java/com/myjavaworld/jftp` | Application bootstrap, Swing window/session UI, preferences, and FTP orchestration. |
| `src/main/java/com/myjavaworld/jftp/actions` | User commands wired to session and file operations. |
| `src/main/java/com/myjavaworld/jftp/ssl` | SSL context, trust and key managers, certificate management UI. |
| `src/main/java/com/myjavaworld/gui` | Shared Swing controls, rendering, themes, window helpers, and custom worker. |
| `src/main/java/com/myjavaworld/util` | File, resource, status/progress, encoding, and monitoring utilities. |
| `src/main/java/com/myjavaworld/zip` | ZIP creation and extraction helpers used by archive workflows. |
| `src/main/resources*` | Default and localized property bundles. |
| `src/main/images` | Application icons and image assets. |
| `src/main/help/helpset` | JavaHelp metadata and HTML help pages. |
| `src/main/assembly` and `src/main/scripts` | Distribution assembly descriptor and launch scripts. |

The static review found no implemented test cases under `src/test`; only placeholder `.gitkeep` files were present. This should be checked again when characterization tests are introduced.

## Important current-state boundaries

- The project is a desktop Swing application; the applet path is legacy and is not the desktop entry point.
- `FTPSession` coordinates operations, but FTP client and parser implementation details live in an external dependency.
- User preferences and favorites are stored as serialized Java objects under the user's `.jftp/data` directory. Their serialized format is a compatibility concern for upgrades.
- Resource bundles, help IDs, images, assembly contents, and UI classes are linked by names and paths; packaging changes need to preserve those relationships.
- SSL trust decisions are implemented by application code and are security-sensitive. They should be understood and explicitly reviewed before behavior is changed.

## Behavior areas for later characterization

These are candidate user-visible workflows for tests before refactoring:

1. Connect to a controlled FTP server, browse and refresh a directory, then disconnect and reconnect.
2. Upload and download representative files and nested directories, checking resulting names, paths, and byte contents.
3. Save and reload preferences and favorites, checking that settings and connection entries remain available.
4. Create, transfer, and extract an archive through the ZIP workflows, checking the resulting directory structure and file contents.

These workflows have not been tested yet. The later test design should use observable outcomes rather than depending on specific internal calls. ZIP extraction also has a path-containment security concern documented separately; any correction should be treated as an explicit security decision.
