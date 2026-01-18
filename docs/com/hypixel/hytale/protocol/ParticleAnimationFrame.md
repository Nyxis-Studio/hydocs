# ParticleAnimationFrame

## Overview
- Documentation for `ParticleAnimationFrame`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ParticleAnimationFrame()`
  - Creates a `ParticleAnimationFrame` instance.
- `ParticleAnimationFrame(@Nullable Range frameIndex, @Nullable RangeVector2f scale, @Nullable RangeVector3f rotation, @Nullable Color color, float opacity)`
  - Creates a `ParticleAnimationFrame` instance.
- `ParticleAnimationFrame(@Nonnull ParticleAnimationFrame other)`
  - Creates a `ParticleAnimationFrame` instance.

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
