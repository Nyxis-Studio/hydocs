**Source Hash:** `b3ec035de2c82750a9f66b4f8ff6d8736a15d89cab1917a5775cd28261d8b81c`

# AssetTree

## Overview

## Constructor Descriptions
- `AssetTree(Path rootPath, String packKey, boolean isReadOnly, boolean canBeDeleted)`
  - Creates a `AssetTree` instance.
- `AssetTree(Path rootPath, String packKey, boolean isReadOnly, boolean canBeDeleted, @Nonnull Collection<AssetTypeHandler> assetTypes)`
  - Creates a `AssetTree` instance.

## Method Descriptions
- `replaceAssetTree(@Nonnull AssetTree assetTree)`: Add description.
  - Executes `replaceAssetTree` behavior.
- `sendPackets(@Nonnull EditorClient editorClient)`: Add description.
  - Executes `sendPackets` behavior.
- `isDirectoryEmpty(@Nonnull Path path)`: Add description.
  - Executes `isDirectoryEmpty` behavior.
- `ensureAsset(@Nonnull Path path, boolean isDirectory)`: Add description.
  - Executes `ensureAsset` behavior.
- `getAssetFile(@Nonnull Path path)`: Add description.
  - Executes `getAssetFile` behavior.
- `removeAsset(@Nonnull Path path)`: Add description.
  - Executes `removeAsset` behavior.
- `applyAssetChanges(@Nonnull Map<Path, ModifiedAsset> createdDirectories, @Nonnull Map<Path, ModifiedAsset> modifiedAssets)`: Add description.
  - Executes `applyAssetChanges` behavior.
- `getAssetListForPath(@Nonnull Path path)`: Add description.
  - Executes `getAssetListForPath` behavior.
- `load(@Nonnull Collection<AssetTypeHandler> assetTypes)`: Add description.
  - Executes `load` behavior.
- `loadServerAssets(@Nonnull Path root, @Nonnull Collection<AssetTypeHandler> assetTypes, @Nonnull List<AssetEditorFileEntry> files)`: Add description.
  - Executes `loadServerAssets` behavior.
- `walkFileTree(final @Nonnull Path root, final @Nonnull Path dirPath, final @Nonnull List<AssetEditorFileEntry> files)`: Add description.
  - Executes `walkFileTree` behavior.
- `preVisitDirectory(Path path, BasicFileAttributes attrs)`: Add description.
  - Executes `preVisitDirectory` behavior.
- `visitFile(@Nonnull Path path, @Nonnull BasicFileAttributes attrs)`: Add description.
  - Executes `visitFile` behavior.

## Notes
- No additional notes.
