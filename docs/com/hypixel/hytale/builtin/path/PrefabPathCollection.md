# PrefabPathCollection

## Overview
- Documentation for `PrefabPathCollection`.
- Declared as a class in `com.hypixel.hytale.builtin.path`.

## Constructors
- `PrefabPathCollection(int id)`
  - Creates a `PrefabPathCollection` instance.

## Methods
- `getNearestPrefabPath(int nameIndex, @Nonnull Vector3d position, Set<UUID> disallowedPaths, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getNearestPrefabPath` behavior.
- `getPath(UUID id)`
  - Executes `getPath` behavior.
- `getOrConstructPath(@Nonnull UUID id, @Nonnull String name, @Nonnull Int2ObjectConcurrentHashMap.IntBiObjFunction<UUID, String, IPrefabPath> pathGenerator)`
  - Executes `getOrConstructPath` behavior.
- `getNearestPrefabPath(@Nonnull Vector3d position, @Nullable Set<UUID> disallowedPaths, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getNearestPrefabPath` behavior.
- `removePathWaypoint(UUID id, int index)`
  - Executes `removePathWaypoint` behavior.
- `unloadPathWaypoint(UUID id, int index)`
  - Executes `unloadPathWaypoint` behavior.
- `removePathWaypoint(UUID id, int index, boolean unload)`
  - Executes `removePathWaypoint` behavior.
- `removePath(UUID id)`
  - Executes `removePath` behavior.
- `isEmpty()`
  - Executes `isEmpty` behavior.
- `forEach(BiConsumer<UUID, IPrefabPath> consumer)`
  - Executes `forEach` behavior.
- `add(IPrefabPath path)`
  - Executes `add` behavior.
- `remove(IPrefabPath path)`
  - Executes `remove` behavior.
- `getNearestPath(@Nonnull Vector3d position, @Nullable Set<UUID> disallowedPaths, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getNearestPath` behavior.

## Notes
- No additional notes.
