# ParticleCollision

## Overview
- Documentation for `ParticleCollision`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ParticleCollision()`
  - Creates a `ParticleCollision` instance.
- `ParticleCollision(@Nonnull ParticleCollisionBlockType blockType, @Nonnull ParticleCollisionAction action, @Nonnull ParticleRotationInfluence particleRotationInfluence)`
  - Creates a `ParticleCollision` instance.
- `ParticleCollision(@Nonnull ParticleCollision other)`
  - Creates a `ParticleCollision` instance.

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
