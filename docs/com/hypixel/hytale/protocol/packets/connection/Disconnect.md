# Disconnect

## Overview
- Documentation for `Disconnect`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.connection`.

## Constructors
- `Disconnect()`
  - Creates a `Disconnect` instance.
- `Disconnect(@Nullable String reason, @Nonnull DisconnectType type)`
  - Creates a `Disconnect` instance.
- `Disconnect(@Nonnull Disconnect other)`
  - Creates a `Disconnect` instance.

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
