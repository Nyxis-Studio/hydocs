# InventoryAction

## Overview
- Documentation for `InventoryAction`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.inventory`.

## Constructors
- `InventoryAction()`
  - Creates a `InventoryAction` instance.
- `InventoryAction(int inventorySectionId, @Nonnull InventoryActionType inventoryActionType, byte actionData)`
  - Creates a `InventoryAction` instance.
- `InventoryAction(@Nonnull InventoryAction other)`
  - Creates a `InventoryAction` instance.

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
