# WorldEnvironmentSpawnData

## Overview
- Documentation for `WorldEnvironmentSpawnData`.
- Declared as a class in `com.hypixel.hytale.server.spawning.world`.

## Constructors
- `WorldEnvironmentSpawnData(int environmentIndex, double density)`
  - Creates a `WorldEnvironmentSpawnData` instance.
- `WorldEnvironmentSpawnData(int index)`
  - Creates a `WorldEnvironmentSpawnData` instance.

## Methods
- `getEnvironmentIndex()`
  - Executes `getEnvironmentIndex` behavior.
- `getSegmentCount()`
  - Executes `getSegmentCount` behavior.
- `isUnspawnable()`
  - Executes `isUnspawnable` behavior.
- `setUnspawnable(boolean unspawnable)`
  - Executes `setUnspawnable` behavior.
- `getExpectedNPCs()`
  - Executes `getExpectedNPCs` behavior.
- `getActualNPCs()`
  - Executes `getActualNPCs` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `hasNPCs()`
  - Executes `hasNPCs` behavior.
- `getNpcStatMap()`
  - Executes `getNpcStatMap` behavior.
- `isFullyPopulated()`
  - Executes `isFullyPopulated` behavior.
- `setFullyPopulated(boolean fullyPopulated)`
  - Executes `setFullyPopulated` behavior.
- `getChunkRefSet()`
  - Executes `getChunkRefSet` behavior.
- `adjustSegmentCount(int delta)`
  - Executes `adjustSegmentCount` behavior.
- `forEachNpcStat(@Nonnull IntObjectConsumer<WorldNPCSpawnStat> consumer)`
  - Executes `forEachNpcStat` behavior.
- `setDensity(double density, @Nonnull Store<ChunkStore> store)`
  - Executes `setDensity` behavior.
- `updateNPCs(WorldSpawnWrapper spawnWrapper, World world)`
  - Executes `updateNPCs` behavior.
- `clearNPCs()`
  - Executes `clearNPCs` behavior.
- `updateSpawnStats(int roleIndex, int spansTried, int spansSuccess, int budgetUsed, @Nonnull Object2IntMap<SpawnRejection> rejections, boolean success)`
  - Executes `updateSpawnStats` behavior.
- `removeNPC(int roleIndex, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `removeNPC` behavior.
- `addNPC(int roleIndex, @Nonnull WorldSpawnWrapper spawnWrapper, @Nonnull RoleSpawnParameters spawnParams, @Nonnull World world, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `addNPC` behavior.
- `spawnWeight()`
  - Executes `spawnWeight` behavior.
- `pickRandomSpawnNPCStat(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `pickRandomSpawnNPCStat` behavior.
- `resetUnspawnable()`
  - Executes `resetUnspawnable` behavior.
- `trackSpawn(int roleNameIndex, int npcCount)`
  - Executes `trackSpawn` behavior.
- `trackDespawn(int roleNameIndex, int npcCount)`
  - Executes `trackDespawn` behavior.
- `removeChunk(@Nonnull Ref<ChunkStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `removeChunk` behavior.
- `addChunk(@Nonnull Ref<ChunkStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `addChunk` behavior.
- `recalculateWeight(int moonPhase)`
  - Executes `recalculateWeight` behavior.
- `updateExpectedNPCs(int moonPhase)`
  - Executes `updateExpectedNPCs` behavior.

## Notes
- No additional notes.
