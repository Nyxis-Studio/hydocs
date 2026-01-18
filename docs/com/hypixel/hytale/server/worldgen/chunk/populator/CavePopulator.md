# CavePopulator

## Overview
- Documentation for `CavePopulator`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.chunk.populator`.

## Constructors
- None.

## Methods
- `populate(int seed, @Nonnull ChunkGeneratorExecution execution)`
  - Executes `populate` behavior.
- `run(int seed, double dx, double dz, @Nonnull ChunkGeneratorExecution execution, Zone zone, @Nonnull CaveType caveType)`
  - Executes `run` behavior.
- `populate(int seed, @Nonnull ChunkGeneratorExecution execution, @Nonnull Cave cave)`
  - Executes `populate` behavior.
- `populateCaveNode(int seed, @Nonnull ChunkGeneratorExecution execution, @Nonnull Cave cave, @Nonnull CaveNode caveNode, @Nonnull Random random)`
  - Executes `populateCaveNode` behavior.
- `populatePrefab(int seed, int environment, @Nonnull ChunkGeneratorExecution execution, @Nonnull Cave cave, @Nonnull CaveNode node, @Nonnull CavePrefab prefab)`
  - Executes `populatePrefab` behavior.
- `generatePrefabAt(int seed, int x, int z, int y, int environment, @Nonnull ChunkGeneratorExecution execution, @Nonnull Cave cave, @Nonnull CaveNode node, BlockMaskCondition configuration, @Nonnull WorldGenPrefabSupplier supplier, PrefabRotation rotation)`
  - Executes `generatePrefabAt` behavior.
- `isMatchingHeightThreshold(int seed, int x, int z, @Nonnull ChunkGenerator chunkGenerator, @Nonnull CaveType caveType)`
  - Executes `isMatchingHeightThreshold` behavior.

## Notes
- No additional notes.
