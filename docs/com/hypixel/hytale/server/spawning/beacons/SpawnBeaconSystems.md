# SpawnBeaconSystems

## Overview
- Documentation for `SpawnBeaconSystems`.
- Declared as a class in `com.hypixel.hytale.server.spawning.beacons`.

## Constructors
- None.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `onStartRun(NPCBeaconSpawnJob spawnJob)`
  - Executes `onStartRun` behavior.
- `onEndProbing(@Nonnull BeaconSpawnController spawnController, @Nonnull NPCBeaconSpawnJob spawnJob, SpawnJobSystem.Result result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onEndProbing` behavior.
- `pickSpawnPosition(@Nonnull BeaconSpawnController spawnController, @Nonnull NPCBeaconSpawnJob spawnJob, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `pickSpawnPosition` behavior.
- `onSpawn(@Nonnull Ref<EntityStore> npcReference, @Nonnull BeaconSpawnController spawnController, @Nonnull NPCBeaconSpawnJob spawnJob, @Nonnull Store<EntityStore> store)`
  - Executes `onSpawn` behavior.
- `postSpawn(@Nonnull NPCEntity entity, @Nonnull Ref<EntityStore> ref, int roleIndex, boolean spawnFrozen, @Nonnull Store<EntityStore> store)`
  - Executes `postSpawn` behavior.
- `isReadyToRespawn(LegacySpawnBeaconEntity spawnBeacon, WorldTimeResource timeManager)`
  - Executes `isReadyToRespawn` behavior.
- `prepareSpawnJobGeneration(@Nonnull BeaconSpawnController spawnController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `prepareSpawnJobGeneration` behavior.
- `createRandomSpawnJobs(@Nonnull BeaconSpawnController spawnController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `createRandomSpawnJobs` behavior.
- `despawnAllSpawns(@Nonnull List<Ref<EntityStore>> spawnedEntities, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `despawnAllSpawns` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
