# ParticleSpawner

## Overview
- Documentation for `ParticleSpawner`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ParticleSpawner()`
  - Creates a `ParticleSpawner` instance.
- `ParticleSpawner(@Nullable String id, @Nullable Particle particle, @Nonnull EmitShape shape, @Nullable RangeVector3f emitOffset, float cameraOffset, boolean useEmitDirection, float lifeSpan, @Nullable Rangef spawnRate, boolean spawnBurst, @Nullable Rangef waveDelay, @Nullable Range totalParticles, int maxConcurrentParticles, @Nullable InitialVelocity initialVelocity, float velocityStretchMultiplier, @Nonnull ParticleRotationInfluence particleRotationInfluence, boolean particleRotateWithSpawner, boolean isLowRes, float trailSpawnerPositionMultiplier, float trailSpawnerRotationMultiplier, @Nullable ParticleCollision particleCollision, @Nonnull FXRenderMode renderMode, float lightInfluence, boolean linearFiltering, @Nullable Rangef particleLifeSpan, @Nullable UVMotion uvMotion, @Nullable ParticleAttractor[] attractors, @Nullable IntersectionHighlight intersectionHighlight)`
  - Creates a `ParticleSpawner` instance.
- `ParticleSpawner(@Nonnull ParticleSpawner other)`
  - Creates a `ParticleSpawner` instance.

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
