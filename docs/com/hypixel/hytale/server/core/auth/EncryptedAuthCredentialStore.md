# EncryptedAuthCredentialStore

## Overview
- Documentation for `EncryptedAuthCredentialStore`.
- Declared as a class in `com.hypixel.hytale.server.core.auth`.

## Constructors
- `EncryptedAuthCredentialStore(@Nonnull Path path)`
  - Creates a `EncryptedAuthCredentialStore` instance.

## Methods
- `deriveKey()`
  - Executes `deriveKey` behavior.
- `load()`
  - Executes `load` behavior.
- `save()`
  - Executes `save` behavior.
- `encrypt(@Nonnull byte[] plaintext)`
  - Executes `encrypt` behavior.
- `decrypt(@Nonnull byte[] encrypted)`
  - Executes `decrypt` behavior.
- `setTokens(@Nonnull IAuthCredentialStore.OAuthTokens tokens)`
  - Executes `setTokens` behavior.
- `setProfile(@Nullable UUID uuid)`
  - Executes `setProfile` behavior.
- `getProfile()`
  - Executes `getProfile` behavior.
- `clear()`
  - Executes `clear` behavior.

## Notes
- No additional notes.
