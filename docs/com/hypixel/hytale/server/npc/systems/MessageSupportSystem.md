# MessageSupportSystem

## Overview
- Documentation for `MessageSupportSystem`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- `MessageSupportSystem(@Nonnull ComponentType<EntityStore, T> messageSupportComponentType, @Nonnull Set<Dependency<EntityStore>> dependencies)`
  - Creates a `MessageSupportSystem` instance.

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
