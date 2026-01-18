**Source Hash:** `4ab170fdf92505edd60cda1890e5704581abf2a9fcf65a0d7d65334dbaf96dfc`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetMonitorEvent

## Overview
Base event describing file-system changes detected for asset packs. Carries lists of created/modified files, removed files, and directory changes.

## Field Descriptions
- `createdOrModifiedFilesToLoad`: Files that were created or modified and should be loaded.
- `removedFilesToUnload`: Files removed from the pack that should be unloaded.
- `createdOrModifiedDirectories`: Directories created or modified.
- `removedFilesAndDirectories`: Files or directories removed from the pack.
- `assetPack`: Identifier of the asset pack that changed.

## Constructor Descriptions
- `AssetMonitorEvent(String assetPack, List<Path> createdOrModified, List<Path> removed, List<Path> createdDirectories, List<Path> removedDirectories)`: Captures asset pack changes and directory events.

## Method Descriptions
- `getAssetPack()`: Returns the asset pack identifier.
- `getCreatedOrModifiedFilesToLoad()`: Returns files to load or reload.
- `getRemovedFilesToUnload()`: Returns files to unload.
- `getRemovedFilesAndDirectories()`: Returns removed files and directories.
- `getCreatedOrModifiedDirectories()`: Returns directories created or modified.

## Usage Notes
- Implemented by asset monitor events for filesystem change handling.

## Examples
```java
String pack = event.getAssetPack();
```
