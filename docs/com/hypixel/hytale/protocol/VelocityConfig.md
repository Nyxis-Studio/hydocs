# VelocityConfig

## Overview
- Documentation for `VelocityConfig`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `VelocityConfig()`
  - Creates a `VelocityConfig` instance.
- `VelocityConfig(float groundResistance, float groundResistanceMax, float airResistance, float airResistanceMax, float threshold, @Nonnull VelocityThresholdStyle style)`
  - Creates a `VelocityConfig` instance.
- `VelocityConfig(@Nonnull VelocityConfig other)`
  - Creates a `VelocityConfig` instance.

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
