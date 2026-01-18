**Source Hash:** `7df0354bf81904e3e1e12dedd8b1593aeb94974547e9eed594f2f066de6439ee`

# DistortedEllipsoidShape

## Overview

## Constructor Descriptions
- `DistortedEllipsoidShape(@Nonnull Vector3d o, Vector3d d, double yaw, double pitch, double radiusX, double radiusY, double radiusZ, GeneralNoise.InterpolationFunction interpolation)`
  - Creates a `DistortedEllipsoidShape` instance.
- `DistortedEllipsoidShape(origin, direction, yaw, pitch, radiusX, radiusY, radiusZ, interpolation)`
  - Creates a `DistortedEllipsoidShape` instance.

## Method Descriptions
- `getAnchor(@Nonnull Vector3d vector, double tx, double ty, double tz)`: Add description.
  - Executes `getAnchor` behavior.
- `getProjection(double x, double z)`: Add description.
  - Executes `getProjection` behavior.
- `isValidProjection(double t)`: Add description.
  - Executes `isValidProjection` behavior.
- `getYAt(double t)`: Add description.
  - Executes `getYAt` behavior.
- `getWidthAt(double t)`: Add description.
  - Executes `getWidthAt` behavior.
- `getHeightAt(double t)`: Add description.
  - Executes `getHeightAt` behavior.
- `getHeight(int seed, double x, double z, double t, double centerY, CaveType caveType, @Nonnull ShapeDistortion distortion)`: Add description.
  - Executes `getHeight` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `wrapPitch(double pitch, double radiusY, double radiusZ)`: Add description.
  - Executes `wrapPitch` behavior.
- `createShape(@Nonnull Vector3d origin, Vector3d direction, double yaw, double pitch, double radiusX, double radiusY, double radiusZ, GeneralNoise.InterpolationFunction interpolation)`: Add description.
  - Executes `createShape` behavior.

## Notes
- No additional notes.
