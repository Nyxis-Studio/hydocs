# CameraShakeConfig

## Overview
- Documentation for `CameraShakeConfig`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `CameraShakeConfig()`
  - Creates a `CameraShakeConfig` instance.
- `CameraShakeConfig(float duration, float startTime, boolean continuous, @Nullable EasingConfig easeIn, @Nullable EasingConfig easeOut, @Nullable OffsetNoise offset, @Nullable RotationNoise rotation)`
  - Creates a `CameraShakeConfig` instance.
- `CameraShakeConfig(@Nonnull CameraShakeConfig other)`
  - Creates a `CameraShakeConfig` instance.

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
