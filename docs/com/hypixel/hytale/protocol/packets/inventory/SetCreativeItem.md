# SetCreativeItem

## Overview
- Documentation for `SetCreativeItem`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.inventory`.

## Constructors
- `SetCreativeItem()`
  - Creates a `SetCreativeItem` instance.
- `SetCreativeItem(int inventorySectionId, int slotId, @Nonnull ItemQuantity item, boolean override)`
  - Creates a `SetCreativeItem` instance.
- `SetCreativeItem(@Nonnull SetCreativeItem other)`
  - Creates a `SetCreativeItem` instance.

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
