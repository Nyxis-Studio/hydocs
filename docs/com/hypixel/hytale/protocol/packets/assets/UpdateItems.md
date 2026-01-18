# UpdateItems

## Overview
- Documentation for `UpdateItems`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.assets`.

## Constructors
- `UpdateItems()`
  - Creates a `UpdateItems` instance.
- `UpdateItems(@Nonnull UpdateType type, @Nullable Map<String, ItemBase> items, @Nullable String[] removedItems, boolean updateModels, boolean updateIcons)`
  - Creates a `UpdateItems` instance.
- `UpdateItems(@Nonnull UpdateItems other)`
  - Creates a `UpdateItems` instance.

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
