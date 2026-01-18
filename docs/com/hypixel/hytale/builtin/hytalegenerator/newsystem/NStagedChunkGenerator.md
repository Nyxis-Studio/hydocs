**Source Hash:** `7bdf03c8c6daefbde67f38b891fb6233ae1927c9a2de84361eb358864f511177`

# NStagedChunkGenerator

## Overview

## Constructor Descriptions
- `NStagedChunkGenerator()`
  - Creates a `NStagedChunkGenerator` instance.

## Method Descriptions
- `generate(@Nonnull ChunkRequest.Arguments arguments)`: Add description.
  - Executes `generate` behavior.
- `createTileTask(int stageIndex, @Nonnull Vector3i position_bufferTileGrid, @Nonnull WorkerIndexer.Id workerId, @Nonnull Map<NBufferType, NBufferBundle.Access> accessMap)`: Add description.
  - Executes `createTileTask` behavior.
- `transferBlockStates(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedBlockStateChunk blockStateChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`: Add description.
  - Executes `transferBlockStates` behavior.
- `transferMaterials(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedChunk generatedChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`: Add description.
  - Executes `transferMaterials` behavior.
- `transferTints(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedChunk generatedChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`: Add description.
  - Executes `transferTints` behavior.
- `transferEnvironments(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedChunk generatedChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`: Add description.
  - Executes `transferEnvironments` behavior.
- `transferEntities(@Nonnull ChunkRequest.Arguments arguments, @Nonnull GeneratedChunk generatedChunk, @Nonnull TimeInstrument.Probe transfer_timeProbe)`: Add description.
  - Executes `transferEntities` behavior.
- `createBufferRequestCacheReport()`: Add description.
  - Executes `createBufferRequestCacheReport` behavior.
- `createContextDependencyReport(int indentation)`: Add description.
  - Executes `createContextDependencyReport` behavior.
- `setSupport(@Nonnull GeneratedChunk chunk, int x, int y, int z, int blockId, int supportValue)`: Add description.
  - Executes `setSupport` behavior.
- `setBoundsToWorldHeight_bufferGrid(@Nonnull Bounds3i bounds_bufferGrid)`: Add description.
  - Executes `setBoundsToWorldHeight_bufferGrid` behavior.
- `isColumnCached(@Nonnull NBufferBundle.Access access, @Nonnull Vector3i position_bufferGrid, int stageIndex)`: Add description.
  - Executes `isColumnCached` behavior.
- `updateTrackersForColumn(int stageIndex, @Nonnull NBufferBundle.Access.View access, @Nonnull Vector3i position_bufferGrid)`: Add description.
  - Executes `updateTrackersForColumn` behavior.
- `build()`: Add description.
  - Executes `build` behavior.
- `withStats(@Nonnull String statsHeader, @Nonnull Set<Integer> statsCheckpoints)`: Add description.
  - Executes `withStats` behavior.
- `withConcurrentExecutor(@Nonnull ExecutorService executor, @Nonnull WorkerIndexer workerIndexer)`: Add description.
  - Executes `withConcurrentExecutor` behavior.
- `withMaterialCache(@Nonnull MaterialCache materialCache)`: Add description.
  - Executes `withMaterialCache` behavior.
- `withBufferCapacity(double factor, double targetViewDistance, double targetPlayerCount)`: Add description.
  - Executes `withBufferCapacity` behavior.
- `appendStage(@Nonnull NStage stage)`: Add description.
  - Executes `appendStage` behavior.
- `createStagesThatReadFrom(int stageIndex)`: Add description.
  - Executes `createStagesThatReadFrom` behavior.
- `createStageDependencyMap()`: Add description.
  - Executes `createStageDependencyMap` behavior.
- `resolveBufferCapacity(@Nonnull NBufferType bufferType, @Nonnull Bounds3i[] stagesOutputBounds)`: Add description.
  - Executes `resolveBufferCapacity` behavior.
- `calculateCapacityFromBounds(@Nonnull Bounds3i bounds, double factor, double viewDistance_voxelGrid, double playerCount)`: Add description.
  - Executes `calculateCapacityFromBounds` behavior.
- `createTotalOutputBoundsForStage(int stageIndex, @Nonnull Map<Integer, Set<Integer>> stageDependencyMap, @Nonnull Bounds3i[] totalOutputBoundsPerStage_bufferGrid)`: Add description.
  - Executes `createTotalOutputBoundsForStage` behavior.
- `createTotalOutputBoundsArray(@Nonnull Map<Integer, Set<Integer>> stageDependencyMap)`: Add description.
  - Executes `createTotalOutputBoundsArray` behavior.
- `createListOfAllBufferTypes()`: Add description.
  - Executes `createListOfAllBufferTypes` behavior.
- `getEncompassingBounds(@Nonnull Collection<Bounds3i> set)`: Add description.
  - Executes `getEncompassingBounds` behavior.
- `isGeneratorOutputBufferType(@Nonnull NBufferType bufferType)`: Add description.
  - Executes `isGeneratorOutputBufferType` behavior.

## Notes
- No additional notes.
