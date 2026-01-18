# Rotation

## Overview
- Documentation for `Rotation`.
- Declared as a enum in `com.hypixel.hytale.server.core.asset.type.blocktype.config`.

## Constructors
- `Rotation(int degrees, com.hypixel.hytale.protocol.Rotation packet, Axis axisOfAlignment, Vector3i axisDirection)`
  - Creates a `Rotation` instance.

## Methods
- `getDegrees()`
  - Executes `getDegrees` behavior.
- `getRadians()`
  - Executes `getRadians` behavior.
- `getAxisOfAlignment()`
  - Executes `getAxisOfAlignment` behavior.
- `getAxisDirection()`
  - Executes `getAxisDirection` behavior.
- `flip()`
  - Executes `flip` behavior.
- `flip(Axis axis)`
  - Executes `flip` behavior.
- `subtract(@Nullable Rotation rotation)`
  - Executes `subtract` behavior.
- `add(@Nullable Rotation rotation)`
  - Executes `add` behavior.
- `add(@Nullable Rotation a, Rotation b)`
  - Executes `add` behavior.
- `rotatePitch(@Nonnull Vector3i in, @Nonnull Vector3i out)`
  - Executes `rotatePitch` behavior.
- `rotatePitch(@Nonnull Vector3f in, @Nonnull Vector3f out)`
  - Executes `rotatePitch` behavior.
- `rotateX(int filler)`
  - Executes `rotateX` behavior.
- `rotateX(@Nonnull Vector3i in, @Nonnull Vector3i out)`
  - Executes `rotateX` behavior.
- `rotateX(@Nonnull Vector3f in, @Nonnull Vector3f out)`
  - Executes `rotateX` behavior.
- `rotateX(@Nonnull Vector3d in, @Nonnull Vector3d out)`
  - Executes `rotateX` behavior.
- `rotateYaw(@Nonnull Vector3i in, @Nonnull Vector3i out)`
  - Executes `rotateYaw` behavior.
- `rotateYaw(@Nonnull Vector3f in, @Nonnull Vector3f out)`
  - Executes `rotateYaw` behavior.
- `rotateY(int filler)`
  - Executes `rotateY` behavior.
- `rotateY(@Nonnull Vector3i in, @Nonnull Vector3i out)`
  - Executes `rotateY` behavior.
- `rotateY(@Nonnull Vector3f in, @Nonnull Vector3f out)`
  - Executes `rotateY` behavior.
- `rotateY(@Nonnull Vector3d in, @Nonnull Vector3d out)`
  - Executes `rotateY` behavior.
- `rotateRoll(@Nonnull Vector3i in, @Nonnull Vector3i out)`
  - Executes `rotateRoll` behavior.
- `rotateRoll(@Nonnull Vector3f in, @Nonnull Vector3f out)`
  - Executes `rotateRoll` behavior.
- `rotateZ(int filler)`
  - Executes `rotateZ` behavior.
- `rotateZ(@Nonnull Vector3i in, @Nonnull Vector3i out)`
  - Executes `rotateZ` behavior.
- `rotateZ(@Nonnull Vector3f in, @Nonnull Vector3f out)`
  - Executes `rotateZ` behavior.
- `rotateZ(@Nonnull Vector3d in, @Nonnull Vector3d out)`
  - Executes `rotateZ` behavior.
- `ofDegrees(int degrees)`
  - Executes `ofDegrees` behavior.
- `closestOfDegrees(float degrees)`
  - Executes `closestOfDegrees` behavior.
- `valueOf(@Nonnull com.hypixel.hytale.protocol.Rotation packet)`
  - Executes `valueOf` behavior.
- `rotate(@Nonnull Vector3i vector3i, @Nonnull Rotation rotationYaw, @Nonnull Rotation rotationPitch)`
  - Executes `rotate` behavior.
- `rotate(@Nonnull Vector3i vector3i, @Nonnull Rotation rotationYaw, @Nonnull Rotation rotationPitch, @Nonnull Rotation rotationRoll)`
  - Executes `rotate` behavior.
- `rotate(@Nonnull Vector3f vector3f, @Nonnull Rotation rotationYaw, @Nonnull Rotation rotationPitch, @Nonnull Rotation rotationRoll)`
  - Executes `rotate` behavior.
- `rotate(@Nonnull Vector3d vector3d, @Nonnull Rotation rotationYaw, @Nonnull Rotation rotationPitch, @Nonnull Rotation rotationRoll)`
  - Executes `rotate` behavior.

## Notes
- No additional notes.
