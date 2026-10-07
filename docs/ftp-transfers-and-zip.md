# FTP transfers and ZIP workflows

This document records the current transfer and archive behavior implemented in the repository. It is a code-oriented description, not a claim that a particular FTP server or Java runtime has been exercised. The FTP protocol implementation is referenced through `com.myjavaworld.ftp.*`, but its source is not present under `src/main/java` in this checkout; details of its wire-level behavior are therefore unverified here.

## Main components

- `com.myjavaworld.jftp.FTPSession` coordinates a connection, directory panes, local and remote file operations, transfer status, and FTP event callbacks.
- `RemoteHost` is a serializable connection profile containing host and credential fields, port, FTP client and listing parser class names, passive mode, commands, initial directories, and SSL options.
- Classes under `com.myjavaworld.jftp.actions` connect Swing actions to session methods. Most are small `ActionListener` wrappers; the session holds the transfer and filesystem operations.
- `com.myjavaworld.zip.Zip` and `Unzip` implement archive creation and extraction using `java.util.zip`.
- The worker used by the session and several actions is `com.myjavaworld.gui.SwingWorker` (a project class; not `javax.swing.SwingWorker`).

## Connection and initial browse flow

`FTPSession.connect(RemoteHost)` stores the selected profile and starts a background worker. The worker reflectively instantiates the profile's FTP client and list parser classes, sets the parser, passive mode, timeout and buffer size from preferences, SSL mode, and data-channel encryption option. If SSL is enabled, it obtains an `SSLContext` from `JFTPSSLContext`. It registers the session as control-connection, data-connection, and FTP-connection listener; connects using the configured host and either the regular port or implicit-SSL port; and logs in with user, password, and account fields. It then sends configured post-login commands, optionally changes to the initial remote directory, gets the working directory, and lists its contents.

Source: `src/main/java/com/myjavaworld/jftp/FTPSession.java` (`connect`, approximately lines 593–697); profile fields/defaults are in `src/main/java/com/myjavaworld/jftp/RemoteHost.java`.

The session's FTP callbacks write command/reply/status messages into the status window, reflect secure state in the status bar, and reset the remote pane and transfer indicators when a connection closes or drops. Directory changes run through a background worker, update the server's working directory, retrieve the current directory and list, then update the remote pane. Local directory listing is performed through `LocalFile` and the local filter. Remote listing uses the selected `ListParser` and remote filter.

**Unverified boundary:** the source for `FTPClient`, its default implementation, and `ListParser` is not present in this checkout's Java source tree. The exact FTP command sequence, passive-mode negotiation details, TLS negotiation, transfer restart semantics, and behavior across server implementations cannot be established from `FTPSession` alone. The classes are referenced from `com.myjavaworld.ftp.*` and default class names are recorded in `RemoteHost`.

## File transfer behavior

The Upload and Download actions check that a current connected session exists, then call `FTPSession.upload()` or `download()`. These methods take the selected local or remote files, respectively, and process them in a worker. The session checks connection and abort state between selected items. Files are transferred through the FTP client; directories are traversed recursively. A download creates a local target directory for a remote directory and lists its children. An upload creates a corresponding remote directory, lists local children, and recurses. Dot entries `.` and `..` are skipped in these recursive paths.

Transfer type is chosen by file extension when automatic detection is enabled. The session looks up the extension in configured transfer types and falls back to the configured default; with auto-detection disabled it uses the session's selected transfer type. The selected type is passed to the FTP client's `download` or `upload` method. Progress and status are surfaced through session listeners and status-bar timers.

Source: `src/main/java/com/myjavaworld/jftp/FTPSession.java` (`getTransferType`, `download`, `downloadDataFile`, `upload`; approximately lines 208–233 and 707–969). The transfer actions are `actions/DownloadAction.java` and `actions/UploadAction.java`.

`DownloadAsAction` and `UploadAsAction` use the same recursive transfer helpers for a selected file and a caller-provided target name. Remote and local create, rename, and delete actions delegate to corresponding `FTPSession` methods. Recursive delete is implemented in the session, separately from the transfer path.

## Temporary downloads and edit monitoring

`FTPSession.downloadToTempFile` downloads a remote file into a Java temporary file whose suffix is based on the source extension. It chooses the transfer type using the same extension preference logic. When requested, it registers the temp file with `FileChangeMonitor` and associates it with a `TransferObject` recording the local file, remote file, and upload direction. `fileChanged` asks the user whether to upload the changed temp file; an affirmative answer starts a worker to upload it and refresh the remote pane.

`FileChangeMonitor` uses a Swing `Timer` with a one-second interval and compares each monitored file's `lastModified()` value with its previous value. It fires a change event when the value increases. It does not compare file contents. Source: `src/main/java/com/myjavaworld/jftp/FTPSession.java` (`downloadToTempFile`, `fileChanged`; approximately lines 153–197 and 1558–1600), `src/main/java/com/myjavaworld/jftp/TransferObject.java`, and `src/main/java/com/myjavaworld/util/FileChangeMonitor.java`.

## ZIP and upload workflow

`ZipAndUploadAction` requires a connected session and at least one selected local file. After the dialog accepts the operation, it creates a `Zip` for the chosen output file, attaches the session as ZIP and progress listener, applies the session's local-file filter, and sets the local working directory as the archive-relative base. It adds each selected file; adding a directory recursively adds its filtered children. Once the ZIP is closed, the action uploads it under the requested remote name. The local ZIP is deleted only when the user selected that option. The action refreshes both panes afterward.

`Zip` writes standard Java ZIP entries, gives entries the source file's modification time, copies file data in 16 KiB chunks, and emits begin/end and progress events. Directory entries end with `/`. The archive-relative entry name is computed by removing the configured base path prefix from the file's canonical path, removing an initial separator, and changing platform separators to `/`.

Sources: `src/main/java/com/myjavaworld/jftp/actions/ZipAndUploadAction.java`; `src/main/java/com/myjavaworld/zip/Zip.java`.

## Download and unzip workflow

`DownloadAndUnzipAction` requires a connected session, a selected remote file, and a `.ZIP` extension (case-insensitive). After dialog approval, a worker downloads the remote file to the selected local archive path, opens it with `Unzip`, sets the selected extraction directory, attaches ZIP/progress listeners, extracts entries, closes the archive, and optionally deletes the downloaded archive. The local pane is refreshed when the worker finishes.

`Unzip` reads entries with `java.util.zip.ZipFile`. It creates directory entries with `mkdirs`; for file entries it creates missing parent directories and copies bytes in 16 KiB chunks. The current implementation constructs each destination as `new File(targetDirectory, entry.getName())` without checking that its canonical path stays under `targetDirectory`. This is an observed path-handling gap with a security consequence: a crafted archive entry using parent traversal may write outside the chosen extraction directory. The action and extractor currently do not expose a separate safe-extraction policy.

Sources: `src/main/java/com/myjavaworld/jftp/actions/DownloadAndUnzipAction.java`; `src/main/java/com/myjavaworld/zip/Unzip.java`.

## Known behavior and risks to account for during modernization

- The ZIP entry-name calculation assumes the input file path begins with the configured relative base path. It uses `substring` without checking that prefix or a path-component boundary; out-of-base inputs may produce incorrect names or an index error. (`Zip.computeEntryName`.)
- ZIP extraction does not normalize and constrain entry paths to the selected output directory. Treat extraction of untrusted archives as unsafe until guarded and regression-tested.
- `Unzip` fires its end-file event with the archive `file` field, while its begin-file event receives the extracted target. This is the current event behavior; listeners may observe an inconsistent file name.
- File monitoring observes increasing modification times only. Same-timestamp edits and file deletion are not detected by the current comparison.
- There are no implemented tests in `src/test/java` at the time this document was written; that directory contains only `.gitkeep`. The behaviors above have been read from source, not verified by running the app or a test suite.

## Candidate behavior-level regression coverage

These are proposed test scenarios, not existing tests:

1. Upload and download a nested directory tree containing text, binary bytes, and an empty file; compare names, hierarchy, and byte contents.
2. Upload and download a selected file under an alternate destination name; verify content and source preservation.
3. Zip a selected nested tree relative to the local working directory, then unzip into an empty directory and compare extracted paths and contents; include filter behavior and timestamps where the platform preserves them.
4. Extract a crafted archive containing `../` and absolute-path entries; verify no file is written outside the selected destination after path containment is added.
