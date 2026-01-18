# ServerAuthManager

## Overview
- Documentation for `ServerAuthManager`.
- Declared as a class in `com.hypixel.hytale.server.core.auth`.

## Constructors
- `ServerAuthManager()`
  - Creates a `ServerAuthManager` instance.

## Methods
- `initialize()`
  - Executes `initialize` behavior.
- `initializeCredentialStore()`
  - Executes `initializeCredentialStore` behavior.
- `getInstance()`
  - Executes `getInstance` behavior.
- `getIdentityToken()`
  - Executes `getIdentityToken` behavior.
- `getSessionToken()`
  - Executes `getSessionToken` behavior.
- `setGameSession(@Nonnull SessionServiceClient.GameSessionResponse session)`
  - Executes `setGameSession` behavior.
- `hasIdentityToken()`
  - Executes `hasIdentityToken` behavior.
- `hasSessionToken()`
  - Executes `hasSessionToken` behavior.
- `setServerCertificate(@Nonnull X509Certificate certificate)`
  - Executes `setServerCertificate` behavior.
- `getServerCertificate()`
  - Executes `getServerCertificate` behavior.
- `getServerCertificateFingerprint()`
  - Executes `getServerCertificateFingerprint` behavior.
- `getServerSessionId()`
  - Executes `getServerSessionId` behavior.
- `startFlowAsync(@Nonnull OAuthBrowserFlow flow)`
  - Executes `startFlowAsync` behavior.
- `startFlowAsync(OAuthDeviceFlow flow)`
  - Executes `startFlowAsync` behavior.
- `registerCredentialStore(IAuthCredentialStore store)`
  - Executes `registerCredentialStore` behavior.
- `swapCredentialStoreProvider(@Nonnull AuthCredentialStoreProvider provider)`
  - Executes `swapCredentialStoreProvider` behavior.
- `createGameSessionFromOAuth(AuthMode mode)`
  - Executes `createGameSessionFromOAuth` behavior.
- `refreshOAuthTokens()`
  - Executes `refreshOAuthTokens` behavior.
- `refreshOAuthTokens(boolean force)`
  - Executes `refreshOAuthTokens` behavior.
- `completeAuthWithProfile(SessionServiceClient.GameProfile profile, AuthMode mode)`
  - Executes `completeAuthWithProfile` behavior.
- `hasPendingProfiles()`
  - Executes `hasPendingProfiles` behavior.
- `selectPendingProfile(int index)`
  - Executes `selectPendingProfile` behavior.
- `selectPendingProfileByUsername(String username)`
  - Executes `selectPendingProfileByUsername` behavior.
- `clearPendingProfiles()`
  - Executes `clearPendingProfiles` behavior.
- `cancelActiveFlow()`
  - Executes `cancelActiveFlow` behavior.
- `validateInitialTokens(@Nullable String sessionToken, @Nullable String identityToken)`
  - Executes `validateInitialTokens` behavior.
- `parseAndScheduleRefresh()`
  - Executes `parseAndScheduleRefresh` behavior.
- `scheduleRefresh(int expiresInSeconds)`
  - Executes `scheduleRefresh` behavior.
- `doRefresh()`
  - Executes `doRefresh` behavior.
- `refreshGameSession(String currentSessionToken)`
  - Executes `refreshGameSession` behavior.
- `refreshGameSessionViaOAuth()`
  - Executes `refreshGameSessionViaOAuth` behavior.
- `logout()`
  - Executes `logout` behavior.
- `getAuthMode()`
  - Executes `getAuthMode` behavior.
- `isSingleplayer()`
  - Executes `isSingleplayer` behavior.
- `isOwner(@Nullable UUID playerUuid)`
  - Executes `isOwner` behavior.
- `getTokenExpiry()`
  - Executes `getTokenExpiry` behavior.
- `getAuthStatus()`
  - Executes `getAuthStatus` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.

## Notes
- No additional notes.
