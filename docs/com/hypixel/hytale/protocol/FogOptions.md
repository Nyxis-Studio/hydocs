# FogOptions

## Overview
- Documentation for `FogOptions`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `FogOptions()`
  - Creates a `FogOptions` instance.
- `FogOptions(boolean ignoreFogLimits, float effectiveViewDistanceMultiplier, float fogFarViewDistance, float fogHeightCameraOffset, boolean fogHeightCameraOverriden, float fogHeightCameraFixed)`
  - Creates a `FogOptions` instance.
- `FogOptions(@Nonnull FogOptions other)`
  - Creates a `FogOptions` instance.

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
