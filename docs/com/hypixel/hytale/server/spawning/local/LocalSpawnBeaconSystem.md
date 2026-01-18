# LocalSpawnBeaconSystem

## Overview
- Documentation for `LocalSpawnBeaconSystem`.
- Declared as a class in `com.hypixel.hytale.server.spawning.local`.

## Constructors
- `LocalSpawnBeaconSystem(ComponentType<EntityStore, LocalSpawnBeacon> componentType, ResourceType<EntityStore, LocalSpawnState> localSpawnStateResourceType)`
  - Creates a `LocalSpawnBeaconSystem` instance.

## Methods
- `onEntityAdded(@Nonnull Ref<EntityStore> reference, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> reference, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
