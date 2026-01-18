# ChunkGeneratorCache

## Overview
- Documentation for `ChunkGeneratorCache`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.cache`.

## Constructors
- `ChunkGeneratorCache(ZoneBiomeResultFunction zoneBiomeResultFunction, BiomeCountFunction biomeCountFunction, HeightFunction heightFunction, HeightNoiseFunction heightNoiseFunction, int maxSize, long expireAfterSeconds)`
  - Creates a `ChunkGeneratorCache` instance.

## Methods
- `get(int seed, int x, int z)`
  - Executes `get` behavior.
- `getZoneBiomeResult(int seed, int x, int z)`
  - Executes `getZoneBiomeResult` behavior.
- `getBiomeCountResult(int seed, int x, int z)`
  - Executes `getBiomeCountResult` behavior.
- `putHeight(int seed, int x, int z, int height)`
  - Executes `putHeight` behavior.
- `getHeight(int seed, int x, int z)`
  - Executes `getHeight` behavior.
- `ensureBiomeCountList(int seed, int x, int z, @Nonnull CoreDataCacheEntry entry)`
  - Executes `ensureBiomeCountList` behavior.
- `ensureHeight(int seed, int x, int z, @Nonnull CoreDataCacheEntry entry)`
  - Executes `ensureHeight` behavior.
- `ensureHeightNoise(int seed, int x, int z, @Nonnull CoreDataCacheEntry entry)`
  - Executes `ensureHeightNoise` behavior.
- `computeValue(@Nonnull CoordinateCache.CoordinateKey key)`
  - Executes `computeValue` behavior.
- `destroyEntry(CoordinateCache.CoordinateKey key, CoreDataCacheEntry value)`
  - Executes `destroyEntry` behavior.
- `compute(int var1, int var2, int var3)`
  - Executes `compute` behavior.
- `compute(int var1, int var2, int var3, InterpolatedBiomeCountList var4)`
  - Executes `compute` behavior.
- `compute(InterpolatedBiomeCountList var1)`
  - Executes `compute` behavior.

## Notes
- No additional notes.
