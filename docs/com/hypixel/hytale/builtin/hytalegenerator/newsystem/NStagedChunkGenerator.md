# NStagedChunkGenerator

## Overview
- Documentation for `NStagedChunkGenerator`.
- Declared as a class in `com.hypixel.hytale.builtin.hytalegenerator.newsystem`.

## Constructors
- `NStagedChunkGenerator()`
  - Creates a `NStagedChunkGenerator` instance.

## Methods
- `generate(@Nonnull ChunkRequest.Arguments arguments)`
  - Executes `generate` behavior.
- `createTileTask(int stageIndex, @Nonnull Vector3i position_bufferTileGrid, @Nonnull WorkerIndexer.Id workerId, @Nonnull Map<NBufferType, NBufferBundle.Access> accessMap)`
  - Executes `createTileTask` behavior.
- `transferBlockStates(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedBlockStateChunk blockStateChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`
  - Executes `transferBlockStates` behavior.
- `transferMaterials(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedChunk generatedChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`
  - Executes `transferMaterials` behavior.
- `transferTints(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedChunk generatedChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`
  - Executes `transferTints` behavior.
- `transferEnvironments(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedChunk generatedChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`
  - Executes `transferEnvironments` behavior.
- `transferEntities(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedChunk generatedChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`
  - Executes `transferEntities` behavior.
- `createBufferRequestCacheReport()`
  - Executes `createBufferRequestCacheReport` behavior.
- `createContextDependencyReport(int indentation)`
  - Executes `createContextDependencyReport` behavior.
- `setSupport(@Nonnull GeneratedChunk chunk, int x, int y, int z, int blockId, int supportValue)`
  - Executes `setSupport` behavior.
- `setBoundsToWorldHeight_bufferGrid(@Nonnull Bounds3i bounds_bufferGrid)`
  - Executes `setBoundsToWorldHeight_bufferGrid` behavior.
- `isColumnCached(@Nonnull NBufferBundle.Access access, @Nonnull Vector3i position_bufferGrid, int stageIndex)`
  - Executes `isColumnCached` behavior.
- `updateTrackersForColumn(int stageIndex, @Nonnull NBufferBundle.Access.View access, @Nonnull Vector3i position_bufferGrid)`
  - Executes `updateTrackersForColumn` behavior.
- `build()`
  - Executes `build` behavior.
- `withStats(@Nonnull String statsHeader, @Nonnull Set<Integer> statsCheckpoints)`
  - Executes `withStats` behavior.
- `withConcurrentExecutor(@Nonnull ExecutorService executor, @Nonnull WorkerIndexer workerIndexer)`
  - Executes `withConcurrentExecutor` behavior.
- `withMaterialCache(@Nonnull MaterialCache materialCache)`
  - Executes `withMaterialCache` behavior.
- `withBufferCapacity(double factor, double targetViewDistance, double targetPlayerCount)`
  - Executes `withBufferCapacity` behavior.
- `appendStage(@Nonnull NStage stage)`
  - Executes `appendStage` behavior.
- `createStagesThatReadFrom(int stageIndex)`
  - Executes `createStagesThatReadFrom` behavior.
- `createStageDependencyMap()`
  - Executes `createStageDependencyMap` behavior.
- `resolveBufferCapacity(@Nonnull NBufferType bufferType, @Nonnull Bounds3i[] stagesOutputBounds)`
  - Executes `resolveBufferCapacity` behavior.
- `calculateCapacityFromBounds(@Nonnull Bounds3i bounds, double factor, double viewDistance_voxelGrid, double playerCount)`
  - Executes `calculateCapacityFromBounds` behavior.
- `createTotalOutputBoundsForStage(int stageIndex, @Nonnull Map<Integer, Set<Integer>> stageDependencyMap, @Nonnull Bounds3i[] totalOutputBoundsPerStage_bufferGrid)`
  - Executes `createTotalOutputBoundsForStage` behavior.
- `createTotalOutputBoundsArray(@Nonnull Map<Integer, Set<Integer>> stageDependencyMap)`
  - Executes `createTotalOutputBoundsArray` behavior.
- `createListOfAllBufferTypes()`
  - Executes `createListOfAllBufferTypes` behavior.
- `getEncompassingBounds(@Nonnull Collection<Bounds3i> set)`
  - Executes `getEncompassingBounds` behavior.
- `isGeneratorOutputBufferType(@Nonnull NBufferType bufferType)`
  - Executes `isGeneratorOutputBufferType` behavior.

## Notes
- No additional notes.
