# NoiseConfig

## Overview
- Documentation for `NoiseConfig`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `NoiseConfig()`
  - Creates a `NoiseConfig` instance.
- `NoiseConfig(int seed, @Nonnull NoiseType type, float frequency, float amplitude, @Nullable ClampConfig clamp)`
  - Creates a `NoiseConfig` instance.
- `NoiseConfig(@Nonnull NoiseConfig other)`
  - Creates a `NoiseConfig` instance.

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
