# Transform

## Overview
- Documentation for `Transform`.
- Declared as a class in `com.hypixel.hytale.math.vector`.

## Constructors
- `Transform()`
  - Creates a `Transform` instance.
- `Transform(@Nonnull Vector3i position)`
  - Creates a `Transform` instance.
- `Transform(@Nonnull Vector3d position)`
  - Creates a `Transform` instance.
- `Transform(double x, double y, double z)`
  - Creates a `Transform` instance.
- `Transform(double x, double y, double z, float pitch, float yaw, float roll)`
  - Creates a `Transform` instance.
- `Transform(@Nonnull Vector3d position, @Nonnull Vector3f rotation)`
  - Creates a `Transform` instance.
- `Transform(this.position.clone()`
  - Creates a `Transform` instance.

## Methods
- `assign(@Nonnull Transform transform)`
  - Executes `assign` behavior.
- `getPosition()`
  - Executes `getPosition` behavior.
- `setPosition(@Nonnull Vector3d position)`
  - Executes `setPosition` behavior.
- `getRotation()`
  - Executes `getRotation` behavior.
- `setRotation(@Nonnull Vector3f rotation)`
  - Executes `setRotation` behavior.
- `getDirection()`
  - Executes `getDirection` behavior.
- `getDirection(float pitch, float yaw)`
  - Executes `getDirection` behavior.
- `getAxisDirection()`
  - Executes `getAxisDirection` behavior.
- `getAxisDirection(float pitch, float yaw)`
  - Executes `getAxisDirection` behavior.
- `getAxis()`
  - Executes `getAxis` behavior.
- `clone()`
  - Executes `clone` behavior.
- `equals(@Nullable Object o)`
  - Executes `equals` behavior.
- `hashCode()`
  - Executes `hashCode` behavior.
- `toString()`
  - Executes `toString` behavior.
- `applyMaskedRelativeTransform(@Nonnull Transform transform, byte relativeMask, @Nonnull Vector3d sourcePosition, @Nonnull Vector3f sourceRotation, @Nonnull Vector3i blockPosition)`
  - Executes `applyMaskedRelativeTransform` behavior.

## Notes
- No additional notes.
