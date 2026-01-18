# PrefabSaver

## Overview
- Documentation for `PrefabSaver`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.prefabeditor.saving`.

## Constructors
- None.

## Methods
- `savePrefab(@Nonnull CommandSender sender, @Nonnull World world, @Nonnull Path pathToSave, @Nonnull Vector3i anchorPoint, @Nonnull Vector3i minPoint, @Nonnull Vector3i maxPoint, @Nonnull Vector3i pastePosition, @Nonnull Vector3i originalFileAnchor, @Nonnull PrefabSaverSettings settings)`
  - Executes `savePrefab` behavior.
- `copyBlocks(@Nonnull CommandSender sender, @Nonnull World world, @Nonnull Vector3i anchorPoint, @Nonnull Vector3i minPoint, @Nonnull Vector3i maxPoint, @Nonnull Vector3i pastePosition, @Nonnull Vector3i originalFileAnchor, @Nonnull PrefabSaverSettings settings)`
  - Executes `copyBlocks` behavior.
- `preloadChunksInSelection(@Nonnull World world, @Nonnull ChunkStore chunkStore, @Nonnull Vector3i minPoint, @Nonnull Vector3i maxPoint)`
  - Executes `preloadChunksInSelection` behavior.
- `save(@Nonnull CommandSender sender, @Nonnull BlockSelection copiedSelection, @Nonnull Path saveFilePath, @Nonnull PrefabSaverSettings settings)`
  - Executes `save` behavior.

## Notes
- No additional notes.
