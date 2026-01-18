# DensityPointEvaluator

## Overview
- Documentation for `DensityPointEvaluator`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic.cell.evaluator`.

## Constructors
- `DensityPointEvaluator(PointEvaluator pointEvaluator, IDoubleCondition density)`
  - Creates a `DensityPointEvaluator` instance.
- `DensityPointEvaluator(PointEvaluator pointEvaluator, IIntCondition density)`
  - Creates a `DensityPointEvaluator` instance.

## Methods
- `getJitter()`
  - Executes `getJitter` behavior.
- `evalPoint(int seed, double x, double y, int cellHash, int cellX, int cellY, double cellPointX, double cellPointY, ResultBuffer.ResultBuffer2d buffer)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellHash, int cellX, int cellY, double cellPointX, double cellPointY, ResultBuffer.ResultBuffer2d buffer)`
  - Executes `evalPoint2` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, ResultBuffer.ResultBuffer3d buffer)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, ResultBuffer.ResultBuffer3d buffer)`
  - Executes `evalPoint2` behavior.
- `collectPoint(int cellHash, int cellX, int cellY, double x, double y, T t, @Nonnull PointConsumer<T> consumer)`
  - Executes `collectPoint` behavior.
- `toString()`
  - Executes `toString` behavior.
- `getDensityCondition(@Nullable IDoubleCondition threshold)`
  - Executes `getDensityCondition` behavior.
- `randomDensityCondition(int seed)`
  - Executes `randomDensityCondition` behavior.

## Notes
- No additional notes.
