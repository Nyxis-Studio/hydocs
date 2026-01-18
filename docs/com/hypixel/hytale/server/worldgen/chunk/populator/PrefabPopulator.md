**Source Hash:** `07ad1c4dba1b0c887e93645405156d189e6be125a64b05a6cac13c2e0d2d0a5b`

# PrefabPopulator

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `populate(int seed, @Nonnull ChunkGeneratorExecution execution)`: Add description.
  - Executes `populate` behavior.
- `run(int seed, @Nonnull ChunkGeneratorExecution execution)`: Add description.
  - Executes `run` behavior.
- `collectBiomes(int seed, ChunkGeneratorExecution execution)`: Add description.
  - Executes `collectBiomes` behavior.
- `collectPrefabs(int seed, ChunkGeneratorExecution execution)`: Add description.
  - Executes `collectPrefabs` behavior.
- `generatePrefabs(int seed, @Nonnull ChunkGeneratorExecution execution)`: Add description.
  - Executes `generatePrefabs` behavior.
- `generateUniquePrefabs(int seed, @Nonnull ChunkGeneratorExecution execution)`: Add description.
  - Executes `generateUniquePrefabs` behavior.
- `collectBiome(@Nonnull Biome biome)`: Add description.
  - Executes `collectBiome` behavior.
- `collectPrefab(double px, double pz)`: Add description.
  - Executes `collectPrefab` behavior.
- `collectConflicts()`: Add description.
  - Executes `collectConflicts` behavior.
- `intersects(int minX1, int minY1, int minZ1, int maxX1, int maxY1, int maxZ1, int minX2, int minY2, int minZ2, int maxX2, int maxY2, int maxZ2)`: Add description.
  - Executes `intersects` behavior.
- `isWithinUniquePrefabExclusionRange(int x, int z, @Nonnull PrefabPatternGenerator generator, @Nonnull UniquePrefabContainer.UniquePrefabEntry[] uniquePrefabs)`: Add description.
  - Executes `isWithinUniquePrefabExclusionRange` behavior.
- `getHeight(int seed, int x, int z, @Nonnull ChunkGeneratorExecution execution, @Nonnull Biome biome, @Nonnull PrefabPatternGenerator prefabPatternGenerator, Random random)`: Add description.
  - Executes `getHeight` behavior.
- `generateRotation(int x, int z, @Nonnull Random random, @Nonnull PrefabPatternGenerator patternGenerator)`: Add description.
  - Executes `generateRotation` behavior.
- `generatePrefabAt(int seed, int x, int z, int height, @Nonnull ChunkGeneratorExecution execution, @Nonnull WorldGenPrefabSupplier supplier, BlockMaskCondition configuration, PrefabRotation rotation, ICoordinateRndCondition heightCondition, int environmentId, boolean fitHeightmap, boolean submerge)`: Add description.
  - Executes `generatePrefabAt` behavior.
- `isMatchingBiome(Biome biome, @Nonnull ZoneBiomeResult zoneAndBiomeResult)`: Add description.
  - Executes `isMatchingBiome` behavior.
- `isMatchingChunkBounds(int x, int z, @Nonnull ChunkGeneratorExecution execution, @Nonnull PrefabRotation rotation, @Nonnull IChunkBounds bounds)`: Add description.
  - Executes `isMatchingChunkBounds` behavior.
- `isMatchingChunkBounds(@Nonnull ChunkGeneratorExecution execution, int lowBoundX, int lowBoundZ, int highBoundX, int highBoundZ)`: Add description.
  - Executes `isMatchingChunkBounds` behavior.
- `isMatchingHeight(int seed, int x, int z, int y, Random random, @Nonnull PrefabPatternGenerator prefabPatternGenerator)`: Add description.
  - Executes `isMatchingHeight` behavior.
- `isMatchingNoiseDensity(int seed, int x, int z, @Nonnull PrefabPatternGenerator prefabPatternGenerator)`: Add description.
  - Executes `isMatchingNoiseDensity` behavior.
- `isMatchingParentBlock(int seed, int x, int z, int y, @Nonnull Random random, @Nonnull ZoneBiomeResult zoneAndBiomeResult, @Nonnull PrefabContainer.PrefabContainerEntry containerEntry)`: Add description.
  - Executes `isMatchingParentBlock` behavior.
- `getCoverInGroundAt(int seed, int x, int z, int y, @Nonnull Random random, @Nonnull Biome biome)`: Add description.
  - Executes `getCoverInGroundAt` behavior.
- `isMatchingCover(int seed, int x, int z, int y, @Nonnull Random random, @Nonnull CoverContainer.CoverContainerEntry coverContainerEntry)`: Add description.
  - Executes `isMatchingCover` behavior.
- `Candidate(int x, int y, int z, int priority, PrefabRotation rotation, IPrefabBuffer buffer, WorldGenPrefabSupplier supplier, PrefabContainer.PrefabContainerEntry entry, PrefabPatternGenerator generator)`: Add description.
  - Executes `Candidate` behavior.

## Notes
- No additional notes.
