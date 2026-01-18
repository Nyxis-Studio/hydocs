**Source Hash:** `0788baf1f2a837d8923929278aa61b09d1544d761068e3458035ff0848f09645`

# UniquePrefabGenerator

## Overview

## Constructor Descriptions
- `UniquePrefabGenerator(String name, PrefabCategory category, IWeightedMap<WorldGenPrefabSupplier> prefabs, UniquePrefabConfiguration configuration, int zoneIndex)`
  - Creates a `UniquePrefabGenerator` instance.

## Method Descriptions
- `getName()`: Add description.
  - Executes `getName` behavior.
- `getCategory()`: Add description.
  - Executes `getCategory` behavior.
- `getPrefabs()`: Add description.
  - Executes `getPrefabs` behavior.
- `generatePrefab(Random random)`: Add description.
  - Executes `generatePrefab` behavior.
- `generate(int seed, @Nullable Vector2i position, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Random random, int maxFailed, @Nonnull UniquePrefabContainer.UniquePrefabEntry[] entries)`: Add description.
  - Executes `generate` behavior.
- `tryPlacement(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Random random, @Nonnull UniquePrefabContainer.UniquePrefabEntry[] entries)`: Add description.
  - Executes `tryPlacement` behavior.
- `forceGeneration(int seed, @Nonnull ChunkGenerator chunkGenerator)`: Add description.
  - Executes `forceGeneration` behavior.
- `forceUniqueZonePlacement(int seed, @Nonnull Vector2i position, @Nonnull ChunkGenerator chunkGenerator)`: Add description.
  - Executes `forceUniqueZonePlacement` behavior.
- `getHeight(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Biome biome, int x, int z)`: Add description.
  - Executes `getHeight` behavior.
- `isMatchingHeight(int seed, int x, int z, Random random, int y)`: Add description.
  - Executes `isMatchingHeight` behavior.
- `isMatchingNoiseDensity(int seed, int x, int z)`: Add description.
  - Executes `isMatchingNoiseDensity` behavior.
- `isMatchingParentBlock(int seed, int x, int y, int z, @Nonnull Random random, @Nonnull ZoneBiomeResult zoneAndBiomeResult)`: Add description.
  - Executes `isMatchingParentBlock` behavior.
- `getCoverInGroundAt(int seed, int x, int y, int z, @Nonnull Random random, @Nonnull Biome biome)`: Add description.
  - Executes `getCoverInGroundAt` behavior.
- `isMatchingCover(int seed, @Nonnull CoverContainer.CoverContainerEntry coverContainerEntry, @Nonnull Random random, int x, int y, int z)`: Add description.
  - Executes `isMatchingCover` behavior.
- `getConfiguration()`: Add description.
  - Executes `getConfiguration` behavior.

## Notes
- No additional notes.
