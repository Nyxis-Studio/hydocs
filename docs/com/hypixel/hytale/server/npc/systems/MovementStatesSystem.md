**Source Hash:** `722ce235e2033990fcc918b1586e3473cb28462f0002b645391dd277985b033d`

# MovementStatesSystem

## Overview

## Constructor Descriptions
- `MovementStatesSystem(@Nonnull ComponentType<EntityStore, NPCEntity> npcComponentType, @Nonnull ComponentType<EntityStore, Velocity> velocityComponentType, @Nonnull ComponentType<EntityStore, MovementStatesComponent> movementStatesComponentType)`
  - Creates a `MovementStatesSystem` instance.

## Method Descriptions
- `getDependencies()`: Add description.
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`: Add description.
  - Executes `isParallel` behavior.
- `steppedTick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `steppedTick` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
