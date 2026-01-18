# CameraSettings

## Overview
- Documentation for `CameraSettings`.
- Declared as a class in `com.hypixel.hytale.protocol`.

## Constructors
- `CameraSettings()`
  - Creates a `CameraSettings` instance.
- `CameraSettings(@Nullable Vector3f positionOffset, @Nullable CameraAxis yaw, @Nullable CameraAxis pitch)`
  - Creates a `CameraSettings` instance.
- `CameraSettings(@Nonnull CameraSettings other)`
  - Creates a `CameraSettings` instance.

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
