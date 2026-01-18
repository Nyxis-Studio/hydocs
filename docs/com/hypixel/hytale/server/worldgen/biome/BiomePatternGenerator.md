# BiomePatternGenerator

## Overview
- Documentation for `BiomePatternGenerator`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.biome`.

## Constructors
- `BiomePatternGenerator(IPointGenerator pointGenerator, @Nonnull IWeightedMap<TileBiome> tileBiomes, @Nonnull CustomBiome[] customBiomes)`
  - Creates a `BiomePatternGenerator` instance.

## Methods
- `getExtents()`
  - Executes `getExtents` behavior.
- `getBiomes()`
  - Executes `getBiomes` behavior.
- `getCustomBiomes()`
  - Executes `getCustomBiomes` behavior.
- `getBiome(int seed, int x, int z)`
  - Executes `getBiome` behavior.
- `getBiomeIndex(int seed, int x, int z)`
  - Executes `getBiomeIndex` behavior.
- `getBiomeDirect(int seed, int x, int z)`
  - Executes `getBiomeDirect` behavior.
- `generateBiomeAt(@Nonnull ZoneGeneratorResult zoneResult, int seed, int x, int z)`
  - Executes `generateBiomeAt` behavior.
- `getCustomBiomeAt(int seed, double x, double z, @Nonnull ZoneGeneratorResult zoneResult, @Nonnull Biome parentResult)`
  - Executes `getCustomBiomeAt` behavior.
- `toString()`
  - Executes `toString` behavior.
- `getExtents(@Nonnull Biome[] biomes)`
  - Executes `getExtents` behavior.

## Notes
- No additional notes.
