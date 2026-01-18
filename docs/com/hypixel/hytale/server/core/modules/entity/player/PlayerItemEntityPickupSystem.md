# PlayerItemEntityPickupSystem

## Overview
- Documentation for `PlayerItemEntityPickupSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.player`.

## Constructors
- `PlayerItemEntityPickupSystem(@Nonnull ComponentType<EntityStore, ItemComponent> itemComponentType, @Nonnull ComponentType<EntityStore, Player> playerComponentType, @Nonnull ResourceType<EntityStore, SpatialResource<Ref<EntityStore>, EntityStore>> playerSpatialComponent)`
  - Creates a `PlayerItemEntityPickupSystem` instance.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.

## Notes
- No additional notes.
