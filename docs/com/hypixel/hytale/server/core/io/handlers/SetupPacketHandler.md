**Source Hash:** `2cedd2603409794854538e7f52a4f36a973fa93579e41382fb8e565b083aeceb`

# SetupPacketHandler

## Overview

## Constructor Descriptions
- `SetupPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, UUID uuid, String username)`
  - Creates a `SetupPacketHandler` instance.
- `SetupPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, UUID uuid, String username, byte[] referralData, HostAddress referralSource)`
  - Creates a `SetupPacketHandler` instance.
- `SetupPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion, String language, @Nonnull PlayerAuthentication auth)`
  - Creates a `SetupPacketHandler` instance.

## Method Descriptions
- `getIdentifier()`: Add description.
  - Executes `getIdentifier` behavior.
- `registered0(@Nonnull PacketHandler oldHandler)`: Add description.
  - Executes `registered0` behavior.
- `accept(@Nonnull Packet packet)`: Add description.
  - Executes `accept` behavior.
- `closed(ChannelHandlerContext ctx)`: Add description.
  - Executes `closed` behavior.
- `handle(@Nonnull Disconnect packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull RequestAssets packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull ViewRadius packet)`: Add description.
  - Executes `handle` behavior.
- `handle(@Nonnull PlayerOptions packet)`: Add description.
  - Executes `handle` behavior.

## Notes
- No additional notes.
