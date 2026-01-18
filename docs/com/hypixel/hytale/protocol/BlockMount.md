# BlockMount

## Overview
- Documentation for `BlockMount`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `BlockMount()`
  - Creates a `BlockMount` instance.
- `BlockMount(@Nonnull BlockMountType type, @Nullable Vector3f position, @Nullable Vector3f orientation, int blockTypeId)`
  - Creates a `BlockMount` instance.
- `BlockMount(@Nonnull BlockMount other)`
  - Creates a `BlockMount` instance.

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
