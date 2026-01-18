# ModelTransform

## Overview
- Documentation for `ModelTransform`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ModelTransform()`
  - Creates a `ModelTransform` instance.
- `ModelTransform(@Nullable Position position, @Nullable Direction bodyOrientation, @Nullable Direction lookOrientation)`
  - Creates a `ModelTransform` instance.
- `ModelTransform(@Nonnull ModelTransform other)`
  - Creates a `ModelTransform` instance.

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
