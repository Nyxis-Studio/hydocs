# PlayerConnectionFlushSystem

## Overview
- Documentation for `PlayerConnectionFlushSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.player`.

## Constructors
- `PlayerConnectionFlushSystem(ComponentType<EntityStore, PlayerRef> componentType)`
  - Creates a `PlayerConnectionFlushSystem` instance.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.

## Notes
- No additional notes.
