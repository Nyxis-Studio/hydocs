# ParticleSystem

## Overview
- Documentation for `ParticleSystem`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `ParticleSystem()`
  - Creates a `ParticleSystem` instance.
- `ParticleSystem(@Nullable String id, @Nullable ParticleSpawnerGroup[] spawners, float lifeSpan, float cullDistance, float boundingRadius, boolean isImportant)`
  - Creates a `ParticleSystem` instance.
- `ParticleSystem(@Nonnull ParticleSystem other)`
  - Creates a `ParticleSystem` instance.

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
