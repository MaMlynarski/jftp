# Preferences and user data (current state)

This is a source-level description of user settings and favorites. Persistence behavior has not been runtime-verified.

## Storage location and preference lifecycle

`JFTP` defines the application data directory as `${user.home}/.jftp/data` (`JFTP.DATA_HOME`). Its static initialization loads a `JFTPPreferences` instance from `preferences.ser` and assigns the saved transfer-type map. If the data directory or preference file is missing, `loadPreferences()` attempts to create them and writes default preferences. The file is read and written with Java `ObjectInputStream` and `ObjectOutputStream`.

The main window saves preferences during exit after updating the saved window bounds. The preferences dialog also validates its panels, applies their changes to the shared `JFTP.prefs` object, saves it, and closes. Restore Defaults populates the panels with a new default preference object; the implementation applies those panel values when Save is pressed. See `src/main/java/com/myjavaworld/jftp/JFTP.java`, `JFTPPreferences.java`, and `PreferencesDlg.java`.

The preference object declares a `serialVersionUID`. Serialized Java data is coupled to class names and serialization compatibility; changing the preference model or package can affect existing installations. Preserve or explicitly migrate existing `preferences.ser` data when changing persistence.

## Settings represented

`JFTPPreferences` stores or exposes:

- Locale, look-and-feel class name, and theme name.
- Initial local directory, email address, and window bounds.
- FTP client implementation and remote listing parser class names.
- Connection timeout, buffer size, passive mode, proxy host/port/user/password, SSL mode and implicit SSL port, certificate-store paths/passwords, and whether the data channel is unencrypted.
- Date/time display formats and the default and extension-specific transfer types.
- Toolbar configuration, the legacy “use Java windows” setting, software-update preference, and license-agreement version/state.

Defaults are assembled in the `JFTPPreferences` constructor. They include the platform default directory, passive mode, binary as the default transfer type, a map of common text-oriented extensions to ASCII, built-in client/parser class names, disabled proxy, and enabled update checking. Some fields use nullable wrapper values to provide backward-compatible getters for missing serialized fields.

The preferences dialog uses a tree and card layout. Its panels are `GeneralConnectionPrefsPanel`, `AdvancedConnectionPrefsPanel`, `ProxyPrefsPanel`, `SecurityPrefsPanel`, `TransferModesPrefsPanel`, `LocalePrefsPanel`, `UIPrefsPanel`, and `SoftwareUpdatePrefsPanel`. Validation runs before the panels save their values. Certificate-store settings are represented by the security/certificate preferences UI; the details of certificate operations are outside this document's scope.

## Favorites

Favorites are stored in `${user.home}/.jftp/data/favorites.ser`, separately from general preferences. `FavoritesManager` ensures the data directory and file exist, then serializes a `List` of favorite/site objects. On save it attempts to encrypt the list using `SealedObject` and AES. If the AES cipher cannot be obtained, it writes the list without encryption. The AES key is a fixed byte array embedded in the source; this is obfuscation/encryption at rest, not a user-secret key-management scheme.

`Favorite` extends `RemoteHost` and is serializable/comparable. It compares favorites by name (case-insensitive for equality and uppercase string ordering for compare). The favorites manager dialog loads, sorts, adds, edits, removes, and saves favorites through `FavoritesManager`. Adding the current connection copies connection/site fields into a new favorite and checks for a duplicate before saving.

The favorites implementation has a compatibility branch for legacy files: if the deserialized object is already a `List`, it treats it as plaintext and saves it again through the current save path; otherwise it expects a `SealedObject` and decrypts it. Existing data must be tested across Java/library updates before changing serialization or cipher handling. This observation comes from source inspection; data files were not present/inspected as part of this audit.

## Compatibility and migration caveats

- `preferences.ser` and `favorites.ser` use Java native serialization. A refactor that changes serialized classes, field types, class names, or `serialVersionUID` can break existing user data.
- Some nullable fields and getter fallbacks appear designed to tolerate older preference objects. Preserve those semantics or migrate values deliberately.
- Favorites contain connection credentials via `RemoteHost`; their current encryption key is embedded in application code and shared by all installations. Do not describe this as strong credential protection.
- Certificate store paths and passwords are preferences, while the actual stores are external files. Moving the data directory or changing defaults can disconnect preferences from those files.
- `JFTP.DATA_HOME` is constructed from the home directory and a dot-directory; changing this path affects both settings and favorites.
- The source has no documented import/export or migration versioning for these files. A migration should retain backups and verify old-file loading with representative fixtures before changing formats.

## Relevant source files

- `src/main/java/com/myjavaworld/jftp/JFTP.java`
- `src/main/java/com/myjavaworld/jftp/JFTPPreferences.java`
- `src/main/java/com/myjavaworld/jftp/PreferencesDlg.java`
- `src/main/java/com/myjavaworld/jftp/FavoritesManager.java`
- `src/main/java/com/myjavaworld/jftp/FavoritesDlg.java`
- `src/main/java/com/myjavaworld/jftp/Favorite.java`
- `src/main/java/com/myjavaworld/jftp/FavoritePropertiesDlg.java`
- `src/main/java/com/myjavaworld/jftp/RemoteHost.java` (site fields; protocol/session behavior not covered here)
