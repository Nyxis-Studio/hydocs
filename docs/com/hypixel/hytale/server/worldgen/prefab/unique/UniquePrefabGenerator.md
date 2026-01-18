# UniquePrefabGenerator

## Overview
- Documentation for `UniquePrefabGenerator`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.prefab.unique`.

## Constructors
- `UniquePrefabGenerator(String name, PrefabCategory category, IWeightedMap<WorldGenPrefabSupplier> prefabs, UniquePrefabConfiguration configuration, int zoneIndex)`
  - Creates a `UniquePrefabGenerator` instance.

## Methods
- `getName()`
  - Executes `getName` behavior.
- `getCategory()`
  - Executes `getCategory` behavior.
- `getPrefabs()`
  - Executes `getPrefabs` behavior.
- `generatePrefab(Random random)`
  - Executes `generatePrefab` behavior.
- `generate(int seed, @Nullable Vector2i position, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Random random, int maxFailed, @Nonnull UniquePrefabContainer.UniquePrefabEntry[] entries)`
  - Executes `generate` behavior.
- `tryPlacement(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Random random, @Nonnull UniquePrefabContainer.UniquePrefabEntry[] entries)`
  - Executes `tryPlacement` behavior.
- `forceGeneration(int seed, @Nonnull ChunkGenerator chunkGenerator)`
  - Executes `forceGeneration` behavior.
- `forceUniqueZonePlacement(int seed, @Nonnull Vector2i position, @Nonnull ChunkGenerator chunkGenerator)`
  - Executes `forceUniqueZonePlacement` behavior.
- `getHeight(int seed, @Nonnull ChunkGenerator chunkGenerator, @Nonnull Biome biome, int x, int z)`
  - Executes `getHeight` behavior.
- `isMatchingHeight(int seed, int x, int z, Random random, int y)`
  - Executes `isMatchingHeight` behavior.
- `isMatchingNoiseDensity(int seed, int x, int z)`
  - Executes `isMatchingNoiseDensity` behavior.
- `isMatchingParentBlock(int seed, int x, int y, int z, @Nonnull Random random, @Nonnull ZoneBiomeResult zoneAndBiomeResult)`
  - Executes `isMatchingParentBlock` behavior.
- `getCoverInGroundAt(int seed, int x, int y, int z, @Nonnull Random random, @Nonnull Biome biome)`
  - Executes `getCoverInGroundAt` behavior.
- `isMatchingCover(int seed, @Nonnull CoverContainer.CoverContainerEntry coverContainerEntry, @Nonnull Random random, int x, int y, int z)`
  - Executes `isMatchingCover` behavior.
- `getConfiguration()`
  - Executes `getConfiguration` behavior.

## Notes
- No additional notes.
