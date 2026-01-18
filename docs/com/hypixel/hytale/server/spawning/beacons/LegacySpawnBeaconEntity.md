# LegacySpawnBeaconEntity

## Overview
- Documentation for `LegacySpawnBeaconEntity`.
- Declared as a class in `com.hypixel.hytale.server.spawning.beacons`.

## Constructors
- `LegacySpawnBeaconEntity(@Nullable World world)`
  - Creates a `LegacySpawnBeaconEntity` instance.
- `LegacySpawnBeaconEntity()`
  - Creates a `LegacySpawnBeaconEntity` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `getSpawnConfigId()`
  - Executes `getSpawnConfigId` behavior.
- `getSpawnController()`
  - Executes `getSpawnController` behavior.
- `setSpawnController(@Nonnull BeaconSpawnController spawnController)`
  - Executes `setSpawnController` behavior.
- `getNextSpawnAfter()`
  - Executes `getNextSpawnAfter` behavior.
- `isNextSpawnAfterRealtime()`
  - Executes `isNextSpawnAfterRealtime` behavior.
- `getDespawnSelfAfter()`
  - Executes `getDespawnSelfAfter` behavior.
- `setSpawnAttempts(int spawnAttempts)`
  - Executes `setSpawnAttempts` behavior.
- `getSpawnWrapper()`
  - Executes `getSpawnWrapper` behavior.
- `setSpawnWrapper(BeaconSpawnWrapper spawnWrapper)`
  - Executes `setSpawnWrapper` behavior.
- `getSpawnAttempts()`
  - Executes `getSpawnAttempts` behavior.
- `getLastPlayerCount()`
  - Executes `getLastPlayerCount` behavior.
- `setLastPlayerCount(int lastPlayerCount)`
  - Executes `setLastPlayerCount` behavior.
- `setSpawnConfiguration(BeaconSpawnWrapper spawn)`
  - Executes `setSpawnConfiguration` behavior.
- `setSpawnConfigId(String spawnConfigId)`
  - Executes `setSpawnConfigId` behavior.
- `getObjectiveUUID()`
  - Executes `getObjectiveUUID` behavior.
- `setObjectiveUUID(@Nullable UUID objectiveUUID)`
  - Executes `setObjectiveUUID` behavior.
- `isHiddenFromLivingEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isHiddenFromLivingEntity` behavior.
- `isCollidable()`
  - Executes `isCollidable` behavior.
- `moveTo(@Nonnull Ref<EntityStore> ref, double locX, double locY, double locZ, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `moveTo` behavior.
- `notifyFailedSpawn()`
  - Executes `notifyFailedSpawn` behavior.
- `notifySpawn(@Nonnull Player target, @Nonnull Ref<EntityStore> spawnedEntity, @Nonnull Store<EntityStore> store)`
  - Executes `notifySpawn` behavior.
- `prepareNextSpawnTimer(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `prepareNextSpawnTimer` behavior.
- `clearDespawnTimer(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `clearDespawnTimer` behavior.
- `setToDespawnAfter(@Nonnull Ref<EntityStore> ref, @Nullable Duration duration, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setToDespawnAfter` behavior.
- `markNPCUnspawnable(int roleIndex)`
  - Executes `markNPCUnspawnable` behavior.
- `prepareSpawnContext(@Nonnull Vector3d playerPosition, int spawnsThisRound, int roleIndex, @Nonnull SpawningContext spawningContext, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `prepareSpawnContext` behavior.
- `processSpawn(@Nonnull Ref<EntityStore> ref, @Nonnull Player target, @Nonnull Store<EntityStore> store)`
  - Executes `processSpawn` behavior.
- `create(@Nonnull BeaconSpawnWrapper spawnWrapper, @Nonnull Vector3d position, @Nonnull Vector3f rotation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `create` behavior.
- `createHolder(@Nonnull BeaconSpawnWrapper spawnWrapper, @Nonnull Vector3d position, @Nonnull Vector3f rotation)`
  - Executes `createHolder` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
