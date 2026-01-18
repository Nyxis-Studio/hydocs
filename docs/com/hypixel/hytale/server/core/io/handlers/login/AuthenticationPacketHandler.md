# AuthenticationPacketHandler

## Overview
- Documentation for `AuthenticationPacketHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.io.handlers.login`.

## Constructors
- `AuthenticationPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, @Nonnull String language, @Nonnull AuthHandlerSupplier authHandlerSupplier, @Nonnull ClientType clientType, @Nonnull String identityToken, @Nonnull UUID uuid, @Nonnull String username, @Nullable byte[] referralData, @Nullable HostAddress referralSource)`
  - Creates a `AuthenticationPacketHandler` instance.

## Methods
- `getIdentifier()`
  - Executes `getIdentifier` behavior.
- `registered0(PacketHandler oldHandler)`
  - Executes `registered0` behavior.
- `onAuthenticated(byte[] passwordChallenge)`
  - Executes `onAuthenticated` behavior.
- `create(Channel var1, ProtocolVersion var2, String var3, PlayerAuthentication var4)`
  - Executes `create` behavior.

## Notes
- No additional notes.
