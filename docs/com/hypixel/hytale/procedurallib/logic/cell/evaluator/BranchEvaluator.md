**Source Hash:** `3122429ee36b9a1fcb086ba6a8b7fa6dbd82dd19d623ce738bad28860ba3c99f`

# BranchEvaluator

## Overview

## Constructor Descriptions
- `BranchEvaluator(@Nonnull CellDistanceFunction parentFunction, @Nonnull CellPointFunction linePointFunction, Direction direction, CellJitter jitter, double branchScale)`
  - Creates a `BranchEvaluator` instance.

## Method Descriptions
- `getJitter()`: Add description.
  - Executes `getJitter` behavior.
- `evalPoint(int seed, double x, double y, int hashA, int cax, int cay, double ax, double ay, @Nonnull ResultBuffer.ResultBuffer2d buffer)`: Add description.
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, int cellHash, int xi, int yi, double vecX, double vecY, ResultBuffer.ResultBuffer2d buffer)`: Add description.
  - Executes `evalPoint2` behavior.
- `evalPoint(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, ResultBuffer.ResultBuffer3d buffer)`: Add description.
  - Executes `evalPoint` behavior.
- `evalPoint2(int seed, double x, double y, double z, int cellHash, int cellX, int cellY, int cellZ, double cellPointX, double cellPointY, double cellPointZ, ResultBuffer.ResultBuffer3d buffer)`: Add description.
  - Executes `evalPoint2` behavior.
- `getConnectionX(Direction direction, int regionHash, double regionCoord, int cellHash, double cellCoord)`: Add description.
  - Executes `getConnectionX` behavior.
- `getConnectionY(Direction direction, int regionHash, double regionCoord, int cellHash, double cellCoord)`: Add description.
  - Executes `getConnectionY` behavior.
- `checkBounds(double x, double y, double ax, double ay, double bx, double by, double thickness)`: Add description.
  - Executes `checkBounds` behavior.

## Notes
- No additional notes.
