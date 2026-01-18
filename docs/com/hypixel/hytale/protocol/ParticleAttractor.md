# ParticleAttractor

## Overview
- Documentation for `ParticleAttractor`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ParticleAttractor()`
  - Creates a `ParticleAttractor` instance.
- `ParticleAttractor(@Nullable Vector3f position, @Nullable Vector3f radialAxis, float trailPositionMultiplier, float radius, float radialAcceleration, float radialTangentAcceleration, @Nullable Vector3f linearAcceleration, float radialImpulse, float radialTangentImpulse, @Nullable Vector3f linearImpulse, @Nullable Vector3f dampingMultiplier)`
  - Creates a `ParticleAttractor` instance.
- `ParticleAttractor(@Nonnull ParticleAttractor other)`
  - Creates a `ParticleAttractor` instance.

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
