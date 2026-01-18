# LocalSpawnForceTriggerSystem

## Overview
- Documentation for `LocalSpawnForceTriggerSystem`.
- Declared as a class in `com.hypixel.hytale.server.spawning.local`.

## Constructors
- `LocalSpawnForceTriggerSystem(ComponentType<EntityStore, LocalSpawnController> spawnControllerComponentType, ResourceType<EntityStore, LocalSpawnState> localSpawnStateResourceType)`
  - Creates a `LocalSpawnForceTriggerSystem` instance.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.

## Notes
- No additional notes.
