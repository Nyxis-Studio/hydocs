# Direction

## Overview
- Documentation for `Direction`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Direction()`
  - Creates a `Direction` instance.
- `Direction(float yaw, float pitch, float roll)`
  - Creates a `Direction` instance.
- `Direction(@Nonnull Direction other)`
  - Creates a `Direction` instance.

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
