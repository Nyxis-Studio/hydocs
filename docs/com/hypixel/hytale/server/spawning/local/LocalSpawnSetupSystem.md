# LocalSpawnSetupSystem

## Overview
- Documentation for `LocalSpawnSetupSystem`.
- Declared as a class in `com.hypixel.hytale.server.spawning.local`.

## Constructors
- `LocalSpawnSetupSystem(ComponentType<EntityStore, Player> componentType)`
  - Creates a `LocalSpawnSetupSystem` instance.

## Methods
- `onEntityAdded(@Nonnull Ref<EntityStore> reference, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> reference, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
