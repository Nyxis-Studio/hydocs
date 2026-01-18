# EntityTickingSystem

## Overview
- Documentation for `EntityTickingSystem`.
- Declared as a class in `com.hypixel.hytale.component.system.tick`.

## Constructors
- None.

## Methods
- `maybeUseParallel(int archetypeChunkSize, int taskCount)`
  - Executes `maybeUseParallel` behavior.
- `useParallel(int archetypeChunkSize, int taskCount)`
  - Executes `useParallel` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, @Nonnull ArchetypeChunk<ECS_TYPE> archetypeChunk, @Nonnull Store<ECS_TYPE> store, @Nonnull CommandBuffer<ECS_TYPE> commandBuffer)`
  - Executes `tick` behavior.
- `tick(float var1, int var2, @Nonnull ArchetypeChunk<ECS_TYPE> var3, @Nonnull Store<ECS_TYPE> var4, @Nonnull CommandBuffer<ECS_TYPE> var5)`
  - Executes `tick` behavior.
- `doTick(@Nonnull EntityTickingSystem<ECS_TYPE> system, float dt, @Nonnull ArchetypeChunk<ECS_TYPE> archetypeChunk, @Nonnull Store<ECS_TYPE> store, @Nonnull CommandBuffer<ECS_TYPE> commandBuffer)`
  - Executes `doTick` behavior.
- `init(EntityTickingSystem<ECS_TYPE> system, float dt, ArchetypeChunk<ECS_TYPE> archetypeChunk, Store<ECS_TYPE> store, CommandBuffer<ECS_TYPE> commandBuffer)`
  - Executes `init` behavior.
- `accept(int index)`
  - Executes `accept` behavior.
- `clear()`
  - Executes `clear` behavior.
- `invokeParallelTask(@Nonnull ParallelTask<SystemTaskData<ECS_TYPE>> parallelTask, @Nonnull CommandBuffer<ECS_TYPE> commandBuffer)`
  - Executes `invokeParallelTask` behavior.

## Notes
- No additional notes.
