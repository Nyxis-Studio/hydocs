# Vector4d

## Overview
- Documentation for `Vector4d`.
- Declared as a class in `com.hypixel.hytale.math.vector`.

## Constructors
- `Vector4d()`
  - Creates a `Vector4d` instance.
- `Vector4d(double x, double y, double z, double w)`
  - Creates a `Vector4d` instance.
- `Vector4d(x, y, z, 1.0)`
  - Creates a `Vector4d` instance.
- `Vector4d(v.x, v.y, v.z, 1.0)`
  - Creates a `Vector4d` instance.
- `Vector4d(x, y, z, 0.0)`
  - Creates a `Vector4d` instance.

## Methods
- `newPosition(double x, double y, double z)`
  - Executes `newPosition` behavior.
- `newPosition(@Nonnull Vector3d v)`
  - Executes `newPosition` behavior.
- `newDirection(double x, double y, double z)`
  - Executes `newDirection` behavior.
- `setDirection()`
  - Executes `setDirection` behavior.
- `setPosition()`
  - Executes `setPosition` behavior.
- `assign(@Nonnull Vector4d v)`
  - Executes `assign` behavior.
- `assign(double x, double y, double z, double w)`
  - Executes `assign` behavior.
- `lerp(@Nonnull Vector4d dest, double lerpFactor, @Nonnull Vector4d target)`
  - Executes `lerp` behavior.
- `perspectiveTransform()`
  - Executes `perspectiveTransform` behavior.
- `isInsideFrustum()`
  - Executes `isInsideFrustum` behavior.
- `get(int component)`
  - Executes `get` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
