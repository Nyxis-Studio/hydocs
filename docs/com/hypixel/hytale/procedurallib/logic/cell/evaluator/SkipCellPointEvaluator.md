**Source Hash:** `0504a8b8adf53d92343bd740b882903da2effe019b0bbd17fe3ce22e899d0fff`

# SkipCellPointEvaluator

## Overview

## Constructor Descriptions
- `SkipCellPointEvaluator(@Nonnull PointEvaluator pointEvaluator, @Nonnull Mode mode, int period)`
  - Creates a `SkipCellPointEvaluator` instance.

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
- `collectPoint(int cellHash, int cellX, int cellY, double cellCentreX, double cellCentreY, T ctx, @NonNullDecl PointConsumer<T> consumer)`: Add description.
  - Executes `collectPoint` behavior.
- `skip(Mode mode, int cx, int cy)`: Add description.
  - Executes `skip` behavior.

## Notes
- No additional notes.
