# WorldSettings

## Overview
- Documentation for `WorldSettings`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.setup`.

## Constructors
- `WorldSettings()`
  - Creates a `WorldSettings` instance.
- `WorldSettings(int worldHeight, @Nullable Asset[] requiredAssets)`
  - Creates a `WorldSettings` instance.
- `WorldSettings(@Nonnull WorldSettings other)`
  - Creates a `WorldSettings` instance.

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
