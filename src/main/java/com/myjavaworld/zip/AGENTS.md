# ZIP and extraction guidance

`Zip` and `Unzip` support zip-and-upload and download-and-unzip workflows. Preserve archive entry names, recursion, filters, timestamps, progress/status events, and cleanup behavior unless an intentional change is documented.

ZIP extraction currently builds destination paths from archive entry names without an observed containment check. Treat archives as untrusted input. Do not claim safe extraction until normalized/canonical destination containment is enforced and tested for parent traversal, absolute paths, mixed separators, and ordinary nested paths. A traversal fix is an explicit security behavior change.

When changing archive code, cover empty files, nested directories, out-of-base ZIP inputs, and event payloads as appropriate. Open `docs/ftp-transfers-and-zip.md` for workflow behavior and `docs/security-and-ssl.md` for the extraction risk. Update both when extraction safety changes.
