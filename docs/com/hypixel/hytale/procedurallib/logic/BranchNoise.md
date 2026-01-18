# BranchNoise

## Overview
- Documentation for `BranchNoise`.
- Declared as a class in `com.hypixel.hytale.procedurallib.logic`.

## Constructors
- `BranchNoise(CellDistanceFunction parentFunction, PointEvaluator parentEvaluator, double parentValue, IDoubleRange parentFade, IIntCondition parentDensity, DistanceNoise.Distance2Function distance2Function, NoiseFormulaProperty.NoiseFormula.Formula noiseFormula, CellDistanceFunction lineFunction, PointEvaluator lineEvaluator, double lineScale, IDoubleRange lineThickness)`
  - Creates a `BranchNoise` instance.

## Methods
- `get(int seed, int offsetSeed, double x, double y)`
  - Executes `get` behavior.
- `get(int seed, int offsetSeed, double x, double y, double z)`
  - Executes `get` behavior.
- `getLineValue(int seed, double x, double y, int parentHash, double parentX, double parentY, double parentDistance, @Nonnull ResultBuffer.ResultBuffer2d buffer)`
  - Executes `getLineValue` behavior.
- `toString()`
  - Executes `toString` behavior.
- `toOutputRange(double value)`
  - Executes `toOutputRange` behavior.

## Notes
- No additional notes.
