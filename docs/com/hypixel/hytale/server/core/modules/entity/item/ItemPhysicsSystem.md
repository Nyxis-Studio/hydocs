# ItemPhysicsSystem

## Overview
- Documentation for `ItemPhysicsSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.item`.

## Constructors
- `ItemPhysicsSystem(@Nonnull ComponentType<EntityStore, ItemPhysicsComponent> itemPhysicsComponentType, @Nonnull ComponentType<EntityStore, Velocity> velocityComponentType, @Nonnull ComponentType<EntityStore, BoundingBox> boundingBoxComponentType)`
  - Creates a `ItemPhysicsSystem` instance.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.

## Notes
- No additional notes.
