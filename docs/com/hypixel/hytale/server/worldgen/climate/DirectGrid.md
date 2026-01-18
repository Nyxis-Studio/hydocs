# DirectGrid

## Overview
- Documentation for `DirectGrid`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.climate`.

## Constructors
- `DirectGrid()`
  - Creates a `DirectGrid` instance.

## Methods
- `nearest2D(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`
  - Executes `nearest2D` behavior.
- `nearest3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `nearest3D` behavior.
- `transition2D(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`
  - Executes `transition2D` behavior.
- `transition3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `transition3D` behavior.
- `evalPoint(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint2` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint2` behavior.
- `collect(int originalSeed, int seed, int minX, int minY, int maxX, int maxY, ResultBuffer.Bounds2d bounds, T ctx, PointConsumer<T> collector, PointEvaluator pointEvaluator)`
  - Executes `collect` behavior.

## Notes
- No additional notes.
