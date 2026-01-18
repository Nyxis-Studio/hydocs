# ItemCategory

## Overview
- Documentation for `ItemCategory`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ItemCategory()`
  - Creates a `ItemCategory` instance.
- `ItemCategory(@Nullable String id, @Nullable String name, @Nullable String icon, int order, @Nonnull ItemGridInfoDisplayMode infoDisplayMode, @Nullable ItemCategory[] children)`
  - Creates a `ItemCategory` instance.
- `ItemCategory(@Nonnull ItemCategory other)`
  - Creates a `ItemCategory` instance.

## Methods
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
