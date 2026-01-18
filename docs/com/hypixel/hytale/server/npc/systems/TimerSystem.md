# TimerSystem

## Overview
- Documentation for `TimerSystem`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- `TimerSystem(@Nonnull ComponentType<EntityStore, Timers> timersComponentType, @Nonnull Set<Dependency<EntityStore>> dependencies)`
  - Creates a `TimerSystem` instance.

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
