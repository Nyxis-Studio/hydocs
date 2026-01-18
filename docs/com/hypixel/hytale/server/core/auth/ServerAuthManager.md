**Source Hash:** `f0ce9f0bb0db63638e9e8a299db4d911b10bda990d0e8d2a2057bac2e98b2c64`

# ServerAuthManager

## Overview

## Constructor Descriptions
- `ServerAuthManager()`
  - Creates a `ServerAuthManager` instance.

## Method Descriptions
- `initialize()`: Add description.
  - Executes `initialize` behavior.
- `initializeCredentialStore()`: Add description.
  - Executes `initializeCredentialStore` behavior.
- `getInstance()`: Add description.
  - Executes `getInstance` behavior.
- `getIdentityToken()`: Add description.
  - Executes `getIdentityToken` behavior.
- `getSessionToken()`: Add description.
  - Executes `getSessionToken` behavior.
- `setGameSession(@Nonnull SessionServiceClient.GameSessionResponse session)`: Add description.
  - Executes `setGameSession` behavior.
- `hasIdentityToken()`: Add description.
  - Executes `hasIdentityToken` behavior.
- `hasSessionToken()`: Add description.
  - Executes `hasSessionToken` behavior.
- `setServerCertificate(@Nonnull X509Certificate certificate)`: Add description.
  - Executes `setServerCertificate` behavior.
- `getServerCertificate()`: Add description.
  - Executes `getServerCertificate` behavior.
- `getServerCertificateFingerprint()`: Add description.
  - Executes `getServerCertificateFingerprint` behavior.
- `getServerSessionId()`: Add description.
  - Executes `getServerSessionId` behavior.
- `startFlowAsync(@Nonnull OAuthBrowserFlow flow)`: Add description.
  - Executes `startFlowAsync` behavior.
- `startFlowAsync(OAuthDeviceFlow flow)`: Add description.
  - Executes `startFlowAsync` behavior.
- `registerCredentialStore(IAuthCredentialStore store)`: Add description.
  - Executes `registerCredentialStore` behavior.
- `swapCredentialStoreProvider(@Nonnull AuthCredentialStoreProvider provider)`: Add description.
  - Executes `swapCredentialStoreProvider` behavior.
- `createGameSessionFromOAuth(AuthMode mode)`: Add description.
  - Executes `createGameSessionFromOAuth` behavior.
- `refreshOAuthTokens()`: Add description.
  - Executes `refreshOAuthTokens` behavior.
- `refreshOAuthTokens(boolean force)`: Add description.
  - Executes `refreshOAuthTokens` behavior.
- `completeAuthWithProfile(SessionServiceClient.GameProfile profile, AuthMode mode)`: Add description.
  - Executes `completeAuthWithProfile` behavior.
- `hasPendingProfiles()`: Add description.
  - Executes `hasPendingProfiles` behavior.
- `selectPendingProfile(int index)`: Add description.
  - Executes `selectPendingProfile` behavior.
- `selectPendingProfileByUsername(String username)`: Add description.
  - Executes `selectPendingProfileByUsername` behavior.
- `clearPendingProfiles()`: Add description.
  - Executes `clearPendingProfiles` behavior.
- `cancelActiveFlow()`: Add description.
  - Executes `cancelActiveFlow` behavior.
- `validateInitialTokens(@Nullable String sessionToken, @Nullable String identityToken)`: Add description.
  - Executes `validateInitialTokens` behavior.
- `parseAndScheduleRefresh()`: Add description.
  - Executes `parseAndScheduleRefresh` behavior.
- `scheduleRefresh(int expiresInSeconds)`: Add description.
  - Executes `scheduleRefresh` behavior.
- `doRefresh()`: Add description.
  - Executes `doRefresh` behavior.
- `refreshGameSession(String currentSessionToken)`: Add description.
  - Executes `refreshGameSession` behavior.
- `refreshGameSessionViaOAuth()`: Add description.
  - Executes `refreshGameSessionViaOAuth` behavior.
- `logout()`: Add description.
  - Executes `logout` behavior.
- `getAuthMode()`: Add description.
  - Executes `getAuthMode` behavior.
- `isSingleplayer()`: Add description.
  - Executes `isSingleplayer` behavior.
- `isOwner(@Nullable UUID playerUuid)`: Add description.
  - Executes `isOwner` behavior.
- `getTokenExpiry()`: Add description.
  - Executes `getTokenExpiry` behavior.
- `getAuthStatus()`: Add description.
  - Executes `getAuthStatus` behavior.
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.

## Notes
- No additional notes.
