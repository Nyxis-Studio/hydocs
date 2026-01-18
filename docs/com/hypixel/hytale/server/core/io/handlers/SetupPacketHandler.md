# SetupPacketHandler

## Overview
- Documentation for `SetupPacketHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.io.handlers`.

## Constructors
- `SetupPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, UUID uuid, String username)`
  - Creates a `SetupPacketHandler` instance.
- `SetupPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, UUID uuid, String username, byte[] referralData, HostAddress referralSource)`
  - Creates a `SetupPacketHandler` instance.
- `SetupPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, @Nonnull PlayerAuthentication auth)`
  - Creates a `SetupPacketHandler` instance.

## Methods
- `getIdentifier()`
  - Executes `getIdentifier` behavior.
- `registered0(@Nonnull PacketHandler oldHandler)`
  - Executes `registered0` behavior.
- `accept(@Nonnull Packet packet)`
  - Executes `accept` behavior.
- `closed(ChannelHandlerContext ctx)`
  - Executes `closed` behavior.
- `handle(@Nonnull Disconnect packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull RequestAssets packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull ViewRadius packet)`
  - Executes `handle` behavior.
- `handle(@Nonnull PlayerOptions packet)`
  - Executes `handle` behavior.

## Notes
- No additional notes.
