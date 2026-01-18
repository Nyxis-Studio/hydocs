# WorldParticle

## Overview
- Documentation for `WorldParticle`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `WorldParticle()`
  - Creates a `WorldParticle` instance.
- `WorldParticle(@Nullable String systemId, float scale, @Nullable Color color, @Nullable Vector3f positionOffset, @Nullable Direction rotationOffset)`
  - Creates a `WorldParticle` instance.
- `WorldParticle(@Nonnull WorldParticle other)`
  - Creates a `WorldParticle` instance.

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
