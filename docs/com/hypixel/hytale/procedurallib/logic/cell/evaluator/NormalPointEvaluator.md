# NormalPointEvaluator

## Overview
- Documentation for `NormalPointEvaluator`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic.cell.evaluator`.

## Constructors
- `NormalPointEvaluator(DistanceCalculationMode.EUCLIDEAN.getFunction()`
  - Creates a `NormalPointEvaluator` instance.
- `NormalPointEvaluator(DistanceCalculationMode.MANHATTAN.getFunction()`
  - Creates a `NormalPointEvaluator` instance.
- `NormalPointEvaluator(DistanceCalculationMode.NATURAL.getFunction()`
  - Creates a `NormalPointEvaluator` instance.
- `NormalPointEvaluator(DistanceCalculationMode.MAX.getFunction()`
  - Creates a `NormalPointEvaluator` instance.
- `NormalPointEvaluator(PointDistanceFunction distanceFunction)`
  - Creates a `NormalPointEvaluator` instance.
- `NormalPointEvaluator(distanceFunction)`
  - Creates a `NormalPointEvaluator` instance.

## Methods
- `evalPoint(int seed, double x, double y, int cellHash, int cellX, int cellY, double cellPointX, double cellPointY, @Nonnull ResultBuffer.ResultBuffer2d buffer)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellHash, int cellX, int cellY, double cellPointX, double cellPointY, @Nonnull ResultBuffer.ResultBuffer2d buffer)`
  - Executes `evalPoint2` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, @Nonnull ResultBuffer.ResultBuffer3d buffer)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, @Nonnull ResultBuffer.ResultBuffer3d buffer)`
  - Executes `evalPoint2` behavior.
- `toString()`
  - Executes `toString` behavior.
- `of(PointDistanceFunction distanceFunction)`
  - Executes `of` behavior.

## Notes
- No additional notes.
