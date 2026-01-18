# NPCPreTickSystem

## Overview
- Documentation for `NPCPreTickSystem`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- `NPCPreTickSystem(@Nonnull ComponentType<EntityStore, NPCEntity> npcComponentType)`
  - Creates a `NPCPreTickSystem` instance.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `steppedTick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `steppedTick` behavior.

## Notes
- No additional notes.
