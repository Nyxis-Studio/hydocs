**Source Hash:** `980d1078cad508f70b182c2c643f9c80c4a658aa16d45d54b02ba5f8abc4646e`

# JWTValidator

## Overview

## Constructor Descriptions
- `JWTValidator(@Nonnull SessionServiceClient sessionServiceClient, @Nonnull String expectedIssuer, @Nonnull String expectedAudience)`
  - Creates a `JWTValidator` instance.

## Method Descriptions
- `validateToken(@Nonnull String accessToken, @Nullable X509Certificate clientCert)`: Add description.
  - Executes `validateToken` behavior.
- `verifySignature(SignedJWT signedJWT, JWKSet jwkSet)`: Add description.
  - Executes `verifySignature` behavior.
- `getJwkSet()`: Add description.
  - Executes `getJwkSet` behavior.
- `getJwkSet(boolean forceRefresh)`: Add description.
  - Executes `getJwkSet` behavior.
- `fetchJwksFromService()`: Add description.
  - Executes `fetchJwksFromService` behavior.
- `verifySignatureWithRetry(SignedJWT signedJWT)`: Add description.
  - Executes `verifySignatureWithRetry` behavior.
- `convertToJWK(SessionServiceClient.JwkKey key)`: Add description.
  - Executes `convertToJWK` behavior.
- `invalidateJwksCache()`: Add description.
  - Executes `invalidateJwksCache` behavior.
- `validateIdentityToken(@Nonnull String identityToken)`: Add description.
  - Executes `validateIdentityToken` behavior.
- `validateSessionToken(@Nonnull String sessionToken)`: Add description.
  - Executes `validateSessionToken` behavior.
- `getSubjectAsUUID()`: Add description.
  - Executes `getSubjectAsUUID` behavior.
- `getScopes()`: Add description.
  - Executes `getScopes` behavior.
- `hasScope(@Nonnull String targetScope)`: Add description.
  - Executes `hasScope` behavior.

## Notes
- No additional notes.
