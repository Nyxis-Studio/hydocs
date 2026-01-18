# WorldPathData

## Overview
- Documentation for `WorldPathData`.
- Declared as a class in `com.hypixel.hytale.builtin.path`.

## Constructors
- None.

## Methods
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `getNearestPrefabPath(int worldgenId, int nameIndex, @Nonnull Vector3d position, Set<UUID> disallowedPaths, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getNearestPrefabPath` behavior.
- `getNearestPrefabPath(int worldgenId, @Nonnull Vector3d position, Set<UUID> disallowedPaths, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getNearestPrefabPath` behavior.
- `getOrConstructPrefabPath(int worldgenId, @Nonnull UUID id, @Nonnull String name, @Nonnull Int2ObjectConcurrentHashMap.IntBiObjFunction<UUID, String, IPrefabPath> pathGenerator)`
  - Executes `getOrConstructPrefabPath` behavior.
- `removePrefabPathWaypoint(int worldgenId, UUID id, int index)`
  - Executes `removePrefabPathWaypoint` behavior.
- `unloadPrefabPathWaypoint(int worldgenId, UUID id, int index)`
  - Executes `unloadPrefabPathWaypoint` behavior.
- `removePrefabPath(int worldgenId, UUID id)`
  - Executes `removePrefabPath` behavior.
- `getPrefabPath(int worldgenId, UUID id, boolean ignoreLoadState)`
  - Executes `getPrefabPath` behavior.
- `compactPrefabPath(int worldgenId, UUID id)`
  - Executes `compactPrefabPath` behavior.
- `getAllPrefabPaths()`
  - Executes `getAllPrefabPaths` behavior.
- `getPrefabPathCollection(int worldgenId)`
  - Executes `getPrefabPathCollection` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
