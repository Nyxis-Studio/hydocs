# Matrix4d

## Overview
- Documentation for `Matrix4d`.
- Declared as a class in `com.hypixel.hytale.math.matrix`.

## Constructors
- `Matrix4d()`
  - Creates a `Matrix4d` instance.
- `Matrix4d(@Nonnull Matrix4d other)`
  - Creates a `Matrix4d` instance.
- `Matrix4d(double[] m)`
  - Creates a `Matrix4d` instance.

## Methods
- `get(int idx)`
  - Executes `get` behavior.
- `get(int col, int row)`
  - Executes `get` behavior.
- `set(int idx, double val)`
  - Executes `set` behavior.
- `set(int col, int row, double val)`
  - Executes `set` behavior.
- `add(int idx, double val)`
  - Executes `add` behavior.
- `add(int col, int row, double val)`
  - Executes `add` behavior.
- `identity()`
  - Executes `identity` behavior.
- `assign(@Nonnull Matrix4d other)`
  - Executes `assign` behavior.
- `assign(double m00, double m10, double m20, double m30, double m01, double m11, double m21, double m31, double m02, double m12, double m22, double m32, double m03, double m13, double m23, double m33)`
  - Executes `assign` behavior.
- `translate(@Nonnull Vector3d vec)`
  - Executes `translate` behavior.
- `translate(double x, double y, double z)`
  - Executes `translate` behavior.
- `scale(double x, double y, double z)`
  - Executes `scale` behavior.
- `multiplyPosition(@Nonnull Vector3d vec)`
  - Executes `multiplyPosition` behavior.
- `multiplyPosition(@Nonnull Vector3d vec, @Nonnull Vector3d result)`
  - Executes `multiplyPosition` behavior.
- `multiplyDirection(@Nonnull Vector3d vec)`
  - Executes `multiplyDirection` behavior.
- `multiply(@Nonnull Vector4d vec)`
  - Executes `multiply` behavior.
- `multiply(@Nonnull Vector4d vec, @Nonnull Vector4d result)`
  - Executes `multiply` behavior.
- `multiply(@Nonnull Matrix4d other)`
  - Executes `multiply` behavior.
- `invert()`
  - Executes `invert` behavior.
- `projectionOrtho(double left, double right, double bottom, double top, double near, double far)`
  - Executes `projectionOrtho` behavior.
- `projectionFrustum(double left, double right, double bottom, double top, double near, double far)`
  - Executes `projectionFrustum` behavior.
- `projectionCone(double fov, double aspect, double near, double far)`
  - Executes `projectionCone` behavior.
- `viewTarget(double eyeX, double eyeY, double eyeZ, double centerX, double centerY, double centerZ, double upX, double upY, double upZ)`
  - Executes `viewTarget` behavior.
- `viewDirection(double eyeX, double eyeY, double eyeZ, double dirX, double dirY, double dirZ, double upX, double upY, double upZ)`
  - Executes `viewDirection` behavior.
- `rotateAxis(double a, double x, double y, double z, @Nonnull Matrix4d tmp)`
  - Executes `rotateAxis` behavior.
- `setRotateAxis(double a, double x, double y, double z)`
  - Executes `setRotateAxis` behavior.
- `rotateEuler(double x, double y, double z, @Nonnull Matrix4d tmp)`
  - Executes `rotateEuler` behavior.
- `setRotateEuler(double x, double y, double z)`
  - Executes `setRotateEuler` behavior.
- `getData()`
  - Executes `getData` behavior.
- `asFloatData()`
  - Executes `asFloatData` behavior.
- `toString()`
  - Executes `toString` behavior.
- `idx(int col, int row)`
  - Executes `idx` behavior.

## Notes
- No additional notes.
