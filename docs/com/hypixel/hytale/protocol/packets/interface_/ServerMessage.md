# ServerMessage

## Overview
- Documentation for `ServerMessage`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.interface_`.

## Constructors
- `ServerMessage()`
  - Creates a `ServerMessage` instance.
- `ServerMessage(@Nonnull ChatType type, @Nullable FormattedMessage message)`
  - Creates a `ServerMessage` instance.
- `ServerMessage(@Nonnull ServerMessage other)`
  - Creates a `ServerMessage` instance.

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
