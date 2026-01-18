**Source Hash:** `897374f1866d80ed646ef0e44d55625f15e269074df3fbcec669e43db0611832`

# ChunkGeneratorCache

## Overview

## Constructor Descriptions
- `ChunkGeneratorCache(ZoneBiomeResultFunction zoneBiomeResultFunction, BiomeCountFunction biomeCountFunction, HeightFunction heightFunction, HeightNoiseFunction heightNoiseFunction, int maxSize, long expireAfterSeconds)`
  - Creates a `ChunkGeneratorCache` instance.

## Method Descriptions
- `get(int seed, int x, int z)`: Add description.
  - Executes `get` behavior.
- `getZoneBiomeResult(int seed, int x, int z)`: Add description.
  - Executes `getZoneBiomeResult` behavior.
- `getBiomeCountResult(int seed, int x, int z)`: Add description.
  - Executes `getBiomeCountResult` behavior.
- `putHeight(int seed, int x, int z, int height)`: Add description.
  - Executes `putHeight` behavior.
- `getHeight(int seed, int x, int z)`: Add description.
  - Executes `getHeight` behavior.
- `ensureBiomeCountList(int seed, int x, int z, @Nonnull CoreDataCacheEntry entry)`: Add description.
  - Executes `ensureBiomeCountList` behavior.
- `ensureHeight(int seed, int x, int z, @Nonnull CoreDataCacheEntry entry)`: Add description.
  - Executes `ensureHeight` behavior.
- `ensureHeightNoise(int seed, int x, int z, @Nonnull CoreDataCacheEntry entry)`: Add description.
  - Executes `ensureHeightNoise` behavior.
- `computeValue(@Nonnull CoordinateCache.CoordinateKey key)`: Add description.
  - Executes `computeValue` behavior.
- `destroyEntry(CoordinateCache.CoordinateKey key, CoreDataCacheEntry value)`: Add description.
  - Executes `destroyEntry` behavior.
- `compute(int var1, int var2, int var3)`: Add description.
  - Executes `compute` behavior.
- `compute(int var1, int var2, int var3, InterpolatedBiomeCountList var4)`: Add description.
  - Executes `compute` behavior.
- `compute(InterpolatedBiomeCountList var1)`: Add description.
  - Executes `compute` behavior.

## Notes
- No additional notes.
