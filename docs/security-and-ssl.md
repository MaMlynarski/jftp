# Security and SSL behavior

This document describes the current FTPS certificate and key-store code and identifies security and Java compatibility concerns visible in the repository. It does not establish which TLS protocol versions or cipher suites work with a given server. The underlying FTP client implementation is not present in this repository's Java source tree, so the way it consumes the configured `SSLContext` is unverified here.

## FTPS configuration and SSL context

Connection profiles (`RemoteHost`) store an SSL usage integer, whether the data channel may be unencrypted, and an implicit-SSL port. Defaults are no SSL, data channel encryption required (`dataChannelUnencrypted == false`), and the FTP library's default implicit SSL port. When `FTPSession.connect` sees SSL enabled, it asks `JFTPSSLContext` for a context scoped to the configured host name and passes that context to the FTP client. For implicit SSL, the session selects the configured implicit port; otherwise it uses the profile's normal port.

`JFTPSSLContext.getSSLContext` requests `SSLContext.getInstance("SSL")`, then initializes it with one `JFTPKeyManager` and one `JFTPTrustManager` (`src/main/java/com/myjavaworld/jftp/ssl/JFTPSSLContext.java`). The source does not explicitly set enabled protocol versions or cipher suites. **Inference:** the effective protocol negotiation therefore depends on the active Java security provider and the absent FTP client implementation's socket setup.

Sources: `src/main/java/com/myjavaworld/jftp/RemoteHost.java` (SSL fields/defaults), `src/main/java/com/myjavaworld/jftp/FTPSession.java` (`connect`), and `src/main/java/com/myjavaworld/jftp/ssl/JFTPSSLContext.java`.

## Server certificate validation and user approval

`JFTPTrustManager` constructs a `TrustManagerFactory` using the provider-specific algorithm name `SunX509`, initializes it with the application's server-certificate JKS store, and retains the first `X509TrustManager`. The trust manager delegates `checkClientTrusted` and `getAcceptedIssuers` to that delegate. For server certificates, however, `checkServerTrusted` does not call the delegate's `checkServerTrusted` method. Instead, the current code:

1. Returns early if the presented chain is equal to the chain previously accepted by this trust-manager instance.
2. Checks the validity date of only the leaf certificate (`chain[0]`).
3. Compares the leaf subject's parsed `CN` to the configured host name using case-insensitive equality.
4. Considers the chain trusted if any certificate in it has an alias in the server certificate store.
5. If any of those date, host, or trust checks fails, asks `SecurityWarningDlg` for a user decision. A rejection raises `CertificateException`; acceptance caches the chain in this trust-manager instance. A chain passing all three checks is also cached.

Source: `src/main/java/com/myjavaworld/jftp/ssl/JFTPTrustManager.java` (`checkServerTrusted`, `isValidDate`, `isValidHost`, `isTrusted`).

Security implications visible from that implementation:

- Host matching uses CN only. It does not inspect Subject Alternative Names, wildcard names, or IP address SANs. The comparison is exact case-insensitive equality.
- The normal PKIX/server-trust check is not invoked for the server chain. Store membership is checked by certificate equality against any chain element, without validating the chain through the retained trust manager.
- The user approval path allows a failing certificate chain for the life of that trust-manager instance. It is not persisted by this method; persistent installation is a separate certificate-manager operation.
- `chain[0]` is assumed to exist and be an X.509 certificate. Empty or malformed chains may fail outside the intended warning flow.

These are current implementation facts, not compatibility recommendations. Any change to trust behavior should be treated as a security-sensitive functional change and covered explicitly with generated-certificate tests. Preserve or intentionally revise the user approval and persistence behavior rather than accidentally changing it during Java API modernization.

## Certificate and key stores

`KeyStoreManager` lazily initializes two static stores on the first access: server trust certificates and client certificates. Both are loaded from preference-configured paths and passwords, using `KeyStore.getInstance("JKS")`. If a file does not exist, it creates and saves an empty store. The initialized stores are cached statically; later preference changes are not reloaded by the code shown. Added chains are stored as certificate entries with generated `JFTP<number>` aliases (or replace a matching certificate alias); delete operations remove an alias and save the corresponding store.

`JFTPKeyManager` uses `KeyManagerFactory.getInstance("SunX509")` initialized with the client store and its configured password, then delegates its `X509KeyManager` methods. Thus client-certificate selection is delegated to the JDK key manager implementation.

Sources: `src/main/java/com/myjavaworld/jftp/ssl/KeyStoreManager.java` and `JFTPKeyManager.java`.

Compatibility considerations:

- `SunX509` names a provider-specific algorithm and can reduce portability across non-Sun-derived providers. The algorithm/provider choice should be validated on target runtimes.
- Hardcoded JKS may affect interoperability with PKCS#12 stores or changed JDK defaults. Existing user stores may contain important trust/client credentials, so any format migration needs a tested import/backup path.
- The static store cache means changing paths/passwords after first use in the same process will not take effect without reinitialization/restart.
- `X509Certificate.getSubjectDN()` and `getIssuerDN()` are used by trust checks and certificate display code; these methods are deprecated on modern Java. The local `DNParser` searches a rendered DN string and is not an RFC 4514 parser. Modernization should use structured certificate name APIs and add SAN-focused tests.

## Certificate UI and import behavior

The certificate manager presents server and client certificate stores in separate tabs, allows viewing/deleting entries, and imports certificates through `CertificateFactory` from a selected file (`ssl/CertificateManagerDlg.java`). `CertificateDlg` can install a presented chain to the server store through `KeyStoreManager.addServerCertificate`. The warning dialog is invoked by the trust manager for chains failing any of the current date, CN, or store-membership checks. This document does not claim the UI installation/import path has been exercised on a current runtime.

## Java/API compatibility inventory

Within this scope, code also uses raw `Hashtable`, `Enumeration`, and `ArrayList` APIs; explicit wrapper constructors (`new Integer`, `new Long`); and reflective `Class.newInstance()` in `FTPSession`. These are modernization/maintenance concerns, separate from TLS policy. Changing these constructs should preserve serialized profile compatibility and transfer behavior.

The FTP client and list parser are loaded using class names stored in `RemoteHost`, whose defaults are `com.myjavaworld.ftp.DefaultFTPClient` and `com.myjavaworld.ftp.DefaultListParser`. Their implementations are not present under `src/main/java` in this checkout. **Unverified:** the repository's dependency/build configuration may supply them; their TLS and socket compatibility must be confirmed when reviewing dependencies and packaging.

## Suggested security-focused behavior tests

These are proposals, not existing tests. `src/test/java` currently contains only `.gitkeep`.

- A trusted, valid certificate for the configured host should connect without warning under the intended policy.
- An untrusted, expired, and host-mismatched certificate should each exercise the existing warning approval/rejection outcomes; test whether approval is scoped to a connection/session and whether it persists only after explicit installation.
- Add SAN-only and wildcard host certificates to expose the current CN-only behavior before deciding on the target hostname-verification policy.
- Test JKS load, creation, add, delete, and restart persistence using temporary preference paths, including the handling of wrong passwords and malformed stores.
- Test explicit and implicit FTPS modes, with protected and unprotected data channels, against a controlled endpoint once the FTP client library is identified. The current code supplies these options but does not prove protocol behavior.
