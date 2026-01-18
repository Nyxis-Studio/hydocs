# ComputeVelocitySystem

## Overview
- Documentation for `ComputeVelocitySystem`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- `ComputeVelocitySystem(@Nonnull ComponentType<EntityStore, NPCEntity> npcEntityComponentType, @Nonnull ComponentType<EntityStore, Velocity> velocityComponentType, @Nonnull Set<Dependency<EntityStore>> dependencies)`
  - Creates a `ComputeVelocitySystem` instance.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `steppedTick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `steppedTick` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
