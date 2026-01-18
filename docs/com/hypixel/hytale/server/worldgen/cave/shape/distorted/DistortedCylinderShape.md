# DistortedCylinderShape

## Overview
- Documentation for `DistortedCylinderShape`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave.shape.distorted`.

## Constructors
- `DistortedCylinderShape(@Nonnull Vector3d o, @Nonnull Vector3d v, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, GeneralNoise.InterpolationFunction interpolation)`
  - Creates a `DistortedCylinderShape` instance.
- `DistortedCylinderShape(@Nonnull Vector3d o, @Nonnull Vector3d v, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, double maxWidth, double maxHeight, GeneralNoise.InterpolationFunction interpolation)`
  - Creates a `DistortedCylinderShape` instance.
- `DistortedCylinderShape(origin, direction, startWidth, startHeight *= scale, midWidth, midHeight *= scale, endWidth, endHeight *= scale, interpolation)`
  - Creates a `DistortedCylinderShape` instance.

## Methods
- `getStart()`
  - Executes `getStart` behavior.
- `getEnd()`
  - Executes `getEnd` behavior.
- `getAnchor(@Nonnull Vector3d vector, double t, double tv, double th)`
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
- `getDistanceSq(double x, double z, double t)`
  - Executes `getDistanceSq` behavior.
- `getHeightComponent(double width, double width2, double dist2)`
  - Executes `getHeightComponent` behavior.
- `toString()`
  - Executes `toString` behavior.
- `getDimAt(double t, double startDim, double midDim, double endDim, @Nonnull GeneralNoise.InterpolationFunction interpolation)`
  - Executes `getDimAt` behavior.
- `getCompensationFactor(@Nonnull Vector3d direction)`
  - Executes `getCompensationFactor` behavior.
- `getHeightCompensation(double factor)`
  - Executes `getHeightCompensation` behavior.
- `create(@Nonnull Vector3d origin, @Nonnull Vector3d direction, double length, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, GeneralNoise.InterpolationFunction interpolation)`
  - Executes `create` behavior.

## Notes
- No additional notes.
