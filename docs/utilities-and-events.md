# Utilities and event/listener patterns

This document summarizes the utility classes under `src/main/java/com/myjavaworld/util/` and how the event helpers are used by nearby ZIP and session code. It describes behavior visible in source. No runtime checks or tests were performed while writing it.

## Package overview

The `com.myjavaworld.util` package contains small support classes for resource bundles, file copying and change detection, progress/status/file-change events, string formatting, hex encoding, random key generation, and cached system information. It also declares a package-level description in `package-info.java`.

## Resources and common strings

`ResourceLoader` wraps `ResourceBundle.getBundle` with overloads for the default locale, an explicit locale, or an explicit class loader. If a bundle lookup throws `MissingResourceException`, it prints the exception, writes a message to standard error, and calls `System.exit(1)` (`ResourceLoader.java`). Thus missing resources are currently treated as fatal by this helper; callers generally do not get a recoverable missing-resource result. If a security manager or runtime policy prevents process exit, the post-exit return path is not a reliable recovery mechanism.

`CommonResources` loads `com.myjavaworld.util.CommonResources` once into a static field and exposes `getString(key)` (`CommonResources.java`). The bundle is selected using the default locale at class initialization. Actual bundle contents are in resource files, not this Java package.

## File helpers

`FileUtilities.copyFile(source, target)` streams bytes from a buffered input stream to a buffered output stream with a 4 KiB buffer (`FileUtilities.java`). It overwrites/creates the target through `FileOutputStream`; it does not create parent directories, preserve file metadata, or perform an atomic replacement. Both streams are closed in a `finally` block. Close failures may escape as `IOException` and may obscure an earlier exception.

`FileChangeMonitor` maintains a raw `Hashtable<File, Long>` in practice (the source uses raw types), where each value is the file's observed `lastModified()` timestamp. `add(file)` records the timestamp and lazily creates/starts a one-second `javax.swing.Timer`. On each timer action it enumerates monitored files, compares the current modification timestamp to the previous one, fires an event only when the timestamp has increased, then records the new timestamp. Listeners are stored using Swing's `EventListenerList` and invoked synchronously from the timer action. `remove(file)` removes the mapping. `stopMonitor()` stops an existing timer but does not null the timer or clear the file table.

Inferred lifecycle consequence from the code: after `stopMonitor()`, another `add(file)` will not restart the timer because the timer field remains non-null and `add` starts it only when that field is null. The monitor also does not report deletion (a missing file commonly returns timestamp zero, which is not greater than the prior timestamp), content changes that do not advance filesystem timestamp resolution, or changes whose timestamp moves backward. Runtime timer threading and filesystem timestamp resolution vary by platform; these behaviors were not exercised locally.

The application uses this monitor for temporary files opened for editing. `FTPSession` adds the downloaded temporary file when monitoring is requested, maps it to a `TransferObject`, and on a change asks whether to upload the modified local file to its remote counterpart (`jftp/FTPSession.java`, `fileChanged` and `downloadToTempFile`). Session shutdown calls `stopMonitor`. The listener callback initiates a worker for the reupload; the monitor itself does not know about FTP.

## Event and listener conventions

The event types extend `java.util.EventObject`, and listener interfaces extend `java.util.EventListener`:

| Event and listener | Payload and callback | Observed role |
| --- | --- | --- |
| `ProgressEvent`, `ProgressListener` | Integer `progress`; `progressChanged(evt)` | Used by `Zip` and `Unzip`; `FTPSession` stores the most recent progress value for its progress timer. |
| `FileChangeEvent`, `FileChangeListener` | File, old timestamp, new timestamp; `fileChanged(evt)` | Emitted by `FileChangeMonitor`; consumed by `FTPSession` for temporary-file upload prompts. |
| `StatusEvent`, `StatusListener` | String `status`; `statusChanged(evt)` | Types are defined, but a search of repository Java sources found no production emitter/registration usage. |
| `ZipEvent`, `ZipListener` | Operation type (`ZIP`/`UNZIP`) and a string file name; begin/end callbacks | Used by ZIP classes to report per-file activity; consumed by `FTPSession` to set status-bar messages. |

`Zip` and `Unzip` also keep listener registrations in `EventListenerList`, traverse its class/listener pairs, and notify listeners synchronously when progress or per-file events occur (`src/main/java/com/myjavaworld/zip/Zip.java`, `Unzip.java`). These classes and `FileChangeMonitor` use raw `EventListenerList` registrations by listener class token. The event payloads are mutable only to the extent exposed by their fields/getters; in particular, `FileChangeEvent` exposes its fields publicly as well as getters.

`ProgressEvent` stores an integer without range validation. ZIP and unzip implementations calculate a percentage from bytes processed and file/entry size. The receiving session stores that number and a Swing timer periodically displays it (`jftp/FTPSession.java`, `progressChanged`, `actionPerformed`, `beginFile`, `endFile`). These notifications are per-file operations rather than a single aggregate multi-file progress value. `StatusEvent` is currently only a data carrier plus interface, with no observed production source.

## Text, encoding, and key helpers

- `Encoder.hexEncode(byte[])` returns two uppercase hexadecimal characters per input byte (`Encoder.java`). It has no null-input guard.
- `RandomKeyGenerator.generate(length)` uses a shared `SecureRandom` and chooses from `A` through `Z`. A length below one throws `IllegalArgumentException`. Although its method comment claims it may generate digits, the actual `CHARSET` contains letters only (`RandomKeyGenerator.java`). `formatKey(key)` inserts a hyphen before each character whose zero-based index is a positive multiple of four; it does not validate input or append a trailing separator.
- `StringUtilities.getFormattedMessage(input, chars)` wraps text on spaces, with a default limit of 120 characters (`StringUtilities.java`). It tokenizes on newlines while retaining delimiters, and tokenizes long lines on spaces; consequently long-line whitespace is not preserved exactly, and an individual word longer than the configured width is not split. Null input and non-positive widths are not validated.

These are observations about the helper implementations; no calling code for the encoder, key generator, or formatter was found in the Java source search used for this documentation. Their external or resource-driven callers, if any, remain unverified.

## System information snapshot

`SystemUtil` reads OS name/version, Java version/vendor/home, user home, and canonical current working directory in a static initializer and exposes static getters (`SystemUtil.java`). Missing system properties are stored as `"Unknown"`; a failure resolving the current directory also yields `"Unknown"`. `isMac()` is set by checking whether the OS name contains `"Mac OS X"`. These values are snapshots taken when `SystemUtil` is initialized, not refreshed on each getter call. Runtime values depend on launch environment and were not verified during this source review.

## Compatibility and maintenance notes

- Several classes use raw collections and deprecated wrapper constructors such as `new Long(...)`; replacing these should preserve their behavior and avoid changing serialized or event payload contracts.
- `FileChangeMonitor` uses a Swing timer and synchronous listeners, so listener work can affect timer responsiveness. Its current session listener dispatches the actual upload via the project worker, but prompts and event processing remain tied to the notification callback path.
- Timestamp polling is not a robust content watcher. If edits need reliable detection, changing the monitoring model is a behavior change and should be covered with tests for edit, delete, rapid edits, and stop/restart lifecycle.
- `ResourceLoader` terminates the process for a missing bundle, which makes locale/resource packaging part of startup correctness. A modernization should retain a clear, tested failure policy rather than silently swallowing missing keys.
- No utility-specific tests are present in `src/test/java` at the time of writing; source behavior described here has not been verified by execution.
