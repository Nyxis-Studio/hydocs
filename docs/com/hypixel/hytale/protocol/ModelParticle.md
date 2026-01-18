# ModelParticle

## Overview
- Documentation for `ModelParticle`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ModelParticle()`
  - Creates a `ModelParticle` instance.
- `ModelParticle(@Nullable String systemId, float scale, @Nullable Color color, @Nonnull EntityPart targetEntityPart, @Nullable String targetNodeName, @Nullable Vector3f positionOffset, @Nullable Direction rotationOffset, boolean detachedFromModel)`
  - Creates a `ModelParticle` instance.
- `ModelParticle(@Nonnull ModelParticle other)`
  - Creates a `ModelParticle` instance.

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
