# ClimateNoise

## Overview
- Documentation for `ClimateNoise`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.climate`.

## Constructors
- `ClimateNoise(@Nonnull Grid grid, @Nonnull NoiseProperty continent, @Nonnull NoiseProperty temperature, @Nonnull NoiseProperty intensity, @Nonnull Thresholds thresholds)`
  - Creates a `ClimateNoise` instance.

## Methods
- `generate(int seed, double x, double y, @Nonnull Buffer buffer, @Nonnull ClimateGraph climate)`
  - Executes `generate` behavior.
- `getContinentFlags(double value, @Nonnull Thresholds thresholds)`
  - Executes `getContinentFlags` behavior.
- `eval(int seed, double x, double y, ResultBuffer.ResultBuffer2d buffer)`
  - Executes `eval` behavior.

## Notes
- No additional notes.
