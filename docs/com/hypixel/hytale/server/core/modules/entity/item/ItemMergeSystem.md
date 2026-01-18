# ItemMergeSystem

## Overview
- Documentation for `ItemMergeSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.item`.

## Constructors
- `ItemMergeSystem(@Nonnull ComponentType<EntityStore, ItemComponent> itemComponentComponentType, @Nonnull ComponentType<EntityStore, Interactable> interactableComponentType, @Nonnull ResourceType<EntityStore, SpatialResource<Ref<EntityStore>, EntityStore>> itemSpatialComponent)`
  - Creates a `ItemMergeSystem` instance.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.

## Notes
- No additional notes.
