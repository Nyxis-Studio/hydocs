# InventorySection

## Overview
- Documentation for `InventorySection`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `InventorySection()`
  - Creates a `InventorySection` instance.
- `InventorySection(@Nullable Map<Integer, ItemWithAllMetadata> items, short capacity)`
  - Creates a `InventorySection` instance.
- `InventorySection(@Nonnull InventorySection other)`
  - Creates a `InventorySection` instance.

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
