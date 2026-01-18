# MaterialQuantity

## Overview
- Documentation for `MaterialQuantity`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `MaterialQuantity()`
  - Creates a `MaterialQuantity` instance.
- `MaterialQuantity(@Nullable String itemId, int itemTag, @Nullable String resourceTypeId, int quantity)`
  - Creates a `MaterialQuantity` instance.
- `MaterialQuantity(@Nonnull MaterialQuantity other)`
  - Creates a `MaterialQuantity` instance.

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
