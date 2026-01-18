# SkipCellPointEvaluator

## Overview
- Documentation for `SkipCellPointEvaluator`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic.cell.evaluator`.

## Constructors
- `SkipCellPointEvaluator(@Nonnull PointEvaluator pointEvaluator, @Nonnull Mode mode, int period)`
  - Creates a `SkipCellPointEvaluator` instance.

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
- `collectPoint(int cellHash, int cellX, int cellY, double cellCentreX, double cellCentreY, T ctx, @NonNullDecl PointConsumer<T> consumer)`
  - Executes `collectPoint` behavior.
- `skip(Mode mode, int cx, int cy)`
  - Executes `skip` behavior.

## Notes
- No additional notes.
