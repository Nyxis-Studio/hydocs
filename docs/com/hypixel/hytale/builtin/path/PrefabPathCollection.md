**Source Hash:** `61f57e15d89135e46c02fed68470b4a7de031f678d2e94d79194a8402779cf10`

# PrefabPathCollection

## Overview

## Constructor Descriptions
- `PrefabPathCollection(int id)`
  - Creates a `PrefabPathCollection` instance.

## Method Descriptions
- `getNearestPrefabPath(int nameIndex, @Nonnull Vector3d position, Set<UUID> disallowedPaths, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getNearestPrefabPath` behavior.
- `getPath(UUID id)`: Add description.
  - Executes `getPath` behavior.
- `getOrConstructPath(@Nonnull UUID id, @Nonnull String name, @Nonnull Int2ObjectConcurrentHashMap.IntBiObjFunction<UUID, String, IPrefabPath> pathGenerator)`: Add description.
  - Executes `getOrConstructPath` behavior.
- `getNearestPrefabPath(@Nonnull Vector3d position, @Nullable Set<UUID> disallowedPaths, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getNearestPrefabPath` behavior.
- `removePathWaypoint(UUID id, int index)`: Add description.
  - Executes `removePathWaypoint` behavior.
- `unloadPathWaypoint(UUID id, int index)`: Add description.
  - Executes `unloadPathWaypoint` behavior.
- `removePathWaypoint(UUID id, int index, boolean unload)`: Add description.
  - Executes `removePathWaypoint` behavior.
- `removePath(UUID id)`: Add description.
  - Executes `removePath` behavior.
- `isEmpty()`: Add description.
  - Executes `isEmpty` behavior.
- `forEach(BiConsumer<UUID, IPrefabPath> consumer)`: Add description.
  - Executes `forEach` behavior.
- `add(IPrefabPath path)`: Add description.
  - Executes `add` behavior.
- `remove(IPrefabPath path)`: Add description.
  - Executes `remove` behavior.
- `getNearestPath(@Nonnull Vector3d position, @Nullable Set<UUID> disallowedPaths, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getNearestPath` behavior.

## Notes
- No additional notes.
