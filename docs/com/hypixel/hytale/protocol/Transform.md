# Transform

## Overview
- Documentation for `Transform`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Transform()`
  - Creates a `Transform` instance.
- `Transform(@Nullable Position position, @Nullable Direction orientation)`
  - Creates a `Transform` instance.
- `Transform(@Nonnull Transform other)`
  - Creates a `Transform` instance.

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
