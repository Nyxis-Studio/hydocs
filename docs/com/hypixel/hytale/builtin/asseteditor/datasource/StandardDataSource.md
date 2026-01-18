# StandardDataSource

## Overview
- Documentation for `StandardDataSource`.
- Declared as a class in `com.hypixel.hytale.builtin.asseteditor.datasource`.

## Constructors
- `StandardDataSource(String packKey, Path rootPath, boolean isImmutable, PluginManifest manifest)`
  - Creates a `StandardDataSource` instance.

## Methods
- `isInModsDirectory(Path path)`
  - Executes `isInModsDirectory` behavior.
- `start()`
  - Executes `start` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `loadRecentModifications()`
  - Executes `loadRecentModifications` behavior.
- `saveRecentModifications()`
  - Executes `saveRecentModifications` behavior.
- `canAssetPackBeDeleted()`
  - Executes `canAssetPackBeDeleted` behavior.
- `resolveAbsolutePath(Path path)`
  - Executes `resolveAbsolutePath` behavior.
- `getFullPathToAssetData(Path assetPath)`
  - Executes `getFullPathToAssetData` behavior.
- `getAssetTree()`
  - Executes `getAssetTree` behavior.
- `isImmutable()`
  - Executes `isImmutable` behavior.
- `getRootPath()`
  - Executes `getRootPath` behavior.
- `getManifest()`
  - Executes `getManifest` behavior.
- `doesDirectoryExist(Path folderPath)`
  - Executes `doesDirectoryExist` behavior.
- `createDirectory(Path dirPath, EditorClient editorClient)`
  - Executes `createDirectory` behavior.
- `deleteDirectory(Path dirPath)`
  - Executes `deleteDirectory` behavior.
- `moveDirectory(Path oldDirPath, Path newDirPath)`
  - Executes `moveDirectory` behavior.
- `doesAssetExist(Path assetPath)`
  - Executes `doesAssetExist` behavior.
- `getAssetBytes(Path assetPath)`
  - Executes `getAssetBytes` behavior.
- `updateAsset(Path assetPath, byte[] bytes, EditorClient editorClient)`
  - Executes `updateAsset` behavior.
- `createAsset(Path assetPath, byte[] bytes, EditorClient editorClient)`
  - Executes `createAsset` behavior.
- `deleteAsset(Path assetPath, EditorClient editorClient)`
  - Executes `deleteAsset` behavior.
- `shouldReloadAssetFromDisk(Path assetPath)`
  - Executes `shouldReloadAssetFromDisk` behavior.
- `getLastModificationTimestamp(Path assetPath)`
  - Executes `getLastModificationTimestamp` behavior.
- `moveAsset(Path oldAssetPath, Path newAssetPath, EditorClient editorClient)`
  - Executes `moveAsset` behavior.
- `loadAssetTree(Collection<AssetTypeHandler> assetTypes)`
  - Executes `loadAssetTree` behavior.
- `putModifiedAsset(ModifiedAsset modifiedAsset)`
  - Executes `putModifiedAsset` behavior.
- `getRecentlyModifiedAssets()`
  - Executes `getRecentlyModifiedAssets` behavior.
- `trackEditorFileSave(Path path, String hash)`
  - Executes `trackEditorFileSave` behavior.

## Notes
- No additional notes.
