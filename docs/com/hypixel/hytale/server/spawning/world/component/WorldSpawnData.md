# WorldSpawnData

## Overview
- Documentation for `WorldSpawnData`.
- Declared as a class in `com.hypixel.hytale.server.spawning.world.component`.

## Constructors
- None.

## Methods
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `getActualNPCs()`
  - Executes `getActualNPCs` behavior.
- `getExpectedNPCs()`
  - Executes `getExpectedNPCs` behavior.
- `getExpectedNPCsInEmptyEnvironments()`
  - Executes `getExpectedNPCsInEmptyEnvironments` behavior.
- `isUnspawnable()`
  - Executes `isUnspawnable` behavior.
- `setUnspawnable(boolean unspawnable)`
  - Executes `setUnspawnable` behavior.
- `getChunkCount()`
  - Executes `getChunkCount` behavior.
- `adjustChunkCount(int amount)`
  - Executes `adjustChunkCount` behavior.
- `adjustSegmentCount(int amount)`
  - Executes `adjustSegmentCount` behavior.
- `getSpiralIterator()`
  - Executes `getSpiralIterator` behavior.
- `averageSegmentCount()`
  - Executes `averageSegmentCount` behavior.
- `getActiveSpawnJobs()`
  - Executes `getActiveSpawnJobs` behavior.
- `adjustActiveSpawnJobs(int amount, int trackedCount)`
  - Executes `adjustActiveSpawnJobs` behavior.
- `getTrackedCountFromJobs()`
  - Executes `getTrackedCountFromJobs` behavior.
- `getTotalSpawnJobBudgetUsed()`
  - Executes `getTotalSpawnJobBudgetUsed` behavior.
- `getTotalSpawnJobsCompleted()`
  - Executes `getTotalSpawnJobsCompleted` behavior.
- `addCompletedSpawnJob(int budgetUsed)`
  - Executes `addCompletedSpawnJob` behavior.
- `getWorldEnvironmentSpawnData(int environmentIndex)`
  - Executes `getWorldEnvironmentSpawnData` behavior.
- `getOrCreateWorldEnvironmentSpawnData(int environmentIndex, @Nonnull World world, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getOrCreateWorldEnvironmentSpawnData` behavior.
- `getWorldEnvironmentSpawnDataIndexes()`
  - Executes `getWorldEnvironmentSpawnDataIndexes` behavior.
- `updateSpawnability()`
  - Executes `updateSpawnability` behavior.
- `forEachEnvironmentSpawnData(Consumer<WorldEnvironmentSpawnData> consumer)`
  - Executes `forEachEnvironmentSpawnData` behavior.
- `trackNPC(int environmentIndex, int roleIndex, int npcCount, @Nonnull World world, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `trackNPC` behavior.
- `untrackNPC(int environmentIndex, int roleIndex, int npcCount)`
  - Executes `untrackNPC` behavior.
- `recalculateWorldCount()`
  - Executes `recalculateWorldCount` behavior.
- `queueUnspawnableChunk(int environmentIndex, long chunkIndex)`
  - Executes `queueUnspawnableChunk` behavior.
- `hasUnprocessedUnspawnableChunks()`
  - Executes `hasUnprocessedUnspawnableChunks` behavior.
- `nextUnspawnableChunk()`
  - Executes `nextUnspawnableChunk` behavior.
- `clone()`
  - Executes `clone` behavior.
- `getEnvironmentIndex()`
  - Executes `getEnvironmentIndex` behavior.
- `getChunkIndex()`
  - Executes `getChunkIndex` behavior.

## Notes
- No additional notes.
