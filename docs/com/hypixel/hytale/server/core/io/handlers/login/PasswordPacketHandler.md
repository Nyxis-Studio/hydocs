# PasswordPacketHandler

## Overview
- Documentation for `PasswordPacketHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.io.handlers.login`.

## Constructors
- `PasswordPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, @Nonnull String language, @Nonnull UUID playerUuid, @Nonnull String username, @Nullable byte[] referralData, @Nullable HostAddress referralSource, @Nullable byte[] passwordChallenge, @Nonnull SetupHandlerSupplier setupHandlerSupplier)`
  - Creates a `PasswordPacketHandler` instance.

## Methods
- `getIdentifier()`
  - Executes `getIdentifier` behavior.
- `registered0(PacketHandler oldHandler)`
  - Executes `registered0` behavior.
- `accept(@Nonnull Packet packet)`
  - Executes `accept` behavior.
- `handle(@Nonnull Disconnect packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull PasswordResponse packet)`
  - Executes `handle` behavior.
- `generateChallenge()`
  - Executes `generateChallenge` behavior.
- `proceedToSetup()`
  - Executes `proceedToSetup` behavior.
- `computePasswordHash(byte[] challenge, String password)`
  - Executes `computePasswordHash` behavior.
- `create(Channel var1, ProtocolVersion var2, String var3, PlayerAuthentication var4)`
  - Executes `create` behavior.

## Notes
- No additional notes.
