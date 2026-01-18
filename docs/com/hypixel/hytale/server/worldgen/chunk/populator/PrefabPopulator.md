# PrefabPopulator

## Overview
- Documentation for `PrefabPopulator`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.chunk.populator`.

## Constructors
- None.

## Methods
- `populate(int seed, @Nonnull ChunkGeneratorExecution execution)`
  - Executes `populate` behavior.
- `run(int seed, @Nonnull ChunkGeneratorExecution execution)`
  - Executes `run` behavior.
- `collectBiomes(int seed, ChunkGeneratorExecution execution)`
  - Executes `collectBiomes` behavior.
- `collectPrefabs(int seed, ChunkGeneratorExecution execution)`
  - Executes `collectPrefabs` behavior.
- `generatePrefabs(int seed, @Nonnull ChunkGeneratorExecution execution)`
  - Executes `generatePrefabs` behavior.
- `generateUniquePrefabs(int seed, @Nonnull ChunkGeneratorExecution execution)`
  - Executes `generateUniquePrefabs` behavior.
- `collectBiome(@Nonnull Biome biome)`
  - Executes `collectBiome` behavior.
- `collectPrefab(double px, double pz)`
  - Executes `collectPrefab` behavior.
- `collectConflicts()`
  - Executes `collectConflicts` behavior.
- `intersects(int minX1, int minY1, int minZ1, int maxX1, int maxY1, int maxZ1, int minX2, int minY2, int minZ2, int maxX2, int maxY2, int maxZ2)`
  - Executes `intersects` behavior.
- `isWithinUniquePrefabExclusionRange(int x, int z, @Nonnull PrefabPatternGenerator generator, @Nonnull UniquePrefabContainer.UniquePrefabEntry[] uniquePrefabs)`
  - Executes `isWithinUniquePrefabExclusionRange` behavior.
- `getHeight(int seed, int x, int z, @Nonnull ChunkGeneratorExecution execution, @Nonnull Biome biome, @Nonnull PrefabPatternGenerator prefabPatternGenerator, Random random)`
  - Executes `getHeight` behavior.
- `generateRotation(int x, int z, @Nonnull Random random, @Nonnull PrefabPatternGenerator patternGenerator)`
  - Executes `generateRotation` behavior.
- `generatePrefabAt(int seed, int x, int z, int height, @Nonnull ChunkGeneratorExecution execution, @Nonnull WorldGenPrefabSupplier supplier, BlockMaskCondition configuration, PrefabRotation rotation, ICoordinateRndCondition heightCondition, int environmentId, boolean fitHeightmap, boolean submerge)`
  - Executes `generatePrefabAt` behavior.
- `isMatchingBiome(Biome biome, @Nonnull ZoneBiomeResult zoneAndBiomeResult)`
  - Executes `isMatchingBiome` behavior.
- `isMatchingChunkBounds(int x, int z, @Nonnull ChunkGeneratorExecution execution, @Nonnull PrefabRotation rotation, @Nonnull IChunkBounds bounds)`
  - Executes `isMatchingChunkBounds` behavior.
- `isMatchingChunkBounds(@Nonnull ChunkGeneratorExecution execution, int lowBoundX, int lowBoundZ, int highBoundX, int highBoundZ)`
  - Executes `isMatchingChunkBounds` behavior.
- `isMatchingHeight(int seed, int x, int z, int y, Random random, @Nonnull PrefabPatternGenerator prefabPatternGenerator)`
  - Executes `isMatchingHeight` behavior.
- `isMatchingNoiseDensity(int seed, int x, int z, @Nonnull PrefabPatternGenerator prefabPatternGenerator)`
  - Executes `isMatchingNoiseDensity` behavior.
- `isMatchingParentBlock(int seed, int x, int z, int y, @Nonnull Random random, @Nonnull ZoneBiomeResult zoneAndBiomeResult, @Nonnull PrefabContainer.PrefabContainerEntry containerEntry)`
  - Executes `isMatchingParentBlock` behavior.
- `getCoverInGroundAt(int seed, int x, int z, int y, @Nonnull Random random, @Nonnull Biome biome)`
  - Executes `getCoverInGroundAt` behavior.
- `isMatchingCover(int seed, int x, int z, int y, @Nonnull Random random, @Nonnull CoverContainer.CoverContainerEntry coverContainerEntry)`
  - Executes `isMatchingCover` behavior.
- `Candidate(int x, int y, int z, int priority, PrefabRotation rotation, IPrefabBuffer buffer, WorldGenPrefabSupplier supplier, PrefabContainer.PrefabContainerEntry entry, PrefabPatternGenerator generator)`
  - Executes `Candidate` behavior.

## Notes
- No additional notes.
