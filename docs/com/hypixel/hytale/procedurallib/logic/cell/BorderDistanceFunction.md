**Source Hash:** `f0d9be732f5399d3955760f611053acfbac85a7dd32d891b7e163dddabe68067`

# BorderDistanceFunction

## Overview

## Constructor Descriptions
- `BorderDistanceFunction(CellDistanceFunction distanceFunction, @Nonnull PointEvaluator borderEvaluator, IDoubleCondition density)`
  - Creates a `BorderDistanceFunction` instance.

## Method Descriptions
- `scale(double value)`: Add description.
  - Executes `scale` behavior.
- `invScale(double value)`: Add description.
  - Executes `invScale` behavior.
- `getCellX(double x, double y)`: Add description.
  - Executes `getCellX` behavior.
- `getCellY(double x, double y)`: Add description.
  - Executes `getCellY` behavior.
- `nearest2D(int seed, double x, double y, int cellX, int cellY, @Nonnull ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`: Add description.
  - Executes `nearest2D` behavior.
- `transition2D(int seed, double x, double y, int cellX, int cellY, @Nonnull ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`: Add description.
  - Executes `transition2D` behavior.
- `nearest3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`: Add description.
  - Executes `nearest3D` behavior.
- `transition3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`: Add description.
  - Executes `transition3D` behavior.
- `evalPoint(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`: Add description.
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`: Add description.
  - Executes `evalPoint2` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`: Add description.
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`: Add description.
  - Executes `evalPoint2` behavior.
- `collect(int originalSeed, int seed, int minX, int minY, int maxX, int maxY, ResultBuffer.Bounds2d bounds, T ctx, PointConsumer<T> collector, PointEvaluator pointEvaluator)`: Add description.
  - Executes `collect` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
