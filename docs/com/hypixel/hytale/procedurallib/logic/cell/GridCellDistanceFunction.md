# GridCellDistanceFunction

## Overview
- Documentation for `GridCellDistanceFunction`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic.cell`.

## Constructors
- `GridCellDistanceFunction()`
  - Creates a `GridCellDistanceFunction` instance.

## Methods
- `getHash(int seed, int cellX, int cellY)`
  - Executes `getHash` behavior.
- `getX(double x, double y)`
  - Executes `getX` behavior.
- `getY(double x, double y)`
  - Executes `getY` behavior.
- `nearest2D(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `nearest2D` behavior.
- `nearest3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `nearest3D` behavior.
- `transition2D(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `transition2D` behavior.
- `transition3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `transition3D` behavior.
- `evalPoint(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `evalPoint` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `evalPoint2` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `evalPoint2` behavior.
- `collect(int originalSeed, int seed, int minX, int minY, int maxX, int maxY, ResultBuffer.Bounds2d bounds, T ctx, @Nonnull PointConsumer<T> collector, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `collect` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
