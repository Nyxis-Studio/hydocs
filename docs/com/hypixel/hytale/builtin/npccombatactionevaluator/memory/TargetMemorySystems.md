# TargetMemorySystems

## Overview
- Documentation for `TargetMemorySystems`.
- Declared as a class in `com.hypixel.hytale.builtin.npccombatactionevaluator.memory`.

## Constructors
- None.

## Methods
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `iterateMemory(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull List<Ref<EntityStore>> targetsList, @Nonnull Int2FloatOpenHashMap targetsMap, @Nonnull String type)`
  - Executes `iterateMemory` behavior.
- `isValidTarget(@Nonnull Ref<EntityStore> targetRef, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `isValidTarget` behavior.
- `removeEntry(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, int targetIndex, @Nonnull Ref<EntityStore> targetRef, @Nonnull List<Ref<EntityStore>> targetsList, @Nonnull Int2FloatOpenHashMap targetsMap, @Nonnull String type)`
  - Executes `removeEntry` behavior.

## Notes
- No additional notes.
