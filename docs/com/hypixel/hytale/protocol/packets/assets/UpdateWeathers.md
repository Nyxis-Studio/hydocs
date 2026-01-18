# UpdateWeathers

## Overview
- Documentation for `UpdateWeathers`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.assets`.

## Constructors
- `UpdateWeathers()`
  - Creates a `UpdateWeathers` instance.
- `UpdateWeathers(@Nonnull UpdateType type, int maxId, @Nullable Map<Integer, Weather> weathers)`
  - Creates a `UpdateWeathers` instance.
- `UpdateWeathers(@Nonnull UpdateWeathers other)`
  - Creates a `UpdateWeathers` instance.

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
