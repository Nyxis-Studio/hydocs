# CustomBiomeGenerator

## Overview
- Documentation for `CustomBiomeGenerator`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.biome`.

## Constructors
- `CustomBiomeGenerator(NoiseProperty noiseProperty, IDoubleThreshold threshold, IIntCondition biomeMask, int priority)`
  - Creates a `CustomBiomeGenerator` instance.

## Methods
- `shouldGenerateAt(int seed, double x, double z, @Nonnull ZoneGeneratorResult zoneResult, @Nonnull Biome customBiome)`
  - Executes `shouldGenerateAt` behavior.
- `isThreshold(double d)`
  - Executes `isThreshold` behavior.
- `isThreshold(double d, double factor)`
  - Executes `isThreshold` behavior.
- `isValidParentBiome(int index)`
  - Executes `isValidParentBiome` behavior.
- `getPriority()`
  - Executes `getPriority` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
