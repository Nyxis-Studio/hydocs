# Equipment

## Overview
- Documentation for `Equipment`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Equipment()`
  - Creates a `Equipment` instance.
- `Equipment(@Nullable String[] armorIds, @Nullable String rightHandItemId, @Nullable String leftHandItemId)`
  - Creates a `Equipment` instance.
- `Equipment(@Nonnull Equipment other)`
  - Creates a `Equipment` instance.

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
