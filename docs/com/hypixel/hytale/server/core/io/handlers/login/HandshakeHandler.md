# HandshakeHandler

## Overview
- Documentation for `HandshakeHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.io.handlers.login`.

## Constructors
- `HandshakeHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, @Nonnull String language, @Nonnull ClientType clientType, @Nonnull String identityToken, @Nonnull UUID playerUuid, @Nonnull String username, @Nullable byte[] referralData, @Nullable HostAddress referralSource)`
  - Creates a `HandshakeHandler` instance.

## Methods
- `getSessionServiceClient()`
  - Executes `getSessionServiceClient` behavior.
- `getJwtValidator()`
  - Executes `getJwtValidator` behavior.
- `accept(@Nonnull Packet packet)`
  - Executes `accept` behavior.
- `registered0(PacketHandler oldHandler)`
  - Executes `registered0` behavior.
- `requestAuthGrant()`
  - Executes `requestAuthGrant` behavior.
- `handle(@Nonnull Disconnect packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull AuthToken packet)`
  - Executes `handle` behavior.
- `exchangeServerAuthGrant(@Nonnull String serverAuthGrant)`
  - Executes `exchangeServerAuthGrant` behavior.
- `generatePasswordChallengeIfNeeded()`
  - Executes `generatePasswordChallengeIfNeeded` behavior.
- `completeAuthentication(byte[] passwordChallenge)`
  - Executes `completeAuthentication` behavior.
- `onAuthenticated(byte[] var1)`
  - Executes `onAuthenticated` behavior.

## Notes
- No additional notes.
