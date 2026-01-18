**Source Hash:** `499ee1cf9462c7c6e8333f4f09a2b38c2f6218a5d909cf716828cc5a469a31b5`

# PasswordPacketHandler

## Overview

## Constructor Descriptions
- `PasswordPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, @Nonnull String language, @Nonnull UUID playerUuid, @Nonnull String username, @Nullable byte[] referralData, @Nullable HostAddress referralSource, @Nullable byte[] passwordChallenge, @Nonnull SetupHandlerSupplier setupHandlerSupplier)`
  - Creates a `PasswordPacketHandler` instance.

## Method Descriptions
- `getIdentifier()`: Add description.
  - Executes `getIdentifier` behavior.
- `registered0(PacketHandler oldHandler)`: Add description.
  - Executes `registered0` behavior.
- `accept(@Nonnull Packet packet)`: Add description.
  - Executes `accept` behavior.
- `handle(@Nonnull Disconnect packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull PasswordResponse packet)`: Add description.
  - Executes `handle` behavior.
- `generateChallenge()`: Add description.
  - Executes `generateChallenge` behavior.
- `proceedToSetup()`: Add description.
  - Executes `proceedToSetup` behavior.
- `computePasswordHash(byte[] challenge, String password)`: Add description.
  - Executes `computePasswordHash` behavior.
- `create(Channel var1, ProtocolVersion var2, String var3, PlayerAuthentication var4)`: Add description.
  - Executes `create` behavior.

## Notes
- No additional notes.
