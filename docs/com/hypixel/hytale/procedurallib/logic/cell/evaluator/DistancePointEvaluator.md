# DistancePointEvaluator

## Overview
- Documentation for `DistancePointEvaluator`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic.cell.evaluator`.

## Constructors
- `DistancePointEvaluator(PointDistanceFunction distanceFunction, IDoubleRange distanceMod)`
  - Creates a `DistancePointEvaluator` instance.
- `DistancePointEvaluator(PointDistanceFunction distanceFunction, ISeedDoubleRange distanceMod)`
  - Creates a `DistancePointEvaluator` instance.

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
- `getDistanceModifier(@Nullable IDoubleRange range)`
  - Executes `getDistanceModifier` behavior.
- `randomDistanceModification(int seed)`
  - Executes `randomDistanceModification` behavior.

## Notes
- No additional notes.
