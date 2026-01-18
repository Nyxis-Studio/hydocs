# UpdateItemQualities

## Overview
- Documentation for `UpdateItemQualities`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.assets`.

## Constructors
- `UpdateItemQualities()`
  - Creates a `UpdateItemQualities` instance.
- `UpdateItemQualities(@Nonnull UpdateType type, int maxId, @Nullable Map<Integer, ItemQuality> itemQualities)`
  - Creates a `UpdateItemQualities` instance.
- `UpdateItemQualities(@Nonnull UpdateItemQualities other)`
  - Creates a `UpdateItemQualities` instance.

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
