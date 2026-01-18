# DistortedPipeShape

## Overview
- Documentation for `DistortedPipeShape`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cave.shape.distorted`.

## Constructors
- `DistortedPipeShape(@Nonnull Vector3d o, @Nonnull Vector3d v, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, double maxWidth, double maxHeight, double compensation, GeneralNoise.InterpolationFunction interpolation)`
  - Creates a `DistortedPipeShape` instance.
- `DistortedPipeShape(origin, direction, startWidth, startHeight, midWidth, midHeight, endWidth, endHeight, maxWidth, maxHeight, compensation, interpolation)`
  - Creates a `DistortedPipeShape` instance.

## Methods
- `getWidthAt(double t)`
  - Executes `getWidthAt` behavior.
- `getHeightAt(double t)`
  - Executes `getHeightAt` behavior.
- `isValidProjection(double t)`
  - Executes `isValidProjection` behavior.
- `toString()`
  - Executes `toString` behavior.
- `getCompensatedDim(double t, double startDim, double midDim, double endDim, double compensation, @Nonnull GeneralNoise.InterpolationFunction interpolation)`
  - Executes `getCompensatedDim` behavior.
- `create(@Nonnull Vector3d origin, @Nonnull Vector3d direction, double length, double startWidth, double startHeight, double midWidth, double midHeight, double endWidth, double endHeight, GeneralNoise.InterpolationFunction interpolation)`
  - Executes `create` behavior.

## Notes
- No additional notes.
