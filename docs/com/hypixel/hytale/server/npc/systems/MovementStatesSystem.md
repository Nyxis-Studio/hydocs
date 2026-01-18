# MovementStatesSystem

## Overview
- Documentation for `MovementStatesSystem`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- `MovementStatesSystem(@Nonnull ComponentType<EntityStore, NPCEntity> npcComponentType, @Nonnull ComponentType<EntityStore, Velocity> velocityComponentType, @Nonnull ComponentType<EntityStore, MovementStatesComponent> movementStatesComponentType)`
  - Creates a `MovementStatesSystem` instance.

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
