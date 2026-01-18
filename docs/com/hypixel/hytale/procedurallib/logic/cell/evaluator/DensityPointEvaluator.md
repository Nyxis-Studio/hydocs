**Source Hash:** `fdea9be7a1dc2f883521e0fd6cb9750959a37f2599c6838ed896d2c816deaebb`

# DensityPointEvaluator

## Overview

## Constructor Descriptions
- `DensityPointEvaluator(PointEvaluator pointEvaluator, IDoubleCondition density)`
  - Creates a `DensityPointEvaluator` instance.
- `DensityPointEvaluator(PointEvaluator pointEvaluator, IIntCondition density)`
  - Creates a `DensityPointEvaluator` instance.

## Method Descriptions
- `getJitter()`: Add description.
  - Executes `getJitter` behavior.
- `evalPoint(int seed, double x, double y, int cellHash, int cellX, int cellY, double cellPointX, double cellPointY, ResultBuffer.ResultBuffer2d buffer)`: Add description.
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellHash, int cellX, int cellY, double cellPointX, double cellPointY, ResultBuffer.ResultBuffer2d buffer)`: Add description.
  - Executes `evalPoint2` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, ResultBuffer.ResultBuffer3d buffer)`: Add description.
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, ResultBuffer.ResultBuffer3d buffer)`: Add description.
  - Executes `evalPoint2` behavior.
- `collectPoint(int cellHash, int cellX, int cellY, double x, double y, T t, @Nonnull PointConsumer<T> consumer)`: Add description.
  - Executes `collectPoint` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `getDensityCondition(@Nullable IDoubleCondition threshold)`: Add description.
  - Executes `getDensityCondition` behavior.
- `randomDensityCondition(int seed)`: Add description.
  - Executes `randomDensityCondition` behavior.

## Notes
- No additional notes.
