# AvoidanceSystem

## Overview
- Documentation for `AvoidanceSystem`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- `AvoidanceSystem(@Nonnull ComponentType<EntityStore, NPCEntity> componentType)`
  - Creates a `AvoidanceSystem` instance.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `steppedTick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `steppedTick` behavior.
- `renderDebugSteeringVector(@Nonnull Vector3d position, @Nonnull Vector3d direction, @Nonnull Vector3f color, @Nonnull World world)`
  - Executes `renderDebugSteeringVector` behavior.
- `renderDebugSteeringVectorInverse(@Nonnull Vector3d position, @Nonnull Vector3d direction, @Nonnull Vector3f color, @Nonnull World world)`
  - Executes `renderDebugSteeringVectorInverse` behavior.

## Notes
- No additional notes.
