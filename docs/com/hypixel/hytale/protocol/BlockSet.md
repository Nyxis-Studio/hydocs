# BlockSet

## Overview
- Documentation for `BlockSet`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `BlockSet()`
  - Creates a `BlockSet` instance.
- `BlockSet(@Nullable String name, @Nullable int[] blocks)`
  - Creates a `BlockSet` instance.
- `BlockSet(@Nonnull BlockSet other)`
  - Creates a `BlockSet` instance.

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
