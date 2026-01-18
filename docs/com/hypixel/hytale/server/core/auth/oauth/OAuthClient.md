**Source Hash:** `0c832ae02c18c79fd2ee9ad0ac8400141be21bd87032479ab38260cea66f9925`

# OAuthClient

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `startFlow(@Nonnull OAuthBrowserFlow flow)`: Add description.
  - Executes `startFlow` behavior.
- `startFlow(OAuthDeviceFlow flow)`: Add description.
  - Executes `startFlow` behavior.
- `refreshTokens(@Nonnull String refreshToken)`: Add description.
  - Executes `refreshTokens` behavior.
- `buildAuthUrl(String state, String codeChallenge, String redirectUri)`: Add description.
  - Executes `buildAuthUrl` behavior.
- `exchangeCodeForTokens(String code, String codeVerifier, String redirectUri)`: Add description.
  - Executes `exchangeCodeForTokens` behavior.
- `requestDeviceAuthorization()`: Add description.
  - Executes `requestDeviceAuthorization` behavior.
- `pollDeviceToken(String deviceCode)`: Add description.
  - Executes `pollDeviceToken` behavior.
- `generateRandomString(int length)`: Add description.
  - Executes `generateRandomString` behavior.
- `generateCodeChallenge(String verifier)`: Add description.
  - Executes `generateCodeChallenge` behavior.
- `extractParam(String query, String name)`: Add description.
  - Executes `extractParam` behavior.
- `encodeStateWithPort(String state, int port)`: Add description.
  - Executes `encodeStateWithPort` behavior.
- `parseTokenResponse(String json)`: Add description.
  - Executes `parseTokenResponse` behavior.
- `parseDeviceAuthResponse(String json)`: Add description.
  - Executes `parseDeviceAuthResponse` behavior.
- `getJsonString(JsonObject obj, String key)`: Add description.
  - Executes `getJsonString` behavior.
- `getJsonInt(JsonObject obj, String key, int defaultValue)`: Add description.
  - Executes `getJsonInt` behavior.
- `buildHtmlPage(boolean success, String title, String heading, String message, @Nullable String errorDetail)`: Add description.
  - Executes `buildHtmlPage` behavior.
- `TokenResponse(@Nullable String accessToken, @Nullable String refreshToken, @Nullable String idToken, @Nullable String error, int expiresIn)`: Add description.
  - Executes `TokenResponse` behavior.
- `isSuccess()`: Add description.
  - Executes `isSuccess` behavior.
- `DeviceAuthResponse(String deviceCode, String userCode, String verificationUri, String verificationUriComplete, int expiresIn, int interval)`: Add description.
  - Executes `DeviceAuthResponse` behavior.

## Notes
- No additional notes.
