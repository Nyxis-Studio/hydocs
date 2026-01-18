**Source Hash:** `92890a9d1e093e1de9cfdac4f42be0402083702532aec5afe2dd112a675ca20f`

# ItemPrePhysicsSystem

## Overview

## Constructor Descriptions
- `ItemPrePhysicsSystem(@Nonnull ComponentType<EntityStore, ItemComponent> itemComponentType, @Nonnull ComponentType<EntityStore, BoundingBox> boundingBoxComponentType, @Nonnull ComponentType<EntityStore, Velocity> velocityComponentType, @Nonnull ComponentType<EntityStore, TransformComponent> transformComponentType, @Nonnull ComponentType<EntityStore, PhysicsValues> physicsValuesComponentType)`
  - Creates a `ItemPrePhysicsSystem` instance.

## Method Descriptions
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`: Add description.
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `moveOutOfBlock(@Nullable WorldChunk chunk, @Nonnull Vector3d position, @Nonnull Velocity velocityComponent, @Nonnull Box boundingBox)`: Add description.
  - Executes `moveOutOfBlock` behavior.
- `applyGravity(float dt, @Nullable Box boundingBox, @Nonnull PhysicsValues values, @Nonnull Vector3d position, @Nonnull Velocity velocity)`: Add description.
  - Executes `applyGravity` behavior.

## Notes
- No additional notes.
