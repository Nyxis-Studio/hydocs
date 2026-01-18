# BranchEvaluator

## Overview
- Documentation for `BranchEvaluator`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic.cell.evaluator`.

## Constructors
- `BranchEvaluator(@Nonnull CellDistanceFunction parentFunction, @Nonnull CellPointFunction linePointFunction, Direction direction, CellJitter jitter, double branchScale)`
  - Creates a `BranchEvaluator` instance.

## Methods
- `getJitter()`
  - Executes `getJitter` behavior.
- `evalPoint(int seed, double x, double y, int hashA, int cax, int cay, double ax, double ay, @Nonnull ResultBuffer.ResultBuffer2d buffer)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellHash, int xi, int yi, double vecX, double vecY, ResultBuffer.ResultBuffer2d buffer)`
  - Executes `evalPoint2` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, ResultBuffer.ResultBuffer3d buffer)`
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, ResultBuffer.ResultBuffer3d buffer)`
  - Executes `evalPoint2` behavior.
- `getConnectionX(Direction direction, int regionHash, double regionCoord, int cellHash, double cellCoord)`
  - Executes `getConnectionX` behavior.
- `getConnectionY(Direction direction, int regionHash, double regionCoord, int cellHash, double cellCoord)`
  - Executes `getConnectionY` behavior.
- `checkBounds(double x, double y, double ax, double ay, double bx, double by, double thickness)`
  - Executes `checkBounds` behavior.

## Notes
- No additional notes.
