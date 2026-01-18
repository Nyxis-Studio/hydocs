# AssetMonitorEvent

**Overview**
Base event describing file-system changes detected for asset packs.
Carries lists of created/modified files, removed files, and directory changes.

**Constructors**
- `AssetMonitorEvent(String assetPack, List<Path> createdOrModified, List<Path> removed, List<Path> createdDirectories, List<Path> removedDirectories)`: captures asset pack changes and directory events.

**Methods**
- `getAssetPack()`: returns the asset pack identifier.
- `getCreatedOrModifiedFilesToLoad()`: returns files to load or reload.
- `getRemovedFilesToUnload()`: returns files to unload.
- `getRemovedFilesAndDirectories()`: returns removed files and directories.
- `getCreatedOrModifiedDirectories()`: returns directories created or modified.

**Notes**
- Implements `IEvent<T>` as a base for asset monitor events.
