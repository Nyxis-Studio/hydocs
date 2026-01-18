# JWTValidator

## Overview
- Documentation for `JWTValidator`.
- Declared as a class in `com.hypixel.hytale.server.core.auth`.

## Constructors
- `JWTValidator(@Nonnull SessionServiceClient sessionServiceClient, @Nonnull String expectedIssuer, @Nonnull String expectedAudience)`
  - Creates a `JWTValidator` instance.

## Methods
- `validateToken(@Nonnull String accessToken, @Nullable X509Certificate clientCert)`
  - Executes `validateToken` behavior.
- `verifySignature(SignedJWT signedJWT, JWKSet jwkSet)`
  - Executes `verifySignature` behavior.
- `getJwkSet()`
  - Executes `getJwkSet` behavior.
- `getJwkSet(boolean forceRefresh)`
  - Executes `getJwkSet` behavior.
- `fetchJwksFromService()`
  - Executes `fetchJwksFromService` behavior.
- `verifySignatureWithRetry(SignedJWT signedJWT)`
  - Executes `verifySignatureWithRetry` behavior.
- `convertToJWK(SessionServiceClient.JwkKey key)`
  - Executes `convertToJWK` behavior.
- `invalidateJwksCache()`
  - Executes `invalidateJwksCache` behavior.
- `validateIdentityToken(@Nonnull String identityToken)`
  - Executes `validateIdentityToken` behavior.
- `validateSessionToken(@Nonnull String sessionToken)`
  - Executes `validateSessionToken` behavior.
- `getSubjectAsUUID()`
  - Executes `getSubjectAsUUID` behavior.
- `getScopes()`
  - Executes `getScopes` behavior.
- `hasScope(@Nonnull String targetScope)`
  - Executes `hasScope` behavior.

## Notes
- No additional notes.
