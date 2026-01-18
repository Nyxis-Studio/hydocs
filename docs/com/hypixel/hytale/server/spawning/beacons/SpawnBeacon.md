# SpawnBeacon

## Overview
- Documentation for `SpawnBeacon`.
- Declared as a class in `com.hypixel.hytale.server.spawning.beacons`.

## Constructors
- `SpawnBeacon()`
  - Creates a `SpawnBeacon` instance.
- `SpawnBeacon(World world)`
  - Creates a `SpawnBeacon` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `getSpawnWrapper()`
  - Executes `getSpawnWrapper` behavior.
- `setSpawnWrapper(@Nonnull BeaconSpawnWrapper spawnWrapper)`
  - Executes `setSpawnWrapper` behavior.
- `getSpawnConfigId()`
  - Executes `getSpawnConfigId` behavior.
- `isHiddenFromLivingEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isHiddenFromLivingEntity` behavior.
- `isCollidable()`
  - Executes `isCollidable` behavior.
- `moveTo(@Nonnull Ref<EntityStore> ref, double locX, double locY, double locZ, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `moveTo` behavior.
- `manualTrigger(@Nonnull Ref<EntityStore> ref, @Nonnull FloodFillPositionSelector positionSelector, @Nonnull Ref<EntityStore> targetRef, @Nonnull Store<EntityStore> store)`
  - Executes `manualTrigger` behavior.
- `markUnspawnable(Ref<EntityStore> ref, int index, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `markUnspawnable` behavior.
- `postSpawn(@Nonnull NPCEntity npc, @Nonnull Ref<EntityStore> selfRef, @Nonnull BeaconNPCSpawn spawn, Ref<EntityStore> targetRef, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `postSpawn` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
