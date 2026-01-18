# ItemQuantity

## Overview
- Documentation for `ItemQuantity`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ItemQuantity()`
  - Creates a `ItemQuantity` instance.
- `ItemQuantity(@Nullable String itemId, int quantity)`
  - Creates a `ItemQuantity` instance.
- `ItemQuantity(@Nonnull ItemQuantity other)`
  - Creates a `ItemQuantity` instance.

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
