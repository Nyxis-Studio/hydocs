# GenericPacketHandler

## Overview
- Documentation for `GenericPacketHandler`.
- Declared as a class in `com.hypixel.hytale.server.core.io.handlers`.

## Constructors
- `GenericPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion)`
  - Creates a `GenericPacketHandler` instance.

## Methods
- `newHandlerArray(int size)`
  - Executes `newHandlerArray` behavior.
- `registerSubPacketHandler(SubPacketHandler subPacketHandler)`
  - Executes `registerSubPacketHandler` behavior.
- `registerHandler(int packetId, @Nonnull Consumer<Packet> handler)`
  - Executes `registerHandler` behavior.
- `registerNoOpHandlers(int ... packetIds)`
  - Executes `registerNoOpHandlers` behavior.
- `accept(@Nonnull Packet packet)`
  - Executes `accept` behavior.

## Notes
- No additional notes.
