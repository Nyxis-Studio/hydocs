# BorderDistanceFunction

## Overview
- Documentation for `BorderDistanceFunction`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic.cell`.

## Constructors
- `BorderDistanceFunction(CellDistanceFunction distanceFunction, @Nonnull PointEvaluator borderEvaluator, IDoubleCondition density)`
  - Creates a `BorderDistanceFunction` instance.

## Methods
- `scale(double value)`
  - Executes `scale` behavior.
- `invScale(double value)`
  - Executes `invScale` behavior.
- `getCellX(double x, double y)`
  - Executes `getCellX` behavior.
- `getCellY(double x, double y)`
  - Executes `getCellY` behavior.
- `nearest2D(int seed, double x, double y, int cellX, int cellY, @Nonnull ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`
  - Executes `nearest2D` behavior.
- `transition2D(int seed, double x, double y, int cellX, int cellY, @Nonnull ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`
  - Executes `transition2D` behavior.
- `nearest3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `nearest3D` behavior.
- `transition3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `transition3D` behavior.
- `evalPoint(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint2` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint2` behavior.
- `collect(int originalSeed, int seed, int minX, int minY, int maxX, int maxY, ResultBuffer.Bounds2d bounds, T ctx, PointConsumer<T> collector, PointEvaluator pointEvaluator)`
  - Executes `collect` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
