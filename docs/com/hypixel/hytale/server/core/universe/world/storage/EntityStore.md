# EntityStore

## Overview
- Documentation for `EntityStore`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.storage`.

## Constructors
- `EntityStore(@Nonnull World world)`
  - Creates a `EntityStore` instance.

## Methods
- `start(@Nonnull IResourceStorage resourceStorage)`
  - Executes `start` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `getStore()`
  - Executes `getStore` behavior.
- `getRefFromUUID(@Nonnull UUID uuid)`
  - Executes `getRefFromUUID` behavior.
- `getRefFromNetworkId(int networkId)`
  - Executes `getRefFromNetworkId` behavior.
- `takeNextNetworkId()`
  - Executes `takeNextNetworkId` behavior.
- `getWorld()`
  - Executes `getWorld` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
