# FlockPlugin

## Overview
- Documentation for `FlockPlugin`.
- Declared as a class in `com.hypixel.hytale.server.flock`.

## Constructors
- `FlockPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `FlockPlugin` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `start()`
  - Executes `start` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `getFlockComponentType()`
  - Executes `getFlockComponentType` behavior.
- `getFlockMembershipComponentType()`
  - Executes `getFlockMembershipComponentType` behavior.
- `getPersistentFlockDataComponentType()`
  - Executes `getPersistentFlockDataComponentType` behavior.
- `getPrefabRemappedFlockReference(int prefabId, UUID oldId)`
  - Executes `getPrefabRemappedFlockReference` behavior.
- `trySpawnFlock(@Nonnull Ref<EntityStore> npcRef, @Nonnull NPCEntity npc, @Nonnull Store<EntityStore> store, int roleIndex, @Nonnull Vector3d position, Vector3f rotation, @Nullable FlockAsset flockDefinition, TriConsumer<NPCEntity, Ref<EntityStore>, Store<EntityStore>> postSpawn)`
  - Executes `trySpawnFlock` behavior.
- `trySpawnFlock(@Nonnull Ref<EntityStore> npcRef, @Nonnull NPCEntity npc, @Nonnull Store<EntityStore> store, int roleIndex, @Nonnull Vector3d position, Vector3f rotation, int flockSize, TriConsumer<NPCEntity, Ref<EntityStore>, Store<EntityStore>> postSpawn)`
  - Executes `trySpawnFlock` behavior.
- `trySpawnFlock(@Nonnull Ref<EntityStore> npcRef, @Nonnull NPCEntity npc, int roleIndex, @Nonnull Vector3d position, Vector3f rotation, int flockSize, FlockAsset flockDefinition, TriConsumer<NPCEntity, Holder<EntityStore>, Store<EntityStore>> preAddToWorld, TriConsumer<NPCEntity, Ref<EntityStore>, Store<EntityStore>> postSpawn, @Nonnull Store<EntityStore> store)`
  - Executes `trySpawnFlock` behavior.
- `getFlock(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> reference)`
  - Executes `getFlock` behavior.
- `createFlock(@Nonnull Store<EntityStore> store, @Nonnull Role role)`
  - Executes `createFlock` behavior.
- `createFlock(@Nonnull Store<EntityStore> store, @Nullable FlockAsset flockDefinition, @Nonnull String[] allowedRoles)`
  - Executes `createFlock` behavior.
- `getFlockReference(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getFlockReference` behavior.
- `isFlockMember(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`
  - Executes `isFlockMember` behavior.
- `handle(@Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull PrefabPasteEvent event)`
  - Executes `handle` behavior.

## Notes
- No additional notes.
