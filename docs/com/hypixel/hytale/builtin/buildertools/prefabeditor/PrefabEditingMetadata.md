# PrefabEditingMetadata

## Overview
- Documentation for `PrefabEditingMetadata`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.prefabeditor`.

## Constructors
- `PrefabEditingMetadata()`
  - Creates a `PrefabEditingMetadata` instance.
- `PrefabEditingMetadata(@Nonnull Path prefabPath, @Nonnull Vector3i minPoint, @Nonnull Vector3i maxPoint, @Nonnull Vector3i anchorPoint, @Nonnull Vector3i pastePosition, @Nonnull World world)`
  - Creates a `PrefabEditingMetadata` instance.

## Methods
- `createAnchorEntityAt(@Nonnull Vector3i position, @Nonnull World world)`
  - Executes `createAnchorEntityAt` behavior.
- `setPrefabPath(@Nonnull Path prefabPath)`
  - Executes `setPrefabPath` behavior.
- `setAnchorPoint(@Nonnull Vector3i newEntityPosition, @Nonnull World world)`
  - Executes `setAnchorPoint` behavior.
- `recreateAnchorEntity(@Nonnull World world)`
  - Executes `recreateAnchorEntity` behavior.
- `sendAnchorHighlightingPacket(@Nonnull PacketHandler displayTo)`
  - Executes `sendAnchorHighlightingPacket` behavior.
- `isLocationWithinPrefabBoundingBox(@Nonnull Vector3i location)`
  - Executes `isLocationWithinPrefabBoundingBox` behavior.
- `getAnchorPoint()`
  - Executes `getAnchorPoint` behavior.
- `getPastePosition()`
  - Executes `getPastePosition` behavior.
- `getOriginalFileAnchor()`
  - Executes `getOriginalFileAnchor` behavior.
- `getPrefabPath()`
  - Executes `getPrefabPath` behavior.
- `getMinPoint()`
  - Executes `getMinPoint` behavior.
- `getMaxPoint()`
  - Executes `getMaxPoint` behavior.
- `getAnchorEntityUuid()`
  - Executes `getAnchorEntityUuid` behavior.
- `getAnchorEntityPosition()`
  - Executes `getAnchorEntityPosition` behavior.
- `getUuid()`
  - Executes `getUuid` behavior.
- `isDirty()`
  - Executes `isDirty` behavior.
- `setDirty(boolean dirty)`
  - Executes `setDirty` behavior.
- `isReadOnly()`
  - Executes `isReadOnly` behavior.

## Notes
- No additional notes.
