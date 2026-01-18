# AssetTree

## Overview
- Documentation for `AssetTree`.
- Declared as a class in `com.hypixel.hytale.builtin.asseteditor`.

## Constructors
- `AssetTree(Path rootPath, String packKey, boolean isReadOnly, boolean canBeDeleted)`
  - Creates a `AssetTree` instance.
- `AssetTree(Path rootPath, String packKey, boolean isReadOnly, boolean canBeDeleted, @Nonnull Collection<AssetTypeHandler> assetTypes)`
  - Creates a `AssetTree` instance.

## Methods
- `replaceAssetTree(@Nonnull AssetTree assetTree)`
  - Executes `replaceAssetTree` behavior.
- `sendPackets(@Nonnull EditorClient editorClient)`
  - Executes `sendPackets` behavior.
- `isDirectoryEmpty(@Nonnull Path path)`
  - Executes `isDirectoryEmpty` behavior.
- `ensureAsset(@Nonnull Path path, boolean isDirectory)`
  - Executes `ensureAsset` behavior.
- `getAssetFile(@Nonnull Path path)`
  - Executes `getAssetFile` behavior.
- `removeAsset(@Nonnull Path path)`
  - Executes `removeAsset` behavior.
- `applyAssetChanges(@Nonnull Map<Path, ModifiedAsset> createdDirectories, @Nonnull Map<Path, ModifiedAsset> modifiedAssets)`
  - Executes `applyAssetChanges` behavior.
- `getAssetListForPath(@Nonnull Path path)`
  - Executes `getAssetListForPath` behavior.
- `load(@Nonnull Collection<AssetTypeHandler> assetTypes)`
  - Executes `load` behavior.
- `loadServerAssets(@Nonnull Path root, @Nonnull Collection<AssetTypeHandler> assetTypes, @Nonnull List<AssetEditorFileEntry> files)`
  - Executes `loadServerAssets` behavior.
- `walkFileTree(final @Nonnull Path root, final @Nonnull Path dirPath, final @Nonnull List<AssetEditorFileEntry> files)`
  - Executes `walkFileTree` behavior.
- `preVisitDirectory(Path path, BasicFileAttributes attrs)`
  - Executes `preVisitDirectory` behavior.
- `visitFile(@Nonnull Path path, @Nonnull BasicFileAttributes attrs)`
  - Executes `visitFile` behavior.

## Notes
- No additional notes.
