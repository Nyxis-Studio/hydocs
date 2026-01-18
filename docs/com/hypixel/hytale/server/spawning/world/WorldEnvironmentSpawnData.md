**Source Hash:** `118fed7261d5b60615f555c39fbca39f016e04cd89ebc6d64a4d0761e696b594`

# WorldEnvironmentSpawnData

## Overview

## Constructor Descriptions
- `WorldEnvironmentSpawnData(int environmentIndex, double density)`
  - Creates a `WorldEnvironmentSpawnData` instance.
- `WorldEnvironmentSpawnData(int index)`
  - Creates a `WorldEnvironmentSpawnData` instance.

## Method Descriptions
- `getEnvironmentIndex()`: Add description.
  - Executes `getEnvironmentIndex` behavior.
- `getSegmentCount()`: Add description.
  - Executes `getSegmentCount` behavior.
- `isUnspawnable()`: Add description.
  - Executes `isUnspawnable` behavior.
- `setUnspawnable(boolean unspawnable)`: Add description.
  - Executes `setUnspawnable` behavior.
- `getExpectedNPCs()`: Add description.
  - Executes `getExpectedNPCs` behavior.
- `getActualNPCs()`: Add description.
  - Executes `getActualNPCs` behavior.
- `isEmpty()`: Add description.
  - Executes `isEmpty` behavior.
- `hasNPCs()`: Add description.
  - Executes `hasNPCs` behavior.
- `getNpcStatMap()`: Add description.
  - Executes `getNpcStatMap` behavior.
- `isFullyPopulated()`: Add description.
  - Executes `isFullyPopulated` behavior.
- `setFullyPopulated(boolean fullyPopulated)`: Add description.
  - Executes `setFullyPopulated` behavior.
- `getChunkRefSet()`: Add description.
  - Executes `getChunkRefSet` behavior.
- `adjustSegmentCount(int delta)`: Add description.
  - Executes `adjustSegmentCount` behavior.
- `forEachNpcStat(@Nonnull IntObjectConsumer<WorldNPCSpawnStat> consumer)`: Add description.
  - Executes `forEachNpcStat` behavior.
- `setDensity(double density, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `setDensity` behavior.
- `updateNPCs(WorldSpawnWrapper spawnWrapper, World world)`: Add description.
  - Executes `updateNPCs` behavior.
- `clearNPCs()`: Add description.
  - Executes `clearNPCs` behavior.
- `updateSpawnStats(int roleIndex, int spansTried, int spansSuccess, int budgetUsed, @Nonnull Object2IntMap<SpawnRejection> rejections, boolean success)`: Add description.
  - Executes `updateSpawnStats` behavior.
- `removeNPC(int roleIndex, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `removeNPC` behavior.
- `addNPC(int roleIndex, @Nonnull WorldSpawnWrapper spawnWrapper, @Nonnull RoleSpawnParameters spawnParams, @Nonnull World world, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `addNPC` behavior.
- `spawnWeight()`: Add description.
  - Executes `spawnWeight` behavior.
- `pickRandomSpawnNPCStat(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `pickRandomSpawnNPCStat` behavior.
- `resetUnspawnable()`: Add description.
  - Executes `resetUnspawnable` behavior.
- `trackSpawn(int roleNameIndex, int npcCount)`: Add description.
  - Executes `trackSpawn` behavior.
- `trackDespawn(int roleNameIndex, int npcCount)`: Add description.
  - Executes `trackDespawn` behavior.
- `removeChunk(@Nonnull Ref<ChunkStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `removeChunk` behavior.
- `addChunk(@Nonnull Ref<ChunkStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `addChunk` behavior.
- `recalculateWeight(int moonPhase)`: Add description.
  - Executes `recalculateWeight` behavior.
- `updateExpectedNPCs(int moonPhase)`: Add description.
  - Executes `updateExpectedNPCs` behavior.

## Notes
- No additional notes.
