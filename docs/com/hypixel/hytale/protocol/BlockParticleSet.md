# BlockParticleSet

## Overview
- Documentation for `BlockParticleSet`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `BlockParticleSet()`
  - Creates a `BlockParticleSet` instance.
- `BlockParticleSet(@Nullable String id, @Nullable Color color, float scale, @Nullable Vector3f positionOffset, @Nullable Direction rotationOffset, @Nullable Map<BlockParticleEvent, String> particleSystemIds)`
  - Creates a `BlockParticleSet` instance.
- `BlockParticleSet(@Nonnull BlockParticleSet other)`
  - Creates a `BlockParticleSet` instance.

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
