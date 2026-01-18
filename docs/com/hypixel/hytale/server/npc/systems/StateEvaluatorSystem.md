# StateEvaluatorSystem

## Overview
- Documentation for `StateEvaluatorSystem`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- `StateEvaluatorSystem(@Nonnull ComponentType<EntityStore, StateEvaluator> stateEvaluatorComponent, @Nonnull ComponentType<EntityStore, NPCEntity> npcComponentType)`
  - Creates a `StateEvaluatorSystem` instance.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.

## Notes
- No additional notes.
