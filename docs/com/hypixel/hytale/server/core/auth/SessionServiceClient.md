**Source Hash:** `743c25dd22114243d6b1e7af899019b976a7c96f917b22852648acf9f2c87f08`

# SessionServiceClient

## Overview

## Constructor Descriptions
- `SessionServiceClient(@Nonnull String sessionServiceUrl)`
  - Creates a `SessionServiceClient` instance.

## Method Descriptions
- `requestAuthorizationGrantAsync(@Nonnull String identityToken, @Nonnull String serverAudience, @Nonnull String bearerToken)`: Add description.
  - Executes `requestAuthorizationGrantAsync` behavior.
- `exchangeAuthGrantForTokenAsync(@Nonnull String authorizationGrant, @Nonnull String x509Fingerprint, @Nonnull String bearerToken)`: Add description.
  - Executes `exchangeAuthGrantForTokenAsync` behavior.
- `getJwks()`: Add description.
  - Executes `getJwks` behavior.
- `getGameProfiles(@Nonnull String oauthAccessToken)`: Add description.
  - Executes `getGameProfiles` behavior.
- `createGameSession(@Nonnull String oauthAccessToken, @Nonnull UUID profileUuid)`: Add description.
  - Executes `createGameSession` behavior.
- `refreshSessionAsync(@Nonnull String sessionToken)`: Add description.
  - Executes `refreshSessionAsync` behavior.
- `terminateSession(@Nonnull String sessionToken)`: Add description.
  - Executes `terminateSession` behavior.
- `escapeJsonString(String value)`: Add description.
  - Executes `escapeJsonString` behavior.
- `externalKey(String key, Codec<T> codec)`: Add description.
  - Executes `externalKey` behavior.
- `getExpiresAtInstant()`: Add description.
  - Executes `getExpiresAtInstant` behavior.

## Notes
- No additional notes.
