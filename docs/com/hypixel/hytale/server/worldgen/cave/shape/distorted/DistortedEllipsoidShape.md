# DistortedEllipsoidShape

## Overview
- Documentation for `DistortedEllipsoidShape`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave.shape.distorted`.

## Constructors
- `DistortedEllipsoidShape(@Nonnull Vector3d o, Vector3d d, double yaw, double pitch, double radiusX, double radiusY, double radiusZ, GeneralNoise.InterpolationFunction interpolation)`
  - Creates a `DistortedEllipsoidShape` instance.
- `DistortedEllipsoidShape(origin, direction, yaw, pitch, radiusX, radiusY, radiusZ, interpolation)`
  - Creates a `DistortedEllipsoidShape` instance.

## Methods
- `getAnchor(@Nonnull Vector3d vector, double tx, double ty, double tz)`
  - Executes `getAnchor` behavior.
- `getProjection(double x, double z)`
  - Executes `getProjection` behavior.
- `isValidProjection(double t)`
  - Executes `isValidProjection` behavior.
- `getYAt(double t)`
  - Executes `getYAt` behavior.
- `getWidthAt(double t)`
  - Executes `getWidthAt` behavior.
- `getHeightAt(double t)`
  - Executes `getHeightAt` behavior.
- `getHeight(int seed, double x, double z, double t, double centerY, CaveType caveType, @Nonnull ShapeDistortion distortion)`
  - Executes `getHeight` behavior.
- `toString()`
  - Executes `toString` behavior.
- `wrapPitch(double pitch, double radiusY, double radiusZ)`
  - Executes `wrapPitch` behavior.
- `createShape(@Nonnull Vector3d origin, Vector3d direction, double yaw, double pitch, double radiusX, double radiusY, double radiusZ, GeneralNoise.InterpolationFunction interpolation)`
  - Executes `createShape` behavior.

## Notes
- No additional notes.
