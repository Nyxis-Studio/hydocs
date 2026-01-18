# Particle

## Overview
- Documentation for `Particle`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `Particle()`
  - Creates a `Particle` instance.
- `Particle(@Nullable String texturePath, @Nullable Size frameSize, @Nonnull ParticleUVOption uvOption, @Nonnull ParticleScaleRatioConstraint scaleRatioConstraint, @Nonnull SoftParticle softParticles, float softParticlesFadeFactor, boolean useSpriteBlending, @Nullable ParticleAnimationFrame initialAnimationFrame, @Nullable ParticleAnimationFrame collisionAnimationFrame, @Nullable Map<Integer, ParticleAnimationFrame> animationFrames)`
  - Creates a `Particle` instance.
- `Particle(@Nonnull Particle other)`
  - Creates a `Particle` instance.

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
