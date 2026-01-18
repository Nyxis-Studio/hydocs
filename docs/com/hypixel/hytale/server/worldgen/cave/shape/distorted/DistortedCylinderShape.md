**Source Hash:** `29a6147ebc8b9c956f7f1e2bf60b6bf0bdebfdefaac33396fe9fc2ff1c2a94f3`

# DistortedCylinderShape

## Overview

## Constructor Descriptions
- `DistortedCylinderShape(@Nonnull Vector3d o, @Nonnull Vector3d v, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, GeneralNoise.InterpolationFunction interpolation)`
  - Creates a `DistortedCylinderShape` instance.
- `DistortedCylinderShape(@Nonnull Vector3d o, @Nonnull Vector3d v, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, double maxWidth, double maxHeight, GeneralNoise.InterpolationFunction interpolation)`
  - Creates a `DistortedCylinderShape` instance.
- `DistortedCylinderShape(origin, direction, startWidth, startHeight *= scale, midWidth, midHeight *= scale, endWidth, endHeight *= scale, interpolation)`
  - Creates a `DistortedCylinderShape` instance.

## Method Descriptions
- `getStart()`: Add description.
  - Executes `getStart` behavior.
- `getEnd()`: Add description.
  - Executes `getEnd` behavior.
- `getAnchor(@Nonnull Vector3d vector, double t, double tv, double th)`: Add description.
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
- `getDistanceSq(double x, double z, double t)`: Add description.
  - Executes `getDistanceSq` behavior.
- `getHeightComponent(double width, double width2, double dist2)`: Add description.
  - Executes `getHeightComponent` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `getDimAt(double t, double startDim, double midDim, double endDim, @Nonnull GeneralNoise.InterpolationFunction interpolation)`: Add description.
  - Executes `getDimAt` behavior.
- `getCompensationFactor(@Nonnull Vector3d direction)`: Add description.
  - Executes `getCompensationFactor` behavior.
- `getHeightCompensation(double factor)`: Add description.
  - Executes `getHeightCompensation` behavior.
- `create(@Nonnull Vector3d origin, @Nonnull Vector3d direction, double length, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, GeneralNoise.InterpolationFunction interpolation)`: Add description.
  - Executes `create` behavior.

## Notes
- No additional notes.
