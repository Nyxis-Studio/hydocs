# HexCellDistanceFunction

## Overview
- Documentation for `HexCellDistanceFunction`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic.cell`.

## Constructors
- `HexCellDistanceFunction()`
  - Creates a `HexCellDistanceFunction` instance.

## Methods
- `scale(double value)`
  - Executes `scale` behavior.
- `normalize(double value)`
  - Executes `normalize` behavior.
- `getHash(int seed, int cellX, int cellY)`
  - Executes `getHash` behavior.
- `getX(double x, double y)`
  - Executes `getX` behavior.
- `getY(double x, double y)`
  - Executes `getY` behavior.
- `invScale(double value)`
  - Executes `invScale` behavior.
- `getCellX(double x, double y)`
  - Executes `getCellX` behavior.
- `getCellY(double x, double y)`
  - Executes `getCellY` behavior.
- `nearest2D(int seed, double x, double y, int cellX, int cellY, @Nonnull ResultBuffer.ResultBuffer2d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `nearest2D` behavior.
- `nearest3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `nearest3D` behavior.
- `transition2D(int seed, double x, double y, int cellX, int cellY, @Nonnull ResultBuffer.ResultBuffer2d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `transition2D` behavior.
- `transition3D(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `transition3D` behavior.
- `evalPoint(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `evalPoint` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellX, int cellY, ResultBuffer.ResultBuffer2d buffer, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `evalPoint2` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellX, int cellY, int cellZ, ResultBuffer.ResultBuffer3d buffer, PointEvaluator pointEvaluator)`
  - Executes `evalPoint2` behavior.
- `collect(int originalSeed, int seed, int minX, int minY, int maxX, int maxY, @Nonnull ResultBuffer.Bounds2d bounds, T ctx, @Nonnull PointConsumer<T> collector, @Nonnull PointEvaluator pointEvaluator)`
  - Executes `collect` behavior.
- `toString()`
  - Executes `toString` behavior.
- `getHash(int seed, int x, int y)`
  - Executes `getHash` behavior.
- `toGridX(double x, double y)`
  - Executes `toGridX` behavior.
- `toGridY(double x, double y)`
  - Executes `toGridY` behavior.
- `toHexX(double hx, double hy)`
  - Executes `toHexX` behavior.
- `toHexY(double hx, double hy)`
  - Executes `toHexY` behavior.
- `hash(int seed, int x, int y)`
  - Executes `hash` behavior.

## Notes
- No additional notes.
