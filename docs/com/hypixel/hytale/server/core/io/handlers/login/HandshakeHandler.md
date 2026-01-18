**Source Hash:** `9d27d43e21fbd637f1ed9764b4cae63f9d0e7e6c4546ca71c43120f022f76b42`

# HandshakeHandler

## Overview

## Constructor Descriptions
- `HandshakeHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, @Nonnull String language, @Nonnull ClientType clientType, @Nonnull String identityToken, @Nonnull UUID playerUuid, @Nonnull String username, @Nullable byte[] referralData, @Nullable HostAddress referralSource)`
  - Creates a `HandshakeHandler` instance.

## Method Descriptions
- `getSessionServiceClient()`: Add description.
  - Executes `getSessionServiceClient` behavior.
- `getJwtValidator()`: Add description.
  - Executes `getJwtValidator` behavior.
- `accept(@Nonnull Packet packet)`: Add description.
  - Executes `accept` behavior.
- `registered0(PacketHandler oldHandler)`: Add description.
  - Executes `registered0` behavior.
- `requestAuthGrant()`: Add description.
  - Executes `requestAuthGrant` behavior.
- `handle(@Nonnull Disconnect packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull AuthToken packet)`: Add description.
  - Executes `handle` behavior.
- `exchangeServerAuthGrant(@Nonnull String serverAuthGrant)`: Add description.
  - Executes `exchangeServerAuthGrant` behavior.
- `generatePasswordChallengeIfNeeded()`: Add description.
  - Executes `generatePasswordChallengeIfNeeded` behavior.
- `completeAuthentication(byte[] passwordChallenge)`: Add description.
  - Executes `completeAuthentication` behavior.
- `onAuthenticated(byte[] var1)`: Add description.
  - Executes `onAuthenticated` behavior.

## Notes
- No additional notes.
