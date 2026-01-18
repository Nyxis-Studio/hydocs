**Source Hash:** `22c5fa482a110a2dde39c0170eb7c24560552185277e30bea24f852bb058e563`

# StandardDataSource

## Overview

## Constructor Descriptions
- `StandardDataSource(String packKey, Path rootPath, boolean isImmutable, PluginManifest manifest)`
  - Creates a `StandardDataSource` instance.

## Method Descriptions
- `isInModsDirectory(Path path)`: Add description.
  - Executes `isInModsDirectory` behavior.
- `start()`: Add description.
  - Executes `start` behavior.
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.
- `loadRecentModifications()`: Add description.
  - Executes `loadRecentModifications` behavior.
- `saveRecentModifications()`: Add description.
  - Executes `saveRecentModifications` behavior.
- `canAssetPackBeDeleted()`: Add description.
  - Executes `canAssetPackBeDeleted` behavior.
- `resolveAbsolutePath(Path path)`: Add description.
  - Executes `resolveAbsolutePath` behavior.
- `getFullPathToAssetData(Path assetPath)`: Add description.
  - Executes `getFullPathToAssetData` behavior.
- `getAssetTree()`: Add description.
  - Executes `getAssetTree` behavior.
- `isImmutable()`: Add description.
  - Executes `isImmutable` behavior.
- `getRootPath()`: Add description.
  - Executes `getRootPath` behavior.
- `getManifest()`: Add description.
  - Executes `getManifest` behavior.
- `doesDirectoryExist(Path folderPath)`: Add description.
  - Executes `doesDirectoryExist` behavior.
- `createDirectory(Path dirPath, EditorClient editorClient)`: Add description.
  - Executes `createDirectory` behavior.
- `deleteDirectory(Path dirPath)`: Add description.
  - Executes `deleteDirectory` behavior.
- `moveDirectory(Path oldDirPath, Path newDirPath)`: Add description.
  - Executes `moveDirectory` behavior.
- `doesAssetExist(Path assetPath)`: Add description.
  - Executes `doesAssetExist` behavior.
- `getAssetBytes(Path assetPath)`: Add description.
  - Executes `getAssetBytes` behavior.
- `updateAsset(Path assetPath, byte[] bytes, EditorClient editorClient)`: Add description.
  - Executes `updateAsset` behavior.
- `createAsset(Path assetPath, byte[] bytes, EditorClient editorClient)`: Add description.
  - Executes `createAsset` behavior.
- `deleteAsset(Path assetPath, EditorClient editorClient)`: Add description.
  - Executes `deleteAsset` behavior.
- `shouldReloadAssetFromDisk(Path assetPath)`: Add description.
  - Executes `shouldReloadAssetFromDisk` behavior.
- `getLastModificationTimestamp(Path assetPath)`: Add description.
  - Executes `getLastModificationTimestamp` behavior.
- `moveAsset(Path oldAssetPath, Path newAssetPath, EditorClient editorClient)`: Add description.
  - Executes `moveAsset` behavior.
- `loadAssetTree(Collection<AssetTypeHandler> assetTypes)`: Add description.
  - Executes `loadAssetTree` behavior.
- `putModifiedAsset(ModifiedAsset modifiedAsset)`: Add description.
  - Executes `putModifiedAsset` behavior.
- `getRecentlyModifiedAssets()`: Add description.
  - Executes `getRecentlyModifiedAssets` behavior.
- `trackEditorFileSave(Path path, String hash)`: Add description.
  - Executes `trackEditorFileSave` behavior.

## Notes
- No additional notes.
