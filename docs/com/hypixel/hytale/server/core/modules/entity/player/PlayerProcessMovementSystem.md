# PlayerProcessMovementSystem

## Overview
- Documentation for `PlayerProcessMovementSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.player`.

## Constructors
- `PlayerProcessMovementSystem(@Nonnull ComponentType<EntityStore, Player> playerComponentType, @Nonnull ComponentType<EntityStore, Velocity> velocityComponentType, @Nonnull ComponentType<EntityStore, CollisionResultComponent> collisionResultComponentType)`
  - Creates a `PlayerProcessMovementSystem` instance.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.

## Notes
- No additional notes.
