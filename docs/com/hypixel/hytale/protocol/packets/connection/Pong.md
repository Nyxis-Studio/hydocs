# Pong

## Overview
- Documentation for `Pong`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.connection`.

## Constructors
- `Pong()`
  - Creates a `Pong` instance.
- `Pong(int id, @Nullable InstantData time, @Nonnull PongType type, short packetQueueSize)`
  - Creates a `Pong` instance.
- `Pong(@Nonnull Pong other)`
  - Creates a `Pong` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
- `deserialize(@Nonnull ByteBuf buf, int offset)`
  - Executes `deserialize` behavior.
- `computeBytesConsumed(@Nonnull ByteBuf buf, int offset)`
  - Executes `computeBytesConsumed` behavior.
- `serialize(@Nonnull ByteBuf buf)`
  - Executes `serialize` behavior.
- `computeSize()`
  - Executes `computeSize` behavior.
- `validateStructure(@Nonnull ByteBuf buffer, int offset)`
  - Executes `validateStructure` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(Object obj)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.

## Notes
- No additional notes.
