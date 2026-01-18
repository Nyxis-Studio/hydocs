# BlockPopulator

## Overview
- Documentation for `BlockPopulator`.
- Declared as a class in `com.hypixel.hytale.server.worldgen.chunk.populator`.

## Constructors
- None.

## Methods
- `populate(int seed, @Nonnull ChunkGeneratorExecution execution)`
  - Executes `populate` behavior.
- `generateBlockColumn(int seed, @Nonnull ChunkGeneratorExecution execution, int cx, int cz, @Nonnull Random random)`
  - Executes `generateBlockColumn` behavior.
- `generateCovers(int seed, @Nonnull ChunkGeneratorExecution execution, int cx, int cz, int x, int z, @Nonnull Random random, @Nonnull Biome biome, @Nonnull IntList surfaceBlockList)`
  - Executes `generateCovers` behavior.
- `isMatchingParentCover(@Nonnull ChunkGeneratorExecution execution, @Nonnull CoverContainer.CoverContainerEntry coverContainerEntry, int cx, int cz, int y, int defaultId, int defaultFluidId)`
  - Executes `isMatchingParentCover` behavior.
- `isMatchingCoverColumn(int seed, @Nonnull CoverContainer.CoverContainerEntry coverContainerEntry, @Nonnull Random random, int x, int z)`
  - Executes `isMatchingCoverColumn` behavior.
- `isMatchingCoverHeight(int seed, @Nonnull CoverContainer.CoverContainerEntry coverContainerEntry, Random random, int x, int y, int z)`
  - Executes `isMatchingCoverHeight` behavior.
- `generateLayers(int seed, @Nonnull ChunkGeneratorExecution execution, int cx, int cz, int x, int z, @Nonnull Biome biome, @Nonnull IntList surfaceBlockList)`
  - Executes `generateLayers` behavior.
- `generateDynamicLayers(int seed, @Nonnull ChunkGeneratorExecution execution, int cx, int cz, int x, int z, @Nonnull Biome biome, @Nonnull IntList surfaceBlockList)`
  - Executes `generateDynamicLayers` behavior.
- `generateStaticLayers(int seed, @Nonnull ChunkGeneratorExecution execution, int cx, int cz, int x, int z, @Nonnull Biome biome)`
  - Executes `generateStaticLayers` behavior.

## Notes
- No additional notes.
