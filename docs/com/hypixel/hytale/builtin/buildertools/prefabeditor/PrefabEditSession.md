**Source Hash:** `351087efff3cd1699d5e5050f85c5d506090018c1e4c2587ca446f5258f63b6b`

# PrefabEditSession

## Overview

## Constructor Descriptions
- `PrefabEditSession()`
  - Creates a `PrefabEditSession` instance.
- `PrefabEditSession(@Nonnull String worldName, @Nonnull UUID worldCreator, @Nonnull UUID worldArrivedFrom, @Nonnull Transform transformArrivedFrom)`
  - Creates a `PrefabEditSession` instance.
- `PrefabEditSession(@Nonnull PrefabEditSession other)`
  - Creates a `PrefabEditSession` instance.
- `PrefabEditSession(this)`
  - Creates a `PrefabEditSession` instance.

## Method Descriptions
- `getResourceType()`: Add description.
  - Executes `getResourceType` behavior.
- `addPrefab(@Nonnull Path prefabPath, @Nonnull Vector3i minPoint, @Nonnull Vector3i maxPoint, @Nonnull Vector3i anchorPoint, @Nonnull Vector3i pastePosition)`: Add description.
  - Executes `addPrefab` behavior.
- `updatePrefabBounds(@Nonnull UUID prefab, @Nonnull Vector3i newMin, @Nonnull Vector3i newMax)`: Add description.
  - Executes `updatePrefabBounds` behavior.
- `setSelectedPrefab(@Nonnull Ref<EntityStore> ref, @Nonnull PrefabEditingMetadata prefabEditingMetadata, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `setSelectedPrefab` behavior.
- `hidePrefabAnchors(@Nonnull PacketHandler packetHandler)`: Add description.
  - Executes `hidePrefabAnchors` behavior.
- `getSelectedPrefab(@Nonnull UUID playerUuid)`: Add description.
  - Executes `getSelectedPrefab` behavior.
- `clearSelectedPrefab(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `clearSelectedPrefab` behavior.
- `getWorldName()`: Add description.
  - Executes `getWorldName` behavior.
- `getWorldArrivedFrom()`: Add description.
  - Executes `getWorldArrivedFrom` behavior.
- `getTransformArrivedFrom()`: Add description.
  - Executes `getTransformArrivedFrom` behavior.
- `getWorldCreator()`: Add description.
  - Executes `getWorldCreator` behavior.
- `getSpawnPoint()`: Add description.
  - Executes `getSpawnPoint` behavior.
- `getLoadedPrefabMetadata()`: Add description.
  - Executes `getLoadedPrefabMetadata` behavior.
- `markPrefabsDirtyAtPosition(@Nonnull Vector3i position)`: Add description.
  - Executes `markPrefabsDirtyAtPosition` behavior.
- `markPrefabsDirtyInBounds(@Nonnull Vector3i min, @Nonnull Vector3i max)`: Add description.
  - Executes `markPrefabsDirtyInBounds` behavior.
- `boundsIntersect(@Nonnull Vector3i aMin, @Nonnull Vector3i aMax, @Nonnull Vector3i bMin, @Nonnull Vector3i bMax)`: Add description.
  - Executes `boundsIntersect` behavior.
- `createPrefabMarkers()`: Add description.
  - Executes `createPrefabMarkers` behavior.
- `createPrefabMarker(@Nonnull PrefabEditingMetadata metadata)`: Add description.
  - Executes `createPrefabMarker` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.

## Notes
- No additional notes.
