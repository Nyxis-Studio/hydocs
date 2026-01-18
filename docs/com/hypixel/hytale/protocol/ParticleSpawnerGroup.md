# ParticleSpawnerGroup

## Overview
- Documentation for `ParticleSpawnerGroup`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ParticleSpawnerGroup()`
  - Creates a `ParticleSpawnerGroup` instance.
- `ParticleSpawnerGroup(@Nullable String spawnerId, @Nullable Vector3f positionOffset, @Nullable Direction rotationOffset, boolean fixedRotation, float startDelay, @Nullable Rangef spawnRate, @Nullable Rangef waveDelay, int totalSpawners, int maxConcurrent, @Nullable InitialVelocity initialVelocity, @Nullable RangeVector3f emitOffset, @Nullable Rangef lifeSpan, @Nullable ParticleAttractor[] attractors)`
  - Creates a `ParticleSpawnerGroup` instance.
- `ParticleSpawnerGroup(@Nonnull ParticleSpawnerGroup other)`
  - Creates a `ParticleSpawnerGroup` instance.

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
