**Source Hash:** `8ebafd468fb6d895586aa07b1492424f5e4d50e3b1145b585a97aa40c3eafea5`

# SpawnBeaconSystems

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `getDependencies()`: Add description.
  - Executes `getDependencies` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`: Add description.
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `onStartRun(NPCBeaconSpawnJob spawnJob)`: Add description.
  - Executes `onStartRun` behavior.
- `onEndProbing(@Nonnull BeaconSpawnController spawnController, @Nonnull NPCBeaconSpawnJob spawnJob, SpawnJobSystem.Result result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onEndProbing` behavior.
- `pickSpawnPosition(@Nonnull BeaconSpawnController spawnController, @Nonnull NPCBeaconSpawnJob spawnJob, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `pickSpawnPosition` behavior.
- `onSpawn(@Nonnull Ref<EntityStore> npcReference, @Nonnull BeaconSpawnController spawnController, @Nonnull NPCBeaconSpawnJob spawnJob, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onSpawn` behavior.
- `postSpawn(@Nonnull NPCEntity entity, @Nonnull Ref<EntityStore> ref, int roleIndex, boolean spawnFrozen, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `postSpawn` behavior.
- `isReadyToRespawn(LegacySpawnBeaconEntity spawnBeacon, WorldTimeResource timeManager)`: Add description.
  - Executes `isReadyToRespawn` behavior.
- `prepareSpawnJobGeneration(@Nonnull BeaconSpawnController spawnController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `prepareSpawnJobGeneration` behavior.
- `createRandomSpawnJobs(@Nonnull BeaconSpawnController spawnController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `createRandomSpawnJobs` behavior.
- `despawnAllSpawns(@Nonnull List<Ref<EntityStore>> spawnedEntities, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `despawnAllSpawns` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
