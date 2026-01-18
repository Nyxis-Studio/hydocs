# BeaconSpawnController

## Overview
- Documentation for `BeaconSpawnController`.
- Declared as a class in `com.hypixel.hytale.server.spawning.controllers`.

## Constructors
- `BeaconSpawnController(@Nonnull World world, @Nonnull Ref<EntityStore> ownerRef)`
  - Creates a `BeaconSpawnController` instance.

## Methods
- `getMaxActiveJobs()`
  - Executes `getMaxActiveJobs` behavior.
- `createRandomSpawnJob(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `createRandomSpawnJob` behavior.
- `initialise(@Nonnull BeaconSpawnWrapper spawnWrapper)`
  - Executes `initialise` behavior.
- `getSpawnsThisRound()`
  - Executes `getSpawnsThisRound` behavior.
- `setRemainingSpawns(int remainingSpawns)`
  - Executes `setRemainingSpawns` behavior.
- `addRoundSpawn()`
  - Executes `addRoundSpawn` behavior.
- `isRoundStart()`
  - Executes `isRoundStart` behavior.
- `setRoundStart(boolean roundStart)`
  - Executes `setRoundStart` behavior.
- `getOwnerRef()`
  - Executes `getOwnerRef` behavior.
- `getBaseMaxConcurrentSpawns()`
  - Executes `getBaseMaxConcurrentSpawns` behavior.
- `getPlayersInRegion()`
  - Executes `getPlayersInRegion` behavior.
- `getCurrentScaledMaxConcurrentSpawns()`
  - Executes `getCurrentScaledMaxConcurrentSpawns` behavior.
- `setCurrentScaledMaxConcurrentSpawns(int currentScaledMaxConcurrentSpawns)`
  - Executes `setCurrentScaledMaxConcurrentSpawns` behavior.
- `getDespawnBeaconAfterTimeout()`
  - Executes `getDespawnBeaconAfterTimeout` behavior.
- `getSpawnRadiusSquared()`
  - Executes `getSpawnRadiusSquared` behavior.
- `getBeaconRadiusSquared()`
  - Executes `getBeaconRadiusSquared` behavior.
- `getBaseMaxTotalSpawns()`
  - Executes `getBaseMaxTotalSpawns` behavior.
- `setCurrentScaledMaxTotalSpawns(int currentScaledMaxTotalSpawns)`
  - Executes `setCurrentScaledMaxTotalSpawns` behavior.
- `getSpawnedEntities()`
  - Executes `getSpawnedEntities` behavior.
- `setNextPlayerIndex(int nextPlayerIndex)`
  - Executes `setNextPlayerIndex` behavior.
- `getEntityTimeoutCounter()`
  - Executes `getEntityTimeoutCounter` behavior.
- `getEntitiesPerPlayer()`
  - Executes `getEntitiesPerPlayer` behavior.
- `isDespawnNPCsIfIdle()`
  - Executes `isDespawnNPCsIfIdle` behavior.
- `getDespawnNPCAfterTimeout()`
  - Executes `getDespawnNPCAfterTimeout` behavior.
- `getThreatComparator()`
  - Executes `getThreatComparator` behavior.
- `notifySpawnedEntityExists(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `notifySpawnedEntityExists` behavior.
- `onJobFinished(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onJobFinished` behavior.
- `notifyNPCRemoval(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `notifyNPCRemoval` behavior.
- `hasSlots()`
  - Executes `hasSlots` behavior.
- `markNPCUnspawnable(int roleIndex)`
  - Executes `markNPCUnspawnable` behavior.
- `clearUnspawnableNPCs()`
  - Executes `clearUnspawnableNPCs` behavior.
- `onAllConcurrentSpawned(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onAllConcurrentSpawned` behavior.

## Notes
- No additional notes.
