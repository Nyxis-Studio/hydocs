# PrefabEditSession

## Overview
- Documentation for `PrefabEditSession`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.prefabeditor`.

## Constructors
- `PrefabEditSession()`
  - Creates a `PrefabEditSession` instance.
- `PrefabEditSession(@Nonnull String worldName, @Nonnull UUID worldCreator, @Nonnull UUID worldArrivedFrom, @Nonnull Transform transformArrivedFrom)`
  - Creates a `PrefabEditSession` instance.
- `PrefabEditSession(@Nonnull PrefabEditSession other)`
  - Creates a `PrefabEditSession` instance.
- `PrefabEditSession(this)`
  - Creates a `PrefabEditSession` instance.

## Methods
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `addPrefab(@Nonnull Path prefabPath, @Nonnull Vector3i minPoint, @Nonnull Vector3i maxPoint, @Nonnull Vector3i anchorPoint, @Nonnull Vector3i pastePosition)`
  - Executes `addPrefab` behavior.
- `updatePrefabBounds(@Nonnull UUID prefab, @Nonnull Vector3i newMin, @Nonnull Vector3i newMax)`
  - Executes `updatePrefabBounds` behavior.
- `setSelectedPrefab(@Nonnull Ref<EntityStore> ref, @Nonnull PrefabEditingMetadata prefabEditingMetadata, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setSelectedPrefab` behavior.
- `hidePrefabAnchors(@Nonnull PacketHandler packetHandler)`
  - Executes `hidePrefabAnchors` behavior.
- `getSelectedPrefab(@Nonnull UUID playerUuid)`
  - Executes `getSelectedPrefab` behavior.
- `clearSelectedPrefab(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `clearSelectedPrefab` behavior.
- `getWorldName()`
  - Executes `getWorldName` behavior.
- `getWorldArrivedFrom()`
  - Executes `getWorldArrivedFrom` behavior.
- `getTransformArrivedFrom()`
  - Executes `getTransformArrivedFrom` behavior.
- `getWorldCreator()`
  - Executes `getWorldCreator` behavior.
- `getSpawnPoint()`
  - Executes `getSpawnPoint` behavior.
- `getLoadedPrefabMetadata()`
  - Executes `getLoadedPrefabMetadata` behavior.
- `markPrefabsDirtyAtPosition(@Nonnull Vector3i position)`
  - Executes `markPrefabsDirtyAtPosition` behavior.
- `markPrefabsDirtyInBounds(@Nonnull Vector3i min, @Nonnull Vector3i max)`
  - Executes `markPrefabsDirtyInBounds` behavior.
- `boundsIntersect(@Nonnull Vector3i aMin, @Nonnull Vector3i aMax, @Nonnull Vector3i bMin, @Nonnull Vector3i bMax)`
  - Executes `boundsIntersect` behavior.
- `createPrefabMarkers()`
  - Executes `createPrefabMarkers` behavior.
- `createPrefabMarker(@Nonnull PrefabEditingMetadata metadata)`
  - Executes `createPrefabMarker` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
