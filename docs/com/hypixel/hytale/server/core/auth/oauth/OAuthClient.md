# OAuthClient

## Overview
- Documentation for `OAuthClient`.
- Declared as a class in `com.hypixel.hytale.server.core.auth.oauth`.

## Constructors
- None.

## Methods
- `startFlow(@Nonnull OAuthBrowserFlow flow)`
  - Executes `startFlow` behavior.
- `startFlow(OAuthDeviceFlow flow)`
  - Executes `startFlow` behavior.
- `refreshTokens(@Nonnull String refreshToken)`
  - Executes `refreshTokens` behavior.
- `buildAuthUrl(String state, String codeChallenge, String redirectUri)`
  - Executes `buildAuthUrl` behavior.
- `exchangeCodeForTokens(String code, String codeVerifier, String redirectUri)`
  - Executes `exchangeCodeForTokens` behavior.
- `requestDeviceAuthorization()`
  - Executes `requestDeviceAuthorization` behavior.
- `pollDeviceToken(String deviceCode)`
  - Executes `pollDeviceToken` behavior.
- `generateRandomString(int length)`
  - Executes `generateRandomString` behavior.
- `generateCodeChallenge(String verifier)`
  - Executes `generateCodeChallenge` behavior.
- `extractParam(String query, String name)`
  - Executes `extractParam` behavior.
- `encodeStateWithPort(String state, int port)`
  - Executes `encodeStateWithPort` behavior.
- `parseTokenResponse(String json)`
  - Executes `parseTokenResponse` behavior.
- `parseDeviceAuthResponse(String json)`
  - Executes `parseDeviceAuthResponse` behavior.
- `getJsonString(JsonObject obj, String key)`
  - Executes `getJsonString` behavior.
- `getJsonInt(JsonObject obj, String key, int defaultValue)`
  - Executes `getJsonInt` behavior.
- `buildHtmlPage(boolean success, String title, String heading, String message, @Nullable String errorDetail)`
  - Executes `buildHtmlPage` behavior.
- `TokenResponse(@Nullable String accessToken, @Nullable String refreshToken, @Nullable String idToken, @Nullable String error, int expiresIn)`
  - Executes `TokenResponse` behavior.
- `isSuccess()`
  - Executes `isSuccess` behavior.
- `DeviceAuthResponse(String deviceCode, String userCode, String verificationUri, String verificationUriComplete, int expiresIn, int interval)`
  - Executes `DeviceAuthResponse` behavior.

## Notes
- No additional notes.
