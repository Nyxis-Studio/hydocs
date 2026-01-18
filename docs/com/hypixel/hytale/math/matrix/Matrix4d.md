**Source Hash:** `9cb1b2bf085796d447ce0d683a5272c14a8552304019a6e80273989dcdb3da5e`

# Matrix4d

## Overview

## Constructor Descriptions
- `Matrix4d()`
  - Creates a `Matrix4d` instance.
- `Matrix4d(@Nonnull Matrix4d other)`
  - Creates a `Matrix4d` instance.
- `Matrix4d(double[] m)`
  - Creates a `Matrix4d` instance.

## Method Descriptions
- `get(int idx)`: Add description.
  - Executes `get` behavior.
- `get(int col, int row)`: Add description.
  - Executes `get` behavior.
- `set(int idx, double val)`: Add description.
  - Executes `set` behavior.
- `set(int col, int row, double val)`: Add description.
  - Executes `set` behavior.
- `add(int idx, double val)`: Add description.
  - Executes `add` behavior.
- `add(int col, int row, double val)`: Add description.
  - Executes `add` behavior.
- `identity()`: Add description.
  - Executes `identity` behavior.
- `assign(@Nonnull Matrix4d other)`: Add description.
  - Executes `assign` behavior.
- `assign(double m00, double m10, double m20, double m30, double m01, double m11, double m21, double m31, double m02, double m12, double m22, double m32, double m03, double m13, double m23, double m33)`: Add description.
  - Executes `assign` behavior.
- `translate(@Nonnull Vector3d vec)`: Add description.
  - Executes `translate` behavior.
- `translate(double x, double y, double z)`: Add description.
  - Executes `translate` behavior.
- `scale(double x, double y, double z)`: Add description.
  - Executes `scale` behavior.
- `multiplyPosition(@Nonnull Vector3d vec)`: Add description.
  - Executes `multiplyPosition` behavior.
- `multiplyPosition(@Nonnull Vector3d vec, @Nonnull Vector3d result)`: Add description.
  - Executes `multiplyPosition` behavior.
- `multiplyDirection(@Nonnull Vector3d vec)`: Add description.
  - Executes `multiplyDirection` behavior.
- `multiply(@Nonnull Vector4d vec)`: Add description.
  - Executes `multiply` behavior.
- `multiply(@Nonnull Vector4d vec, @Nonnull Vector4d result)`: Add description.
  - Executes `multiply` behavior.
- `multiply(@Nonnull Matrix4d other)`: Add description.
  - Executes `multiply` behavior.
- `invert()`: Add description.
  - Executes `invert` behavior.
- `projectionOrtho(double left, double right, double bottom, double top, double near, double far)`: Add description.
  - Executes `projectionOrtho` behavior.
- `projectionFrustum(double left, double right, double bottom, double top, double near, double far)`: Add description.
  - Executes `projectionFrustum` behavior.
- `projectionCone(double fov, double aspect, double near, double far)`: Add description.
  - Executes `projectionCone` behavior.
- `viewTarget(double eyeX, double eyeY, double eyeZ, double centerX, double centerY, double centerZ, double upX, double upY, double upZ)`: Add description.
  - Executes `viewTarget` behavior.
- `viewDirection(double eyeX, double eyeY, double eyeZ, double dirX, double dirY, double dirZ, double upX, double upY, double upZ)`: Add description.
  - Executes `viewDirection` behavior.
- `rotateAxis(double a, double x, double y, double z, @Nonnull Matrix4d tmp)`: Add description.
  - Executes `rotateAxis` behavior.
- `setRotateAxis(double a, double x, double y, double z)`: Add description.
  - Executes `setRotateAxis` behavior.
- `rotateEuler(double x, double y, double z, @Nonnull Matrix4d tmp)`: Add description.
  - Executes `rotateEuler` behavior.
- `setRotateEuler(double x, double y, double z)`: Add description.
  - Executes `setRotateEuler` behavior.
- `getData()`: Add description.
  - Executes `getData` behavior.
- `asFloatData()`: Add description.
  - Executes `asFloatData` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `idx(int col, int row)`: Add description.
  - Executes `idx` behavior.

## Notes
- No additional notes.
