# ItemPrePhysicsSystem

## Overview
- Documentation for `ItemPrePhysicsSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.item`.

## Constructors
- `ItemPrePhysicsSystem(@Nonnull ComponentType<EntityStore, ItemComponent> itemComponentType, @Nonnull ComponentType<EntityStore, BoundingBox> boundingBoxComponentType, @Nonnull ComponentType<EntityStore, Velocity> velocityComponentType, @Nonnull ComponentType<EntityStore, TransformComponent> transformComponentType, @Nonnull ComponentType<EntityStore, PhysicsValues> physicsValuesComponentType)`
  - Creates a `ItemPrePhysicsSystem` instance.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `moveOutOfBlock(@Nullable WorldChunk chunk, @Nonnull Vector3d position, @Nonnull Velocity velocityComponent, @Nonnull Box boundingBox)`
  - Executes `moveOutOfBlock` behavior.
- `applyGravity(float dt, @Nullable Box boundingBox, @Nonnull PhysicsValues values, @Nonnull Vector3d position, @Nonnull Velocity velocity)`
  - Executes `applyGravity` behavior.

## Notes
- No additional notes.
