**Source Hash:** `11ee65a723e686c881cc46633e9c46411f4245a4be246f605c9c23305494ddc1`

# FlockPlugin

## Overview

## Constructor Descriptions
- `FlockPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `FlockPlugin` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `start()`: Add description.
  - Executes `start` behavior.
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.
- `getFlockComponentType()`: Add description.
  - Executes `getFlockComponentType` behavior.
- `getFlockMembershipComponentType()`: Add description.
  - Executes `getFlockMembershipComponentType` behavior.
- `getPersistentFlockDataComponentType()`: Add description.
  - Executes `getPersistentFlockDataComponentType` behavior.
- `getPrefabRemappedFlockReference(int prefabId, UUID oldId)`: Add description.
  - Executes `getPrefabRemappedFlockReference` behavior.
- `trySpawnFlock(@Nonnull Ref<EntityStore> npcRef, @Nonnull NPCEntity npc, @Nonnull Store<EntityStore> store, int roleIndex, @Nonnull Vector3d position, Vector3f rotation, @Nullable FlockAsset flockDefinition, TriConsumer<NPCEntity, Ref<EntityStore>, Store<EntityStore>> postSpawn)`: Add description.
  - Executes `trySpawnFlock` behavior.
- `trySpawnFlock(@Nonnull Ref<EntityStore> npcRef, @Nonnull NPCEntity npc, @Nonnull Store<EntityStore> store, int roleIndex, @Nonnull Vector3d position, Vector3f rotation, int flockSize, TriConsumer<NPCEntity, Ref<EntityStore>, Store<EntityStore>> postSpawn)`: Add description.
  - Executes `trySpawnFlock` behavior.
- `trySpawnFlock(@Nonnull Ref<EntityStore> npcRef, @Nonnull NPCEntity npc, int roleIndex, @Nonnull Vector3d position, Vector3f rotation, int flockSize, FlockAsset flockDefinition, TriConsumer<NPCEntity, Holder<EntityStore>, Store<EntityStore>> preAddToWorld, TriConsumer<NPCEntity, Ref<EntityStore>, Store<EntityStore>> postSpawn, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `trySpawnFlock` behavior.
- `getFlock(@Nonnull ComponentAccessor<EntityStore> componentAccessor, @Nonnull Ref<EntityStore> reference)`: Add description.
  - Executes `getFlock` behavior.
- `createFlock(@Nonnull Store<EntityStore> store, @Nonnull Role role)`: Add description.
  - Executes `createFlock` behavior.
- `createFlock(@Nonnull Store<EntityStore> store, @Nullable FlockAsset flockDefinition, @Nonnull String[] allowedRoles)`: Add description.
  - Executes `createFlock` behavior.
- `getFlockReference(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getFlockReference` behavior.
- `isFlockMember(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `isFlockMember` behavior.
- `handle(@Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull PrefabPasteEvent event)`: Add description.
  - Executes `handle` behavior.

## Notes
- No additional notes.
