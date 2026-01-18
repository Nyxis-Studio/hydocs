# AbstractDistortedBody

## Overview
- Documentation for `AbstractDistortedBody`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave.shape.distorted`.

## Constructors
- `AbstractDistortedBody(@Nonnull Vector3d o, Vector3d v, double yaw, double pitch, double radiusX, double radiusY, double radiusZ)`
  - Creates a `AbstractDistortedBody` instance.
- `AbstractDistortedBody(@Nonnull Vector3d o, Vector3d v, @Nonnull CoordinateRotator rotation, double radiusX, double radiusY, double radiusZ)`
  - Creates a `AbstractDistortedBody` instance.

## Methods
- `getHeight(int var1, double var2, double var4, double var6, double var8, CaveType var10, ShapeDistortion var11)`
  - Executes `getHeight` behavior.
- `getStart()`
  - Executes `getStart` behavior.
- `getEnd()`
  - Executes `getEnd` behavior.
- `getHeightAtProjection(int caveSeed, double x, double z, double t, double centerY, CaveType caveType, ShapeDistortion distortion)`
  - Executes `getHeightAtProjection` behavior.
- `getFloor(double x, double z, double centerY, double height)`
  - Executes `getFloor` behavior.
- `getCeiling(double x, double z, double centerY, double height)`
  - Executes `getCeiling` behavior.
- `maxX(@Nonnull CoordinateRotator rotation, double radiusX, double radiusY, double radiusZ)`
  - Executes `maxX` behavior.
- `maxY(@Nonnull CoordinateRotator rotation, double radiusX, double radiusY, double radiusZ)`
  - Executes `maxY` behavior.
- `maxZ(@Nonnull CoordinateRotator rotation, double radiusX, double radiusY, double radiusZ)`
  - Executes `maxZ` behavior.
- `create(Vector3d origin, @Nonnull Vector3d direction, double length, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, GeneralNoise.InterpolationFunction interpolation)`
  - Executes `create` behavior.
- `createShape(Vector3d var1, Vector3d var2, double var3, double var5, double var7, double var9, double var11, GeneralNoise.InterpolationFunction var13)`
  - Executes `createShape` behavior.

## Notes
- No additional notes.
