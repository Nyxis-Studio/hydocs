# OpenWindow

## Overview
- Documentation for `OpenWindow`.
- Declared as a class in `com.hypixel.hytale.protocol.packets.window`.

## Constructors
- `OpenWindow()`
  - Creates a `OpenWindow` instance.
- `OpenWindow(int id, @Nonnull WindowType windowType, @Nullable String windowData, @Nullable InventorySection inventory, @Nullable ExtraResources extraResources)`
  - Creates a `OpenWindow` instance.
- `OpenWindow(@Nonnull OpenWindow other)`
  - Creates a `OpenWindow` instance.

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
