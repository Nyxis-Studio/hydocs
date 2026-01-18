# SessionServiceClient

## Overview
- Documentation for `SessionServiceClient`.
- Declared as a class in `com.hypixel.hytale.server.core.auth`.

## Constructors
- `SessionServiceClient(@Nonnull String sessionServiceUrl)`
  - Creates a `SessionServiceClient` instance.

## Methods
- `requestAuthorizationGrantAsync(@Nonnull String identityToken, @Nonnull String serverAudience, @Nonnull String bearerToken)`
  - Executes `requestAuthorizationGrantAsync` behavior.
- `exchangeAuthGrantForTokenAsync(@Nonnull String authorizationGrant, @Nonnull String x509Fingerprint, @Nonnull String bearerToken)`
  - Executes `exchangeAuthGrantForTokenAsync` behavior.
- `getJwks()`
  - Executes `getJwks` behavior.
- `getGameProfiles(@Nonnull String oauthAccessToken)`
  - Executes `getGameProfiles` behavior.
- `createGameSession(@Nonnull String oauthAccessToken, @Nonnull UUID profileUuid)`
  - Executes `createGameSession` behavior.
- `refreshSessionAsync(@Nonnull String sessionToken)`
  - Executes `refreshSessionAsync` behavior.
- `terminateSession(@Nonnull String sessionToken)`
  - Executes `terminateSession` behavior.
- `escapeJsonString(String value)`
  - Executes `escapeJsonString` behavior.
- `externalKey(String key, Codec<T> codec)`
  - Executes `externalKey` behavior.
- `getExpiresAtInstant()`
  - Executes `getExpiresAtInstant` behavior.

## Notes
- No additional notes.
