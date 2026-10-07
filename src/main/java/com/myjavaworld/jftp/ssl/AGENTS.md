# SSL and certificate guidance

This package builds SSL contexts, trust/key managers, certificate stores, certificate parsing, and security dialogs. Changes can alter which servers users trust and whether client credentials remain usable.

- Treat trust policy and hostname validation as security-sensitive behavior. Record the existing rule and intended new rule before changing them.
- Preserve certificate approval, installation, rejection, and session-caching behavior unless a deliberate security change is in scope.
- Test trust outcomes with generated certificates and a controlled endpoint. Cover expiry, trust-store membership, host/SAN cases, and approval/rejection as required by the chosen policy.
- Protect existing stores. Test with temporary copies; never overwrite a user's real certificate store.
- Do not infer negotiated TLS versions or socket behavior from SSL context construction alone; validate against the selected Java baseline and FTP library.

Open `docs/security-and-ssl.md` for trust/key-store behavior and known risks. Open `docs/preferences-and-user-data.md` when changing configured certificate paths/passwords or stored profiles. Update those guides with verified behavior and migration decisions.
