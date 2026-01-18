**Source Hash:** `94454470544f6b7fb29d4272aff23c68eb8ed1c6d422cad67c259a2f5539634f`

# GenericPacketHandler

## Overview

## Constructor Descriptions
- `GenericPacketHandler(@Nonnull Channel channel, @Nonnull ProtocolVersion protocolVersion)`
  - Creates a `GenericPacketHandler` instance.

## Method Descriptions
- `newHandlerArray(int size)`: Add description.
  - Executes `newHandlerArray` behavior.
- `registerSubPacketHandler(SubPacketHandler subPacketHandler)`: Add description.
  - Executes `registerSubPacketHandler` behavior.
- `registerHandler(int packetId, @Nonnull Consumer<Packet> handler)`: Add description.
  - Executes `registerHandler` behavior.
- `registerNoOpHandlers(int ... packetIds)`: Add description.
  - Executes `registerNoOpHandlers` behavior.
- `accept(@Nonnull Packet packet)`: Add description.
  - Executes `accept` behavior.

## Notes
- No additional notes.
