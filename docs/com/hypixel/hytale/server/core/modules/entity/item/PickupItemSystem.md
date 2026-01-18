**Source Hash:** `719fa356818c8a6c317914c6547f83c73ae57fa82a5337804926ad61c2851563`

# PickupItemSystem

## Overview

## Constructor Descriptions
- `PickupItemSystem(@Nonnull ComponentType<EntityStore, PickupItemComponent> pickupItemComponentType, @Nonnull ComponentType<EntityStore, TransformComponent> transformComponentType)`
  - Creates a `PickupItemSystem` instance.

## Method Descriptions
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `updateMovement(@Nonnull PickupItemComponent pickupItemComponent, @Nonnull Vector3d current, @Nonnull Vector3d target, float dt)`: Add description.
  - Executes `updateMovement` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
