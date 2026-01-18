# PickupItemSystem

## Overview
- Documentation for `PickupItemSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.item`.

## Constructors
- `PickupItemSystem(@Nonnull ComponentType<EntityStore, PickupItemComponent> pickupItemComponentType, @Nonnull ComponentType<EntityStore, TransformComponent> transformComponentType)`
  - Creates a `PickupItemSystem` instance.

## Methods
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `updateMovement(@Nonnull PickupItemComponent pickupItemComponent, @Nonnull Vector3d current, @Nonnull Vector3d target, float dt)`
  - Executes `updateMovement` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
